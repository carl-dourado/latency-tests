#!/usr/bin/env python3
import argparse
import csv
import re
import statistics
import subprocess
import time
from datetime import datetime


def ping_once(target, timeout):
    command = ["ping", "-c", "1", "-W", str(timeout), target]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    output = f"{result.stdout}\n{result.stderr}"
    match = re.search(r"time[=<]([0-9.]+)\s*ms", output)
    latency = float(match.group(1)) if match else None

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "target": target,
        "ok": latency is not None and result.returncode == 0,
        "latency_ms": latency,
    }


def percentile(values, percent):
    if not values:
        return None
    values = sorted(values)
    index = round((len(values) - 1) * (percent / 100))
    return values[index]


def summarize(rows):
    values = [row["latency_ms"] for row in rows if row["latency_ms"] is not None]
    if not values:
        return {"sent": len(rows), "received": 0}

    gaps = [abs(values[index] - values[index - 1]) for index in range(1, len(values))]
    return {
        "sent": len(rows),
        "received": len(values),
        "min_ms": min(values),
        "avg_ms": round(statistics.mean(values), 2),
        "p95_ms": percentile(values, 95),
        "max_ms": max(values),
        "jitter_ms": round(statistics.mean(gaps), 2) if gaps else 0,
    }


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "target", "ok", "latency_ms"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="rodadas pequenas para olhar latencia")
    parser.add_argument("--target", default="1.1.1.1")
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--interval", type=float, default=1.0)
    parser.add_argument("--timeout", type=int, default=2)
    parser.add_argument("--csv", help="arquivo CSV para salvar")
    args = parser.parse_args()

    rows = []
    for index in range(args.rounds):
        row = ping_once(args.target, args.timeout)
        rows.append(row)
        value = "-" if row["latency_ms"] is None else f"{row['latency_ms']}ms"
        print(f"{index + 1:02d}/{args.rounds} {args.target} {value}")
        if index + 1 < args.rounds:
            time.sleep(args.interval)

    summary = summarize(rows)
    print("\nresumo")
    for key, value in summary.items():
        print(f"{key}: {value}")

    if args.csv:
        write_csv(args.csv, rows)
        print(f"\ncsv salvo em: {args.csv}")


if __name__ == "__main__":
    main()


import csv
from pathlib import Path
from typing import Dict, List

def load_prices_by_state(csv_path: Path) -> Dict[str, List[float]]:
    prices_by_state = {}

    with csv_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            state = row["state"].strip().upper()
            price = float(row["price"])

            if state not in prices_by_state:
                prices_by_state[state] = []

            prices_by_state[state].append(price)

    return prices_by_state

def mean(values: List[float]) -> float:
    return sum(values) / len(values)

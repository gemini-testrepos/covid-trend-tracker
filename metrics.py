"""Rolling average and epidemic growth metric calculations."""

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass(frozen=True)
class DailyRecord:
    date: str
    new_cases: int


def load_csv(path: Path) -> List[DailyRecord]:
    records: List[DailyRecord] = []
    with path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            records.append(DailyRecord(row["date"], max(0, int(row["new_cases"]))))
    return sorted(records, key=lambda r: r.date)


def rolling_average(records: List[DailyRecord], window: int = 7) -> List[float]:
    out: List[float] = []
    for i in range(len(records)):
        slice_vals = [r.new_cases for r in records[max(0, i - window + 1) : i + 1]]
        out.append(round(sum(slice_vals) / len(slice_vals), 2))
    return out


def doubling_time_days(start_val: float, end_val: float, elapsed_days: int) -> Optional[float]:
    if start_val <= 0 or end_val <= start_val or elapsed_days <= 0:
        return None
    rate = math.log(end_val / start_val) / elapsed_days
    return round(math.log(2) / rate, 2)

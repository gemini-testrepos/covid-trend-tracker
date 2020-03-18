"""Rolling average and epidemic growth metric calculations."""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List


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

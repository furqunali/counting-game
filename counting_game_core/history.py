from dataclasses import dataclass
from collections.abc import Iterable

@dataclass(frozen=True)
class RoundRecord:
    correct: bool
    attempts: int
    points: int

class RoundHistory:
    def __init__(self, records: Iterable[RoundRecord] = ()):
        self._records = list(records)

    def add(self, record: RoundRecord):
        if record.attempts < 1 or record.points < 0:
            raise ValueError("invalid round record")
        self._records.append(record)
        return record

    def records(self) -> tuple[RoundRecord, ...]:
        return tuple(self._records)

    def total_points(self) -> int:
        return sum(r.points for r in self._records)

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    id: str
    exposure: float
    signal: float
    urgency: int

    @classmethod
    def from_dict(cls, raw: dict) -> "Record":
        return cls(
            id=str(raw["id"]),
            exposure=float(raw["exposure"]),
            signal=float(raw["signal"]),
            urgency=int(raw["urgency"]),
        )

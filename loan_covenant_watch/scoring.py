from __future__ import annotations

from .models import Record


def score_record(record: Record) -> float:
    exposure_weight = min(record.exposure / 100000, 1.0)
    urgency_weight = record.urgency / 10
    return round((record.signal * 0.55) + (exposure_weight * 0.25) + (urgency_weight * 0.20), 4)


def rank_records(records: list[Record]) -> list[tuple[Record, float]]:
    scored = [(record, score_record(record)) for record in records]
    return sorted(scored, key=lambda item: item[1], reverse=True)


def summarize(records: list[Record]) -> dict:
    ranked = rank_records(records)
    scores = [score for _, score in ranked]
    return {
        "count": len(records),
        "top_id": ranked[0][0].id if ranked else None,
        "breach_risk_max": max(scores) if scores else 0,
        "breach_risk_avg": round(sum(scores) / len(scores), 4) if scores else 0,
    }

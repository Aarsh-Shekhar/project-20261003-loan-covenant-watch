from __future__ import annotations

import json
from pathlib import Path

from .models import Record


def load_records(path: str | Path) -> list[Record]:
    raw_records = json.loads(Path(path).read_text())
    return [Record.from_dict(item) for item in raw_records]

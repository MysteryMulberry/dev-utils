"""Date utility functions."""
from datetime import datetime, timedelta, timezone
from typing import Optional

def now_utc() -> datetime:
    return datetime.now(timezone.utc)

def format_iso(dt: datetime) -> str:
    return dt.isoformat()

def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s)

def days_between(d1: datetime, d2: datetime) -> int:
    return abs((d2 - d1).days)

def add_business_days(dt: datetime, days: int) -> datetime:
    current = dt
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current

def is_weekend(dt: datetime) -> bool:
    return dt.weekday() >= 5

def quarter_of_year(dt: datetime) -> int:
    return (dt.month - 1) // 3 + 1

def age_in_years(birthday: datetime, reference: Optional[datetime] = None) -> int:
    ref = reference or now_utc()
    age = ref.year - birthday.year
    if (ref.month, ref.day) < (birthday.month, birthday.day):
        age -= 1
    return age

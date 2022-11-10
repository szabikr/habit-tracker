from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class RawActivity:
    activity_name: str
    life_aspect: str
    more_info: str

RawJournalEntry = str

@dataclass
class RawDay:
    habits_date: date
    activities: List[RawActivity]
    journal_entry: RawJournalEntry

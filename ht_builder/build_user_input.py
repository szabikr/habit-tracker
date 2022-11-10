from typing import List

from ht_models.raw_models import RawDay
from ht_models.domain_models import UserInput

from ht_builder.build_habits_date import build_habits_date
from ht_builder.build_activity import build_activity
from ht_builder.build_journal_entry import build_journal_entry

def build_user_input(raw_days: List[RawDay]) -> UserInput:
    activities = []
    journal_entries = []
    
    for raw_day in raw_days:
        habits_date = build_habits_date(raw_day.habits_date)
        for raw_activity in raw_day.activities:
            activities.append(build_activity(raw_activity, habits_date))
        if raw_day.journal_entry:
            journal_entries.append(build_journal_entry(raw_day.journal_entry, habits_date))

    return UserInput(activities, journal_entries)

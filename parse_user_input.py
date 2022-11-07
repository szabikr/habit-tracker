import sys
import logging
from typing import List
from dataclasses import dataclass
from datetime import date

from split_list import split_list

from parse_day import parse_day
from parse_habits_date import parse_habits_date
from parse_activity import parse_activity, RawActivity
from parse_journal_entry import parse_journal_entry, RawJournalEntry

@dataclass
class RawDay:
    habits_date: date
    activities: List[RawActivity]
    journal_entry: RawJournalEntry

def parse_user_input(lines: List[str]) -> List[RawDay]:
    if len(lines) == 0:
        return []
        
    days = split_list(lines)

    raw_days = []
    for day in days:
        parsed_day = parse_day(day)
        
        habits_date = parse_habits_date(parsed_day.date)
        activities = [parse_activity(activity) for activity in parsed_day.activities]
        journal_entry = parse_journal_entry(parsed_day.journal_entry)

        raw_days.append(RawDay(habits_date, activities, journal_entry))
    
    return raw_days


if __name__ == "__main__":
    from read_user_input import read_user_input
    from exceptions import ActivityValueError, JournalEntryValueError

    filename = "user_input_example.txt"

    user_input_lines = read_user_input(filename)

    try:
        raw_days = parse_user_input(user_input_lines)
    except ActivityValueError:
        logging.error(f"There has been an issue parsing activities in '{filename}'")
        sys.exit()
    except JournalEntryValueError:
        logging.error(f"There has been an issue parsing journal entries is '{filename}'")
        sys.exit()
    
    for day in raw_days:
        print(day.habits_date)
        for activity in day.activities:
            print(activity)
        print("journal:")
        print(day.journal_entry)


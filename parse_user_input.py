import sys
import logging
from typing import List
from collections import namedtuple

from read_user_input import read_user_input
from split_list import split_list
from exceptions import ActivityValueError, JournalEntryValueError

from parse_day import parse_day
from parse_habits_date import parse_habits_date
from parse_activity import parse_activity
from parse_journal_entry import parse_journal_entry

from build_activity import build_activity
from build_journal_entry import build_journal_entry

UserInputFields = ["activities", "journal_entries"]
UserInput = namedtuple("UserInput", UserInputFields)

def parse_user_input(lines: List[str]) -> UserInput:
    if len(lines) == 0:
        return UserInput([], [])
        
    days = split_list(lines)

    activities = []
    journal_entries = []
    for day in days:
        parsed_day = parse_day(day)
        habits_date = parse_habits_date(parsed_day.raw_date)
        parsed_activities = [parse_activity(raw_activity) for raw_activity in parsed_day.raw_activities]
        parsed_journal_entry = parse_journal_entry(parsed_day.raw_journal_entry)

        activities += [build_activity(parsed_activity, habits_date) for parsed_activity in parsed_activities]
        journal_entry = build_journal_entry(parsed_journal_entry, habits_date)
        if journal_entry:
            journal_entries.append(journal_entry)
    
    return UserInput(activities, journal_entries)


if __name__ == "__main__":
    filename = "user_input_example.txt"

    user_input_lines = read_user_input(filename)

    try:
        user_input = parse_user_input(user_input_lines)
    except ActivityValueError:
        logging.error(f"There has been an issue parsing activities in '{filename}'")
        sys.exit()
    except JournalEntryValueError:
        logging.error(f"There has been an issue parsing journal entries is '{filename}'")
        sys.exit()
    
    print("ACTIVITIES")
    for activity in user_input.activities:
        print(activity.print())
    print("JOURNAL ENTRIES")
    for journal_entry in user_input.journal_entries:
        print(journal_entry)

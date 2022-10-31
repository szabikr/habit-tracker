from typing import List
from collections import namedtuple

from read_user_input import read_user_input
from split_list import split_list

from parse_day import parse_day
from parse_habits_date import parse_habits_date
from parse_activity import parse_activity
from parse_journal_entry import parse_journal_entry

from build_activity import build_activity
from build_journal_entry import build_journal_entry

UserInputFields = ["activities", "journal_entries"]
UserInput = namedtuple("UserInput", UserInputFields)

def parse_user_input(raw_user_input: str) -> UserInput:
    lines = raw_user_input.splitlines()
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

    raw_user_input = read_user_input(filename)
    user_input = parse_user_input(raw_user_input)

    print("ACTIVITIES:")
    [print(activity.print()) for activity in user_input.activities]
    print("JOURNAL_ENTRIES:")
    [print(journal_entry) for journal_entry in user_input.journal_entries]
        
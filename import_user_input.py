import sys
import logging
from pathlib import Path
from typing import List
from collections import namedtuple

from read_user_input import read_user_input
from parse_user_input import parse_user_input

from exceptions import ActivityValueError, JournalEntryValueError
from activities.activity import Activity
from journal.journal_entry import JournalEntry

logger = logging.getLogger(__name__)

def append_activities(activities: List[Activity]):
    activity_data_filename = "activity.txt"
    file = Path.cwd().joinpath(activity_data_filename)

    with file.open("a", encoding="utf-8") as f:
        f.writelines([f"{activity.print()}\n" for activity in activities])

def append_journal_entries(journal_entries: List[JournalEntry]):
    journal_entry_data_filename = "journal_entry.txt"
    file = Path.cwd().joinpath(journal_entry_data_filename)

    with file.open("a", encoding="utf-8") as f:
        f.writelines([f"{journal_entry.print()}\n" for journal_entry in journal_entries])

ImportedEntityCounts = namedtuple("ImportedEntityCounts", ["activity_count", "journal_entry_count"])

def import_user_input(filename: str):
    user_input_lines = read_user_input(filename)

    try:
        user_input = parse_user_input(user_input_lines)
    except ActivityValueError:
        logging.error(f"There has been an issue parsing activities in '{filename}'")
        sys.exit()
    except JournalEntryValueError:
        logging.error(f"There has been an issue parsing journal entries is '{filename}'")
        sys.exit()

    append_activities(user_input.activities)
    append_journal_entries(user_input.journal_entries)

    return ImportedEntityCounts(len(user_input.activities), len(user_input.journal_entries))

if __name__ == "__main__":
    filename = "user_input_example.txt"

    entity_counts = import_user_input(filename)

    print(f"Imported {entity_counts.activity_count} activities")
    print(f"Imported {entity_counts.journal_entry_count} journal entries")

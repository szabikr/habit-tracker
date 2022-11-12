from typing import List
from pathlib import Path

from ht_models.domain_models import Activity, JournalEntry

def append_activities(activities: List[Activity]):
    # see what happens when list is empty or null
    activity_data_filename = "activity.txt"
    file = Path.cwd().joinpath(activity_data_filename)

    with file.open("a", encoding="utf-8") as f:
        f.writelines([f"{activity.print()}\n" for activity in activities])

def append_journal_entries(journal_entries: List[JournalEntry]):
    # see what happens when list is empty or null
    journal_entry_data_filename = "journal_entry.txt"
    file = Path.cwd().joinpath(journal_entry_data_filename)

    with file.open("a", encoding="utf-8") as f:
        f.writelines([f"{journal_entry.print()}\n" for journal_entry in journal_entries])

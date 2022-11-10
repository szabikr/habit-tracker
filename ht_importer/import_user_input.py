import sys
import logging
from collections import namedtuple

from ht_builder.exceptions import ActivityValueError, JournalEntryValueError
from ht_parser.parse_user_input import parse_user_input
from ht_builder.build_user_input import build_user_input

from ht_importer.read_user_input import read_user_input
from ht_importer.write_db import append_activities, append_journal_entries

logger = logging.getLogger(__name__)

ImportedEntityCounts = namedtuple("ImportedEntityCounts", ["activity_count", "journal_entry_count"])

def import_user_input(filename: str):
    user_input_lines = read_user_input(filename)

    raw_days = parse_user_input(user_input_lines)

    try:
        user_input = build_user_input(raw_days)
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

from datetime import date

from exceptions import JournalEntryValueError
from journal.journal_entry import JournalEntry

def build_journal_entry(parsed_record: str, record_date: date) -> JournalEntry:
    if not parsed_record:
        return None
    if not record_date:
        raise JournalEntryValueError
    return JournalEntry(parsed_record, record_date)
from datetime import date

from exceptions import JournalEntryValueError
from parse_journal_entry import RawJournalEntry
from journal.journal_entry import JournalEntry

def build_journal_entry(raw_journal_entry: RawJournalEntry, record_date: date) -> JournalEntry:
    if not raw_journal_entry:
        return None
    if not record_date:
        raise JournalEntryValueError
    return JournalEntry(raw_journal_entry, record_date)

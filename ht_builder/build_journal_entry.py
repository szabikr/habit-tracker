from datetime import date

from ht_models.raw_models import RawJournalEntry
from ht_models.domain_models import JournalEntry

from ht_builder.exceptions import JournalEntryValueError

def build_journal_entry(raw_journal_entry: RawJournalEntry, record_date: date) -> JournalEntry:
    if not raw_journal_entry:
        return None
    if not record_date:
        raise JournalEntryValueError
    return JournalEntry(raw_journal_entry, record_date)

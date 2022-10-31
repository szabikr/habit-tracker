from datetime import date

from journal.journal_entry import JournalEntry

def build_journal_entry(parsed_record: str, record_date: date) -> JournalEntry:
    # TODO: Validation
    if not parsed_record:
        return None
    return JournalEntry(parsed_record, record_date)
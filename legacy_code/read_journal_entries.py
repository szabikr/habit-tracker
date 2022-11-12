import logging
from typing import List

from ht_models.domain_models import JournalEntry

logger = logging.getLogger(__name__)

def read_journal_entries_from_db(file_name: str) -> List[JournalEntry]:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File {file_name} does not exist")
        return []

    logger.info(f"Reading db journal entries from {file_name}")
    journal_entries = []

    while True:
        line = f.readline().strip()
        if not line:
            break

        journal_entry_props = (prop.strip() for prop in line.split(';'))

        id = next(journal_entry_props)
        record_date = next(journal_entry_props)
        record = next(journal_entry_props)

        journal_entries.append(JournalEntry(id=id, record_date=record_date, record=record))
    
    f.close()
    logger.info(f"Read {len(journal_entries)} journal entries from db file {file_name}")
    return journal_entries

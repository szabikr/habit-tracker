import logging
from typing import List
from journal.journal_entry import JournalEntry

logger = logging.getLogger("import_logger")

def write_journal_entries_to_db(journal_entries: List[JournalEntry], file_name: str):
    if not journal_entries:
        logger.warning(f"There are no journal entries to write to {file_name}")
        return
    
    logger.info(f"Opening {file_name} for writing journal entries")
    with open(file_name, "w", encoding="utf-8") as f:
        for journal_entry in journal_entries:
            f.write(journal_entry.print())
            f.write("\n")
        
    logger.info(f"Wrote {len(journal_entries)} journal entries to {file_name}")

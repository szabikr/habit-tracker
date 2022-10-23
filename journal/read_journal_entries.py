import logging
from typing import List

from journal.journal_entry import JournalEntry
from activities import utils

logger = logging.getLogger(__name__)

def read_journal_entries_from_user_input(file_name: str) -> List[JournalEntry]:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File {file_name} does not exist")
        return []

    logger.info(f"Reading user input journal entries from {file_name}")

    journal_entries = []

    while True:
        line = f.readline().strip()
        if not line:
            break

        try:
            record_date = utils.get_activity_date(line)
        except ValueError:
            logger.exception(f"'{line}' is not a correct date format, no journal entries will be read from '{file_name}'")
            f.close()
            return []
        
        while True:
            line = f.readline().strip()
            if not line or line == "":
                break

            if line == "journal:":
                record = ""
                while True:
                    line = f.readline().strip()
                    if not line or line == "":
                        break
                    
                    if record != "":
                        raw_new_line = r"\n"
                        record = f"{record}{raw_new_line}"
                    record = f"{record}{line}"

                journal_entries.append(JournalEntry(record, record_date))
                break
    
    f.close()
    logger.info(f"Read {len(journal_entries)} journal entries from use input file {file_name}")
    return journal_entries

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

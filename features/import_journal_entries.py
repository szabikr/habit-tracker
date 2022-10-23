import logging
from journal.write_journal_entries_to_db import write_journal_entries_to_db
from journal.read_journal_entries import read_journal_entries_from_user_input, read_journal_entries_from_db

def import_journal_entries(file_name: str, db_file_name: str):
    logger = logging.getLogger(__name__)
    logger.info(f"Begin importing journal entries from user input ({file_name}) to db...")

    journal_entries_from_user_input = read_journal_entries_from_user_input(file_name)
    journal_entries_from_db = read_journal_entries_from_db(db_file_name)
    journal_entries = journal_entries_from_db + journal_entries_from_user_input
    write_journal_entries_to_db(journal_entries, db_file_name)

    logger.info("Finished importing journal entries from user input to db file.")

    return len(journal_entries_from_user_input)

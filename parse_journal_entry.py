from typing import List
from datetime import date

from journal.journal_entry import JournalEntry

def parse_journal_entry(lines: List[str], record_date: date) -> JournalEntry:
    record = ""
    for line in lines:
        if record != "":
            raw_new_line = r"\n"
            record = f"{record}{raw_new_line}"
        record = f"{record}{line}"

    if record == "": 
        return None

    return JournalEntry(record, record_date)

if __name__ == "__main__":
    journal_entry_date = date.today()
    journal_lines1 = ["first line", "then the second line", "finally the third one"]
    journal_entry1 = parse_journal_entry(journal_lines1, journal_entry_date)
    print(journal_entry1.print())
    journal_lines2 = ["first line"]
    journal_entry2 = parse_journal_entry(journal_lines2, journal_entry_date)
    print(journal_entry2.print())
    journal_lines2 = []
    journal_entry2 = parse_journal_entry(journal_lines2, journal_entry_date)
    print(journal_entry2 == None)

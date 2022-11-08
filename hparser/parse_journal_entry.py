from typing import List

RawJournalEntry = str

def parse_journal_entry(lines: List[str]) -> RawJournalEntry:
    if not lines:
        return None
    return r"\n".join(lines)

if __name__ == "__main__":
    journal_lines1 = ["first line", "then the second line", "finally the third one"]
    journal_entry1 = parse_journal_entry(journal_lines1)
    print(journal_entry1)
    journal_lines2 = ["first line"]
    journal_entry2 = parse_journal_entry(journal_lines2)
    print(journal_entry2)
    journal_lines3 = []
    journal_entry3 = parse_journal_entry(journal_lines3)
    print(journal_entry3)

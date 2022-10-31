from typing import List
from collections import namedtuple

ParsedDayFields = ["raw_date", "raw_activities", "raw_journal_entry"]
ParsedDay = namedtuple("ParsedDay", ParsedDayFields)

def parse_day(lines: List[str]) -> ParsedDay:
    raw_date = lines[0]
    
    try: 
        journal_entry_index = lines.index("journal:")
    except ValueError:
        journal_entry_index = None
        
    if journal_entry_index:
        raw_activities = lines[1:journal_entry_index]
        raw_journal_entry = lines[journal_entry_index + 1:len(lines)]
    else:
        raw_activities = lines[1:len(lines) - 1]
        raw_journal_entry = None
    
    return ParsedDay(raw_date, raw_activities, raw_journal_entry)
from typing import List
from collections import namedtuple

ParsedDayFields = ["date", "activities", "journal_entry"]
ParsedDay = namedtuple("ParsedDay", ParsedDayFields)

def parse_day(lines: List[str]) -> ParsedDay:
    date = lines[0]
    
    try: 
        journal_entry_index = lines.index("journal:")
    except ValueError:
        journal_entry_index = None
        
    if journal_entry_index:
        activities = lines[1:journal_entry_index]
        journal_entry = lines[journal_entry_index + 1:len(lines)]
    else:
        activities = lines[1:len(lines)]
        journal_entry = None
    
    return ParsedDay(date, activities, journal_entry)
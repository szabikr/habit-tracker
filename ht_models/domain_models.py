from dataclasses import dataclass, field
from datetime import date
from typing import List
import uuid

# TODO: Use a sort index for the activities that happend on the same day
#       so that I can put activities in order when merging different lists

@dataclass
class Activity:
    activity_name: str
    activity_date: date
    life_aspect: str
    more_info: str = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    
    def __str__(self):
        more_info_str = "" if self.more_info == None else f" | {self.more_info}"
        return f"{self.activity_date.strftime('%a %d %b')}: {self.activity_name}; {self.life_aspect}{more_info_str}"

    def print(self):
        more_info_str = "null" if self.more_info == None else f"{self.more_info}"
        return f"{self.id};{self.activity_date.strftime('%Y-%m-%d')};{self.activity_name};{self.life_aspect};{more_info_str}"


@dataclass
class JournalEntry:
    record: str
    record_date: date
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __str__(self):
        # TODO: Should be the decoded self.record cuz now the special characters such as '\n' are just printed as they are
        return f"{self.record_date}\n{self.record}"

    def print(self):
        return f"{self.id};{self.record_date};{self.record}"


@dataclass
class UserInput:
    activities: List[Activity]
    journal_entries: List[JournalEntry]

from dataclasses import dataclass, field
from datetime import date
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
        more_info_str = "" if self.more_info == None else f"; {self.more_info}"
        return f"{self.id}; {self.activity_date.strftime('%Y-%m-%d')}; {self.activity_name}; {self.life_aspect}{more_info_str}"
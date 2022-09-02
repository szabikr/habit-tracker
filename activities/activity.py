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
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    
    def __str__(self):
        return f"{self.activity_date.strftime('%a %d %b')}: {self.activity_name}  ^ {self.life_aspect}"

    def print(self):
        return f"{self.id}; {self.activity_date.strftime('%Y-%m-%d')}; {self.activity_name}; {self.life_aspect}"
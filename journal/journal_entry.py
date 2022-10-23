from dataclasses import dataclass, field
from datetime import date
import uuid

@dataclass
class JournalEntry:
    record: str
    record_date: date
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __str__(self):
        # TODO: Should be decode self.record cuz now the special characters such as '\n' are just printed as they are
        return f"{self.record_date}\n{self.record}"

    def print(self):
        return f"{self.id};{self.record_date};{self.record}"

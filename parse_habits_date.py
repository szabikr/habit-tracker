import logging
from datetime import date, datetime

logger = logging.getLogger(__name__)

def parse_habits_date(partial_date: str) -> date:
    full_date = f"{partial_date} {date.today().year}"
    try:
        habits_date = datetime.strptime(full_date, '%d %b %Y').date()
    except ValueError:
        logger.exception(f"Partial date '{partial_date}' has incorrect format, use '%d %b', i.e. 10 Aug")
        return None
    return habits_date

if __name__ == "__main__":
    user_input_date = "30 Oct"
    result = parse_habits_date(user_input_date)
    if not result:
        print("Unable to construct date")
    else:
        print(result)
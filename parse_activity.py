import logging
from datetime import date

from activities.activity import Activity
from activities.guess_life_aspect import guess_life_aspect

logger = logging.getLogger(__name__)

def parse_activity(line: str, activity_date: date) -> Activity:
    activity_parts = line.split("|")
    raw_activity_props = activity_parts[0]
    try:
        more_info = activity_parts[1].strip()
    except IndexError:
        more_info = None
    activity_props = raw_activity_props.split(";")
    activity_name = activity_props[0].strip()
    try:
        life_aspect = activity_props[1].strip()
    except IndexError:
        life_aspect = guess_life_aspect(activity_name)
        if not life_aspect:
            logger.exception(f"'{line}' is not a correct activity description")
            return None
    return Activity(activity_name, activity_date, life_aspect, more_info)

if __name__ == "__main__":
    activity_date = date.today()
    activity_line1 = "developing my habit tracker; Career | Working on the more info feature"
    activity1 = parse_activity(activity_line1, activity_date)
    print(activity1.print())
    activity_line2 = "developing my habit tracker; Career"
    activity2 = parse_activity(activity_line2, activity_date)
    print(activity2.print())
    activity_line3 = "developing my habit tracker | Working on the more info feature"
    activity3 = parse_activity(activity_line3, activity_date)
    print(activity3.print())

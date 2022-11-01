import logging
from datetime import date

from activities.activity import Activity
from activities.guess_life_aspect import guess_life_aspect
from parse_activity import ParsedActivity
from exceptions import ActivityValueError

logger = logging.getLogger(__name__)

def build_activity(parsed_activity: ParsedActivity, activity_date: date) -> Activity:
    if not activity_date:
        logger.error(f"activity_date is not defined")
        raise ActivityValueError("Activity date is missing")
    life_aspect = parsed_activity.life_aspect or guess_life_aspect(parsed_activity.activity_name)
    if not life_aspect:
        logger.error(f"Parsed activity '{parsed_activity}' is missing life aspect and can't be guessed")
        raise ActivityValueError("Life aspect is missing")
    return Activity(parsed_activity.activity_name, activity_date, life_aspect, parsed_activity.more_info)

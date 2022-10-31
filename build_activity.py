import logging
from datetime import date

from activities.activity import Activity
from activities.guess_life_aspect import guess_life_aspect
from parse_activity import ParsedActivity

logger = logging.getLogger(__name__)

def build_activity(parsed_activity: ParsedActivity, activity_date: date) -> Activity:
    # TODO: Validation
    life_aspect = parsed_activity.life_aspect or guess_life_aspect(parsed_activity.activity_name)
    if not life_aspect:
        logger.error(f"Parsed activity '{parsed_activity}' is missing life aspect and can't be guessed")
        return None
    return Activity(parsed_activity.activity_name, activity_date, life_aspect, parsed_activity.more_info)

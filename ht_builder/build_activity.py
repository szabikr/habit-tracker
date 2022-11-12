import logging
from datetime import date

from ht_models.raw_models import RawActivity
from ht_models.domain_models import Activity

from ht_builder.exceptions import ActivityValueError
from ht_builder.guess_life_aspect import guess_life_aspect

logger = logging.getLogger(__name__)

def build_activity(raw_activity: RawActivity, activity_date: date) -> Activity:
    if not activity_date:
        logger.error(f"activity_date is not defined")
        raise ActivityValueError("Activity date is missing")
    
    life_aspect = raw_activity.life_aspect or guess_life_aspect(raw_activity.activity_name)
    if not life_aspect:
        logger.error(f"Raw activity '{raw_activity}' is missing life aspect and can't be guessed")
        raise ActivityValueError("Life aspect is missing")
    
    return Activity(raw_activity.activity_name, activity_date, life_aspect, raw_activity.more_info)

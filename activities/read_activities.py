import logging
from typing import List

from activities import utils
from activities.activity import Activity
logger = logging.getLogger(__name__)

def read_activities_from_db(file_name: str) -> List[Activity]:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File {file_name} does not exist")
        return []
    
    logger.info(f"Reading db activities from {file_name}")
    activities = []
    while True:
        line = f.readline().strip()
        if not line:
            break

        activity_props = (prop.strip() for prop in line.split(';'))

        id = next(activity_props)
        activity_date = utils.convert_str_to_date(next(activity_props))
        activity_name = next(activity_props)
        life_aspect = next(activity_props)
        try:
            more_info = next(activity_props)
            if more_info == "null":
                more_info = None
        except StopIteration:
            more_info = None

        activities.append(Activity(id=id,
                                   activity_date=activity_date,
                                   activity_name=activity_name,
                                   life_aspect=life_aspect,
                                   more_info=more_info))
    f.close()
    logger.info(f"Read {len(activities)} activity from db file {file_name}")
    return activities

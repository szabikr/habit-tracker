import logging
from typing import List
from activities import utils
from activities.activity import Activity

logger = logging.getLogger(__name__)

def read_activities_from_user_input(file_name: str) -> List[Activity]:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File {file_name} does not exists")
        return []

    logger.info(f"Reading user input activities from {file_name}")
    activities = []
    while True:
        line = f.readline().strip()
        if not line:
            break

        try:
            activity_date = utils.get_activity_date(line)
        except ValueError:
            logger.exception(f"'{line}' is not a correct date format, no activities will be read from '{file_name}'")
            f.close()
            return []

        while True:
            line = f.readline().strip()
            if not line or line == "":
                break

            activity_props = (prop.strip() for prop in line.split(';'))
            try:
                activity_name = next(activity_props)
                life_aspect = next(activity_props)
            except StopIteration:
                logger.exception(f"'{line}' is not a correct activity description, no activities will be read from '{file_name}'")    
                f.close()
                return []

            activities.append(Activity(activity_name, activity_date, life_aspect))
    f.close()
    logger.info(f"Read {len(activities)} activity from user input file {file_name}")
    return activities

def read_activities_from_db(file_name: str) -> List[Activity]:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File {file_name} does not exists")
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

        activities.append(Activity(id=id,
                                   activity_date=activity_date,
                                   activity_name=activity_name,
                                   life_aspect=life_aspect))
    f.close()
    logger.info(f"Read {len(activities)} activity from db file {file_name}")
    return activities

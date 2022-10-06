import logging
from typing import Dict

logger = logging.getLogger(__name__)

def get_registered_activities(file_name: str) -> Dict:
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        logger.exception(f"File '{file_name}' does not exist.")
        return None

    registered_activities = {}
    while True:
        line = f.readline().strip()
        if not line:
            break

        life_aspect = line

        registered_activities[life_aspect] = []

        while True:
            line = f.readline().strip()
            if not line or line == "":
                break

            activity_name = line
            registered_activities[life_aspect].append(activity_name)
    
    f.close()
    return registered_activities
    

def guess_life_aspect(activity_name: str) -> str:
    cache_file_name = "cache.txt"
    registered_activities = get_registered_activities(cache_file_name)
    if not registered_activities:
        return None
        
    activity_name_appears_count = 0
    life_aspect_guess = None
    
    for life_aspect, activity_names in registered_activities.items():
        if activity_name in activity_names:
            activity_name_appears_count += 1
            life_aspect_guess = life_aspect
    
    if activity_name_appears_count > 1:
        logger.info(f"More than one life aspect has the given activity name '{activity_name}'")
        return None

    return life_aspect_guess

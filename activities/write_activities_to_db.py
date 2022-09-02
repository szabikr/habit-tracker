import logging
from typing import List
from activities.activity import Activity

logger = logging.getLogger("import_logger")

def write_activities_to_db(activities: List[Activity], file_name: str):
    if not activities:
        logger.warning(f"There are no activities to write to {file_name}")
        return

    logger.info(f"Opening {file_name} for writing the activities")
    with open(file_name, "w", encoding="utf-8") as f:
        for activity in activities:
            f.write(activity.print())
            f.write("\n")
    logger.info(f"Wrote {len(activities)} activities to {file_name}")
    
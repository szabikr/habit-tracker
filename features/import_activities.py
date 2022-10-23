import sys
import logging
from activities.write_activities_to_db import write_activities_to_db
from activities.read_activities import read_activities_from_user_input, read_activities_from_db

def import_activities(file_name, db_file_name):
    logger = logging.getLogger(__name__)
    logger.info(f"Begin importing activities from user input ({file_name}) to db...")
    
    activities_from_user_input = read_activities_from_user_input(file_name)
    activities_from_db = read_activities_from_db(db_file_name)
    activities = activities_from_db + activities_from_user_input
    write_activities_to_db(activities, db_file_name)

    logger.info("Finished importing activities from user input to db file.")
    
    return len(activities_from_user_input)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Import activities process has been called without file name argument")
        sys.exit("Specify the user input filename as program argument and try again.")

    file_name = sys.argv[1]
    db_file_name = "activity.txt" # this should come from an environment variable
    import_activities(file_name, db_file_name)
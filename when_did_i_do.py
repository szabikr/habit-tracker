import sys
from activities.read_activities import read_activities_from_db

def when_did_i_do(activity_name, db_file_name):
    activities = read_activities_from_db(db_file_name)

    filtered_activities = filter(lambda activity: activity.activity_name == activity_name, activities)

    activities_count = 0
    for activity in filtered_activities:
        activities_count += 1
        print(activity)

    return activities_count 

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Please specify the activity name as program argument and try again.")

    activity_name = sys.argv[1]
    db_file_name = 'data.txt'
    
    when_did_i_do(activity_name, db_file_name)

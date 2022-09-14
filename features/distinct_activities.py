from typing import Dict
from activities.read_activities import read_activities_from_db

def get_distinct_activities(file_name: str) -> Dict:
    activities = read_activities_from_db(file_name) # get distinct activities doesn't have to have a dependency on read_activities_from_db

    distinct_activities = {}
    
    for activity in activities:
        if activity.life_aspect not in distinct_activities:
            distinct_activities[activity.life_aspect] = { activity.activity_name }
            continue

        distinct_activities[activity.life_aspect].add(activity.activity_name)

    return distinct_activities

def display_distinct_activities(file_name: str) -> int:
    activities = get_distinct_activities(file_name)
    for life_aspect, activity_names in activities.items():
        print(life_aspect)
        for activity_name in activity_names:
            print(f"- {activity_name}")
        print()
    
    return len(activities)

if __name__ == "__main__":
    db_file_name = "data.txt"
    display_distinct_activities(db_file_name)

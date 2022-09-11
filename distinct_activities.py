from activities.read_activities import read_activities_from_db

def distinct_activities(file_name: str) -> int:
    activities = read_activities_from_db(file_name)
    result = set([f"{activity.activity_name} - {activity.life_aspect}" for activity in activities])
    for activity in result:
        print(activity)
    return len(result)

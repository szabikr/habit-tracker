from activities.read_activities import read_activities_from_db

def get_latest_activities(activities, activities_count=10):
    latest_activities = {}

    for activity in activities[-activities_count:]:
        if activity.activity_date not in latest_activities:
            latest_activities[activity.activity_date] = [ activity.activity_name ]
            continue

        latest_activities[activity.activity_date].append(activity.activity_name)

    return latest_activities


def display_latest_activities(db_file_name, activities_count=10):
    activities = read_activities_from_db(db_file_name)
    latest_activities = get_latest_activities(activities, activities_count) 
    for activity_date, activity_names in latest_activities.items():
        print(activity_date.strftime('%a %d %b'))
        for activity_name in activity_names:
            print(f" {activity_name}")
        print()


if __name__ == "__main__":
    db_file_name = "activity.txt"
    display_latest_activities(db_file_name)

from datetime import date
import re
from activities.activity import Activity

uuid_regex = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

activity_name = "walk"
activity_date = date(year=2022, month=8, day=11)
life_aspect = "Health & Fitness"

def test_activity_constructor():
    activity = Activity(activity_name, activity_date, life_aspect)

    assert activity.activity_name == activity_name
    assert activity.activity_date == activity_date
    assert activity.life_aspect == life_aspect
    assert re.search(uuid_regex, str(activity.id)) != None

def test_activity___str__():
    activity = Activity(activity_name, activity_date, life_aspect)

    result = str(activity)
    assert result == 'Thu 11 Aug: walk  ^ Health & Fitness'

def test_activity_print():
    activity = Activity(activity_name, activity_date, life_aspect)

    result = activity.print()
    activity_id = activity.id
    assert result == f'{activity_id}; 2022-08-11; walk; Health & Fitness'
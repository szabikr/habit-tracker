import datetime
from uuid import UUID
from unittest.mock import patch, mock_open, call
from activities.activity import Activity
from activities.write_activities_to_db import write_activities_to_db

def test_writing_activities_list_to_db_file():
    activities = [
        Activity(activity_name='developing my habit tracker', activity_date=datetime.date(2022, 8, 10), life_aspect='Career', id=UUID('b0f3160f-6509-4a1e-8ee9-90fd2973eebe')),
        Activity(activity_name='walk', activity_date=datetime.date(2022, 8, 10), life_aspect='Health & Fitness', id=UUID('6219b595-c6ce-4b86-b923-b2665e27a0f4')),
    ]

    db_file_name = "tests/output_files/test_output_db_file.txt"

    with patch("activities.write_activities_to_db.open", mock_open()) as mocked_file:
        write_activities_to_db(activities, db_file_name)

        mocked_file.assert_called_once_with(db_file_name, "w", encoding="utf-8")
        mocked_file().write.assert_has_calls([
            call(activities[0].print()),
            call("\n"),
            call(activities[1].print()),
            call("\n"),
        ])

def test_writing_no_activities_to_db_file():
    db_file_name = "tests/output_files/test_output_db_file.txt"

    activities = []
    with patch("activities.write_activities_to_db.open", mock_open()) as mocked_file:
        write_activities_to_db(activities, db_file_name)

        mocked_file.assert_not_called()

    activities = None
    with patch("activities.write_activities_to_db.open", mock_open()) as mocked_file:
        write_activities_to_db(activities, db_file_name)

        mocked_file.assert_not_called()

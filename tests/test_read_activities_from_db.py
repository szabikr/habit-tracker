import pytest
from features.read_activities import read_activities_from_db

# TODO: Mock file open and read function

def test_read_from_non_existant_file():
    file_name = 'non-existent-file'
    result = read_activities_from_db(file_name)

    assert result == []

def test_read_from_valid_db_file():
    file_name = 'tests/db_files/valid_db.txt'
    result = read_activities_from_db(file_name)

    assert len(result) == 5

def test_read_from_inccrect_db_file():
    file_name = 'tests/db_files/incorrect_db.txt'

    with pytest.raises(StopIteration):
        read_activities_from_db(file_name)
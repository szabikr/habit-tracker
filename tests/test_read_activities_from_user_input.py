from activities.read_activities import read_activities_from_user_input

# TODO: Mock file open and read function

def test_read_from_non_existant_file():
    file_name = 'non-existent-file'
    result = read_activities_from_user_input(file_name)

    assert result == []

def test_read_from_valid_file():
    file_name = 'tests/user_input_files/valid_user_input.txt'
    result = read_activities_from_user_input(file_name)

    assert len(result) == 5

def test_read_from_file_with_incorrect_date_format():
    file_name = 'tests/user_input_files/incorrect_date_format.txt'
    result = read_activities_from_user_input(file_name)

    assert result == []

def test_read_from_file_with_incorrect_activity_description():
    file_name = 'tests/user_input_files/incorrect_activity_description.txt'
    result = read_activities_from_user_input(file_name)

    assert result == []
    
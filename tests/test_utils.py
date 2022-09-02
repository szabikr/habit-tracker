import pytest
from datetime import date
from activities.utils import get_activity_date, convert_str_to_date

def test_get_activity_date_with_correct_partial_date():
    partial_date = "10 Aug"
    result = get_activity_date(partial_date)
    assert result == date(year=2022, month=8, day=10)

def test_get_activity_date_with_incorrect_date_format():
    partial_date = "Aug 10"
    with pytest.raises(ValueError) as exception_info:
        get_activity_date(partial_date)
    assert exception_info.value.args[0] == "Partial date 'Aug 10' has incorrect format, use '%d %b', i.e. 10 Aug"

def test_convert_str_to_date_with_correct_date_str():
    date_str = '2022-08-10'
    result = convert_str_to_date(date_str)
    assert result == date(year=2022, month=8, day=10)

def test_convert_str_to_date_with_incorrect_date_format():
    date_str = '10-08-2022'
    with pytest.raises(ValueError) as exception_info:
        convert_str_to_date(date_str)
    assert exception_info.value.args[0] == "time data '10-08-2022' does not match format '%Y-%m-%d'"
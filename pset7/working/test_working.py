import pytest
from working import convert


def test_time_case():
    """Check that convert is case insensitive."""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 Am to 5:00 Pm") == "09:00 to 17:00"
    assert convert("9:00 aM to 5:00 pM") == "09:00 to 17:00"
    assert convert("9:00 am to 5:00 pm") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_time_format():
    """Check that convert is able to convert both simple and complex time."""
    assert convert("6:00 AM to 6:00 PM") == "06:00 to 18:00"
    assert convert("6 AM to 6 PM") == "06:00 to 18:00"
    assert convert("1:45 AM to 5:35 PM") == "01:45 to 17:35"


def test_max_range():
    """Check that convert handles maximum time ranges."""
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("12 AM to 12 AM") == "00:00 to 00:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_range_edge_cases():
    """Check that convert handles range edge cases."""
    assert convert("12:01 AM to 12:01 AM") == "00:01 to 00:01"
    assert convert("12:01 PM to 12:01 PM") == "12:01 to 12:01"
    assert convert("11:59 PM to 11:59 AM") == "23:59 to 11:59"


def test_poor_formatting():
    """Check that convert raises ValueErrors when time values are poorly formatted."""
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    
    with pytest.raises(ValueError):
        convert("9 AM to 5PM")

    with pytest.raises(ValueError):
        convert("6:19 AM 4:20 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9 to 5")

    with pytest.raises(ValueError):
        convert("from 9:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("-9:00 AM to -5:00 PM")

    with pytest.raises(ValueError):
        convert("-9 AM to -5 PM")
    
    with pytest.raises(ValueError):
        convert("9.00 AM to 5.00 PM")


def test_mixed_formats():
    """Check that convert raises ValueErrors mixing 12H and 24H time."""
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_incorrect_minutes():
    """Check that convert raises ValueErrors when minute ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("12:61 AM to 5:00 PM")
    
    with pytest.raises(ValueError):
        convert("12:61 PM to 5:00 AM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_incorrect_hours():
    """Check that convert raises ValueErrors when hour ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("12:00 AM to 25:00 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("14 AM to 5 PM")
    
    with pytest.raises(ValueError):
        convert("25 PM to 5 AM")


def test_no_entry():
    """Check that convert raises ValueErrors when nothing is entered."""
    with pytest.raises(ValueError):
        convert("")

    with pytest.raises(ValueError):
        convert(" ")

    with pytest.raises(ValueError):
        convert(" to ")
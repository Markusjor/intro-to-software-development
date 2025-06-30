
from geo_calculator.calculations import find_average

def test_find_average() -> None:
    test_list = [1,2,3,4,5]
    try:
        assert find_average(test_list) == 3
    except:
        raise AssertionError("Formating error")

def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6
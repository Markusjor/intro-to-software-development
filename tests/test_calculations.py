
from geo_calculator.calculations import find_average
from geo_calculator.calculations import gardners_equation
import pytest

def test_find_average() -> None:
    test_list = [1,2,3,4,5]
    try:
        assert find_average(test_list) == 3
    except:
        raise AssertionError("Formating error")

def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)

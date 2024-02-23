import pytest

from template.maths import adder

def test_postive_numbers():
    """
    Checks if postive floats sum together correctly
    """
    # Define experiment variables
    v1, v2 = 1.5, 2.5
    expected_result = 4.0

    # Run function
    result = adder(v1,v2)

    # Compare results to expected outcome
    assert result == expected_result, f"Expected result {expected_result} doesn't match actual {result}"


def test_input_types():
    """
    Checks putting in incorrect dtypes will throw an error
    """
    # Define experiment variables
    v1, v2 = "1.5", 2.5

    # Run function and await error
    with pytest.raises(TypeError):
        adder(v1,v2)

    # Run function and await error
    v1, v2 = 1.5, "2.5"

    # Run function
    with pytest.raises(TypeError):
        adder(v1,v2)


def test_mixed_numbers():
    """
    Checks if it will correctly sum negative and positive floats
    """
    # Define experiment variables
    v1, v2 = 1.5, -2.5
    expected_result = -1.0

    # Run function
    result = adder(v1,v2)

    # Compare results to expected outcome
    assert result == expected_result, f"Expected result {expected_result} doesn't match actual {result}"
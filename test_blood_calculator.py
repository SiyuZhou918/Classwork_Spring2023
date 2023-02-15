import pytest

@pytest.mark.parametrize("HDL_input, expected",
[
(65, "Normal"),
(40, "Borderline Low"),
(20, "Low")
])
def test_HDL_analysis(expected, HDL_input):
    from blood_calculator import HDL_analysis
    # Arrange
    # HDL_input = 65
    # Act
    answer = HDL_analysis(HDL_input)
    # Assert
    assert answer == expected 


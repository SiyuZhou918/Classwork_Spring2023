import pytest


@pytest.mark.parametrize("x_input, expected", [
    ([1, 1, 2, 2, 3], 3),
    ([1, 2, 2, 3, 3], 4),
    ([1, 2, 1, 2, 3], None)
]
                         )
def test_calculate_y_value(x_input, expected):
    from in_class_exercise_Test_Driven_Development import calculate_y_value
    answer = calculate_y_value(x_input)
    assert answer == expected

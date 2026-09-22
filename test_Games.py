import pytest
from Games import check_guess, validate_input


# ===== Тесты корректной работы =====

def test_check_guess_correct():
    assert check_guess(25, 25) == "correct"

def test_check_guess_higher():
    assert check_guess(40, 15) == "higher"

def test_check_guess_lower():
    assert check_guess(10, 35) == "lower"

def test_validate_input_ok():
    assert validate_input("25") == 25
    assert validate_input("  8  ") == 8


# ===== Тесты некорректных данных =====

def test_validate_input_empty():
    with pytest.raises(ValueError):
        validate_input("")

def test_validate_input_spaces():
    with pytest.raises(ValueError):
        validate_input("    ")

def test_validate_input_letters():
    with pytest.raises(ValueError):
        validate_input("abc")

def test_validate_input_float():
    with pytest.raises(ValueError):
        validate_input("3.14")
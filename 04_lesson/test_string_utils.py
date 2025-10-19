import pytest
from string_utils import StringUtils


# проверки функции замены первой буквы на заглавную
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("skypro", "Skypro"),
        ("привет", "Привет"),
        ("привет класс", "Привет класс")
    ]
)

def test_capitalize_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.capitalize(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" ", " "),
        (" .", " ."),
        ("1", "1")
    ]
)
def test_capitalize_negative(input_text, expected_output):
    processor = StringUtils()
    assert processor.capitalize(input_text) == expected_output


# проверки функции удаления пробела в начале строки
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" skypro", "skypro"),
        (" привет", "привет"),
        ("1", "1")
    ]
)
def test_trim_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.trim(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (".", "."),
        (" 1", "1"),
        (" ", "")
    ]
)
def test_trim_negative(input_text, expected_output):
    processor = StringUtils()
    assert processor.trim(input_text) == expected_output


# проверки функции поиска символа
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "П", True),
        ("Тест", "е", True),
        ("Homework", "m", True),
    ] 
)
def test_contains_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_text, symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "", True),
        ("Тест ", "Тест", True),
        ("Homework", "h", False),
    ]
)
def test_contains_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_text, symbol) == expected_output


# проверки функции удаления символа
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "П", "ривет"),
        ("Homework", "w", "Homeork"),
        ("телефон", "т", "елефон")
    ]
)
def test_delete_symbol_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "R", "Привет"),
        ("Homework", "!", "Homework"),
        ("102", "?", "102")
    ]
)
def test_delete_symbol_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.delete_symbol(input_text, symbol) == expected_output
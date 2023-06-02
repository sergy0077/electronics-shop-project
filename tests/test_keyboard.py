import pytest
from src.keyboard import Keyboard


def test_repr():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_str():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(keyboard) == "Dark Project KD87A"


def test_default_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.language == "EN"


def test_change_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    keyboard.change_lang()
    assert keyboard.language == "RU"


def test_multiple_language_changes():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"


def test_invalid_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(ValueError):
        keyboard.language = "CH"


if __name__ == "__main__":
    pytest.main()

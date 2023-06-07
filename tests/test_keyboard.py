import pytest
from src.keyboard import Keyboard


def test_keyboard_str_representation():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(keyboard) == "Dark Project KD87A"


def test_keyboard_language_initialization():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.language == "EN"


def test_keyboard_change_language():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)

    keyboard.change_lang()
    assert keyboard.language == "RU"

    keyboard.change_lang()
    assert keyboard.language == "EN"

    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"


def test_keyboard_language_setter():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)

    with pytest.raises(AttributeError) as e:
        keyboard.language = 'CH'
    assert str(e.value) == "can't set attribute"


def test_keyboard_repr():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert repr(keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_keyboard_invalid_language():
    with pytest.raises(ValueError) as e:
        keyboard = Keyboard('Dark Project KD87A', 9600, 5)
        keyboard.change_lang()
        keyboard.language = 'CH'
    assert str(e.value) == "Invalid language. Supported languages: EN, RU"


if __name__ == "__main__":
    pytest.main()

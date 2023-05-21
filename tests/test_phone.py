import pytest
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def phone_1():
    return Phone('Маяк', 20000, 5, 1)


def test_setter(phone_1):
    assert phone_1.number_of_sim == 1

def test_keyboard():
    kb = Keyboard("клава", 1000, 10)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"

    try:
        kb.language = "CH"
    except AttributeError:
        print("EN / RU")



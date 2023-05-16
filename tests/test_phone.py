import pytest
from src.phone import Phone


@pytest.fixture
def phone_1():
    return Phone('Маяк', 20000, 5, 1)


def test_setter(phone_1):
    assert phone_1.number_of_sim == 1

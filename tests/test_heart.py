import pytest
from berserker import Berserker
from gladiator import Gladiator
from heart import Heart


@pytest.fixture()
def heart_guy():
    heart_guy = Heart("Dorian", 5, 2, 1)
    return heart_guy


def test_name(heart_guy): # NIE DZIALA !!! chyba?
    heart_guy.name('Andre')
    assert False


def test_hp_potion_usage(heart_guy):
    heart_guy.hp_potion_usage()
    assert heart_guy.health_points == 15

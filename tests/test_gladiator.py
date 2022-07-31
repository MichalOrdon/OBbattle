import pytest
from berserker import Berserker
from gladiator import Gladiator


@pytest.fixture()
def berserker():
    berserker = Berserker("Greg", 20, 1)
    return berserker


@pytest.fixture()
def gladiator():
    gladiator = Gladiator("Gunter", 10, 4)
    return gladiator


def test_gladiator():
    gladiator = Gladiator("Imie", 40, 5)
    assert gladiator.name == "Imie"
    assert gladiator.health_points == 40
    assert gladiator.strenght == 5
    assert gladiator.defense_points == 1


def test_attack_move_received(berserker, gladiator):
    gladiator.attack_move_received(berserker.strenght)
    assert gladiator.health_points == 9

import pytest
from berserker import Berserker
from gladiator import Gladiator


@pytest.fixture()
def berserker():
    berserker = Berserker("Greg", 10, 4)
    return berserker


@pytest.fixture()
def gladiator():
    gladiator = Gladiator("Gunter", 20, 1)
    return gladiator


def test_berserker():
    berserker = Berserker("Imie", 40, 5)
    assert berserker.name == "Imie"
    assert berserker.health_points == 40
    assert berserker.strenght == 5
    assert berserker.defense_points == 1


def test_attack_move_received(berserker, gladiator):
    berserker.attack_move_received(gladiator.strenght)
    assert berserker.health_points == 9


def test_defense_pose(berserker):
    berserker.defense_pose()
    assert berserker.defense_points == 5


def test_amok(berserker):
    berserker.amok()
    assert berserker.health_points == 5
    assert berserker.strenght == 6


def test_special_attack(berserker, gladiator):
    gladiator.attack_move_received(berserker.special_attack())
    assert gladiator.health_points == 12

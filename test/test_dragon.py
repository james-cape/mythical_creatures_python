import pytest
from lib.dragon import *

def test_it_has_attributes():
    dragon = Dragon("Ramoth", "gold", "Lessa")
    assert dragon.name == "Ramoth"
    assert dragon.rider == "Lessa"
    assert dragon.color == "gold"

def test_a_different_dragon():
    dragon = Dragon("Mnementh", "bronze", "F'lar")
    assert dragon.name == "Mnementh"
    assert dragon.rider == "F'lar"
    assert dragon.color == "bronze"

def test_dragons_are_born_hungry():
    dragon = Dragon("Canth", "brown", "F'nor")
    assert dragon.is_hungry()

def test_dragons_eat_a_lot():
    dragon = Dragon("Canth", "brown", "F'nor")
    assert dragon.is_hungry()
    dragon.eat()
    assert dragon.is_hungry()
    dragon.eat()
    assert dragon.is_hungry()
    dragon.eat()
    assert not dragon.is_hungry()

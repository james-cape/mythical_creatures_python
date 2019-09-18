import pytest
from lib.vampire import *

def test_it_has_a_name():
    vampire = Vampire("Dracula")

    assert vampire.name == "Dracula"

def test_it_has_another_name():
    vampire = Vampire("Vladimir")

    assert vampire.name == "Vladimir"

def test_it_keeps_a_pet_bat_by_default():
    vampire = Vampire("Ruthven")

    assert vampire.pet == "bat"

def test_it_can_have_other_pets():
    vampire = Vampire("Varney", "fox")
    assert vampire.pet == "fox"

def test_it_is_thirsty_by_default():
    vampire = Vampire("Count von Count")
    assert vampire.is_thirsty()

def test_it_is_not_thirsty_after_drinking():
    vampire = Vampire("Elizabeth Bathory")
    vampire.drink()
    assert vampire.is_thirsty() == False
    assert not vampire.is_thirsty()

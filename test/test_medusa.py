import pytest
from lib.medusa import *

def test_has_name():
    medusa = Medusa("Cassiopeia")
    assert medusa.name == "Cassiopeia"

def test_when_first_created_she_has_no_statues():
    medusa = Medusa("Cassiopeia")
    assert not medusa.statues

def test_when_staring_at_a_person_she_gains_a_statue():
    medusa = Medusa("Cassiopeia")
    victim = Person("Perseus")

    medusa.stare(victim)
    assert len(medusa.statues) == 1
    assert medusa.statues[0].name == "Perseus"

def test_when_staring_at_a_person_that_person_turns_to_stone():
    medusa = Medusa("Cassiopeia")
    victim = Person("Perseus")

    assert victim.is_stoned() == False
    medusa.stare(victim)
    assert victim.is_stoned() == True

def test_can_only_have_three_victims():
    medusa = Medusa("Cassiopeia")
    medusa.statues = []
    victim1 = Person("Perseus")
    victim2 = Person("Bories")
    victim3 = Person("Canta")
    victim4 = Person("Wonta")
    medusa.stare(victim1)
    medusa.stare(victim2)
    medusa.stare(victim3)
    medusa.stare(victim4)

    assert len(medusa.statues) == 3

def test_if_a_fourth_victim_is_stoned_first_is_unstoned():
    medusa = Medusa("Cassiopeia")
    medusa.statues = []
    victim1 = Person("Perseus")
    victim2 = Person("Bories")
    victim3 = Person("Canta")
    victim4 = Person("Wonta")

    medusa.stare(victim1)
    medusa.stare(victim2)
    medusa.stare(victim3)
    assert len(medusa.statues) == 3
    assert victim1.is_stoned() == True

    medusa.stare(victim4)
    assert len(medusa.statues) == 3
    assert victim1.is_stoned() == False
    assert victim2.is_stoned() == True
    assert victim3.is_stoned() == True
    assert victim4.is_stoned() == True

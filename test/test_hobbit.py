import pytest
from lib.hobbit import *

def test_it_has_a_name():
    hobbit = Hobbit("Bilbo")
    assert hobbit.name == "Bilbo"

def test_it_is_named_something_else():
    hobbit = Hobbit("Peregrin")
    assert hobbit.name == "Peregrin"

def test_disposition_is_unadventurous():
    hobbit = Hobbit("Samwise")
    assert hobbit.disposition == "homebody"

def test_can_have_a_different_disposition():
    hobbit = Hobbit("Frodo", "adventurous")
    assert hobbit.disposition == "adventurous"

def test_grows_older_when_celebrating_birthdays():
    hobbit = Hobbit("Meriadoc")
    assert hobbit.age == 0
    for _ in range(5):
        hobbit.celebrate_birthday()
    assert hobbit.age == 5

def test_is_considered_a_child_at_32():
    hobbit = Hobbit("Gerontius")
    for _ in range(32):
        hobbit.celebrate_birthday()
    assert not hobbit.is_adult()

    hobbit.celebrate_birthday()
    assert hobbit.is_adult()

def test_comes_of_age_at_33():
    hobbit = Hobbit("Otho")
    for _ in range(33):
        hobbit.celebrate_birthday()
    assert hobbit.is_adult()

    hobbit.celebrate_birthday()
    assert hobbit.is_adult()

def test_is_old_at_age_of_101():
    hobbit = Hobbit("Parko")
    hobbit.age = 100
    assert not hobbit.is_old()
    hobbit.age = 101
    assert hobbit.is_old()
    hobbit.age = 101
    assert hobbit.is_old()

def test_hobbit_has_the_ring_if_its_name_is_frodo():
    hobbit_1 = Hobbit("Frodo")
    hobbit_2 = Hobbit("Sam")
    assert hobbit_1.has_ring()
    assert not hobbit_2.has_ring()

def test_hobbits_are_short():
    hobbit = Hobbit("Russ")
    assert hobbit.is_short()

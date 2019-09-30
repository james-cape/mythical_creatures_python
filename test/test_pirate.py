import pytest
from lib.pirate import *

def test_it_has_a_name():
    pirate = Pirate("Jack")
    assert pirate.name == "Jack"

def test_it_has_a_different_name():
    pirate = Pirate("Blackbeard")
    assert pirate.name == "Blackbeard"

def test_it_is_a_scallywag_by_default():
    pirate = Pirate("Jack")
    assert pirate.job == "Scallywag"

def test_its_not_always_a_scallywag():
    pirate = Pirate("Jack", "Cook")
    assert pirate.job == "Cook"

def test_isnt_cursed_by_default():
    pirate = Pirate("Jack")
    assert pirate.is_cursed() == False
    # assert not pirate.is_cursed
#
#   def test_isnt_cursed_by_default
#     skip
#     pirate = Pirate.new("Jack")
#     refute pirate.cursed?
#   end
#
#   def test_becomes_cursed_after_enough_heinous_acts
#     skip
#     pirate = Pirate.new("Jack")
#     refute pirate.cursed?
#     pirate.commit_heinous_act
#     refute pirate.cursed?
#     pirate.commit_heinous_act
#     refute pirate.cursed?
#     pirate.commit_heinous_act
#     assert pirate.cursed?
#   end
#
#   def test_a_pirate_has_booty
#     skip
#     # create a pirate
#     # check that the pirate starts with 0 booty
#   end
#
#   def test_a_pirate_gets_100_booty_for_robbing_ships
#     skip
#     # create a pirate
#     # rob some ships
#     # check that the pirate got 100 booty for each ship it robbed
#   end

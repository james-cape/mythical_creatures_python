import pytest
from lib.werewolf import *

def test_it_has_name():
    werewolf = Werewolf("David")
    assert werewolf.name == "David"

def test_it_has_a_location():
    werewolf = Werewolf("David", "London")
    assert werewolf.location == "London"

def test_it_is_by_default_in_human_form():
    werewolf = Werewolf("David", "London")
    assert werewolf.is_human() == True

def test_when_starting_as_a_human_changing_means_it_is_no_longer_human():
    werewolf = Werewolf("David", "London")
    assert werewolf.is_human() == True
    werewolf.change()
    assert werewolf.is_human() == False

def test_when_starting_as_a_human_changing_turns_it_into_a_werewolf():
    werewolf = Werewolf("David", "London")
    assert werewolf.is_human() == True
    werewolf.change()
    assert werewolf.is_wolf() == True

def test_when_starting_as_a_human_changing_a_second_time_it_becomes_human_again():
    werewolf = Werewolf("David", "London")
    assert werewolf.is_human() == True
    werewolf.change()
    assert werewolf.is_human() == False
    werewolf.change()
    assert werewolf.is_human() == True

def test_when_starting_as_a_werewolf_changing_a_second_time_it_becomes_werewolf_again():
    werewolf = Werewolf("David","London", human_state = False)
    assert werewolf.is_wolf() == True
    werewolf.change()
    assert werewolf.is_wolf() == False
    werewolf.change()
    assert werewolf.is_wolf() == True

def test_is_not_hungry_by_default():
    werewolf = Werewolf("David","London")
    assert werewolf.is_hungry() == False

def test_becomes_hungry_after_changing_to_a_werewolf():
    werewolf = Werewolf("David","London")
    assert werewolf.is_hungry() == False
    werewolf.change()
    assert werewolf.is_hungry() == True

def test_victim_starts_alive():
    human = Victim()
    assert human.status == "Alive"

def test_consumes_a_victim():
    human = Victim()
    werewolf = Werewolf("David","London")

    werewolf.consume(human)

def test_cannot_consume_victim_if_in_human_form():
    human = Victim()
    werewolf = Werewolf("David","London")

    assert werewolf.consume(human) == "No one was consumed"

def test_a_werewolf_who_has_consumed_a_victim_is_no_longer_hungry():
    human = Victim()
    werewolf = Werewolf("David","London", human_state = False, hungry = True)

    assert werewolf.is_hungry() == True
    werewolf.consume(human)
    assert werewolf.is_hungry() == False

def test_a_werewolf_who_has_consumed_a_victim_makes_the_victim_dead():
    human = Victim()
    werewolf = Werewolf("David","London", human_state = False, hungry = True)

    werewolf.consume(human)
    assert human.status == "Dead"

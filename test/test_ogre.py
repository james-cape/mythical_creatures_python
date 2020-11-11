import pytest
from lib.ogre import *

def test_it_has_a_name():
    ogre = Ogre('Brak')
    assert ogre.name == 'Brak'

def test_it_can_live_somewhere_by_default():
    ogre = Ogre('Brak')
    assert ogre.home == 'Swamp'

def test_it_doesnt_have_to_live_in_a_swamp():
    ogre = Ogre('Brak', 'The Ritz')
    assert ogre.home == 'The Ritz'

def test_it_can_meet_humans():
    ogre = Ogre('Brak')
    human = Human()

    assert human.name == 'Jane'
    ogre.encounter(human)
    assert human.encounter_counter == 1

def test_humans_only_notices_ogre_every_third_encounter():
    ogre = Ogre('Brak')
    human = Human()
    ogre.encounter(human)
    ogre.encounter(human)
    assert not human.notices_ogre()
    ogre.encounter(human)
    assert human.notices_ogre()

def test_human_notices_ogre_the_sixth_time():
    ogre = Ogre('Brak')
    human = Human()
    for i in range(6):
        ogre.encounter(human)
    assert human.notices_ogre()

def test_it_can_swing_a_club():
    ogre = Ogre('Brak')
    human = Human()

    ogre.swing_at(human)
    assert ogre.swings == 1

def test_it_swings_the_club_when_the_human_notices_it():
    ogre = Ogre('Brak')
    human = Human()
    ogre.encounter(human)
    assert ogre.swings == 0
    assert not human.notices_ogre()
    ogre.encounter(human)
    ogre.encounter(human)

    assert ogre.swings == 1
    assert human.notices_ogre()

def test_it_hits_the_human_every_second_time_it_swings():
    ogre = Ogre('Brak')
    human = Human()
    for i in range(6):
        ogre.encounter(human)
    assert human.encounter_counter == 6
    assert ogre.swings == 2
    assert human.knocked_out

def test_human_wakes_up_when_ogre_apologizes():
    ogre = Ogre('Brak')
    human = Human()
    for i in range(6):
        ogre.encounter(human)
    assert human.encounter_counter == 6
    assert ogre.swings == 2
    assert human.knocked_out

    ogre.apologize(human)
    assert not human.knocked_out

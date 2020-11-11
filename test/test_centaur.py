import pytest
from lib.centaur import *

def test_it_has_name():
    centaur = Centaur("George", "Palomino")
    assert centaur.name == "George"

def test_it_has_a_horse_breed():
    centaur = Centaur("George", "Palomino")
    assert centaur.breed == "Palomino"

def test_it_has_excellent_bow_skills():
    centaur = Centaur("George", "Palomino")
    assert centaur.shoot() == "Twang!!!"

def test_it_makes_a_horse_sound_when_it_runs():
    centaur = Centaur("George", "Palomino")
    assert centaur.run() == "Clop clop clop clop!!!"

def test_when_first_created_it_is_not_cranky():
    centaur = Centaur("George", "Palomino")
    assert not centaur.is_cranky()

def test_when_first_created_it_is_standing_up():
    centaur = Centaur("George", "Palomino")
    assert centaur.is_standing()

def test_after_running_or_shooting_a_bow_three_times_it_gets_cranky():
    centaur = Centaur("George", "Palomino")
    assert not centaur.is_cranky()
    centaur.shoot()
    centaur.run()
    assert not centaur.is_cranky()
    centaur.shoot()
    assert centaur.is_cranky()

def test_when_cranky_it_will_not_shoot_a_bow():
    centaur = Centaur("George", "Palomino")
    centaur.shoot()
    centaur.shoot()
    centaur.shoot()
    assert centaur.shoot() == "NO!"

def test_when_cranky_it_will_not_run():
    centaur = Centaur("George", "Palomino")
    centaur.shoot()
    centaur.shoot()
    centaur.shoot()
    assert centaur.run() == "NO!"

def test_when_standing_it_will_not_sleep():
    centaur = Centaur("George", "Palomino")
    assert centaur.is_standing()
    assert centaur.sleep() == "NO!"

def test_after_laying_down_it_is_not_standing():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    assert not centaur.is_standing()
    assert centaur.is_laying()

def test_it_can_sleep_when_laying_down():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    assert not centaur.sleep() == "NO!"

def test_when_laying_down_it_cannot_shoot_a_bow():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    assert centaur.shoot() == "NO!"

def test_when_laying_down_it_cannot_run():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    assert centaur.run() == "NO!"

def test_it_can_stand_up():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    centaur.stand_up()
    assert centaur.is_standing()

def test_after_sleeping_it_is_no_longer_cranky():
    centaur = Centaur("George", "Palomino")
    centaur.shoot()
    centaur.run()
    centaur.shoot()
    assert centaur.is_cranky()

    centaur.lay_down()
    centaur.sleep()
    assert not centaur.is_cranky()

    centaur.stand_up()

    assert centaur.shoot() == "Twang!!!"
    assert centaur.run() == "Clop clop clop clop!!!"

def test_becomes_rested_after_drinking_a_potion():
    centaur = Centaur("George", "Palomino")
    assert not centaur.is_cranky()
    centaur.shoot()
    centaur.run()
    centaur.run()
    assert centaur.is_cranky()
    centaur.drink_potion()
    assert not centaur.is_cranky()

def test_can_only_drink_potion_while_standing():
    centaur = Centaur("George", "Palomino")
    centaur.lay_down()
    assert centaur.drink_potion() == "Can't, I'm laying"

def test_gets_sick_if_drinks_potion_while_rested():
    centaur = Centaur("George", "Palomino")
    assert not centaur.is_cranky()
    assert centaur.drink_potion() == "Now I'm sick"

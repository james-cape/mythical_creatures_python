import pytest
from lib.wizard import *

def test_has_name():
    wizard = Wizard("Eric")
    assert wizard.name == "Eric"

def test_can_have_different_name():
    wizard = Wizard("Alex")
    assert wizard.name == "Alex"

def test_is_bearded_by_default():
    wizard = Wizard("Ben")
    assert wizard.is_bearded()

def test_is_not_always_bearded():
    wizard = Wizard("Valerie", bearded=False)
    assert not wizard.is_bearded()

def test_has_root_powers():
    wizard = Wizard("Sarah", bearded=False)
    assert wizard.incantation("chown ~/bin") == "sudo chown ~/bin"

def test_has_lots_of_root_powers():
    wizard = Wizard("Rob", bearded=False)
    assert wizard.incantation("rm -rf /home/mirandax") == "sudo rm -rf /home/mirandax"

def test_starts_rested():
    wizard = Wizard("Steve")
    assert wizard.is_rested()

def test_can_cast_spells():
    wizard = Wizard("Ben")
    assert wizard.cast() == "MAGIC MISSILE!"

def test_gets_tired_after_casting_three_spells():
    wizard = Wizard("Steve")
    wizard.cast()
    wizard.cast()
    assert wizard.is_rested()
    wizard.cast()
    assert not wizard.is_rested()

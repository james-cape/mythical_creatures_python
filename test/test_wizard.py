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
    assert wizard.is_bearded() == True

def test_is_not_always_bearded():
    wizard = Wizard("Valerie", bearded = False)
    assert wizard.is_bearded() == False

def test_has_root_powers():
    wizard = Wizard("Sarah", bearded = False)
    assert wizard.incantation("chown ~/bin") == "sudo chown ~/bin"

def test_has_lots_of_root_powers():
    wizard = Wizard("Rob", bearded = False)
    assert wizard.incantation("rm -rf /home/mirandax") == "sudo rm -rf /home/mirandax"

#   def test_starts_rested
#     skip
#     # create wizard
#     # .rested? returns true
#   end
#
#   def test_can_cast_spells
#     skip
#     # create wizard
#     # .cast returns "MAGIC MISSILE!"
#   end
#
#   def test_gets_tired_after_casting_three_spells
#     skip
#     # create wizard
#     # casts spell twice
#     # check wizard is rested
#     # casts spell
#     # check wizard is not rested
#   end

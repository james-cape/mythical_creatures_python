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



#
#   def test_when_staring_at_a_person_that_person_turns_to_stone
#     skip
#     medusa = Medusa.new("Cassiopeia")
#     victim = Person.new("Perseus")
#
#     refute victim.stoned?
#     medusa.stare(victim)
#     assert victim.stoned?
#   end
#
#   def test_can_only_have_three_victims
#     skip
#     # your code here
#   end
#
#   def test_if_a_fourth_victim_is_stoned_first_is_unstoned
#     skip
#     # your code here
#   end

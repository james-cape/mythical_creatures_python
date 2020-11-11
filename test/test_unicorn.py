import pytest
from lib.unicorn import *

def test_it_has_a_name():
    unicorn = Unicorn("Robert")
    assert unicorn.name == "Robert"

def test_it_is_white_by_default():
    unicorn = Unicorn("Robert")
    assert unicorn.color == "white"
    assert unicorn.is_white()

def test_it_does_not_have_to_be_white():
    unicorn = Unicorn("Robert", "purple")
    assert unicorn.color == "purple"
    assert not unicorn.is_white()

def test_unicorn_says_sparkly_stuff():
    unicorn = Unicorn("Robert")
    assert unicorn.say("Wonderful!"), "**;* Wonderful! **;*"
    assert unicorn.say("I don't like you very much"), "**;* I don't like you very much **;*"

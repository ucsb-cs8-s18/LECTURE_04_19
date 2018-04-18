# CS5nm, E01 2009M
#  This is question from an old midterm
# It has some test cases written in the old "check_expect" style.
# Here is what those test cases would look like today, using pytest


def theLongerOne(s1,s2):
    return "stub" # this is an incorrect solution

def test_theLongerOne_1():
    assert theLongerOne("mouse","cat")=="mouse"

def test_theLongerOne_2():
    assert theLongerOne("mouse","chicken")=="chicken"

def test_theLongerOne_3():
    assert theLongerOne("cat","dog")=="cat"
    

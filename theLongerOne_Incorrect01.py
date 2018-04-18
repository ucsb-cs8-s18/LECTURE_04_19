# CS5nm, E01 2009M
#  This is question from an old midterm
# It has some test cases written in the old "check_expect" style.
# Here is what those test cases would look like today, using pytest

# HERE IS AN ANSWER THAT HAS PERFECT LOGIC,
# BUT QUITE A FEW PYTHON SYNTAX PROBLEMS.

# Can you spot them all?

def theLongerOne("animal A","animal B"):
    if len('animal A') > len('animal B'):
        return animal A
    if len('animal B') > len('animal A'):
        return animal B
    if len('animal A') = len('animal B'):
        return animal A
    

def test_theLongerOne_1():
    assert theLongerOne("mouse","cat")=="mouse"

def test_theLongerOne_2():
    assert theLongerOne("mouse","chicken")=="chicken"

def test_theLongerOne_3():
    assert theLongerOne("cat","dog")=="cat"
    

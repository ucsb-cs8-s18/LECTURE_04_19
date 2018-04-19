# CS5nm, E01 2009M
#  This is question from an old midterm
# It has some test cases written in the old "check_expect" style.
# Here is what those test cases would look like today, using pytest

# HERE IS AN ANSWER THAT HAS PERFECT LOGIC,
# BUT QUITE A FEW PYTHON SYNTAX PROBLEMS.

# Can you spot them all?

def theLongerOne(animal_A,animal_B):
    if len(animal_A) > len(animal_B):
        return animal_A
    if len(animal_B) > len(animal_A):
        return animal_B
    if len(animal_A) == len(animal_B):
        return animal_A
    
def test_theLongerOne_1():
    assert theLongerOne("mouse","cat")=="mouse"

def test_theLongerOne_2():
    assert theLongerOne("mouse","chicken")=="chicken"

def test_theLongerOne_3():
    assert theLongerOne("cat","dog")=="cat"
    

noun = input("Pick a noun ")

verb = input("Pick a verb ")

body = input("Pick a body part ")

thing = input("Pick an object ")

def make_madlib(noun, verb, body, thing):
    return print("One day, Maggie walked across the %s to go to the store. When she got there, she %s onto the floor. She hurt her %s and the cashier got a %s to ease her pain." % (noun, verb, body, thing))

make_madlib(noun, verb, body, thing)

def make_madlib(noun, verb, body, thing):
    madlib = print("One day, Maggie walked across the %s to go to the store. When she got there, she %s onto the floor. She hurt her %s and the cashier got a %s to ease her pain." % (noun, verb, body, thing))
    return madlib 

make_madlib(noun, verb, body, thing)

person = input("What is your name?")
subject = input("What is your favorite subject?")

def fix_name(person):
    # DO THE THING THAT MAKES THE NAME CORRECT
    return person 

def make_madlib(person, subject):
    fixed_name = fix_name(person)
    madlib = print ("Your name is %s and your favorite subject is %s" % (fixed_name, subject))
    return madlib

make_madlib(person, subject)
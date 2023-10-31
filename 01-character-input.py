"""

Exercise 1:

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that 
they will turn 100 years old. Note: for this exercise, the
expectation is that you explicitly write out the year (and therefore 
be out of date the next year). If you want to do this in a generic 
way, see

"""

import datetime

name = input("What's your name? ").capitalize()
age = int(input(("And age? ")))

current_year = datetime.date.today()
year = current_year.year

century_birthday = year - age
century = century_birthday + 100
rem_years = century - year

print(f"Hi {name}! So you will turn 100 in the year {century}. That's in {rem_years} years time")

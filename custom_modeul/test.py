# import greetings
# greetings.say_hi()
# print(greetings.name)

# from greetings import name, say_hi
# print(name)
# say_hi()

# from ABCD import expence
# expence.calculate_expance()

# import ABCD.expence # expence ke chinaite hobe
# ABCD.expence.calculate_expance()

## nothing.py
# import ABCD.XYZ.nothing
# print(ABCD.XYZ.nothing.a)

# from ABCD.XYZ import nothing
# print(nothing.a)

## __init__
import ABCD
# print(ABCD.check_init) # access kora easy

ABCD.expence.calculate_expance() # import pura file path deya lagtese na
# ABCD.calculate_expance()
ABCD.income.calculate_income() # import pura file path deya lagtese na
# ABCD.calculate_income()

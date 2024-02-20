def add(first_param, second_param):
    added= int(first_param) + int(second_param)
    return added

def subtract(first_param, second_param):
    subtracted= int(first_param) - int(second_param)
    return subtracted

def multiply(first_param, second_param):
    multiplied= int(first_param) * int(second_param)
    return multiplied

def divide(first_param, second_param):
    divided= int(first_param) / int(second_param)
    return divided

###############################################################################
# TODO: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def if_calc():
    print("Hello! How lovely for you to be here!")
    operator=input("""This is a calculator, which operation do you want to perform? These are the options:
    (+) Add *put "+" *
    (-) Subtract *put "-" *
    (*) Multiply put "*" *
    (/) Division put "/" *: """)
    first_param =input("What would you like your first variable to be?")
    second_param =input("Thanks, now how about a second variable?")
    print("Thanks")
    if operator == "+":
        added =add(first_param,second_param)
        print(added)
    if operator == "-":
        subtracted=subtract(first_param,second_param)
        print(subtracted)
    if operator == "*":
        multiplied=multiply(first_param,second_param)
        return multiplied
    if operator == "/":
        divided=divide(first_param,second_param)
        return divided
    else: print("Invalid Operation!")


if_calc()
###############################################################################
# TODO: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

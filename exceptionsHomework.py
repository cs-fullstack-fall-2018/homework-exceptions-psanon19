# *Problem 1*
# Handle the exception thrown by the code below by using try and except blocks. Display a meaningful message.
#
# for i in ['a','b','c']:
#     print(i**2)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-1-908335551eea> in <module>()
# 1 for i in ['a','b','c']:
# ----> 2     print i**2
#
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# try:
#     for i in ['a','b','c']:
#         print()

# *Problem 2*
# # Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print('All Done.')

# x = 5
# y = 0
#
# z = x/y
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-3effb78be709> in <module>()
# 2 y = 0
# 3
# ----> 4 z = x/y
#
# ZeroDivisionError: integer division or modulo by zero

# *Problem 3*
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, else block to account for incorrect inputs.
#
# def ask():
#     *# STUDENTS, YOU FILL OUT THE FUNCTION LIKE WE DID IN CLASS THAT WILL PROMPT AND RESPOND AS FOLLOWS #*
#
# Input an integer: crappy_entry
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, you number squared is:  4


def ask():

    while True:
        try:
            n = int(input('Input an Integer: '))
        except:
            print ('An error occurred! Please try agian!')
            continue
        else:
            break
    return n

print('Thank you, your number squared is: ', ask()**2)
'''This function tries to convert a input to a float
If the conversion suceeds it returns the value as a float
else it consoles a error message and since it is in a loop it asks the user to submit a number.'''
#=============================================================================================
def number_verification():
    verification = False
    while verification == False:
        try:
            user_entry = float(input(f'Please fill in the grade: '))
            verification = True
            return float(user_entry)
        except ValueError:
            print('The input was not a number. Please try again below.')
#=============================================================================================
# Commands below were used to test my function.
number = number_verification()
print(number)
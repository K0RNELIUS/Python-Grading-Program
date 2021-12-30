'''This function takes as a parameter a list of options the program will consider
It verifies if the user entry is in the list
if it is the code allows the user to keep going
else it makes the user answer the question with one of the options.'''
#=============================================================================================
def finish_verification(options):
    verification = False
    while verification == False:
        user_entry = input('Would you like to continue using the calculator? ')
        if user_entry in options:
            verification = True
            return user_entry
        else:
            print('Please answer the question with yes or no.')
#=============================================================================================
# Commands below were used to test my function.
answer = finish_verification(options=['Yes', 'yes', 'No', 'no'])
print(answer)
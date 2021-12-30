# Functions below will be called in the main code of the program and have already been tested in their separate files.
#=============================================================================================
def number_verification(number):
    verification = False
    while verification == False:
        try:
            user_entry = float(input(f'Please fill in the {number} number of the operation: '))
            verification = True
            return float(user_entry)
        except ValueError:
            print('The input was not a number. Please try again below.')
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
# Main Code:
keep_going = True
while keep_going:



    # Checking if the user would like to keep going:
    answer = finish_verification(options=['Yes', 'yes', 'No', 'no'])
    if answer in ['No', 'no']:
        keep_going = False
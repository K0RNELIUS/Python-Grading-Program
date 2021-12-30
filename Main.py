# Functions below will be called in the main code of the program and have already been tested in their separate files.
#=============================================================================================
def number_verification_int(input_string):
    verification = False
    while verification == False:
        try:
            user_entry = int(input(f'Please fill in the {input_string}: '))
            verification = True
            return int(user_entry)
        except ValueError:
            print('The input was not a number. Please try again below.')
#=============================================================================================
def number_verification_float(input_string):
    verification = False
    while verification == False:
        try:
            user_entry = float(input(f'Please fill in the {input_string}: '))
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
grade_components_and_respective_weights = dict()
keep_going = True
percent_verification = True
while keep_going:

    # Checking if the user would like to keep going:
    answer = finish_verification(options=['Yes', 'yes', 'No', 'no'])
    if answer in ['No', 'no']:
        keep_going = False
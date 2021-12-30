'''This function has the objective to check if the user made number inputs
if these numbers are between 0 and 100 since we want percent values
once these requirements are met we will also need to see if the sum of the percent values are equal to 100
this part will be done in the components and weights section where we will have all of these weights'''
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
def components_and_weights(grade_components_and_respective_weights):
    percent_verification = False
    while percent_verification == False:
        number_of_components = number_verification_int('number of components in the grading system')
        for i in range(1, number_of_components + 1):
            component = input(f'The name of your number {i} component in your grading system is: ')

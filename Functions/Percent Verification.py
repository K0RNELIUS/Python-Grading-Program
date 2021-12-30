'''This function has the objective to check if the user made number inputs
if these numbers are between 0 and 100 since we want percent values
once these requirements are met we will also need to see if the sum of the percent values are equal to 100
this part will be done in the components and weights section where we will have all of these weights'''
#=============================================================================================
def percent_verification(input_string):
    verification = False
    while verification == False:
        try:
            user_entry = int(input(f'Please fill in the {input_string}: '))
            if 0 < user_entry <= 100:
                verification = True
                return int(user_entry)
            else:
                print('The input must also be a percent value (between 1 & 100). Please try again below.')
        except ValueError:
            print('The input was not a number. Please try again below.')
# =============================================================================================
# Testing the function implemented above:
percent_value = percent_verification('percent value')

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
#=============================================================================================
# Main Code:
#=============================================================================================
# Giving the user the option to chose the respective weights of each component in the grading system:
grade_components_and_respective_weights = dict()
percent_check = True
number_of_components = number_verification_int('number components in the grading system')
while percent_check:
    sum = 0
    for i in range(1, number_of_components + 1):
        component = input(f'{i}. component in the grading system: ')
        weight = percent_verification('percent value of the component said above')
        grade_components_and_respective_weights[component] = weight
    for keys in grade_components_and_respective_weights:
        sum += grade_components_and_respective_weights[keys]
    if sum == 100:
        percent_check = False
    else:
        print("The weights of the components did't add to 100%. Please fill them in again below.")
#=============================================================================================
# Entering the main loop where the teacher will be able to perform actions in the system:
keep_going = True
print('''Please type: 
1 - to add a student in the records
2 - to add a grade to a certain component
3 - to change information or grade of a student
4 - to display the grades of one student
5 - to display the grades of all students 
6 - to finish using the grading system''')
while keep_going:
    user_entry = number_verification_int('a number in our options')
    if user_entry == 1:
        print('vamos')
    elif user_entry == 2:
        print('vamos')
    elif user_entry == 3:
        print('vamos')
    elif user_entry == 4:
        print('vamos')
    elif user_entry == 5:
        print('vamos')
    elif user_entry == 6:
        keep_going = False
    else:
        print("The value typed isn't one of our options. Please try again below.")

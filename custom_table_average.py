# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a program that lets you input customly shaped table then finds the average of that table

from numpy import random

table = []

def find_average(array):
    # Finds the average
    
    array_average = 0.0
    total_elements = 0
    
    for add_up_columns in array:
        for add_total_elements in add_up_columns:
            array_average = array_average + add_total_elements
            total_elements = total_elements + 1
    
    array_average = array_average / total_elements
    
    return array_average

while True:
    # Gets the decision from the user whether they want to customize their lower and upper bounds of the random integer generation.
    
    chose_upper_lower_bounds = raw_input('Would you like to customize the upper and lower bounds of the random elements in your table? (yes/no) ')
    
    if chose_upper_lower_bounds == 'yes' or chose_upper_lower_bounds == 'Yes':
        while True:
            random_int_lower_bound = int(raw_input('Enter the lower bound: '))
            random_int_upper_bound = int(raw_input('Enter the upper bound: '))
            if random_int_lower_bound > random_int_upper_bound:
                print('The lower bound must be less than the upper bound.')
            else:
                break
        break
    
    elif chose_upper_lower_bounds == 'no' or chose_upper_lower_bounds == 'No':
        random_int_lower_bound = 0
        random_int_upper_bound = 100
        print('The lower bound is 0 and the upper bound is 100.')
        break
    
    else:
        print('Please enter "Yes" or "No".')

while True:
    # Gets the user input about how many columns and the number of elements in each column. Then it randomly generates elements based on the upper and lower bounds to fill the table.
    
    number_of_columns = int(raw_input('Enter the number of columns: '))
    
    if number_of_columns > 0:
        for add_row in range(0, int(number_of_columns)):
            table.append([])
            while True:
                elements_in_column = int(raw_input('Enter the number of elements in column ' + str(add_row + 1) + ': '))
                if elements_in_column > 0:
                    for add_element in range(0, int(elements_in_column)):
                        table[add_row].append(random.randint(int(random_int_lower_bound),
                                              int(random_int_upper_bound) + 1))
                    break
                else:
                    print('The number of elements must be above 0.')
        break
    else:
        print('The number of columns must be above 0.')

# Finds the average then prints it along with the table.
average = find_average(table)
print('Your table is: ' + str(table))
print('Your average is: ' + str(round(average, 4)))

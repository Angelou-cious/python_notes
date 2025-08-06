# creating variables

#string typed variable
string_name = 'sample_name'

#integer types variable
int_age = 69

#float typed variable
float_height = 89.1

#boolean typed variable
is_alive = True

#list type variable
list_fruits = ["apple", "orange", "berry"]
list_ages = [1,2,3,4,5]

list_fruits.append("grape") # add to the last list
list_ages.append(9) # add to the last list


# a variable can be change to assignment
list_ages = [5,4,3,2,1]

print(list_ages, list_fruits, is_alive, string_name, int_age, is_alive, float_height)


print(isinstance(list_ages, list))
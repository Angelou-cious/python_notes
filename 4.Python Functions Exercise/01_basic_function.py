# Define a function named 'person' that takes two parameters:
# - name: a string representing the person's name
# - age: a number representing the person's age
def person(name, age):
    
    # Print a formatted string using f-string syntax
    # that combines the name and age parameters into a greeting message
    print(f'Hi {name}, your now {age} year old.')

# Call the person function with arguments:
# - 'Angelou' as the name parameter
# - 13 as the age parameter
person('Angelou', 13)
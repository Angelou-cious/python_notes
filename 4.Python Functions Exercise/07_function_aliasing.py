# Define a function named 'display_student' that takes two parameters: name and age
def display_student(name, age):
    # Print the name and age parameters passed to the function
    print(name, age)

# Call the display_student function with arguments "Emma" and 26
# This will print: Emma 26
display_student("Emma", 26)

# Create an alias/reference to the display_student function
# show_student now points to the same function as display_student
# This is called function aliasing
show_student = display_student

# Call the same function using the alias name 'show_student'
# This will print: Angelou 40
# It behaves exactly the same as display_student("Angelou", 40)
show_student('Angelou', 40)
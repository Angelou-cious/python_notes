# Define a function 'show_employee' with two parameters: name and salary (salary has default value 9000)
def show_employee(name, salary=9000):
    
    # Print employee details using f-string. :<3 ensures minimum width of 3 characters for alignment
    print(f'Name: {name:<3} Salary: {salary:<3}')

# Call function with both parameters (name='Angelou', salary=8000)
show_employee('Angelou', 8000)

# Call function with only name parameter, salary will use default value of 9000
show_employee('Angelou')
# Define a function that takes two parameters: animal_type and pet_name
def describe_pet(animal_type, pet_name):
    
    # Print a formatted string using f-string syntax to display the pet's name and type
    print(f'{pet_name} and a {animal_type}')


# Call the function with positional arguments: 'hustkou' as animal_type, 'hunter' as pet_name
describe_pet('hustkou', 'hunter')

# Call the function with keyword arguments, explicitly specifying which parameter gets which value
describe_pet(animal_type='hello', pet_name='huntest')

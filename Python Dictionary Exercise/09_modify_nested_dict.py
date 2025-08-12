"""
    Exercise 9: Modify Nested Dictionary
"""

def mod_dict(dict): # Define a function named mod_dict that takes a dictionary as an argument.

    dict["class"]["student"]["name"] = "Jessa" # Access the nested dictionary and change the value of the "name" key to "Jessa".

    return dict # Return the modified dictionary.



nested_student_dict = { # Define a nested dictionary.
    "class": { # The first level of the dictionary with a key "class".
        "student": { # The second level of the dictionary with a key "student".
            "name": "Mike", # The third level of the dictionary with a key "name" and value "Mike".
            "marks": { # The third level of the dictionary with a key "marks".
                "physics": 70, # A key-value pair within the "marks" dictionary.
                "history": 80 # A key-value pair within the "marks" dictionary.
            }
        }
    }
}

x = mod_dict(nested_student_dict) # Call the mod_dict function with the nested_student_dict and store the returned dictionary in x.

print(x) # Print the modified dictionary.

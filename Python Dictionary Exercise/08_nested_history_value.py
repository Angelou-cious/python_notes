"""
    Exercise 8: Print the value of key ‘history’ from nested dict


"""

sampleDict = { # Define a nested dictionary.
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

history = sampleDict["class"]["student"]["marks"]["history"] # Access the value of the "history" key from the nested dictionary.

print(history) # Print the value of the "history" key.

"""
    Exercise 15: Get the key of a minimum value

    Write a code to print the key of a minimum value from the following dictionary.
"""

sample_dict = {  # Create sample dictionary with subject scores
    'Physics': 82,  # Physics score
    'Math': 65,  # Math score (lowest value)
    'following': 75  # History score
}

print(min(sample_dict, key=sample_dict.get))  # Find and print the key with minimum value using min() with key parameter

print(max(sample_dict, key=sample_dict.get))  # Find and print the key with maximum value using max() with key parameter

print(min(sample_dict, key=lambda x : len(x)))  # Find and print the key with shortest length using min() with lambda function

print(max(sample_dict, key=lambda x : len(x)))  # Find and print the key with longest length using max() with lambda function


"""
    Exercise 14: Filter Tuples

    Write a code to filter out students with scores less than 90 from a given a list of tuples.
"""

# Original list of student tuples, where each tuple contains a name and a score.
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Initialize an empty list to store students with scores of 90 or higher.
new_list = []
# Iterate through each student tuple in the 'students' list.
for item in students:
    # Check if the student's score (the second element in the tuple) is 90 or greater.
    if item[1] >= 90:
        # If the score is 90 or higher, add the student's tuple to 'new_list'.
        new_list.append(tuple(item))

# Print the list of students who have a high average.
print(f'Student with High Average: {new_list}')

# Use a list comprehension to create a new list of students with scores of 90 or higher.
# This is a more concise way to achieve the same result as the loop above.
student = [student for student in students if student[1] >= 90]
# Print the list of students created using the list comprehension.
print(student)

"""
    You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
"""

# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]


def add_list(sub_list, list1):

    list1 = list1

    for sub in sub_list:
        list1[2][1][2].append(sub)

    return list1

print(f'Output: {add_list(sub_list, list1)}')
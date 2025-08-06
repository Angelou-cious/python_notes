
def middle_last(s1,s2):

    first = s1[0] + s2[0]
    middle = s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)]
    last = s1[-1]  + s2[-1]


    print(f'{first}{middle}{last}')

s1 = "America"
s2 = "Japan"

middle_last(s1, s2)

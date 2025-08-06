
def mix_string(s1,s2):

    new_string = []

    s2_reversed = s2[::-1]

    for a, b in zip(s1, s2_reversed):

        new_string.append(a + b)

    return ''.join(new_string)

s1 = "Abc"
s2 = "Xyz"
s3 = mix_string(s1,s2)

print(s3)
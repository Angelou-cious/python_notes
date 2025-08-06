# print reverse for l

num = 10

for i in range(1, num + 1):
    for j in range(num - i + 1):
        print(i, end=" ")
    print()
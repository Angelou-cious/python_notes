def myfunc(ranges):
    
    previous_num = 0

    print('Printing current and \
          previous number sum in a range(10)')
    
    for i in range(ranges):
        sum = previous_num + i

        print(f'Current Number {i} Previous Number  {previous_num}  Sum: {sum}')

        previous_num += 1

print(myfunc(10))
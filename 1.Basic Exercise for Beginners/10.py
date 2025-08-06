def myfunc(list1,list2):
    
    print(f'{list1}\n{list2}')

    new_list = []

    for i in list1:
        if i % 2 != 0:
            new_list.append(i)
        


    for i in list2:
        if i % 2 == 0:
            new_list.append(i)
        

    return new_list

print(f"merge lists: {myfunc([10, 20, 25, 30, 35],[40, 45, 60, 75, 90])}")
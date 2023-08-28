#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = ""
        count = 0

        for i in my_list:
            count += 1

        if x < count:
            count = x

        for i in range(1, count + 1):
            new_list = new_list + str(i)

        print(new_list)

        return my_list[count - 1]
    except IndexError:
        print("Index Error found")

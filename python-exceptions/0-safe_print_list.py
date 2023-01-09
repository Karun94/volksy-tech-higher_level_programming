#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[e], end="")
            e += i
            except:
            pass
    print('')
    return e

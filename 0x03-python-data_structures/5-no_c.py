#!/usr/bin/python3
def no_c(my_string):
    j = 0
    my_string1 = my_string[:]
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            my_string1 = my_string1[:(i - j)] + my_string[(i + 1):]
            j += 1
    return (my_string1)

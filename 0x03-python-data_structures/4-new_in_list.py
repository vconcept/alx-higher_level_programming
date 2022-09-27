#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    my_list1 = my_list[:]
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list1[idx] = new_element
        return (my_list1)

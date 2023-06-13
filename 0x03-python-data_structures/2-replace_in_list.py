#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    mylist_length = len(my_list)
    if idx < 0:
        return(my_list)
    if idx > (mylist_length - 1):
        return(my_list)
    my_list[idx] = element
    return(my_list)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_y = tuple_a + (0, 0)
    tuple_z = tuple_b + (0, 0)
    newtuple = (tuple_y[0] + tuple_z[0], tuple_y[1] + tuple_z[1])
    return newtuple

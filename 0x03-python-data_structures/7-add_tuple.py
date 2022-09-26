#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        return tuple_b
    elif len(tuple_a) < 2:
        return (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif not tuple_b:
        return tuple_a
    elif len(tuple_b) < 2:
       return (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif (len(tuple_a) >= 2 or len(tuple_b) >= 2):
        return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

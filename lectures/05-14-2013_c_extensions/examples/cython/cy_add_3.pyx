"""
Cython implimentation of the add.c example

This one calls an actual C function to do the work

creates a cython funcion to call the C function.

"""

cdef extern from "add.h":
    # pull in C add funciton, renaming to c_add for Cython
    int c_add "add" (int x, int y)


def add(x, y):
    return c_add(x, y)









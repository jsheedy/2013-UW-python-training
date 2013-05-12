#!/usr/bin/env python

"""
simple test code for cy_add
"""

import cy_add


def test_1():
    assert cy_add.add(3,4) == 7

def test_2():
    assert cy_add.add(5,6) == 11


if __name__ == "__main__":
    test_1()
    test_2()
    print "if you didn't get an asertion, it worked"





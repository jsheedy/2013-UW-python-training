#!/usr/bin/env python

from integrate import integrate_f as _integrate_f
from decorators import timer

@timer
def integrate_f(*args):
    return _integrate_f(*args)

a = 0.0
b = 10.0

for N in (10**i for i in xrange(1,8)):
    print "Numerical solution with N=%(N)d : %(x)f" % \
        {'N': N, 'x': integrate_f(a, b, N)}

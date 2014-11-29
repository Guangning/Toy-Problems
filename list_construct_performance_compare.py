#!/usr/bin/env python

# This code is to look at the performance when using four different ways to 
# generate a list of n numbers starting with 0.

import timeit

def list_construct1(length_of_list):
    l = []
    for i in range(length_of_list):
        l = l + [i]
    return l

def list_construct2(length_of_list):
    l = []
    for i in range(length_of_list):
        l.append(i)
    return l

def list_construct3(length_of_list):
    l = [i for i in range(length_of_list)]
    return l

def list_construct4(length_of_list):
    l = range(length_of_list)
    return l

time1 = timeit.Timer('list_construct1(1000)', 'from __main__ import list_construct1')
time2 = timeit.Timer('list_construct2(1000)', 'from __main__ import list_construct2')
time3 = timeit.Timer('list_construct3(1000)', 'from __main__ import list_construct3')
time4 = timeit.Timer('list_construct4(1000)', 'from __main__ import list_construct4')

print 'concat        took %.8f seconds' % time1.timeit(number=1000)
print 'append        took %.8f seconds' % time2.timeit(number=1000)
print 'comprehension took %.8f seconds' % time3.timeit(number=1000)
print 'list range    took %.8f seconds' % time4.timeit(number=1000)


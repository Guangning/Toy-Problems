#!/usr/bin/env python

'''
How many ways can you draw N cards from a deck of cards?
'''

from math import factorial

CARDS_NUM = 52

def calculate_number_of_ways(N):
    '''
    drawing cards without replacement
    '''
    return factorial(CARDS_NUM) / (factorial(N) * factorial(CARDS_NUM - N))

if __name__ == '__main__':
    N = raw_input('> How many cards do you want to draw from a deck? ')
    res = calculate_number_of_ways(int(N))
    print('> There are %d ways of doing that!' % res)

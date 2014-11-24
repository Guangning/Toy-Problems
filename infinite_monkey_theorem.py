word_list = ['cat', 'dog', 'rabbit']
letter_list = []

#for word in word_list:
#    for letter in word:
#        if letter not in letter_list:
#            letter_list.append(letter)

#letter_list = list(set([c for c in ''.join(word_list)]))
#
#print letter_list

import math

#number = input('Please enter a number: ')

#try:
#    print math.sqrt(number)
#except:
#    print 'Bad value for square root'

#if number < 0:
#    raise RuntimeError('You cant use a negative number!')
#else:
#    print math.sqrt(number)
#
#print 'Hello, world!'

def square_root(n):
    iteration = 20   # times of iteration
    root = n / 2.0   # first guess

    for k in range(iteration):
        root = (1.0 / 2.0) * (root + (n / root))
    return root

#print square_root(number)

import random
import string


def gen_random_string(n):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    sentence = ''
    for i in range(n):
        sentence = sentence + random.choice(letters)
    return sentence

def eval_random_string(random, target):
    score = 0.0
    for i in range(len(target)):
        if random[i] == target[i]:
            score += 1.0
    #print 'random sentence is: %s' % random
    #print 'target sentence is: %s' % target
    #print 'score is: %.0f'         % score
    return score

def try_n_times(times):
    target = 'methink it is like a weasel'
    best_string = ''
    best_score = 0.0
    for i in range(times):
        random = gen_random_string(len(target))
        score = eval_random_string(random, target)
        if score > best_score:
            best_score = score
            best_string = random
    print 'orig sentence is: %s' % target
    print 'best sentence is: %s' % best_string
    print 'best score is: %.0f'  % best_score
    return best_string

def find_the_best_string():
    target = 'methi'
    score = 0.0
    times = 0.0
    while score != len(target):
        random = gen_random_string(len(target))
        score = eval_random_string(random, target)
        times += 1.0
    print 'it used %.0f time to find the best string' % times

try_n_times(10000)
find_the_best_string()


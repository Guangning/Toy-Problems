#!/usr/bin/env python

# The infinite monkey theorem states that a monkey hittig keys at random on a 
# typewriter keyboard for an infinite amount of time will almost surely type a 
# given text, such as the complete works of William Shakespeare.

import random
import string

def dummy_monkey_typing(target_sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    length_of_sentence = len(target_sentence)
    random_sentence = ''
    for i in range(length_of_sentence):
        random_sentence = random_sentence + random.choice(letters)
    return random_sentence

def compare_two_sentences(random_sentence, target_sentence):
    if len(random_sentence) != len(target_sentence):
        raise RuntimeError('Please compare two sentences of the same length!')
    score = 0.0
    for i in range(len(target_sentence)):
        if random_sentence[i] == target_sentence[i]:
            score += 1.0
    return int(score)

def dummy_monkey_try_n_times(target_sentence, number_of_times):
    best_sentence = ''
    best_score = 0.0
    for i in range(number_of_times):
        random_sentence = dummy_monkey_typing(target_sentence)
        score = compare_two_sentences(random_sentence, target_sentence)
        if score > best_score:
            best_score = score
            best_sentence = random_sentence
    print ''
    print 'Dummy monkey has tried %d times:' % number_of_times
    print 'Orig sentence is: %s'             % target_sentence
    print 'Best sentence is: %s'             % best_sentence
    print 'Best score is: %d/%d characters'  % (best_score, len(target_sentence))
    print ''
    return best_sentence

def smart_monkey_typing(best_sentence_so_far, target_sentence):
    if len(best_sentence_so_far) != len(target_sentence):
        raise RuntimeError('Smart monkey needs two sentences of the same length!')
    letters = 'abcdefghijklmnopqrstuvwxyz '
    length_of_sentence = len(target_sentence)
    random_sentence = ''
    for i in range(length_of_sentence):
        if best_sentence_so_far[i] == target_sentence[i]:
            random_sentence = random_sentence + target_sentence[i]
        else:
            random_sentence = random_sentence + random.choice(letters)
    return random_sentence

def smart_monkey_try_n_times(target_sentence, number_of_times):
    best_sentence = dummy_monkey_typing(target_sentence)
    best_score = 0.0
    for i in range(number_of_times):
        best_sentence = smart_monkey_typing(best_sentence, target_sentence)
        best_score = compare_two_sentences(best_sentence, target_sentence)
    print ''
    print 'Smart monkey has tried %d times:' % number_of_times
    print 'Orig sentence is: %s'             % target_sentence
    print 'Best sentence is: %s'             % best_sentence
    print 'Best score is: %d/%d characters'  % (best_score, len(target_sentence))
    print ''
    return best_sentence

def main():
    target_sentence = input('Please enter the sentence you want: ')
    number_of_times = input('Please enter how many times you want the monkey to try: ')
    dummy_monkey_try_n_times(target_sentence, int(number_of_times))
    smart_monkey_try_n_times(target_sentence, int(number_of_times))

if __name__ == '__main__':
    main()


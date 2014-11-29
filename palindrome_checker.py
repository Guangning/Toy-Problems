#!/usr/bin/env python

# A palindrome is a string that reads the same forward and backward, for example,
# radar, toot, and madam. This program is to check whether the input string is a
# palindrome.

class Deque:

    def __init__(self, input_string):
        self.deque = list(input_string)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def whether_is_a_palindrome(self):
        still_equal = True
        while self.size() > 1 and still_equal:
            first = self.remove_front()
            last = self.remove_rear()
            if first != last:
                still_equal = False
        print still_equal

def main():
    print 'This program is to check whether a word is a palindrome.'
    input_string = input('Please input the word you want to check: ')
    word = Deque(input_string)
    word.whether_is_a_palindrome()

if __name__ == '__main__':
    main()


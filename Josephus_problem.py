#!/usr/bin/env python

# The problem is named after Flavius Josephus, a Jewish historian living in the
# 1st century. According to Josephus' account of the siege of Yodfat, he and his
# 40 soldiers were trapped in a cave, the exit of which was blocked by Romans.
# They chose suicide over captured and decided that they would form a circle and
# start killing themselves using a step of three. Josephus states that by luck or
# possibly by the hand of God, he and another man remained the last and gave up
# to the Romans.

# This program will input a list of names and a constant, call it "magic_number"
# to be used for counting. It will return the name of the last person remaining
# after repetitive counting by num.

class DeathQueue:

    # This is a actually a QUEUE.

    def __init__(self):
        self.items = []

    def is_all_dead(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

def get_the_last_man(names, magic_number):

    death_circle = Queue()
    name_list = names.replace(' ', '').split(',')


    for name in name_list:
        death_circle.enqueue(name)

#    while death_circle.size() > 1:
    for i in range(magic_number):
        death_circle.enqueue(death_circle.dequeue())
    print death_circle.display()
    for i in range(magic_number):
        death_circle.enqueue(death_circle.dequeue())
    print death_circle.display()

    for i in range(magic_number):
        death_circle.enqueue(death_circle.dequeue())
    print death_circle.display()
def main():

#    print "Please enter the name list, such as 'Batel, Asaf, Chaya, Dekel, Galia, Herut'."
#    names = input('Your name list is: ')
#    print ""
#
#    print "Please enter the magic number, such as '3'."
#    magic_number = input('Your magic number is: ')
#    print ""

    names = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n'
    magic_number = 3
    get_the_last_man(names, magic_number)

if __name__ == '__main__':
    main()


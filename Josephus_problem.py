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

class DeathCircle:

    # This is a actually a QUEUE.

    def __init__(self, name_list):
        self.persons = name_list

    def next_one(self):
        self.persons.insert(0, self.persons.pop())

    def kill_him(self):
        print '%s died.' % self.persons.pop()

    def how_many_left(self):
        return len(self.persons)

    def show_current_circle(self):
        print 'The current circle is: %s.' % self.persons

    def who_is_the_lucky_bastard(self, magic_number):
        while self.how_many_left() > 1:
            for i in range(magic_number - 1):
                self.next_one()
            self.kill_him()
        print 'The lucky bastard is %s.' % self.persons[0]

def main():

    print "Please enter the name list, such as 'Batel, Asaf, Chaya, Dekel, Galia, Herut'."
    names = input('Your name list is: ')
    print ""

    print "Please enter the magic number, such as '3'."
    magic_number = input('Your magic number is: ')
    print ""

    name_list = names.replace(' ', '').split(',')
    name_list.reverse()
    death_circle = DeathCircle(name_list)

    death_circle.show_current_circle()
    death_circle.who_is_the_lucky_bastard(magic_number)

if __name__ == '__main__':
    main()


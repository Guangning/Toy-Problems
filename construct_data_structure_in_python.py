#!/usr/bin/env python

# 1.Implement a stack in Python

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def main():

    # 1.Test a stack
    s = Stack()
    print s.is_empty()
    s.push(4)
    print s.peek()
    s.push('dog')
    print s.peek()
    s.push(True)
    print s.peek()
    s.push(8.4)
    print s.peek()
    print s.size()
    print s.pop()
    print s.size()

if __name__ == '__main__':
    main()

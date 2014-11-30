#!/usr/bin/env python

# Fractals come from a branch of mathematics, and have much in common with recursion.
# The definition of a fractal is that when you look at it the fractal has the same
# basic shape no matter how much you magnify it. Some examples from nature are the
# coastlines of continents, snowflakes, mountains, and even trees or shrubs.

# This program uses Python Turtle module to recursively draw a fractal tree.

import turtle

def tree(branch_length, turtle):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        tree(branch_length - 15, turtle)

        turtle.left(40)
        tree(branch_length - 15, turtle)

        turtle.right(20)
        turtle.backward(branch_length)

def main():
    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()

    # Go to the initial position
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color('green')
    my_screen.bgcolor('black')

    # Collect inputs
    main_branch_length = input('Please enter the length of main branch, such as 100: ')

    # Draw a fractal tree
    tree(int(main_branch_length), my_turtle)

    my_screen.exitonclick()

if __name__ == '__main__':
    main()


#!/usr/bin/env python3

"""
At the bottom of this page is a very long file called mystery.txt The lines of this file contain either the word UP or DOWN or a pair of numbers. UP and DOWN are instructions for a turtle to lift up or put down its tail. The pairs of numbers are some x,y coordinates. Write a program that reads the file mystery.txt and uses the turtle to draw the picture described by the commands and the set of points.
"""

import turtle


def get_data():
    data = open("mystery.txt", "r")
    values = []
    for line in data:
        line = line.rstrip()
        if line == "UP" or line == "DOWN":
            values.append(line)
        else:
            line = line.split()
            line[0] = int(line[0])
            line[1] = int(line[1])
            values.append(line)
    return values


def create_screen():
    wn = turtle.Screen()
    return wn


def create_turtle():
    tess = turtle.Turtle()
    return tess


def draw_mystery(t, acts):
    for act in acts:
        if act == "UP":
            t.penup()
        elif act == "DOWN":
            t.pendown()
        else:
            t.goto(act[0], act[1])


wn = create_screen()
draw_mystery(create_turtle(), get_data())
wn.exitonclick()
from turtle import Turtle
import math


def drawCircle(t, center, radius):
    t = Turtle()
    degree = 3
    count = 0
    center = (2.0 * math.pi * radius / 120)
    t.home()
    t.setheading(degree)
    while count <= 120:
        t.down()
        t.forward(2.0 * math.pi * radius / 120)
        t.up()
        degree += 3
        t.setheading(degree)
        count += 1

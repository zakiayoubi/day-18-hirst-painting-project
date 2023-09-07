from turtle import Turtle, Screen
import turtle
import random

zaki = Turtle()
zaki.pensize(1)
zaki.speed(0)
paths = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def colorful_circles():
    for i in range(90):
        zaki.pencolor(random_color())
        zaki.circle(100)
        zaki.right(4)


colorful_circles()

screen = Screen()
screen.exitonclick()




















# from turtle import Turtle, Screen
# import turtle
# import random
#
# zaki = Turtle()
# zaki.pensize(10)
# zaki.speed(0)
# paths = [0, 90, 180, 270]
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# def draw_random_walk():
#     for i in range(40):
#         zaki.pencolor(random_color())
#         zaki.forward(30)
#         zaki.setheading(random.choice(paths))
#
#
# draw_random_walk()
#
# screen = Screen()
# screen.exitonclick()
#
#














# from turtle import Turtle, Screen
# import random
#
# zaki = Turtle()
# zaki.penup()
# zaki.goto(-50, 100)
# zaki.pendown()
# num_sides = 3
# colors = ["red", "blue", "yellow", "black", "green"]
#
#
# def draw_shape():
#     global num_sides
#     zaki.pencolor(random.choice(colors))
#     for i in range(num_sides):
#         zaki.forward(100)
#         zaki.right(360 / num_sides)
#     num_sides += 1
#
#
# while num_sides <= 10:
#     draw_shape()
#
# screen = Screen()
# screen.exitonclick()

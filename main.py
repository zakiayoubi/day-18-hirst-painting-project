from turtle import Turtle, Screen
import turtle
import random

colors_list = [(243, 243, 245), (244, 240, 232), (244, 237, 242), (236, 243, 240), (214, 154, 105), (49, 96, 139),
               (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18),
               (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156),
               (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52),
               (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)
               ]

zaki = Turtle()
zaki.speed(0)
turtle.colormode(255)


def colorful_circles():
    distance = 0
    for j in range(10):
        zaki.penup()
        zaki.goto(-200, -200 + distance)
        zaki.pendown()
        distance += 50
        for i in range(10):
            zaki.dot(20, random.choice(colors_list))
            zaki.penup()
            zaki.forward(50)
            zaki.pendown()


colorful_circles()

screen = Screen()
screen.exitonclick()

# import colorgram
# colors_list = []
# colors = colorgram.extract("hirst_painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
#
# print(colors_list)

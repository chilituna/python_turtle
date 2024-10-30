# import colorgram
#
# colors = colorgram.extract('2queens.jpg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     color_list.append(rgb_color)
# print(color_list)
import random
import turtle
from turtle import Turtle, Screen

color_list = [(68, 99, 65), (139, 102, 42), (28, 31, 38), (148, 63, 75), (30, 57, 45), (174, 139, 22), (44, 76, 53), (56, 32, 45), (189, 79, 84), (75, 86, 98), (105, 43, 61), (41, 37, 21), (189, 82, 78), (158, 156, 127), (78, 77, 29), (136, 153, 135), (52, 60, 82), (103, 147, 76), (137, 147, 158), (52, 69, 71), (91, 52, 49), (218, 201, 183), (176, 138, 146), (115, 124, 146), (206, 197, 158), (194, 202, 219), (117, 132, 135), (195, 212, 196), (180, 200, 180), (210, 198, 202)]

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
t.penup()
t.hideturtle()
t.speed(10)
x = -250
y = -250
t.setpos(x, y)
for _ in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    y += 50
    x = -250
    t.setpos(x, y)
print(t.position())

screen.exitonclick()
# import colorgram
#
# rgb_colors=[]
# colors = colorgram.extract('painting.jpg', 20)
# for x in colors:
#     #rgb_colors.append(x.rgb)
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(249, 248, 248), (239, 246, 244), (235, 240, 244), (248, 242, 246), (2, 13, 31), (53, 25, 17), (219, 127, 106),
 (9, 105, 159), (242, 213, 68), (149, 83, 39), (215, 87, 64), (164, 162, 32), (158, 7, 24), (157, 62, 102),
 (11, 62, 31), (206, 74, 104), (97, 6, 20), (11, 96, 57), (173, 135, 162), (0, 63, 145)]

import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
#move starting dot to the left

tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)



def pattern():

    for i in range(10):
        for i in range(10):
            tim.dot(18, random.choice(color_list))
            tim.penup()
            tim.forward(50)

        tim.backward(50)
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.penup()
        tim.forward(450)
        tim.left(180)

pattern()

screen = Screen()
screen.exitonclick()
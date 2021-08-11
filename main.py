import colorgram
import turtle
import random

colors = colorgram.extract('hirst.jpg', 10)
rgb_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if (r + g + b) < 740:
        rgb_list.append((r, g, b))

tim = turtle.Turtle()
tim.speed(0)
turtle.colormode(255)
tim.penup()
y = 225
tim.goto(-225, y)

for _ in range(9):
    tim.dot(20, random.choice(rgb_list))
    for _ in range(9):
        tim.forward(50)
        tim.dot(20, random.choice(rgb_list))
    y -= 50
    tim.goto(-225, y)

print(rgb_list)
screen = turtle.Screen()

screen.exitonclick()
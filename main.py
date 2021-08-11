from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(10)
colors = ["LightSteelBlue", "SkyBlue", "DarkCyan", "MediumSpringGreen", "Gold", "RosyBrown", "MediumVioletRed", "MediumPurple"]

screen = Screen()
screen.colormode(255)

for _ in range(100):
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(rand_color)
    tim.setheading(random.randint(0, 360))
    tim.forward(25)



screen.exitonclick()
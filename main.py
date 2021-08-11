from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed(10)
colors = ["LightSteelBlue", "SkyBlue", "DarkCyan", "MediumSpringGreen", "Gold", "RosyBrown", "MediumVioletRed", "MediumPurple"]

for _ in range(100):
    tim.pencolor(random.choice(colors))
    tim.setheading(random.choice([0, 90, 180, 270]))
    tim.forward(25)


screen = Screen()

screen.exitonclick()
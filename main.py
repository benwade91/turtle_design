import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed(0)
colors = ["LightSteelBlue", "SkyBlue", "DarkCyan", "MediumSpringGreen", "Gold", "RosyBrown", "MediumVioletRed", "MediumPurple"]

turtle.colormode(255)
heading = 0
for _ in range(100):
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(rand_color)
    tim.setheading(heading)
    tim.circle(150)
    heading += 20

screen = turtle.Screen()
screen.exitonclick()
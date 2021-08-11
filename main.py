from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.goto(-50, 150)
tim.pendown()
tim.pensize(15)
colors = ["white", "white", "white", "LightSteelBlue", "SkyBlue", "DarkCyan",
          "MediumSpringGreen", "Gold", "RosyBrown", "MediumVioletRed", "MediumPurple"]

for i in range(3, 11):
    tim.pencolor(colors[i])
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)


screen = Screen()
screen.exitonclick()
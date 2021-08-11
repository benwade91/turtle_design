from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

tim.penup()
tim.goto(-50, 50)
tim.pendown()

for _ in range(4):
    tim.forward(100)
    tim.rt(90)



screen = Screen()
screen.exitonclick()
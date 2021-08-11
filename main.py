from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.goto(-200, 0)
tim.pendown()

for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen = Screen()
screen.exitonclick()
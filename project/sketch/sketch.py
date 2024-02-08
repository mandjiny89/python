import turtle
from turtle import Turtle, Screen
s = Screen()
t = Turtle()
t.shape("turtle")
t.speed(0)

def m_forward():
    t.forward(10)
def m_backward():
    t.backward(10)
def m_left():
    current_heading = t.heading() + 10
    t.setheading(current_heading)
def m_right():
    current_heading = t.heading() - 10
    t.setheading(current_heading)
def clear():
    t.clear()
    t.penup()main.py
    t.home()

s.listen()
s.onkey(key="w", fun=m_forward)
s.onkey(key="s", fun=m_backward)
s.onkey(key="d", fun=m_left)
s.onkey(key="a", fun=m_right)
s.onkey(key="c", fun=clear)


# Screen exit should be in the end
s.setup(width=1000, height=1000)

s.exitonclick()
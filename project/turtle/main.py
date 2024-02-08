import turtle
from turtle import Turtle, Screen
import random
import colorgram

t = Turtle()
t.shape("turtle")
t.speed(0)
turtle.colormode(255)
t.hideturtle()


# ToDo get the colors from the given image and store it in a list as tuples,
#  so we can use in our turtle drawing

# Image color extraction
color_palette = []
color_list = colorgram.extract('hirst.jpg', 2 ** 6)

def pick_color():
    for count in range(len(color_list)):
        extract = color_list[count]
        r = extract.rgb.r
        g = extract.rgb.g
        b = extract.rgb.b
        one_color = (r, g, b)
        color_palette.append(one_color)

def initial_position():
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)

def move_left(f_count):
    global forward_count
    t.penup()
    t.left(90)
    t.forward(f_count)
    forward_count += 50

def move_right():
    t.penup()
    t.right(90)

def turtle_work():
    for _ in range(10):
        t.pencolor(random.choice(color_palette))
        t.pendown()
        t.dot(20)
        t.penup()
        t.forward(50)
    t.home()

pick_color()

count = 0
forward_count = 50

initial_position()
turtle_work()

while count <=8:
    count += 1
    initial_position()
    move_left(forward_count)
    move_right()
    turtle_work()

# Screen exit should be in the end
t_screen = Screen()
t_screen.setup(width=1000, height=1000)
t_screen.exitonclick()


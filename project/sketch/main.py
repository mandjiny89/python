import random
import turtle
from turtle import Turtle, Screen

# ToDO: Create a popup at the screen asking which color will win,
#  Once entered will bring all the turtles to the race and it will start the race.
#  When one of the turtle hit the end of the screen it will finish the game. Enter the result in the console


t1 = Turtle()
t1.shape("turtle")
t1.color("green")

t2 = Turtle()
t2.shape("turtle")
t2.color("blue")

t3 = Turtle()
t3.shape("turtle")
t3.color("orange")

t4 = Turtle()
t4.shape("turtle")
t4.color("cyan")

t5 = Turtle()
t5.shape("turtle")
t5.color("red")

t6 = Turtle()
t6.shape("turtle")
t6.color("yellow")

s = Screen()
s.setup(width=500, height=400)
result = s.textinput("Winner", "select your Turtle:")

turtle_list = [t1, t2, t3, t4, t5, t6]
turtle_start_position = [-100, -60, -20, +20, +60, +100]
is_running = False

def initial_state():
    for T in turtle_list:
        T.penup()
        for position in range(len(turtle_start_position)):
        T.goto(x=-230, y=turtle_start_position[position])


def turtle_move():
    if result:
        is_running = True
    while is_running:
        for T in turtle_list:
            if T.xcor() > 230:
                winning_color = T.pencolor()
                if winning_color == result:
                    print(f"You won, The winning color is {winning_color} won")
                else:
                    print(f"You lose, The winning color is {winning_color} ")
            T.forward(random.randint(0, 10))

initial_state()
turtle_move()


# Screen exit should be in the end

print(result)
s.exitonclick()
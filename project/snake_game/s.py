from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segment = []
        self.set_snake_position()
        self.head = self.segment[0]

    def set_snake_position(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_instance = Turtle("square")
        new_instance.color("white")
        new_instance.penup()
        new_instance.goto(position)
        self.segment.append(new_instance)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move_snake(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




from turtle import Turtle, Screen
import time
Move_Distance = 20
screen = Screen()
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_Snake()
        self.head = self.segments[0]



    def create_Snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(Move_Distance)

    def move_forward(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_backward(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def turn_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)









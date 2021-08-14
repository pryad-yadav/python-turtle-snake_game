from time import clock_getres
from turtle import Turtle, position

START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_STEPS = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment(START_POSITION[i])

    def add_segment(self,positon):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(positon)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                newX  = self.segments[seg_num -1 ].xcor()
                newY  = self.segments[seg_num -1 ].ycor()
                self.segments[seg_num].goto((newX,newY))
            self.segments[0].fd(MOVE_STEPS)

    def up(self):
        if self.segments[0].heading() != 270:  
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:  
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:  
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:  
            self.segments[0].setheading(0)
from turtle import Turtle,Screen
import random
# these are constants
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.make_snake()
        self.head=self.segments[0]

    def make_snake(self):
        for i in range(3):
            self.add_segment(POSITIONS[i])


    def reset_snake(self):
        for segment in self.segments:
            segment.setpos(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.head=self.segments[0]



    def add_segment(self,position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.up()
        new_turtle.setpos(position)
        self.segments.append(new_turtle)

    def extend_snake(self):

            self.add_segment(self.segments[-1].pos())
            # x_cor=self.segments[-1].xcor()
            # y_cor=self.segments[-1].ycor()
            # if self.segments[-1].heading() == 0:
            #    self.add_segment((x_cor-10,y_cor))
            #
            # elif self.segments[-1].heading()==90:
            #     self.add_segment((x_cor , y_cor -10))
            #
            # elif self.segments[-1].heading() ==180:
            #     self.add_segment((x_cor+10 , y_cor ))
            #
            # elif self.segments[-1].heading() == 270:
            #     self.add_segment((x_cor , y_cor+10 ))



    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setpos(new_x, new_y)
        # turtles[0].forward(20)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(180)


    def right(self):
        if self.head.heading() !=LEFT:
           self.segments[0].setheading(0)




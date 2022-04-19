from turtle import Turtle
MOVE_DIST = 20
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.pu()
        self.setpos(position)


    def move_up(self):
        new_y = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DIST
        self.goto(self.xcor(), new_y)
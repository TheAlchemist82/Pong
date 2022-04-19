from turtle import Turtle
MOVE_ANGLE = 15
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75, 0.75)
        self.color("white")
        self.pu()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    
    def bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1
    
    def refresh(self):
        self.home()
        self.paddle_bounce()
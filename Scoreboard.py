from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.scole = 0
        self.score = 0
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.scole, False, 'center', ('Comic Sans MS', 50, 'bold'))
        self.goto(100, 200)
        self.write(self.score, False, 'center', ('Comic Sans MS', 50, 'bold'))
        
    def point_l(self):
        self.scole += 1
        self.update()
        
    def point_r(self):
        self.score += 1
        self.update()
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0,y=270)
        self.color('white')
        self.write(f'Score = {self.score} ',align='center',font=('Courier',18,'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear() 
        self.write(f'Score = {self.score} ',align='center',font=('Courier',18,'normal'))

    def gameOver(self):
        self.goto(0,0)
        self.write('Game Over!',align='center',font=('Courier',18,'normal'))


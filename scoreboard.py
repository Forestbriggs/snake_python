from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write_score()
        
    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def increment_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
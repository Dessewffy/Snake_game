from turtle import Turtle
MOVE = False
ALIGN = "Center"
FONT = ('Arial', 20, 'normal')

class ScooreBoard(Turtle):
    def __init__(self, counter):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0.0, 300)
        self.color("white")
        self.counter = counter
        self.write(f"Score: {self.counter}", move=MOVE, align=ALIGN, font=FONT)
# Scoore
    def scoore(self):
        self.clear()
        self.counter += 1
        self.write(f"Score: {self.counter}", move=MOVE, align=ALIGN, font=FONT)
# End of the game
    def game_over(self):
        self.goto(0.0, 0.0)
        self.write("Game Over!", move=MOVE, align=ALIGN, font=FONT)

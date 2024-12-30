from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0

        self.penup()
        self.goto(-10, 260)
        self.updated_score()


    def updated_score(self):
        self.clear()

        self.write(f"Score: {self.score}", align="center" , font=("Arial", 20, "normal") )
        self.score += 1

    def game_end(self):

        # self.screen.clear()
        # self.screen.bgcolor("black")
        self.goto(-10, 0)
        self.write(f"Game over", align="center", font=("Arial", 30, "normal"))








from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def new_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(arg=" GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode="w") as highscore:
                highscore.write(f"{self.high_score}")
        self.score = 0
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

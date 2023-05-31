from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_score()

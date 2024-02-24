from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)

    def puntuacion(self):
        self.write(f"{self.player_1}            {self.player_2}", align="center", font=("Arial", 20, "normal"))

    def update_score_player_1(self):
        self.player_1 += 1
        self.clear()
        self.puntuacion()

    def update_score_player_2(self):
        self.player_2 += 1
        self.clear()
        self.puntuacion()



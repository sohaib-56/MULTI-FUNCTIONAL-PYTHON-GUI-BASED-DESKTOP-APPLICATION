from turtle import Turtle

AlIGN = "left"
FONT = ("Arial",14,"normal")


class Scoreboard(Turtle):
    """ This class will write and updaate the scoreboard as the Player pases level """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-275,255)
        self.update_level()


    def update_level(self):
        self.write(f"Level = {self.level}",align=AlIGN,font=FONT)


    def increment_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)























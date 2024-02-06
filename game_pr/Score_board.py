from turtle import Turtle
import random
ALIGNMENT="center"
FONT=("Arial",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.setpos(0,260)
        self.color("white")
        self.write(f"Score:{self.score} High Score:{self.high_score}", False,align= ALIGNMENT,font= FONT)

        self.hideturtle()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", False,align= ALIGNMENT,font= FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



    def reset(self):
        if self.score> int(self.high_score):
            self.high_score=self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()


    # changing this game over function
    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write("GAME OVER ", False, align=ALIGNMENT, font=FONT)
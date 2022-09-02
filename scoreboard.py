from turtle import Turtle
FONT = ("Courier", 24, "normal")

#  to show the current game level
#  to display Game Over when turtle hits a car
class Scoreboard(Turtle):
    
    # Creates the scoreboard, penup to not write, moves to screen top left co-ordinates
    # Uses the display_level function to show the current level (starts at 1)
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-285, 260)
        self.level = 1
        self.display_level()

    # self.clear to clear the previous score, then calls the display_level function to show increased level
    def increase_level(self):
        self.clear()
        self.level += 1
        self.display_level()
    
    # uses the write function to write an "f"string
    def display_level(self):
        self.write(f'Level:{self.level}', align="left", font=FONT)
       
    # Shows the end of the game 
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=FONT)
        
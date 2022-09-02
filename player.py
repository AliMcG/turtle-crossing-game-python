from turtle import Turtle;
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
# global variables to use with this class

class Player(Turtle):
    # This creates a new class called Player that inherits everything from Turtle.
    # Player is then given the following attributes. 
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    # Function to move Player by the varibale MOVE_DISTANCE.
    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    #  Re-starts the turtle in the original position
    def respawn(self):
        self.goto(STARTING_POSITION)

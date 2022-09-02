import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

speed = 0.1
# Defines the game screen size and setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Creates a new object from the Player class
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Lets the screen listen oyut for a key - "up".
screen.listen()
screen.onkey(player.go_up, "Up")

# A continues while loop to let the game run and run until "Game over"
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            # play_again = screen.textinput("CONTINUE?", "Y or N:")
            # if play_again == "y":
            #     scoreboard.clear()
            #     screen.clear()
            #     game_is_on = True
    
    
    if player.ycor() > 275:
        player.respawn()
        speed -= 0.01
        scoreboard.increase_level()

# To exit game screen
screen.exitonclick()

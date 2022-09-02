import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Defines the game screen size and setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creates a new object from the Player class
player = Player()
car_manager = CarManager()

# Lets the screen listen oyut for a key - "up".
screen.listen()
screen.onkey(player.go_up, "Up")

# A continues while loop to let the game run and run until "Game over"
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 280:
        player.respawn()

# To exit game screen
screen.exitonclick()
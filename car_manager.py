from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    #  creats an empty list object to store each new car object
    def __init__(self):
        self.all_cars = []

    # creates a new car every each time the random number is 1. 
    # The function is called in the game every second but will only make a new car one 6th of the time.
    # Use the random module to pick a random colour and a random stating position.
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    #  Function loops through the [list of cars] and for each car, it moves the DISTANCE.
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            
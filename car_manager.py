import random
from turtle import Turtle
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_cage = []
        self.hideturtle()
        
       
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_cage.append(new_car)

    def move_car(self):
        for move in self.car_cage:
            move.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for move in self.car_cage:
            move.forward(MOVE_INCREMENT)

            


        



    
        
        

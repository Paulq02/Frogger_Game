import random
from turtle import Turtle
import time

#Here is a list of colors which will be randomly chosen by the random module each time a car is generated
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

#The default starting movement for each car is 5 pixels
STARTING_MOVE_DISTANCE = 5

#The default starting movement is increased by 10 pixels after each successful Turtle crossing
MOVE_INCREMENT = 10




class CarManager(Turtle):
    """
    CarManager class inherits from the Turtle module -
    When an object is created an empty list is initialized, along with the car_speed setting being set to the STARTING_MOVE_DISTANCE constant value of 5 pixels.
    
    
    """

    def __init__(self):
        super().__init__()
        self.car_cage = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        
       
        
    def create_car(self):
        """
        The create_car method controls each car that is generated.
        Firstly a random number is generated (from 1 to 6) if a 3 is generated a car is then generated.
        Each car that is generated has a random color chosen from the COLORS list.
        Each car that is generated has it's heading set to west to move from the right side of the screen to the left.
        Each car that is generated will only be generated from a random location on the Y-axis ranging from -250 to 250
        Each car that is generated is appended to the car_cage list.
        """
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
        """
        This method controls the movement of the randomly generated cars.
        A for loop iterates in the car_cage list, each car that has been created and appended to this list is then instructed to move forward at the pace that is current.
        """
        for move in self.car_cage:
            move.forward(self.car_speed)

    def increase_speed(self):
        """
        Controls the movment speed of the cars.
        If a successful turtle street crossing occurs the car_speed setting is increased by 10 pixels
        """
        self.car_speed += MOVE_INCREMENT
        
            


        



    
        
        

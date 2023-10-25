from turtle import Turtle

#The starting position of the Player/Turtle is 0 (X-axis) and -280 (Y-axis) - essentially the very bottom of the screen (This doesn't change)
STARTING_POSITION = (0, -280)

#The default movement of the Player/Turtle is 10 pixels (This doesn't change)
MOVE_DISTANCE = 10

#The finish line in which a Player/Turtle crossing is considered successful is 280 on the Y-axis (This doesn't change)
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    The player class inherits from the Turtle module -
    When an object is created from this class a Turtle will appear on the bottom of the screen (which is the starting position) -
    The heading will be pointed upwards 
    """
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

        
    def move(self):
        """
        Controls the movement of the Players Turtle - 
        By default the movement is 10 pixels
        """
        self.forward(MOVE_DISTANCE)

    def reset(self):
        """
        Controls the resetting of the Players Turtle - 
        If a successful crossing occurs, the turtle is reset to the bottom of the screen 
        """
        self.goto(STARTING_POSITION)


    

        

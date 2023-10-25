import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

#Screen setup 
screen = Screen()
screen.setup(width=600, height=600)
#Turned the animation off
screen.tracer(0)

#Player object is created from the Player class - which is the turtle
player = Player()

#Car object is created from the Car class - Controls the movement of the cars, speed increase when a succesfull crossing of the road
car = CarManager()

#Score object is created from the Scoreboard class - Keeps track of the levels and Game Over sequence
score = ScoreBoard()

#Here I use the listen method to tell the screen to listen to specific key presses, in this case the "Up" key - It controls the turtle moving forward
screen.listen()
screen.onkey(player.move, "Up")

#Game continues to run until the turtle has a collision with a car
game_is_on = True
while game_is_on:
    #Sleep method is used to slow the game down to make it more playable
    time.sleep(0.1)
    #Game is continuously being updated 
    screen.update()
    #Here the create_car method is called 
    car.create_car()


    



    #If the player/turtle successfully crosses the "road" (which is past the 250 mark on the Y-axis) the players Turtle is reset to the bottom of the screen
    if player.ycor() > 250:
        player.reset()

        #Along with the reset, the increase_speed method is called which increases the speed by 10 pixels after each successful turtle crossing
        car.increase_speed()

        #After a successfull turtle crossing and speed increase, Your level score/attribute is increased by 1 (essentially keeping track of how many consecutive successful crossing)
        score.level_up()
        
    else:
        #If the previous conditions have not yet been met, the move_car method is constantly being called 
        #This controls the forward movement of the randomly generated cars, which move at the default speed which is 5 pixels
        car.move_car()

    #A for loop is constantly being run to check the poisitions of the Player/Turtle and each Car in the "car_cage" list
    for position in car.car_cage:
        
        #If any Car is within 20 pixels of the Players Turtle, it is ruled a collision which triggers the Game Over sequence
        #The while loop ends and the game_over method is called - which alerts the player that the game is over
        if position.distance(player.position()) < 20:
            game_is_on = False
            score.game_over()
            

#This controls the screen, it keeps the screen open - until you click the X to exit
screen.exitonclick()
    
    
    
    

    

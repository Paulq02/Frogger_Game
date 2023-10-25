from turtle import Turtle

#Game font value is set here
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    """
    ScoreBoard class inherits from the Turtle module.
    When is ScoreBoard object is created the write method is called, which displays the starting level the player is on, at the top left of the screen
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.level = 1
        self.write(f"Level:{ self.level}", font=FONT)

    
    def level_up(self):
        """
        This method controls the updating of the level the player is currently on. After every successful Turtle crossing the scoreboard is cleared
        of the previous level.The level is then updated by 1 , then the new updated and current level is written and diplayed at the top left of the screen
        """
        self.clear()
        self.level += 1
        self.write(f"Level:{ self.level}", font=FONT)


    def game_over(self):
        """
        Controls the game over sequence. If the Players Turtle comes into contact with a car, the scoreboard is cleared, and the text "Game Over" is displayed across middle of the screen
        """
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)



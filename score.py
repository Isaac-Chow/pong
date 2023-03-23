# Import turtle from the turtle module
from turtle import Turtle


"""
    > Create a class called ScoreBoard
    > Inherit from the Turtle class
    > [ Inside the class ]> Create a constructor method that takes in left_name and right_name
    > [ Inside the class ]> [ Inside the constructor method ]> Call the super() method
    > [ Inside the class ]> [ Inside the constructor method ]> Set the left to left_name
    > [ Inside the class ]> [ Inside the constructor method ]> Set the right to right_name
    > [ Inside the class ]> [ Inside the constructor method ]> Set the color to #ff6700
    > [ Inside the class ]> [ Inside the constructor method ]> Call the penup() method
    > [ Inside the class ]> [ Inside the constructor method ]> Call the hideturtle() method
    > [ Inside the class ]> [ Inside the constructor method ]> Set the l_score to 0
    > [ Inside the class ]> [ Inside the constructor method ]> Set the r_score to 0
    > [ Inside the class ]> [ Inside the constructor method ]> Call the update_score() method
"""


class ScoreBoard(Turtle):
    def __init__(self, left_name, right_name):
        super().__init__()
        self.left = left_name
        self.right = right_name
        self.color('#ff6700')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    """
        > Create a method called update_score
        > [ Inside the method ]> Call the clear() method to clear the previous score
        > [ Inside the method ]> Call the goto() method with -270 and 270
        > [ Inside the method ]> Call the write() method with the left name and the left score
        > [ Inside the method ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the write() method ]> Set the font to courier, 14, normal
        > [ Inside the method ]> Call the goto() method with 270 and 270
        > [ Inside the method ]> Call the write() method with the right name and the right score
        > [ Inside the method ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the write() method ]> Set the font to courier, 14, normal
    """

    def update_score(self):
        self.clear()
        self.goto(-270, 270)
        self.write(arg=(f"{self.left}:{self.l_score}"),
                   align="center", font=("courier", 14, "normal"))
        self.goto(270, 270)
        self.write(arg=(f"{self.right}:{self.r_score}"),
                   align="center", font=("courier", 14, "normal"))

    """
        > Create a method called l_point
        > [ Inside the method ]> Increment the l_score by 1
        > [ Inside the method ]> Call the update_score() method
    """

    def l_point(self):
        self.l_score += 1
        self.update_score()

    """
        > Create a method called r_point
        > [ Inside the method ]> Increment the r_score by 1
        > [ Inside the method ]> Call the update_score() method
    """

    def r_point(self):
        self.r_score += 1
        self.update_score()

    """
        > Create a method called end_game
        > [ Inside the method ]> Call the clear() method
        > [ Inside the method ]> Call the update_score() method
        > [ Inside the method ]> Call the goto() method with 0 and 0 as the arguments
        > [ Inside the method ]> Call the write() method with the argument "GAME OVER"
        > [ Inside the method ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the write() method ]> Set the font to courier, 40, bold
        
        > [ Inside the method ]> Create an if statement that checks if the left score is greater than the right score
        > [ Inside the method ]> [ Inside the if statement ]> Call the goto() method with 0 and 50
        > [ Inside the method ]> [ Inside the if statement ]> Call the write() method with the left name and "Wins !!"
        > [ Inside the method ]> [ Inside the if statement ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the if statement ]> [ Inside the write() method ]> Set the font to CaskaydiaCove NF, 30, normal
        
        > [ Inside the method ]> Create an if statement that checks if the left score is less than the right score
        > [ Inside the method ]> [ Inside the if statement ]> Call the goto() method with 0 and 50
        > [ Inside the method ]> [ Inside the if statement ]> Call the write() method with the right name and "Wins !!"
        > [ Inside the method ]> [ Inside the if statement ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the if statement ]> [ Inside the write() method ]> Set the font to CaskaydiaCove NF, 30, normal

        > [ Inside the method ]> Create an else statement
        > [ Inside the method ]> [ Inside the else statement ]> Call the goto() method with 0 and 50
        > [ Inside the method ]> [ Inside the else statement ]> Call the write() method with the argument "Draw"
        > [ Inside the method ]> [ Inside the else statement ]> [ Inside the write() method ]> Set the align to center
        > [ Inside the method ]> [ Inside the else statement ]> [ Inside the write() method ]> Set the font to CaskaydiaCove NF, 30, normal
    """

    def end_game(self):
        self.clear()
        self.update_score()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center",
                   font=("courier", 40, "bold"))
        if self.l_score > self.r_score:
            self.goto(0, 50)
            self.write(arg=f"{self.left} Wins !!", align="center",
                       font=('CaskaydiaCove NF', 30, 'normal'))
        elif self.l_score < self.r_score:
            self.goto(0, 50)
            self.write(arg=f"{self.right} Wins !!", align="center", font=(
                'CaskaydiaCove NF', 30, 'normal'))
        else:
            self.goto(0, 50)
            self.write(arg="Draw", align="center", font=(
                'CaskaydiaCove NF', 30, 'normal'))

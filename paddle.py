# Import turtle form the turtle module
from turtle import Turtle

"""
    > Create a class called Paddle
    > Inherit from the Turtle class
    > [ Inside the class ]> Create a constructor method that takes in a position
    > [ Inside the class ]> [ Inside the constructor method ]> Call the super() method
    > [ Inside the class ]> [ Inside the constructor method ]> Set the shape to square
    > [ Inside the class ]> [ Inside the constructor method ]> Set the color to #541388
    > [ Inside the class ]> [ Inside the constructor method ]> Call the penup() method
    > [ Inside the class ]> [ Inside the constructor method ]> Call the goto() method with the position
"""


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('#541388')
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)

    """
        > Create a method called go_up to move the paddle up
        > [ Inside the method ]> Set the new_y to the current ycor() + 20
        > [ Inside the method ]> Call the goto() method with the current xcor() and new_y
    """

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    """
        > Create a method called go_down to move the paddle down
        > [ Inside the method ]> Set the new_y to the current ycor() - 20
        > [ Inside the method ]> Call the goto() method with the current xcor() and new_y
    """

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

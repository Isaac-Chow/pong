# Import turtle form the turtle module
from turtle import Turtle


"""
    > Create a class called Ball
    > Inherit from the Turtle class
    > Create a constructor method
    > [Inside the constructor method]> Call the super() method
    > [Inside the constructor method]> Set the shape to circle
    > [Inside the constructor method]> Set the color to #d90429
    > [Inside the constructor method]> Call the penup() method
    > [Inside the constructor method]> Set the x_move and y_move to 10
    > [Inside the constructor method]> Set the move_speed to 0.1
"""


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('#d90429')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    """
        > Create a method called move to move the ball on the canvas
        > [Inside the method]> Set the x_pos to the current xcor() + x_move
        > [Inside the method]> Set the y_pos to the current ycor() + y_move
        > [Inside the method]> Call the goto() method with the x_pos and y_pos
    """

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    """
        > Create a method called y_bounce to bounce the ball on the y axis
        > [Inside the method]> Set the y_move to the current y_move * -1
    """

    def y_bounce(self):
        self.y_move *= -1

    """
        > Create a method called x_bounce to bounce the ball on the x axis
        > [Inside the method]> Set the x_move to the current x_move * -1
        > [Inside the method]> Set the move_speed to the current move_speed * 0.9
    """

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    """
        > Create a method called reset_pos to reset the ball to the center
        > [Inside the method]> Call the goto() method with the x and y coordinates of 0, 0
        > [Inside the method]> Set the move_speed to 0.1
        > [Inside the method]> Call the x_bounce() method
    """

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()

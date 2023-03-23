# Import time from the time module
# Import os from the os module
# Import Screen from the turtle module
# Import Ball from the ball module within this current folder
# Import Paddle from the paddle module within this current folder
# Import ScoreBoard from the score module within this current folder
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
from tkinter import *
import time
import os

# Initialize the screen using the Tk() method
# Configure the screen using the config() method
# [ Inside the config method ]> Set the width to 800
# [ Inside the config method ]> Set the height to 600
# [ Inside the config method ]> Set the x-axis padding to 10
# [ Inside the config method ]> Set the y-axis padding to 10
window = Tk()
window.config(width=1000, height=700, padx=10, pady=10)

# Set the frame count of the gif to be attached to the window to 10
# Create a list of frames using a list comprehension
frameCnt = 10
frames = [PhotoImage(file='ping.gif', format='gif -index %i' % (i))
          for i in range(10)]


# Create a function called update to update the gif
# [ Inside the update function ]> Set the frame to the current frame
# [ Inside the update function ]> Set the ind to the current ind + 1
# [ Inside the update function ]> If the ind is equal to the frame count
# [ Inside the update function ]> [ Inside the if condition ]> Set the ind to 0
# [ Inside the update function ]> Set the image of the w1 widget to the frame using the configure() method
# [ Inside the update function ]> Call the window.after() method with the update function and the ind
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    w1.configure(image=frame)
    window.after(50, update, ind)


#
w1 = Label(window)
w1.place(x=10, y=50)
window.after(0, update, 0)

game_name = Label(text='🎳 PING PONG 🎳', font=(
    'courier', 40, 'bold'), fg='green')
game_name.place(x=490, y=5)

l_player = Label(text=' PLAYER 1 ', fg='white', bg='black',
                 font=('CaskaydiaCove NF', 12, 'normal'))
l_player.place(x=550, y=150)
left_detail = Label(text="W : Up & S : Down",
                    font=('CaskaydiaCove NF', 12, 'bold'))
left_detail.place(x=550, y=200)

r_player = Label(text=' PLAYER 2 ', fg='white', bg='black',
                 font=('CaskaydiaCove NF', 12, 'normal'))
r_player.place(x=550, y=300)
right_details = Label(text="Up arrow : Up & Down arrow : Down",
                      font=('CaskaydiaCove NF', 12, 'bold'))
right_details.place(x=550, y=350)

l_entry = Entry(width=24, font=('CaskaydiaCove NF', 12, 'normal'))
l_entry.place(x=700, y=150)
l_entry.focus()
r_entry = Entry(width=24, font=('CaskaydiaCove NF', 12, 'normal'))
r_entry.place(x=700, y=300)

bug_information_1 = Label(text='Disclaimer: The code still has a pending bug.', font=(
    'CaskaydiaCove NF', 10, 'normal'), fg='red')
bug_information_1.place(x=550, y=500)
bug_information_2 = Label(text='** Ball need to hit almost middle on paddles **',
                          font=('CaskaydiaCove NF', 10, 'normal'), fg='red')
bug_information_2.place(x=550, y=520)

my_info = Label(text='SUMAN', font=(
    'CaskaydiaCove NF', 7, 'normal'), fg='black')
my_info.place(x=-5, y=675)


def Start_Game():

    Score = ScoreBoard(l_entry.get(), r_entry.get())

    screen = Screen()
    screen.bgcolor("#bde0fe")
    screen.setup(width=800, height=600)
    screen.title('PING PONG')
    screen.tracer(0)

    l_paddle = Paddle((-385, 0))
    r_paddle = Paddle((380, 0))
    game_ball = Ball()

    screen.listen()
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')

    game_is_on = True
    while game_is_on:
        time.sleep(game_ball.move_speed)
        screen.update()
        game_ball.move()

        if game_ball.ycor() > 280:
            game_ball.y_bounce()

        if game_ball.ycor() < -280:
            game_ball.y_bounce()

        if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 330:
            game_ball.x_bounce()
            Score.r_point()

        if game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -330:
            game_ball.x_bounce()
            Score.l_point()

        if game_ball.xcor() > 380:
            game_ball.reset_pos()
            Score.end_game()
            game_is_on = False

        if game_ball.xcor() < -380:
            game_ball.reset_pos()
            Score.end_game()
            game_is_on = False

    window.destroy()
    screen.exitonclick()


button = Button(text='Enter', relief=RAISED, font=(
    'CaskaydiaCove NF', 12, 'normal'), command=Start_Game)
button.place(x=680, y=600)
window.mainloop()

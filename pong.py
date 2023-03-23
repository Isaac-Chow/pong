import tkinter

# Define the game class to contain the game functions
class Game():
    # Initialize the game
    # > Set the window
    # > Set the window title
    # > Set the canvas
    # > Set the canvas size
    # > Set the canvas background color to black
    # > Pack the canvas
    def __init__(self):
        # Create the game window
        self.win=tkinter.Tk()
        # Provide the window ID
        self.win.title("P O N G")
        # Set the width to 800
        self.width = 800
        # Set the height to 600
        self.height = 600
        # Set up the canvas setup and the background
        self.canvas=tkinter.Canvas(self.win, width=self.width, height=self.height, bg="black")
        # Use the pack function to place the canvas into the window
        self.canvas.pack()
        # self.canvas.place(relx=1, rely=1, anchor="center")



    # Create the new game method
    # > Set the player 1 score to 0
    # > Set the player 2 score to 0
    # > Create the left paddle
    # > Create the right paddle
    # > Create the ball
    # > Create the score
    # > Set the ball speed
    # > Run the game
    def new_game(self):
        # Create the player scores => Player One and Player Two
        self.player1_score = 0
        self.player2_score = 0

        # Set up the canvas left
        self.paddle1 = self.canvas.create_rectangle(40, 255, 60,345,fill="white")
        # Set up the canvas right
        self.paddle2 = self.canvas.create_rectangle(740, 255,760, 345,fill="white")
        # Set up the canvas ball
        self.ball = self.canvas.create_oval(400, 300, 420, 320, fill="white")
        # Set up the canvas score display
        self.score = self.canvas.create_text(380,50,fill="white",font="Courier 24 normal",text=(f"Player 1:0   Player 2:0"))
        
        # Provide the speed on the x-axis
        self.dx = .05
        # Provide the speed on the y-axis
        self.dy = .05

        self.run()
    
    # Create the run method
    # > Set the playing variable to True
    # > While the playing variable is True
    # > > Run the events method
    # > > Run the update method
    def run(self):
        self.playing=True
        
        while self.playing:
            self.events()
            self.update()

    # Create the events method
    # > Bind the event for the left paddle up movement
    # > Bind the event for the left paddle down movement
    # > Bind the event for the right paddle up movement
    # > Bind the event for the right paddle down movement    
    def events(self):
        # Bind the w key to move the left paddle up
        self.canvas.bind_all("<KeyPress-w>",self.paddle_move)
        # Bind the s key to move the left paddle down
        self.canvas.bind_all("<KeyPress-s>",self.paddle_move)
        # Bind the up arrow key to move the right paddle up
        self.canvas.bind_all("<KeyPress-Up>",self.paddle_move)
        # Bind the down arrow key to move the right paddle down
        self.canvas.bind_all("<KeyPress-Down>",self.paddle_move)

    # Create the paddle move method
    # > If the event is w
    # > > Move the left paddle up
    # > If the event is s
    # > > Move the left paddle down
    # > If the event is Up
    # > > Move the right paddle up
    # > If the event is Down
    # > > Move the right paddle down
    def paddle_move(self,event):
        # Use the 'W' key to move the left paddle up
        if event.keysym=="w":
            self.canvas.move(self.paddle1,0,-30)
            
        # Use the 'S' key to move the left paddle up
        elif event.keysym=="s":
            self.canvas.move(self.paddle1,0,30)

        # Use the Up arrow key to move the left paddle up
        elif event.keysym=="Up":
            self.canvas.move(self.paddle2,0,-30)

        # Use the Down arrow key to move the left paddle up
        elif event.keysym=="Down" and self.paddle2_pos[]:
            self.canvas.move(self.paddle2,0,30)
    
    # Create the update method
    # > Move the ball
    # > Get the ball position
    # > Get the left paddle position
    # > Get the right paddle position
    def update(self):
        self.canvas.move(self.ball, self.dx, self.dy)

        # Place the ball on the canvas
        self.ball_pos = self.canvas.coords(self.ball)
        # Place the left paddle on the canvas
        self.paddle1_pos = self.canvas.coords(self.paddle1)
        # Place the right paddle on the canvas
        self.paddle2_pos = self.canvas.coords(self.paddle2)

        if self.ball_pos[1]<=0 or self.ball_pos[3] >= 600:
            self.dy *= -1

        if (self.paddle1_pos[2] >= self.ball_pos[0] >= self.paddle1_pos[0] or self.paddle2_pos[2] >= self.ball_pos[0] >= self.paddle2_pos[0]) and self.dx <0:
            # if self.ball_pos[3] >= self.paddle1_pos[1] and self.ball_pos[1] <= self.paddle2_pos[3]:
            if self.ball_pos[3] >= self.paddle1_pos[1] and self.ball_pos[3] <= self.paddle2_pos[1]:
                self.dx *=-1
                
        # Score Player 1
        if self.ball_pos[2] >= self.width:
            self.dx*=-1
            self.canvas.coords(self.ball, 400, 300, 420, 320)
            self.player1_score += 1
            self.canvas.delete(self.score)
            self.score=self.canvas.create_text(380,50,fill="white",font="Courier 24 normal",text=(f"Player1: {self.player1_score} | Player 2: {self.player2_score}"))
        
        # Score Player 2
        if self.ball_pos[0] <= 0:
            self.dx*=-1
            self.canvas.coords(self.ball, 400, 300, 420, 320)
            self.canvas.delete(self.score)
            self.player2_score+=1
            self.score=self.canvas.create_text(380,50,fill="white",font="Courier 24 normal",text=(f"Player1: {self.player1_score} | Player 2: {self.player2_score}"))

        self.win.update()

    # Create the show start screen method
    # > Set the waiting variable to True
    # > Bind the space key to the wait for keypress method
    # > Create the start message
    # > While the waiting variable is True
    # > > Update the window
    # > Delete the start message
    def show_start_screen(self):
        self.waiting=True
        self.canvas.bind_all("<KeyPress-space>",self.wait_for_keypress)

        self.start_message=self.canvas.create_text(380,250,fill="white",font="courier 24 normal",text=('Simple Pong Game with Py3 and Tk\n\t Press "space[ ]" to start.'))

        self.win.update()
        
        while self.waiting:
            self.win.update()

        self.canvas.delete(self.start_message)

    def show_game_over_screen(self):
        self.waiting=True

    # Create the wait for keypress method
    # > If the event is space
    # > > Set the waiting variable to False
    def wait_for_keypress(self,event):
        if event.keysym=="space":
            self.waiting=False

game=Game()
game.show_start_screen()

while True:
    game.new_game()
    game.show_game_over_screen()
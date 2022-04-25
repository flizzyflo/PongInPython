from GameItem import GameItem
from tkinter import *
from random import randrange


class Ball(GameItem):

    def __init__(self, GameBoardObject: object, PlankObject: object, speed: int, size: int = 15, colour: str = "blue"):
        super().__init__(GameBoardObject)
        self.SPEED = speed
        self.size = size
        self.colour = colour
        self.plank_object = PlankObject
        

    def create_ball(self):
        """Initialization of the ball item"""

        self.ball = self.gameboard.canvasItem.create_oval(self.size, self.size * 3, self.size * 3, self.size * 5, fill=self.colour)


    def random_start(self):
        """Random selection of a starting direction of the ball"""

        random_value = randrange(0, 3)
        if random_value == 0:
            self.move_left()
            self.move_down()

        elif random_value == 1:
            self.move_right()
            self.move_down()

        elif random_value == 2:
            self.move_left()
            self.move_up()

        elif random_value == 3:
            self.move_right()
            self.move_up()


    def move_left(self):
        """Move the ball left until it hits the left border. Bounces back 
        from the left border of the gameboard rightwards."""

        self.gameboard.canvasItem.move(self.ball, -1, 0)
        ball_x1_coord = self.get_coords(self.ball)[0]

        if ball_x1_coord < 1:
            self.move_right()

        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_left)


    def move_right(self):
        """Move the ball right until it hits the right border. Bounces back 
        from the right border of the gameboard leftwards."""

        self.gameboard.canvasItem.move(self.ball, 1, 0)
        ball_x2_coord= self.get_coords(self.ball)[2]

        if ball_x2_coord >= self.gameboard.get_width():
            self.move_left()
        
        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_right)


    def move_up(self):
        """Move the ball up until it hits the topmost border. Bounces back 
        from the border of the gameboard downwards."""

        self.gameboard.canvasItem.move(self.ball, 0, -1)
        ball_y1_coord= self.get_coords(self.ball)[1]

        if ball_y1_coord <= 0:
            self.move_down()

        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_up)


    def move_down(self):
        """Move the ball down until it hits either the plank and bounces back
        or it hits the border. If it hits the lower boundary, the game is over."""

        self.gameboard.canvasItem.move(self.ball, 0, 1)
        ball_y2_coord = self.get_coords(self.ball)[3]
        plank_x1, plank_x2= self.get_coords(self.plank_object.plank)[0], self.get_coords(self.plank_object.plank)[3]
        
        
        if (self.get_coords(self.plank_object.plank)[1] == ball_y2_coord) and (plank_x1 <= self.get_coords(self.ball)[2] <= plank_x2):
            self.move_up()

        elif self.get_coords(self.plank_object.plank)[1] < ball_y2_coord - 5:
            self.gameboard.canvasItem.after_cancel(self.gameboard.canvasItem.after(self.SPEED, self.move_down))

        else:
            self.gameboard.canvasItem.after(self.SPEED, self.move_down)
        
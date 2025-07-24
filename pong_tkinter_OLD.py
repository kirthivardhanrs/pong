from tkinter import *
from tkinter import ttk
import random

WIDTH = 800
HEIGHT = 800
BALL_DIAMETER = 10
PADDLE_PADDING = 10
PADDLE_THICKNESS = 10
PADDLE_LENGTH = 100
PADDLE_VELOCITY = 10

BALL_BOX_X1 = BALL_DIAMETER/2
BALL_BOX_X2 = BALL_BOX_X1
BALL_BOX_Y1 = WIDTH-BALL_DIAMETER/2
BALL_BOX_Y2 = HEIGHT-PADDLE_PADDING-PADDLE_THICKNESS-BALL_DIAMETER/2

root = Tk()
root.title("Pong")

class Ball:
    def __init__(self):
        self.body = canvas.create_oval(500, 500, 500+BALL_DIAMETER, 500+BALL_DIAMETER, fill='white')
        self.vx = random.randint(10, 15) * (random.randint(0, 1)*2-1)
        self.vy = random.randint(10, 15) * (random.randint(0, 1)*2-1)
        self.move()
    def move(self):
        canvas.move(self.body, self.vx, self.vy)
        coords_list = canvas.coords(self.body)
        coords = [(coords_list[0] + coords_list[2])/2, (coords_list[1] + coords_list[3])/2]
        if not (BALL_BOX_X1 < coords[0] < BALL_BOX_Y1):
            self.vx *= -1
        if not (BALL_BOX_X2 < coords[1] < BALL_BOX_Y2):
            paddle_coords_list = canvas.coords(paddle.body)
            if coords[1] >= BALL_BOX_Y2 and not (paddle_coords_list[0] <= coords[0] <= paddle_coords_list[2]):     
                print("rip")
                canvas.coords(self.body, 500, 500, 500+BALL_DIAMETER, 500+BALL_DIAMETER)
                self.vx = random.randint(10, 15) * (random.randint(0, 1)*2-1)
                self.vy = random.randint(10, 15) * (random.randint(0, 1)*2-1)
            else:
                self.vy *= -1
        canvas.after(50, self.move)

class Paddle:
    def __init__(self):
        self.body = canvas.create_rectangle(400, HEIGHT-PADDLE_PADDING-PADDLE_THICKNESS, 400+PADDLE_LENGTH, HEIGHT-PADDLE_PADDING
                                                , fill='white')
        root.bind('<Right>', self.move)
        root.bind('<Left>', self.move)
    def move(self, event):
        if event.keysym == "Right":
            canvas.move(self.body, PADDLE_VELOCITY, 0)
        elif event.keysym == "Left":
            canvas.move(self.body, -PADDLE_VELOCITY, 0)

            
        
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background='#121212')
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

ball = Ball()

paddle = Paddle()


root.mainloop()
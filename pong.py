from tkinter import *
import random


class Pong:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(self.master, width=800, height=400, bg="black")
        self.canvas.pack()

        self.paddle1 = self.canvas.create_rectangle(50, 150, 70, 250, fill="white")
        self.paddle2 = self.canvas.create_rectangle(730, 150, 750, 250, fill="white")
        self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")

        self.paddle1_speed = 0
        self.paddle2_speed = 0
        self.ball_speed_x = random.choice([-2, 2])
        self.ball_speed_y = random.choice([-2, 2])

        self.canvas.bind_all("<KeyPress-w>", self.move_paddle1_up)
        self.canvas.bind_all("<KeyPress-s>", self.move_paddle1_down)
        self.canvas.bind_all("<KeyPress-Up>", self.move_paddle2_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_paddle2_down)

        self.game_loop()

    def move_paddle1_up(self, event):
        self.paddle1_speed = -3

    def move_paddle1_down(self, event):
        self.paddle1_speed = 3

    def move_paddle2_up(self, event):
        self.paddle2_speed = -3

    def move_paddle2_down(self, event):
        self.paddle2_speed = 3

    def game_loop(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        self.canvas.move(self.paddle1, 0, self.paddle1_speed)
        self.canvas.move(self.paddle2, 0, self.paddle2_speed)

        ball_pos = self.canvas.coords(self.ball)
        paddle1_pos = self.canvas.coords(self.paddle1)
        paddle2_pos = self.canvas.coords(self.paddle2)

        if ball_pos[1] <= 0 or ball_pos[3] >= 400:
            self.ball_speed_y *= -1

        if ball_pos[0] <= 0 or ball_pos[2] >= 800:
            self.ball_speed_x *= -1

        if ball_pos[0] <= paddle1_pos[2] and ball_pos[1] >= paddle1_pos[1] and ball_pos[3] <= paddle1_pos[3]:
            self.ball_speed_x *= -1

        if ball_pos[2] >= paddle2_pos[0] and ball_pos[1] >= paddle2_pos[1] and ball_pos[3] <= paddle2_pos[3]:
            self.ball_speed_x *= -1

        if paddle1_pos[1] <= 0:
            self.paddle1_speed = 0

        if paddle1_pos[3] >= 400:
            self.paddle1_speed = 0

        if paddle2_pos[1] <= 0:
            self.paddle2_speed = 0

        if paddle2_pos[3] >= 400:
            self.paddle2_speed = 0

        self.master.after(10, self.game_loop)


root = Tk()
root.title("Pong")
pong = Pong(root)
root.mainloop()

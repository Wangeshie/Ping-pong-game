import tkinter as tk
from tkinter import ttk
import time

class Paddle:
    def __init__(self, canvas, color, x, y, left_key, right_key):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, x, y)
        self.x = 0
        self.score = 0  # Initialize score attribute
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all(left_key, self.turn_left)
        self.canvas.bind_all(right_key, self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 400, 300)
        self.x = 1
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
            self.paddle2.score += 1
            self.canvas.itemconfig(score2_text, text=f"Player 2: {self.paddle2.score}")
        if pos[3] >= self.canvas_height:
            self.y = -1
            self.paddle1.score += 1
            self.canvas.itemconfig(score1_text, text=f"Player 1: {self.paddle1.score}")
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
        self.hit_paddle(pos)

    def hit_paddle(self, pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle1_pos[0] and pos[0] <= paddle1_pos[2]:
            if pos[3] >= paddle1_pos[1] and pos[3] <= paddle1_pos[3]:
                self.y = -self.y
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[1] <= paddle2_pos[3] and pos[1] >= paddle2_pos[1]:
                self.y = -self.y

def pause_game():
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")

def restart_game():
    global ball, paddle1, paddle2
    canvas.delete("all")
    paddle1 = Paddle(canvas, "blue", 350, 550, "<Left>", "<Right>")
    paddle2 = Paddle(canvas, "green", 350, 50, "a", "d")
    ball = Ball(canvas, paddle1, paddle2, "red")
    create_scoreboard()

def create_scoreboard():
    global score1_text, score2_text
    score1_text = canvas.create_text(50, 30, text=f"Player 1: {paddle1.score}", font=("Arial", 16), fill="blue")
    score2_text = canvas.create_text(750, 30, text=f"Player 2: {paddle2.score}", font=("Arial", 16), fill="green")

def create_buttons():
    global pause_button, restart_button
    pause_button = ttk.Button(button_frame, text="Pause", command=pause_game)
    pause_button.pack(side="left", padx=10)
    restart_button = ttk.Button(button_frame, text="Restart", command=restart_game)
    restart_button.pack(side="left", padx=10)

def main():
    global window, canvas, ball, paddle1, paddle2, paused, button_frame
    paused = False

    window = tk.Tk()
    window.title("Ping Pong Game")
    window.resizable(0, 0)
    window.wm_attributes("-topmost", 1)

    button_frame = tk.Frame(window)
    button_frame.pack(side="top", pady=10)

    canvas = tk.Canvas(window, width=800, height=600, bd=0, highlightthickness=0)
    canvas.pack()
    window.update()

    paddle1 = Paddle(canvas, "blue", 350, 550, "<Left>", "<Right>")
    paddle2 = Paddle(canvas, "green", 350, 50, "a", "d")
    ball = Ball(canvas, paddle1, paddle2, "red")

    create_scoreboard()
    create_buttons()

    while True:
        if not paused:
            ball.draw()
            paddle1.draw()
            paddle2.draw()
        window.update_idletasks()
        window.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
































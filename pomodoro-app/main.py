import tkinter as tk
from tkinter import Canvas, PhotoImage

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50)

def start_timer():
    count_down(WORK_MIN * 60)
def count_down(count):
    # canvas.itemconfig(text, text= count)
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        window.after(1000, count_down, count - 1)





title_label = tk.Label(text="Timer", fg="GREEN",font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(window, width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
text = canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

start_button = tk.Button(text="Reset")
start_button.grid(column=2, row=2)

check_marks = tk.Label(text="✓", fg=GREEN,)
check_marks.grid(column=1,row=2)
window.mainloop()
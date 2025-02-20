import tkinter as tk
import math

# Pomodoro Constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

reps = 0
is_running = False
timer = None

def reset_timer():
    global reps, is_running
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Pomodoro")
    check_marks.config(text="")
    reps = 0
    is_running = False

def start_timer():
    global reps, is_running
    if not is_running:
        reps += 1
        is_running = True
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        
        if reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="Long Break", fg="red")
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="Short Break", fg="orange")
        else:
            count_down(work_sec)
            title_label.config(text="Work", fg="green")

def count_down(count):
    global timer
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        global is_running
        is_running = False
        start_timer()
        # # marks = "✔" * (reps // 2)
        # check_marks.config(text=marks)

# UI Setup
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=20, bg="white")

title_label = tk.Label(text="Pomodoro", fg="green", font=("Arial", 24, "bold"), bg="white")
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg="white", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="25:00", fill="black", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer, font=("Arial", 12))
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer, font=("Arial", 12))
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg="green", font=("Arial", 16), bg="white")
check_marks.grid(column=1, row=3)

window.mainloop()

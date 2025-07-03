from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def correct_format(time):
    return f"{time:02}"

def convert_to_standard(time):
    minutes = time // 60
    seconds = time % 60
    return f"{correct_format(minutes)}:{correct_format(seconds)}"

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=convert_to_standard(count))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        tick_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0, bg=YELLOW, fg=RED)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, bg=YELLOW, fg=RED)
reset_button.grid(row=2, column=2)

tick_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
tick_mark.grid(row=3, column=1)

window.mainloop()

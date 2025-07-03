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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def correct_format(time):
    length = len(str(time))
    if length == 1:
        return "0" + str(time)
    else:
        return time

def convert_to_standard(time):
    if time > 59:
        seconds = time % 60
        minutes = int((time - seconds) / 60)
        minutes = correct_format(minutes)
        seconds = correct_format(seconds)
        new_time = f"{minutes}:{seconds}"
        return new_time
    return time

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps

    if reps % 7 == 0 and reps != 0:
        count_down(20)
    else:
        if reps % 2 == 0:
            count_down(5)
        else:
            count_down(2)
    reps += 1
def count_down(count):
    if count >= 0:
        canvas.itemconfig(timer_text, text=convert_to_standard(count))
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# start button
start_button = Button(window, text="Start", bg=YELLOW, fg=RED, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(window, text="Reset", bg=YELLOW, fg=RED)
reset_button.grid(row=2, column=2)

# Tick mark
tick_mark = Label(window, text="✔", bg=YELLOW, fg=GREEN)
tick_mark.grid(row=3, column=1)
window.mainloop()
#IMPORTS
import tkinter
import math

#CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


#TIMER SETUP
#TIMER MECHANISM

def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        count_down(long_break_sec)
        label.config(fg=RED, text="Break")
    
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        label.config(fg=PINK, text="Break")

    else:
        count_down(work_sec)
        label.config(fg=GREEN, text="Work")
    

#COUNTDOWN MECHANISM

def count_down(count):
    count_min = math.floor((count/60))
    count_secs = count % 60

    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_secs}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


#UI MECHANISM

#WINDOW
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


#CANVAS
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="0",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#LABEL
label = tkinter.Label(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

#CHECK MARK
check_mark = tkinter.Label(text="✓", font=(FONT_NAME, 15, "normal"), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


#START BUTTON
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.config(width=5, height=1)
start_button.grid(row=2, column=0)

#RESET BUTTON
reset_button = tkinter.Button(text="Reset", highlightthickness=0)
reset_button.config(width=5, height=1)
reset_button.grid(row=2, column=2)







window.mainloop()
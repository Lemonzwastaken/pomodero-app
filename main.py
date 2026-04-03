# IMPORTS
import tkinter
import tkinter.simpledialog
 
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
 
# Defaults (can be changed via settings)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
 
# State variables (not true constants — use lowercase)
reps = 0
check_mark_str = ""
timer = None
paused = False
remaining_count = 0

#TIMER RESET

def reset_timer():
    global reps, check_mark_str, timer, paused, remaining_count
 
    if timer is not None:
        window.after_cancel(timer)
        timer = None
 
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)
    reps = 0
    check_mark_str = ""
    paused = False
    remaining_count = 0
 
    check_mark.config(text="")
    start_button.config(state="normal")
    pause_button.config(text="Pause", state="disabled")
    window.title("Pomodoro App")

#PAUSE BUTTON

def pause_resume():
    global paused, timer, remaining_count
 
    if not paused:
        # Pause: cancel the scheduled callback and remember remaining time
        if timer is not None:
            window.after_cancel(timer)
            timer = None
        paused = True
        pause_button.config(text="Resume")
    else:
        # Resume: restart countdown from where we left off
        paused = False
        pause_button.config(text="Pause")
        count_down(remaining_count)

#SETTINGS

def open_settings():
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
 
    work = tkinter.simpledialog.askinteger(
        "Settings", "Work duration (minutes):",
        initialvalue=WORK_MIN, minvalue=1, maxvalue=120,
    )

    if work is None:
        return
    short = tkinter.simpledialog.askinteger(
        "Settings", "Short break duration (minutes):",
        initialvalue=SHORT_BREAK_MIN, minvalue=1, maxvalue=60
    )
    if short is None:
        return
    long = tkinter.simpledialog.askinteger(
        "Settings", "Long break duration (minutes):",
        initialvalue=LONG_BREAK_MIN, minvalue=1, maxvalue=120
    )
    if long is None:
        return
 
    WORK_MIN = work
    SHORT_BREAK_MIN = short
    LONG_BREAK_MIN = long


#TIMER MECHANISM

def start_timer():
    global reps
 
    reps += 1
    session_num = (reps + 1) // 2  # current work session number
 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
 
    start_button.config(state="disabled")
    pause_button.config(state="normal")
 
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(fg=RED, text="Break")
        window.title("Pomodoro – Long Break")
 
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(fg=PINK, text="Break")
        window.title("Pomodoro – Short Break")
 
    else:
        count_down(work_sec)
        label.config(fg=GREEN, text="Work")
        total_sessions = 4
        window.title(f"Pomodoro – Work (Session {session_num} of {total_sessions})")


#COUNTDOWN MECHANISM

def count_down(count):
    global timer, check_mark_str, remaining_count
 
    remaining_count = count
 
    count_min = count // 60
    count_secs = count % 60
 
    if count_secs < 10:
        count_secs = f"0{count_secs}"
 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
 
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Add a checkmark after each completed work session (odd reps)
        if reps % 2 != 0:
            check_mark_str += "✓"
            check_mark.config(text=check_mark_str)



#UI MECHANISM

def setup_ui():
    global window, canvas, timer_text, label, check_mark
    global start_button, pause_button, reset_button
 
    # Window
    window = tkinter.Tk()
    window.title("Pomodoro App")
    window.config(padx=100, pady=50, bg=YELLOW)
 
    # Canvas
    canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tkinter.PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    canvas.tomato_img = tomato_img  # keep reference to avoid GC
    timer_text = canvas.create_text(
        100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
    )
    canvas.grid(row=1, column=1)
 
    # Title label
    label = tkinter.Label(
        text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW
    )
    label.grid(row=0, column=1)
 
    # Session info label
    session_label = tkinter.Label(
        text="", font=(FONT_NAME, 10, "normal"), fg=GREEN, bg=YELLOW
    )
    session_label.grid(row=0, column=1, sticky="s", pady=(60, 0))
 
    # Check mark label
    check_mark = tkinter.Label(
        text="", font=(FONT_NAME, 15, "normal"), fg=GREEN, bg=YELLOW
    )
    check_mark.grid(row=3, column=1)
 
    # Start button
    start_button = tkinter.Button(
        text="Start", highlightthickness=0,
        command=start_timer, width=5, height=1
    )
    start_button.grid(row=2, column=0)
 
    # Pause button (disabled until started)
    pause_button = tkinter.Button(
        text="Pause", highlightthickness=0,
        command=pause_resume, width=5, height=1, state="disabled"
    )
    pause_button.grid(row=2, column=1)
 
    # Reset button
    reset_button = tkinter.Button(
        text="Reset", highlightthickness=0,
        command=reset_timer, width=5, height=1
    )
    reset_button.grid(row=2, column=2)
 
    # Settings button
    settings_button = tkinter.Button(
        text="⚙ Settings", highlightthickness=0,
        command=open_settings, width=10, height=1
    )
    settings_button.grid(row=4, column=1, pady=(10, 0))
 
    window.mainloop()


setup_ui()
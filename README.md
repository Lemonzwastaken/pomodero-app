# 🍅 Pomodoro Timer

A simple desktop Pomodoro timer built with Python and Tkinter.

## How It Works

The Pomodoro technique breaks work into focused sessions separated by short breaks:

- **Work session** — 25 minutes of focused work
- **Short break** — 5 minutes of rest
- **Long break** — 20 minutes of rest after every 4 work sessions

Completed work sessions are tracked with ✓ checkmarks at the bottom of the app.

## Usage

### Running from source
Make sure Python is installed, then:
```bash
python pomodoro.py
```

### Running the compiled app
Just double-click the `.exe` inside the `dist/` folder — no Python required.

## Controls

| Button | Action |
|--------|--------|
| Start | Begin the current session |
| Pause / Resume | Pause or continue the timer |
| Reset | Cancel the timer and start over |
| ⚙ Settings | Customize session durations |

## Requirements

- Python 3.x
- Tkinter (included with Python by default)
- `tomato.png` in the same directory as `pomodoro.py`

## Building from Source

```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --add-data "tomato.png;." pomodoro.py
```

The compiled `.exe` will appear in the `dist/` folder.
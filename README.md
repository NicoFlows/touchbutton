# Touch Button for SuperWhisper

A minimal floating microphone button for Windows touchscreens that triggers [SuperWhisper](https://superwhisper.com/) voice transcription with a single tap.

## Features

- **Always-on-top** floating button that stays visible over other windows
- **Touch-friendly** large microphone button (200x200px)
- **Non-intrusive** — doesn't steal focus from your active application
- **Position memory** — remembers where you placed it between sessions

## Requirements

- Windows
- Python 3.x
- [pynput](https://pypi.org/project/pynput/)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/touchbutton.git
   cd touchbutton
   ```

2. Install dependencies:
   ```bash
   pip install pynput
   ```

## Usage

```bash
python touchbutton.py
```

Drag the button to your preferred screen location. Click or tap the microphone button to send `Ctrl+Space`, which activates SuperWhisper transcription.

The window position is saved automatically when you close the application.

## Configuration

The button sends `Ctrl+Space` by default. To change the shortcut, modify the `send_shortcut()` function in `touchbutton.py`:

```python
def send_shortcut():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    keyboard.release(Key.ctrl)
```

Window position is stored in `whisper_pos.json` in the same directory as the script.

## How It Works

The application uses tkinter for the GUI and pynput for keyboard simulation. To prevent the button from stealing focus when clicked (which would interrupt typing), it uses the Windows API to apply the `WS_EX_NOACTIVATE` extended window style via ctypes.

## License

MIT

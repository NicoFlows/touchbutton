import tkinter as tk
from pynput.keyboard import Controller, Key
import ctypes
import json
import os

GWL_EXSTYLE = -20
WS_EX_NOACTIVATE = 0x08000000
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "whisper_pos.json")

keyboard = Controller()

def send_shortcut():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    keyboard.release(Key.ctrl)

def save_position():
    with open(CONFIG_FILE, 'w') as f:
        json.dump({'x': root.winfo_x(), 'y': root.winfo_y()}, f)

def load_position():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

root = tk.Tk()
root.title("Whisper")
root.geometry("200x200")
root.configure(bg="#2d2d2d")
root.attributes('-topmost', True)

pos = load_position()
if pos:
    root.geometry(f"200x200+{pos['x']}+{pos['y']}")

btn = tk.Button(
    root,
    text="🎤",
    font=("Arial", 48),
    command=send_shortcut,
    bg="#4a9eff",
    fg="white",
    activebackground="#3a8eef",
    relief="flat",
    width=4,
    height=1
)
btn.pack(expand=True, fill="both", padx=10, pady=10)

root.update()
hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_NOACTIVATE)

root.protocol("WM_DELETE_WINDOW", lambda: (save_position(), root.destroy()))

root.mainloop()
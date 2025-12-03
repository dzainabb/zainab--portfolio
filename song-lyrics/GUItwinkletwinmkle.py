import tkinter as tk
from tkinter import scrolledtext
import time
import threading

def print_lyrics(text_widget):
    lyrics = [
        'Twinkle, twinkle, little star,',
        'How I wonder what you are!',
        'Up above the world so high,',
        'Like a diamond in the sky.',
        'Twinkle, twinkle, little star,'
    ]
    delays = [1, 1, 1.5, 1.5, 1]

    text_widget.insert(tk.END, "Starting to sing the song...\n")
    text_widget.see(tk.END)
    time.sleep(2)

    for i, line in enumerate(lyrics):
        for char in line:
            text_widget.insert(tk.END, char)
            text_widget.see(tk.END)
            time.sleep(0.05)
        text_widget.insert(tk.END, "\n")
        text_widget.see(tk.END)

        delay = delays[i] if i < len(delays) else 1
        time.sleep(delay)

def start_singing():
    # run animation on a background thread so UI stays responsive
    t = threading.Thread(target=print_lyrics, args=(text_area,))
    t.start()


root = tk.Tk()
root.title("Twinkle Twinkle")

text_area = scrolledtext.ScrolledText(root, width=50, height=15, font=("Times New Roman", 30))
text_area.pack(padx=10, pady=10)

start_button = tk.Button(root, text="Start Singing",command=start_singing, font=("Times New Roman", 35))
start_button.pack(pady=5)

root.mainloop()

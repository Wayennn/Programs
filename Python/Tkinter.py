import tkinter as tk

window=tk.Tk()
window.title("yo")
greeting = tk.Label(text="Hello, Python tkinter!",
                    bg="#34A2FE",
                    fg="#fc7468",
                    height=5)
greeting.pack()
entry = tk.Entry()
entry.pack()
text = tk.Text()
text.pack()
button = tk.Button(window,
    text="Click me!",
    height=5,
    bg="#fc7468",
    fg="#34A2FE",
)
button.pack()
canvas = tk.Canvas()
canvas.pack()

entry.insert(0, "asdfasdf")


window.mainloop()
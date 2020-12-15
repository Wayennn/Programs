import tkinter as tk

window = tk.Tk()
window.title("Calculator")

frameField = tk.Frame(window,
                      bd = 5,
                      bg = "#8C86AA")
textField = tk.Text(frameField,
                    width=10,
                    height=2)

frameButtons = tk.Frame(window,
                      bd = 1,
                      bg = "#81559B")

def oper(button):
    textField.insert(tk.END, button["text"])

def btn(lbl):
    button = tk.Button(frameButtons,
                           bg = "#DAFF7D",
                           activebackground = "#8C86AA",
                           text = lbl,
                           width = 4,
                           height = 2)
    return button

btndg = [btn(0)]
for i in range(3):
    for j in range(3):
        btndg.append(btn(1+j+3*i))
        btndg[1+j+3*i]["command"] = lambda : oper(btndg[1+j+3*i])
        btndg[1+j+3*i].grid(row = 2-i,
                    column = j,
                    padx = 2,
                    pady = 2)

btndg[0].grid(row = 3, column = 1)

btns = ["+", "-", "*", "/", "="]
for i in range(len(btns) - 1):
    button = btn(btns[i])
    button.grid(row = i,
                column = 3)
button = btn(btns[4])
button.grid(row = 3,
            column = 2)


textField.pack(fill = tk.BOTH, expand=True)
frameField.pack(fill = tk.BOTH, expand=True)
frameButtons.pack(fill = tk.BOTH, expand=True)

window.mainloop()
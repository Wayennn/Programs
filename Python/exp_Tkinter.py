import tkinter as tk

opera = True
num1 = 0
num2 = 0
op = ["+", "-", "*", "/"]
ops = 0

class Button():
    def __init__(self, kind, txt, display = None):
        self.kind = kind
        self.txt = txt
        self.display = display
        self.btnFrame = tk.Frame(self.kind, bd = 2, padx = 2, pady = 2, bg = "#57A773")
        self.btn = tk.Button(self.btnFrame, text = self.txt, font = "Helvetica 20", bg = "#08B2E3", height = 1, width = 3)
        if self.txt=="AC" or self.txt=="=":
            self.btn["height"] = 3
        if self.txt=="AC" or self.txt=="DEL":
            self.btn["bg"] = "#EE6352"
        global op
        if self.txt in op:
            self.btn["bg"] = "#767991"
        self.btn.pack(fill = tk.BOTH, expand = True)
    
    def oper(self):
        global opera, num1, op, ops
        if ops!=0:
            self.eq()
        try:
            num1 = float(self.display.get())
        except ValueError:
            if self.display.get()=="":
                num1 = 0
                self.display.insert(tk.END, num1)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "SYNTAX ERROR")
        opera = True
        for i in range(len(op)):
            if self.txt==op[i]:
                ops = i + 1
                break
        
    def eq(self):
        global ops, num1, num2, opera
        try:
            num2 = float(self.display.get())
            self.display.delete(0, tk.END)
            if ops==0:
                self.display.insert(tk.END, self.wholer(num2))
            elif ops==1:
                self.display.insert(tk.END, self.wholer(num1+num2))
            elif ops==2:
                self.display.insert(tk.END, self.wholer(num1-num2))
            elif ops==3:
                self.display.insert(tk.END, self.wholer(num1*num2))
            elif ops==4:
                try:
                    self.display.insert(tk.END, num1/num2)
                except ZeroDivisionError:
                    self.display.insert(tk.END, "MATH ERROR")
        except ValueError:
            if self.display.get()=="":
                num2 = 0
                self.display.insert(tk.END, num2)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "SYNTAX ERROR")
        opera = True
        num1 = num2
        ops = 0
    
    def clearer(self):
        global num1, num2, opera
        self.display.delete(0, tk.END)
        num1 = 0
        num2 = 0
        self.display.insert(tk.END, 0)
        opera = True
        
    def deleter(self):
        global num2, opera
        self.display.delete(len(self.display.get())-1, tk.END)
        if self.display.get()=="":
            num2 = 0
            self.display.insert(tk.END, num2)
            opera = True
    
    def click(self):
        global opera
        if opera:
            self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.txt)
        opera = False
    
    def wholer(self, num):
        if num%1==0:
            return int(num)
        else:
            return num

class Calculator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.add_display()
        self.keysFrame = tk.Frame(self.window, bg = "#484D6D")
        self.keysFrame.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
        for i in range(5):
            for j in range(4):
                tk.Grid.rowconfigure(self.keysFrame, j, weight = 1)
            tk.Grid.columnconfigure(self.keysFrame, i, weight = 1)
        self.add_digitsButtons()
        self.add_operationButtons()
        
    def add_display(self):
        self.dispFrame = tk.Frame(self.window, bd = 10, bg = "#484D6D")
        self.dispFrame.pack(fill = tk.BOTH, expand = True)
        self.disp = tk.Entry(self.dispFrame, font = "Helvetica 30", width = 10, justify = "right")
        self.disp.pack(fill = tk.BOTH, expand = True)
        self.disp.insert(tk.END, 0)
        
    def add_digitsButtons(self):
        self.digitButtons = [Button(self.keysFrame, 0, self.disp)]
        self.digitButtons[0].btnFrame.grid(row = 3, column = 0, sticky = tk.N+tk.S+tk.E+tk.W)
        self.digitButtons[0].btn["command"] = self.digitButtons[0].click
        for i in range(3):
            for j in range(3):
                self.digitButtons.append(Button(self.keysFrame, 1+j+3*i, self.disp))
                self.digitButtons[1+j+3*i].btnFrame.grid(row = 2-i, column = j, sticky = tk.N+tk.S+tk.E+tk.W)
                self.digitButtons[1+j+3*i].btn["command"] = self.digitButtons[1+j+3*i].click
        self.digitButtons.append(Button(self.keysFrame, ".", self.disp))
        self.digitButtons[-1].btnFrame.grid(row = 3, column = 1, sticky = tk.N+tk.S+tk.E+tk.W)
        self.digitButtons[-1].btn["command"] = self.digitButtons[-1].click
    
    def add_operationButtons(self):
        global op
        self.oper = []
        for i in range(len(op)):
            self.oper.append(Button(self.keysFrame, op[i], self.disp))
            self.oper[i].btnFrame.grid(row = i, column = 3, sticky = tk.N+tk.S+tk.E+tk.W)
            self.oper[i].btn["command"] = self.oper[i].oper
        self.delete = Button(self.keysFrame, "DEL", self.disp)
        self.delete.btnFrame.grid(row = 3, column = 2, sticky = tk.N+tk.S+tk.E+tk.W)
        self.delete.btn["command"] = self.delete.deleter
        self.clear = Button(self.keysFrame, "AC", self.disp)
        self.clear.btnFrame.grid(row = 0, column = 4, rowspan = 2, sticky = tk.N+tk.S+tk.E+tk.W)
        self.clear.btn["command"] = self.clear.clearer
        self.equ = Button(self.keysFrame, "=", self.disp)
        self.equ.btnFrame.grid(row = 2, column = 4, rowspan = 2, sticky = tk.N+tk.S+tk.E+tk.W)
        self.equ.btn["command"] = self.equ.eq
        
        
calc = Calculator()
calc.window.mainloop()
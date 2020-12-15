import tkinter as tk
from numpy import random

class GenerateKeys():
    def __init__(self):
        primes = []
        with open("Files\primes-500-to-1k.txt", "r") as fl:
            for line in fl.readlines():
                primes.append(int(line))
        l = int(len(primes))
        while True:
            p = primes[random.randint(0, l)]
            q = primes[random.randint(0, l)]
            if (p-1)%3!=0 and (q-1)%3!=0 and p!=q:
                break
        self.n = p*q
        self.d = int((2*(p-1)*(q-1)+1)/3)
        self.mKey = random.randint(self.n - 1000, self.n)
        
    def putKey(self, keysFrame, keyType):
        self.keyL = tk.Label(keysFrame, text = keyType, bg="#E38AE6", font=("Georgia", 12), padx=10, pady=2)
        self.keyL.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.key = tk.Entry(keysFrame, bg="#E8C2D2", font=("Segoe UI", 14), width=7, justify = "right")
        if keyType=="Public Key":
            self.key.insert(tk.END, str(self.n))
        elif keyType=="Private Key":
            self.key.insert(tk.END, str(self.d))
        self.key.config(state = "readonly")
        self.key.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        
class SendKeys():
    def __init__(self, keysFrame, keyType, s = None):
        self.keyL = tk.Label(keysFrame, text = keyType, bg="#6E81F7", font=("Georgia", 12), padx=10, pady=2)
        self.keyL.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.key = tk.Entry(keysFrame, bg="#FFFFFF", font=("Segoe UI", 14), width=7, justify = "right")
        if keyType=="Master Key" and s==None:
            self.key.config(state = "readonly")
        elif keyType=="Master Key":
            self.keyL["bg"] = "#E38AE6"
        self.key.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        self.mKeyT = None
        
    def mcreate(self, pkey):
        try:
            self.mKey = random.randint(int(pkey) - 1000, int(pkey))
            self.mKeyT = self.mKey
            self.mKey = (self.mKey**3)%int(pkey)
            self.key.config(state = "normal")
            self.key.delete(0, tk.END)
            self.key.insert(tk.END, self.mKey)
            self.key.config(state = "readonly")
        except (ValueError, ZeroDivisionError):
            self.key.config(state = "normal")
            self.key.delete(0, tk.END)
            self.key.insert(tk.END, "404 Key!")
            self.key.config(state = "readonly")

class MakeMessage():
    def __init__(self, messagesFrame, messageType):
        self.messageL = tk.Label(messagesFrame, text = messageType, bg="#E38AE6", font=("Arial Rounded MT Bold", 16), padx=0, pady=2, width=27)
        self.messageL.pack(side = tk.TOP, fill = tk.X)
        self.message = tk.Text(messagesFrame, width = 55, height = 5)
        if messageType=="Encrypted Message" or messageType=="Decrypted Message":
            self.message.config(state = "disabled")
        if messageType=="Message" or messageType=="Encrypted Message":
            self.messageL["bg"] = "#6E81F7"
        self.message.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
    
    def encrypt(self, msg, mKey):
        self.mKey = mKey
        self.msg = [ord(i) for i in list(msg)]
        try:
            if len(msg)==0:
                raise IndexError("No Message")
            mKeyk = list(str(bin(self.mKey)[2:]))
            self.enc = [chr((((self.msg[i]) + i*int(mKeyk[i%len(mKeyk)]))%95) + 32) for i in range(len(self.msg))]
        except (TypeError, ValueError):
            self.enc = list("ERROR: Invalid Master Key!")
        except IndexError:
            self.enc = list("ERROR: No Message!")
        self.message.config(state = "normal")
        self.message.delete("1.0", tk.END)
        self.message.insert(tk.END, "".join(self.enc))
        self.message.config(state = "disabled")
        
    def decrypt(self, rmsg, mKey, d, n):
        try:
            if len(rmsg)==0:
                raise IndexError("No Message")
            self.mKey = (int(mKey)**d)%n
            self.rmsg = [ord(i) for i in list(rmsg)]
            mKeyk = list(str(bin(self.mKey)[2:]))
            self.dec = [chr((((self.rmsg[i] - 32) - 32 - i*int(mKeyk[i%len(mKeyk)])))%95 + 32) for i in range(len(self.rmsg))]
        except ValueError:
            self.dec = list("ERROR: Invalid Master Key!")
        except IndexError:
            self.dec = list("ERROR: No Message!")
        self.message.config(state = "normal")
        self.message.delete("1.0", tk.END)
        self.message.insert(tk.END, "".join(self.dec))
        self.message.config(state = "disabled")

window = tk.Tk()
window.title("RSA Terminal")
window.iconbitmap("Files\RSA Icon.ico")
window.geometry("1250x500+25+75")

generatorFrame = tk.LabelFrame(window, bd=3, bg="#E8C2D2", text = "Generator and Decoder", font = ("Rockwell", 23), labelanchor = "n", padx=10, pady=10, width=625)
generatorFrame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

gen = GenerateKeys()
keysFrame = tk.Frame(generatorFrame, bd=5, bg="#E8C2D2")
gen.putKey(keysFrame, "Public Key")
filler = tk.Frame(keysFrame, width=15, bg="#E8C2D2")
filler.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
gen.putKey(keysFrame, "Private Key")
filler = tk.Frame(keysFrame, width=15, bg="#E8C2D2")
filler.pack(side = tk.LEFT, fill = tk.X)
rmkey = SendKeys(keysFrame, "Master Key", "s")
keysFrame.pack(side = tk.TOP, fill = tk.X)
messagesFrame = tk.Frame(generatorFrame, bd=5, bg="#E8C2D2")
messagesFrame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
rmsg = MakeMessage(messagesFrame, "Received Message")
filler = tk.Frame(messagesFrame, height=25, bg="#E8C2D2")
filler.pack(side = tk.TOP, fill = tk.X)
submit = tk.Button(messagesFrame, text = "Decrypt", font = ("Cooper Black", 15), fg="#000000", bg="#E4A9B8", padx=150, pady=5, relief = tk.GROOVE, cursor = "hand2",
                   command = lambda : dmsg.decrypt(rmsg.message.get("1.0", "end-1c"), rmkey.key.get(), gen.d, gen.n))
submit.pack(side = tk.TOP)
filler = tk.Frame(messagesFrame, height=15, bg="#E8C2D2")
filler.pack(side = tk.TOP, fill = tk.X)
dmsg = MakeMessage(messagesFrame, "Decrypted Message")

senderFrame = tk.LabelFrame(window, bd=3, bg="#9CA9FA", text = "Sender", font = ("Rockwell", 23), labelanchor = "n", padx=10, pady=10, width=625)
senderFrame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

sen = GenerateKeys()
keysFrame = tk.Frame(senderFrame, bd=5, bg="#9CA9FA")
pkey = SendKeys(keysFrame, "Public Key")
filler = tk.Frame(keysFrame, width=15, bg="#9CA9FA")
filler.pack(side = tk.LEFT, fill = tk.X)
enter = tk.Button(keysFrame, text = "Enter", font = ("Cooper Black", 11), fg="#000000", bg="#6E81F7", padx=20, pady=1, relief = tk.GROOVE, cursor = "hand2",
                  command = lambda : mkey.mcreate(pkey.key.get()))
enter.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
filler = tk.Frame(keysFrame, width=45, bg="#9CA9FA")
filler.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
mkey = SendKeys(keysFrame, "Master Key")
keysFrame.pack(side = tk.TOP, fill = tk.X)
messagesFrame = tk.Frame(senderFrame,  bd=5, bg="#9CA9FA")
messagesFrame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
msg = MakeMessage(messagesFrame, "Message")
filler = tk.Frame(messagesFrame, height=25, bg="#9CA9FA")
filler.pack(side = tk.TOP, fill = tk.X)
submit = tk.Button(messagesFrame, text = "Encrypt", font = ("Cooper Black", 15), fg="#000000", bg="#7587F8", padx=150, pady=5, relief = tk.GROOVE, cursor = "hand2",
                   command = lambda : emsg.encrypt(msg.message.get("1.0", "end-1c"), mkey.mKeyT))
submit.pack(side = tk.TOP)
filler = tk.Frame(messagesFrame, height=15, bg="#9CA9FA")
filler.pack(side = tk.TOP, fill = tk.X)
emsg = MakeMessage(messagesFrame, "Encrypted Message")

window.mainloop()
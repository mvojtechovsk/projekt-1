#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox as msb
import matplotlib.pyplot as py
import numpy as np

# from tkinter import ttk


class Uloha1(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Uloha2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        def Graf():
            R = float(vstupR.get())
            C = float(vstupC.get()) * 0.000001
            U = float(vstupU.get())
            if R == 0 or C == 0:
                msb.showwarning("Chyba!", "Graf nejde udelat")
            else:
                x = np.arange(0, 5 * R * C, 5 * R * C / 50)
                y = []
                for i in x:
                    y.append(U * (1 - np.e ** ((-i) / (R * C))))
                py.title("Graf")
                py.xlabel("t[s]")
                py.ylabel("U[V]")
                py.plot(x, y)
                py.grid(True)
                py.show()

        popisR = tk.Label(self, text="zadej ohm", font="Calibri 10")
        popisR.grid()
        vstupR = tk.Entry(self, font="Calibri 10")
        vstupR.grid(row=1, padx=5)

        popisC = tk.Label(self, text="zadej C", font="Calibri 10")
        popisC.grid(row=2)
        vstupC = tk.Entry(self, font="Calibri 10")
        vstupC.grid(row=3, padx=5)

        popisU = tk.Label(self, text="zadej U", font="Calibri 10")
        popisU.grid(row=4)
        vstupU = tk.Entry(self, font="Calibri 10")
        vstupU.grid(row=5, padx=5)

        graf = tk.Button(self, text="vytvoř \ngraf", font="Calibri 10 bold", command=Graf)
        graf.grid(row=0, column=1, rowspan=6, sticky=tk.N + tk.S, padx=5)


class Uloha3(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()
        self.labelM = tk.Label(self, text="m")
        self.labelM.pack()
        self.entryM = tk.Entry(self)
        self.entryM.pack()
        self.labelN = tk.Label(self, text="n")
        self.labelN.pack()
        self.entryN = tk.Entry(self)
        self.entryN.pack()
        self.labelX = tk.Label(self, text="x")
        self.labelX.pack()
        self.entryX = tk.Entry(self)
        self.entryX.pack()
        btn = tk.Button(self, text="Výpočet", command=self.vypocet3)
        btn.pack()

        self.labelV = tk.Label(self, text="Vysledek")
        self.labelV.pack()
        self.entryV = tk.Entry(self)
        self.entryV.pack()
        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()


    def vypocet3(self):
        x = self.entryX.get()
        n = self.entryN.get()
        m = self.entryM.get() 
        if m<=n:
            """"tady místo 1 bude vzorec"""
            vysledek=1
            print(vysledek)


        else:
            msb.showwarning("Chyba!")    


    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "App"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn1 = tk.Button(self, text="Uloha 1", command=self.uloha1)
        self.btn1.pack()
        self.btn2 = tk.Button(self, text="Uloha 2", command=self.uloha2)
        self.btn2.pack()
        self.btn3 = tk.Button(self, text="Uloha 3", command=self.uloha3)
        self.btn3.pack()

    def uloha1(self):
        window = Uloha1(self)
        window.grab_set()

    def uloha2(self):
        window = Uloha2(self)
        window.grab_set()

    def uloha3(self):
        window = Uloha3(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()

    def vypocet3(self, event=None):
        pass


app = Application()
app.mainloop()

import tkinter as tk
from tkinter import ttk

key = tk.Tk()
key.title('On Screen Keyboard - Vowel QWERTY')

# key.resizable(True,True)
# sizegrip = ttk.Sizegrip(key)
# sizegrip.grid(row=4, sticky= tk.SE)

#ADJUST THESE TO MATCH SPECS OF SCREEN WE GET LOANED
key.geometry('1385x320')  # Window size
# key.maxsize(width=1385, height=320) 
# key.minsize(width=1385, height=320)

key.resizable(True,True)
sizegrip = ttk.Sizegrip(key)
sizegrip.grid(row=4, sticky= tk.SE)

#Style
style = ttk.Style()
key.configure(bg='DarkSlateGrey')
style.configure('TButton', background='DarkSlateGray4')
style.configure('TButton', foreground='white')
theme = "light"
style.map('TButton', background=[('active','red')])

#my code
style.configure('.', font=('Helvetica', 12, 'bold'), background='blue', foreground='white')
style.configure('JS.TButton', font=('Helvetica', 12), background='blue', foreground='black')

#Entry Box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)

# Initializing Global Variables
text = " "
is_shift = False
is_Caps = False

def Caps():
    global is_Caps
    is_Caps = not is_Caps
    display()
    
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def Backspace():
    global exp
    exp = exp[:-1]
    equation.set(exp)
def Clear():
    global exp
    exp = " "
    equation.set(exp)
def Shift():
    global is_dhift
    is_shift = not is_shift
    display()
    
def Theme():
    global theme
    if theme == "dark":
        key.configure(bg='DarkSlateGrey')
        style.configure('TButton', background='DarkSlateGray4')
        style.configure('TButton', foreground='white')
        theme = "light"
    elif theme == "light":
        key.configure(bg='gray99')
        style.configure('TButton', background='azure')
        style.configure('TButton', foreground='black')
        theme = "dark"

def Cap_s():
    if (is_shift == False):
        #First Row
        tick = ttk.Button(key, text='`', width=6, command=lambda: press('`'))
        tick.grid(row=1, column=0, ipadx=6, ipady=10)

        num1 = ttk.Button(key, text='1', width=6, command=lambda: press('1'))
        num1.grid(row=1, column=1, ipadx=6, ipady=10)

        num2 = ttk.Button(key, text='2', width=6, command=lambda: press('2'))
        num2.grid(row=1, column=2, ipadx=6, ipady=10)

        num3 = ttk.Button(key, text='3', width=6, command=lambda: press('3'))
        num3.grid(row=1, column=3, ipadx=6, ipady=10)

        num4 = ttk.Button(key, text='4', width=6, command=lambda: press('4'))
        num4.grid(row=1, column=4, ipadx=6, ipady=10)

        num5 = ttk.Button(key, text='5', width=6, command=lambda: press('5'))
        num5.grid(row=1, column=5, ipadx=6, ipady=10)

        num6 = ttk.Button(key, text='6', width=6, command=lambda: press('6'))
        num6.grid(row=1, column=6, ipadx=6, ipady=10)

        num7 = ttk.Button(key, text='7', width=6, command=lambda: press('7'))
        num7.grid(row=1, column=7, ipadx=6, ipady=10)

        num8 = ttk.Button(key, text='8', width=6, command=lambda: press('8'))
        num8.grid(row=1, column=8, ipadx=6, ipady=10)

        num9 = ttk.Button(key, text='9', width=6, command=lambda: press('9'))
        num9.grid(row=1, column=9, ipadx=6, ipady=10)

        num0 = ttk.Button(key, text='0', width=6, command=lambda: press('0'))
        num0.grid(row=1, column=10, ipadx=6, ipady=10)

        minus = ttk.Button(key, text='-', width=6, command=lambda: press('-'))
        minus.grid(row=1, column=11, ipadx=6, ipady=10)

        equal = ttk.Button(key, text='=', width=6, command=lambda: press('='))
        equal.grid(row=1, column=12, ipadx=6, ipady=10)
        
        backspace = ttk.Button(key, text="<--", width = 6, command = Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10)
        
        


def display():
    if is_Caps:
        Cap_s()
        

display()
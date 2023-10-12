from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry('600x500')
window.title('Available Trains')
window.configure(bg='white')
window.resizable(False,False)

L1 = Label(window, text = '''
           LALBAGH EXP(12607)       Runs On: M T W Th F Sa S
           15:30| MGR CHENNAI CTL    ---01:18---   15:43| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           GARUDADRI EXP(16203)       Runs On: M T W Th F Sa S
           16:35| MGR CHENNAI CTL    ---01:23---   16:48| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           17:55| MGR CHENNAI CTL    ---01:23---   18:08| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           YERCAUD EXP(22649)       Runs On: M T W Th F Sa S
           23:00| MGR CHENNAI CTL    ---01:18---   23:14| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()

window.mainloop()

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
           YERCAUD EXP(22650)       Runs On: M T W Th F Sa S
           02:10| ARAKKONAM JN    ---01:18---   03:08| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           CHENNAI CENTRAL EXP(22652)       Runs On: M T W Th F Sa S
           02:30 ARAKKONAM JN   ---01:23---   03:23| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           CHENNAI CENTRAL MAIL EXP(12658)       Runs On: M T W Th F Sa S
           02:50| ARAKKONAM    ---01:28---   03:38| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           NILGIRI EXP(12672)       Runs On: M T W Th F Sa S
           04:45| ARAKKONAM   ---01:28---   05:38| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           CHENGALPATTU EXP(17652)       Runs On: M T W Th F Sa S
           04:55| ARAKKONAM     ---01:28---   05:53| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()


window.mainloop()

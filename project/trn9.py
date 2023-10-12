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
           02:10| ARAKKONAM JN    ---01:18---   03:40| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           CHENNAI CENTRAL EXP(22652)       Runs On: M T W Th F Sa S
           02:30 ARAKKONAM JN   ---01:23---   07:48| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           CHENNAI CENTRAL MAIL EXP(12658)       Runs On: M T W Th F Sa S
           02:50| ARAKKONAM    ---01:28---   04:15| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           NILGIRI EXP(12672)       Runs On: M T W Th F Sa S
           04:45| ARAKKONAM   ---01:28---   6:20| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           KAVERI EXP(16022)       Runs On: M T W Th F Sa S
           05:05| ARAKKONAM     ---01:28---   06:45| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()
L6 = Label(window, text = '''
           CHERAN EXP(12674)       Runs On: M T W Th F Sa S
           05:20| ARAKKONAM JN    ---01:28---   19:43| MGR CHENNAI CTL 
           ''',
           bg='light blue', font=('Cambria Bold',13))
L6.pack()

window.mainloop()

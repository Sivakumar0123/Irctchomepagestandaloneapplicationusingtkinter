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
           02:35| TIRUVALLUR    ---00:18---   03:08| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           CHENNAI CENTRAL EXP(22652)       Runs On: M T W Th F Sa S
           02:55| TIRUVALLUR   ---00:23---   03:23| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           KAVERI EXP(16022)       Runs On: M T W Th F Sa S
           05:30| TIRUVALLUR    ---00:28---   05:58| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           YELAGIRI EXP(16090)       Runs On: M T W Th F Sa S
           08:15| TIRUVALLUR ---00:28---   08:43| PERAMBUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           GARUDADRI EXP(16204)       Runs On: M T W Th F Sa S
           08:50| TIRUVALLUR ---00:28---   09:46| PERAMBUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()


window.mainloop()

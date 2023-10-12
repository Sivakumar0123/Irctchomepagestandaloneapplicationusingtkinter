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
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           14:15| TIRUVALLUR    ---00:18---   14:58| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           18:40| TIRUVALLUR   ---00:23---   19:35| SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           KAVERI EXP(16021)       Runs On: M T W Th F Sa S
           21:55| TIRUVALLUR    ---00:28---   22:43| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()

window.mainloop()

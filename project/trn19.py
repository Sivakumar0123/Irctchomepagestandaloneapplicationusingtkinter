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
           15:45| PERAMBUR    ---00:18---   16:33| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           GARUDADRI EXP(16203)       Runs On: M T W Th F Sa S
           16:50| PERAMBUR   ---00:23---   17:38| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           18:10| PERAMBUR    ---00:28---   19:03| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           YERCAUD EXP(22649)       Runs On: M T W Th F Sa S
           23:15| PERAMBUR   ---00:23---   12:03| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()

window.mainloop()

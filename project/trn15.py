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
           ALAPPUZHA EXP(13351)       Runs On: M T W Th F Sa S
           12:20| TIRUVALLUR    ---00:18---   12:43| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           SAPTHAGIRI EXP(16057)       Runs On: M T W Th F Sa S
           07:10| TIRUVALLUR   ---00:23---   07:33| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           MUMBAI CSMT EXP(22160)       Runs On: M T W Th F Sa S
           14:05| TIRUVALLUR    ---00:28---   14:28| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           14:15| TIRUVALLUR ---00:28---   14:28| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           TIRUPATI EXP(16053)       Runs On: M T W Th F Sa S
           14:55| TIRUVALLUR ---00:28---   15:23| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()


window.mainloop()

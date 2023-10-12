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
           BRINDAVAN EXP(12639)       Runs On: M T W Th F Sa S
           08:40| ARAKKONAM JN    ---00:18---   08:58| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           14:40| ARAKKONAM JN   ---00:23---   15:58| SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           LALBAGH EXP(12607)       Runs On: M T W Th F Sa S
           16:35| ARAKKONAM JN    ---00:28---   16:53| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           19:05| ARAKKONAM JN  ---00:28---   19:35| SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           KAVERI EXP(16021)       Runs On: M T W Th F Sa S
           22:20| ARAKKONAM JN    ---00:28---   08:48| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()


window.mainloop()

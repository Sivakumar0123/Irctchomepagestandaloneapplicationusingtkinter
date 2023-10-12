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
           KAVERI EXP(16022)       Runs On: M T W Th F Sa S
           04:30| SHOLINGHUR    ---00:18---   05:03| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           YELAGIRI EXP(16090)       Runs On: M T W Th F Sa S
           07:10 SHOLINGHUR   ---00:23---   07:48| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           ARAKKONAM MEMU EXP(16086)       Runs On: M T W Th F Sa S
           09:13| SHOLINGHUR    ---00:28---   09:45| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           LALBAGH EXP(12608)       Runs On: M T W Th F Sa S
           10:25| SHOLINGHUR    ---00:28---   10:43| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           MGR CHENNAI EXP(12610)       Runs On: M T W Th F Sa S
           12:35| SHOLINGHUR    ---00:28---   12:48| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()
L6 = Label(window, text = '''
           BRINDAVAN EXP(12640)       Runs On: M T W Th F Sa S
           19:20| SHOLINGHUR    ---00:28---   19:43| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L6.pack()
L7 = Label(window, text = '''
           SALEM - ARAKKONAM EXP(16088)       Runs On: M T W Th F Sa S
           19:50| SHOLINGHUR    ---00:28---   20:45| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L7.pack()

window.mainloop()

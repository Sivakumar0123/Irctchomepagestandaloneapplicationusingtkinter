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
           KOVAI SF EXP(12675)       Runs On: M T W Th F Sa S
           06:10| MGR CHENNAI CTL    ---01:18---   07:08| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           KSR BENGALURU EXP(22625)       Runs On: M T W Th F Sa S
           07:25| MGR CHENNAI CTL    ---01:23---   08:23| ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           BRINDAVAN EXP(12639)       Runs On: M T W Th F Sa S
           07:40| MGR CHENNAI CTL    ---01:23---   08:38| ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           13:15| MGR CHENNAI CTL    ---01:18---   14:38|ARAKKONAM JN
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           LALBAGH EXP(12695)       Runs On: M T W Th F Sa S
           15:30| MGR CHENNAI CTL    ---01:40---   16:33|ARAKKONAM JN
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()

window.mainloop()

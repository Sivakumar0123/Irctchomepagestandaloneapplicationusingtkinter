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
           04:30| SHOLINGHUR    ---01:18---   06:45| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           YELAGIRI EXP(16090)       Runs On: M T W Th F Sa S
           07:10 SHOLINGHUR   ---01:23---   09:10| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           LALBAGH SF EXP(12608)       Runs On: M T W Th F Sa S
           10:25| SHOLINGHUR    ---01:28---   12:15| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           MGR CHENNAI EXP(12610)       Runs On: M T W Th F Sa S
           12:35| SHOLINGHUR    ---01:28---   14:30| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           YELAGIRI EXP(12640)       Runs On: M T W Th F Sa S
           15:20| SHOLINGHUR    ---01:40---   17:10| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()

window.mainloop()

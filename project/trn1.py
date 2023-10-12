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
           07:40| MGR CHENNAI CTL    ---01:18---   08:58|SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           13:35| MGR CHENNAI CTL    ---01:23---   14:58|SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           LALBAGH EXPRESS(12607)       Runs On: M T W Th F Sa S
           15:30| MGR CHENNAI CTL    ---01:23---   16:53|SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           KAVERI EXPRESS(12639)       Runs On: M T W Th F Sa S
           21:15| MGR CHENNAI CTL    ---01:28---   22:43|SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           17:55| MGR CHENNAI CTL    ---01:40---   19:35|SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()

window.mainloop()

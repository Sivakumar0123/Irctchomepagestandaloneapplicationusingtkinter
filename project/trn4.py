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
           SAPTHAGIRI EXP(16057)       Runs On: M T W Th F Sa S
           06:25| MGR CHENNAI CTL    ---01:18---   07:08| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           MUMBAI CSMT EXP(22160)       Runs On: M T W Th F Sa S
           13:25| MGR CHENNAI CTL    ---01:23---   14:03| TIRUVALLUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           MYSURU EXP(12609)       Runs On: M T W Th F Sa S
           13:35| MGR CHENNAI CTL    ---01:23---   14:13| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           TIRUPATI EXP(16053)       Runs On: M T W Th F Sa S
           14:15| MGR CHENNAI CTL    ---01:18---   14:53| TIRUVALLUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           LALBAGH EXP(16089)       Runs On: M T W Th F Sa S
           17:55| MGR CHENNAI CTL    ---01:40---   18:38| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()

window.mainloop()

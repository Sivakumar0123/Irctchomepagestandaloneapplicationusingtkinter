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
           02:10| ARAKKONAM JN    ---00:18---   02:33| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           CHENNAI CENTRAL EXP(22652)       Runs On: M T W Th F Sa S
           02:30 ARAKKONAM JN   ---00:23---   05:53| TIRUVALLUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           KAVERI EXP(16022)       Runs On: M T W Th F Sa S
           05:05| ARAKKONAM JN    ---00:28---   05:28| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           YELAGIRI EXP(16090)       Runs On: M T W Th F Sa S
           07:50| ARAKKONAM JN  ---00:28---   08:13| TIRUVALLUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           GARUDADRI EXP(16204)       Runs On: M T W Th F Sa S
           08:25| ARAKKONAM JN    ---00:28---   08:48| TIRUVALLUR
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()


window.mainloop()

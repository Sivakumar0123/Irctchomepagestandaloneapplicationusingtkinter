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
           03:10| PERAMBUR    ---00:18---   03:40| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           CHENNAI EXP(22652)       Runs On: M T W Th F Sa S
           03:25| PERAMBUR   ---00:23---   04:05| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()
L3 = Label(window, text = '''
           NILGIRI EXP(12672)       Runs On: M T W Th F Sa S
           05:40| PERAMBUR    ---00:28---   06:20| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L3.pack()
L4 = Label(window, text = '''
           CHERAN EXP(12674)       Runs On: M T W Th F Sa S
           06:50| PERAMBUR   ---00:23---   07:00| MGR CHENNAI CTL
           ''',
           bg='light blue', font=('Cambria Bold',13))
L4.pack()
L5 = Label(window, text = '''
           YELAGIRI EXP(16090)       Runs On: M T W Th F Sa S
           08:45| PERAMBUR    ---00:28---   09:10| MGR CHENNAI CTL
           ''',
           bg='white', font=('Cambria Bold',13))
L5.pack()
window.mainloop()

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
           15:45| PERAMBUR    ---00:35---   16:53| SHOLINGHUR
           ''',
           bg='white', font=('Cambria Bold',13))
L1.pack()
L2 = Label(window, text = '''
           YELAGIRI EXP(16089)       Runs On: M T W Th F Sa S
           18:10| PERAMBUR    ---00:35---   19:35| SHOLINGHUR
           ''',
           bg='light blue', font=('Cambria Bold',13))
L2.pack()

window.mainloop()

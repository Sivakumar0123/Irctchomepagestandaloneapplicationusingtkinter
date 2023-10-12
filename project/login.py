#Loginpage

from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality part

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established. Please try again')
            return
        
        query = 'use userdata'
        mycursor.execute(query)
        
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))  
        row = mycursor.fetchone()
        
        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is successful')
            login_window.destroy()
            import Train



        
def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=show)


def show():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=hide)
    


def user_enter(event):
    if usernameEntry.get()=='username':
        usernameEntry.delete(0,'end')



def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,'end')

#Gui part
        
login_window = Tk()
login_window.geometry('1000x650')
login_window.resizable(0,0)

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading = Label(login_window,text='USER LOGIN',font=('Microsoft Yahel UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#usernameEntry

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

#passwordEntry

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahel UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)


forgetButton = Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahel UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=715,y=295)

#loginButton

loginButton = Button(login_window,text='Login',font=('Open Sans',16,
            'bold'),bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

orLabel = Label(login_window,text='-------------- OR --------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)


twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel = Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

# accountButton

newaccountButton = Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)


login_window.mainloop()



    

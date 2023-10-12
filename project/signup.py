from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,'end')
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    confirmEntry.delete(0,'end')

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Condation')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, emaail varchar(20), username varchar(20), password varchar(20))'  # Add 'email' column
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            
        query = 'select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        
        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already exists')
            
        else:
            query = 'insert into data (emaail,username,password)values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
        
def login_page():
    signup_window.destroy()
    import login
    

signup_window = Tk()
signup_window.title('Signup page')
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window,image=background)
bgLabel.grid()

frame = Frame(signup_window,bg='white')
frame.place(x=554,y=100)


heading = Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahel UI Light',18,'bold'),bg='white',fg='firebrick1')

heading.grid(row=0,column=0,padx=10,pady=10)


emailLabel = Label(frame,text='email',font=('Microsoft Yahel U1 Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry = Entry(frame,width=30,font=('Microsoft Yahel U1 Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel = Label(frame,text='username',font=('Microsoft Yahel U1 Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry = Entry(frame,width=30,font=('Microsoft Yahel U1 Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


passwordLabel = Label(frame,text='Password',font=('Microsoft Yahel U1 Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry = Entry(frame,width=30,font=('Microsoft Yahel U1 Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)



confirmLabel = Label(frame,text='confirmPassword',font=('Microsoft Yahel U1 Light',10,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry = Entry(frame,width=30,font=('Microsoft Yahel U1 Light',10,'bold'),fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()

termscondations = Checkbutton(frame,text='I agree to the terms & Conditions',font=('Microsoft Yahel U1 Light',9,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termscondations.grid(row=9,column=0,pady=10,padx=15)


signupButton = Button(frame,text='Signup',font=('Open sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width='17',command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount = Label(frame,text="Don't have an account",font=('Open sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton = Button(frame,width=6,text='Login',border=0,cursor='hand2',font=('Open Sans',9,'bold underline'),bg='white',fg='blue',command=login_page)
loginButton.place(x=160,y=375)


signup_window.mainloop()

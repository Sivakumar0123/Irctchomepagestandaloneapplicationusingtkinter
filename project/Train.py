from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image


win = tk.Tk()
win.geometry('1000x1000')
win.title('IRCTC Rail Connect')
win.config(bg='white')
win.resizable(False,False)

def FindTrains():

    value1 = C1.get()
    value2 = C2.get()
    if(value1 == 'MGR Chennai Central(MAS)' and value2 == 'Sholinghur(SHU)'):
        import trn1
    elif(value1 == 'Sholinghur(SHU)' and value2 == 'MGR Chennai Central(MAS)'):
        import trn2
    elif(value1 == 'MGR Chennai Central(MAS)' and value2 == 'Arakkonam Junction(AJJ)'):
        import trn3
    elif(value1 == 'MGR Chennai Central(MAS)' and value2 == 'Tiruvallur(TRL)'):
        import trn4
    elif(value1 == 'MGR Chennai Central(MAS)' and value2 == 'Perambur(PER)'):
        import trn5
    elif(value1 == 'Sholinghur(SHU)' and value2 == 'Perambur(PER)'):
        import trn6
    elif(value1 == 'Sholinghur(SHU)'  and value2 == 'Tiruvallur(TRL)' ):
        import trn7
    elif(value1 == 'Sholinghur(SHU)'  and value2 == 'Arakkonam Junction(AJJ)' ):
        import trn8
    elif(value1 == 'Arakkonam Junction(AJJ)' and value2 == 'MGR Chennai Central(MAS)'):
        import trn9
    elif(value1 == 'Arakkonam Junction(AJJ)' and value2 == 'Perambur(PER)'):
        import trn10
    elif(value1 == 'Arakkonam Junction(AJJ)' and value2 == 'Tiruvallur(TRL)'):
        import trn11     
    elif(value1 == 'Arakkonam Junction(AJJ)' and value2 == 'Sholinghur(SHU)'):
        import trn12
    elif(value1 == 'Tiruvallur(TRL)' and value2 == 'MGR Chennai Central(MAS)'):
        import trn13
    elif(value1 == 'Tiruvallur(TRL)' and value2 == 'Perambur(PER)'):
        import trn14
    elif(value1 == 'Tiruvallur(TRL)' and value2 == 'Arakkonam Junction(AJJ)'):
        import trn15
    elif(value1 == 'Tiruvallur(TRL)' and value2 == 'Sholinghur(SHU)'):
        import trn16
    elif(value1 == 'Perambur(PER)' and value2 == 'MGR Chennai Central(MAS)'):
        import trn17
    elif(value1 == 'Perambur(PER)' and value2 == 'Tiruvallur(TRL)'):
        import trn18
    elif(value1 == 'Perambur(PER)' and value2 == 'Arakkonam Junction(AJJ)'):
        import trn19
    elif(value1 == 'Perambur(PER)' and value2 == 'Sholinghur(SHU)'):
        import trn20

        
url2 = "C:\\Users\\siva kumar velu\\Desktop\\project\\train.jpg"
search_img = Image.open(url2)
new_width = 1000
new_height = 1000
search_img1 = search_img.resize((new_width,new_height),Image.Resampling.NEAREST)
temp_path = "C:\\Users\\siva kumar velu\\Desktop\\temp_train.jpg"
search_img1.save(temp_path)
search_img_tk = ImageTk.PhotoImage(search_img1) 
label = Label(win, image=search_img_tk)
label.image = search_img_tk
label.place(x=0, y=0)


L1 = Label(label,text='From:',font=('Cambria Bold',13))
L1.place(x=200, y=300)
L2 = Label(label,text='To:',font=('Cambria Bold',13))
L2.place(x=500, y=300)



C1 = Combobox(label,width=30)
C1['values']=('MGR Chennai Central(MAS)','Perambur(PER)','Tiruvallur(TRL)','Arakkonam Junction(AJJ)','Sholinghur(SHU)')
C1.place(x=270,y=300)
C2 = Combobox(label,width=30)
C2['values']=('MGR Chennai Central(MAS)','Perambur(PER)','Tiruvallur(TRL)','Arakkonam Junction(AJJ)','Sholinghur(SHU)')
C2.place(x=550,y=300)





B1 = tk.Button(label,text='Find Trains',command=FindTrains)
B1.place(x=470,y=350)




win.mainloop()

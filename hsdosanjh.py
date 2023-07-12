import studentmanag
from tkinter import *
mainroot  = Tk()
mainroot.title('student managment system')
mainroot.config(bg='Blue')
mainroot.geometry('1174x700+200+50')
mainroot.resizable(True, True)
#mainroot.iconbitmap('logo.ico')
conButton = Button(mainroot, text='Login ', width=10, font=('oracle', 19, 'bold'), relief=GROOVE, bg = 'green', activebackground='firebrick1',activeforeground='royal blue',command =  studentmanag.main)
conButton.place(x=0,y=0)
mainroot.mainloop()

import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry('200x200')
def Add():
    x=int(a.get())
    y=int(b.get())
    z=x+y
    l=Label(t,text=str(z),font=('arial',12))
    l.place(x=120,y=60)
def Min():
    x=int(a.get())
    y=int(b.get())
    z=x-y
    l=Label(t,text=str(z),font=('arial',12))
    l.place(x=120,y=60)

def Mul():
    x=int(a.get())
    y=int(b.get())
    z=x+y
    l=Label(t,text=str(z),font=('arial',12))
    l.place(x=120,y=60) 
    
def Div():
    x=int(a.get())
    y=int(b.get())
    z=x+y
    l=Label(t,text=str(z),font=('arial',12))
    l.place(x=120,y=60)
    
t.title(" Basic Calculater") 
a=Entry(t,width=200)
a.place(x=0,y=0)
b=Entry(t,width=200)
b.place(x=0,y=30)
l1=Label(t,text="Answer:",font=('arial',12))
l1.place(x=60,y=60)
btn=Button(t,text="+",fg="black",bg="gray",width="13",font=('arial',10),command=Add)
btn.place(x=0,y=120)
btn1=Button(t,text="-",fg="black",bg="gray",width="13",font=('arial',10),command=Min)
btn1.place(x=100,y=120)
btn2=Button(t,text="*",fg="black",bg="gray",width="13",font=('arial',10),command=Mul)
btn2.place(x=0,y=150)
btn3=Button(t,text="/",fg="black",bg="gray",width="13",font=('arial',10),command=Div)
btn3.place(x=100,y=150)
t.mainloop()
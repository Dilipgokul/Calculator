from tkinter import *
import re
roo = Tk()
roo.title("Calculator")
roo.geometry("200x300")
e = Entry(roo,width=33,bg="light grey")
e.grid(row=1,column=1,columnspan=4)

l2=Label(roo,text="0",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
l2.grid(row=0,column=1,columnspan=4)

def bclick(num):
    cur = e.get()
    e.delete(0,END)
    e.insert(0,str(cur) + str(num))

def bequal():
    try:
        ans = str(eval(str(e.get())))
        ans = ans[:14]
        l2=Label(roo,text=ans,font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
        l2.grid(row=0,column=1,columnspan=4)
    except:
        l2=Label(roo,text="Error",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
        l2.grid(row=0,column=1,columnspan=4)
        e.delete(0,END)
    print(str(ans))

def bc():
    e.delete(0,END)
    l2=Label(roo,text="0",font="Times 20",bd=1,relief="solid",anchor=SE,width=13,height=2)
    l2.grid(row=0,column=1,columnspan=4)

b1=Button(roo,text="1",bg="light gray",fg="black",bd=1,relief="solid",padx=19,pady=8,command=lambda:bclick(1))
b2=Button(roo,text="2",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=8,command=lambda:bclick(2))
b3=Button(roo,text="3",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=8,command=lambda:bclick(3))
b4=Button(roo,text="4",bg="light gray",fg="black",bd=1,relief="solid",padx=19,pady=6,command=lambda:bclick(4))
b5=Button(roo,text="5",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=6,command=lambda:bclick(5))
b6=Button(roo,text="6",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=6,command=lambda:bclick(6))
b7=Button(roo,text="7",bg="light gray",fg="black",bd=1,relief="solid",padx=19,pady=8,command=lambda:bclick(7))
b8=Button(roo,text="8",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=8,command=lambda:bclick(8))
b9=Button(roo,text="9",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=8,command=lambda:bclick(9))
b0=Button(roo,text="0",bg="light gray",fg="black",bd=1,relief="solid",padx=18,pady=7,command=lambda:bclick(0))
b=Button(roo,text=".",bg="light gray",fg="black",bd=1,relief="solid",padx=21,pady=7,command=lambda:bclick("."))
bf=Button(roo,text="C",bg="light gray",fg="black",bd=1,relief="solid",padx=17,pady=7,command=bc)
bd=Button(roo,text="/",bg="mint cream",fg="black",bd=1,relief="solid",padx=16,pady=7,command=lambda:bclick("/"))
bm=Button(roo,text="x",bg="mint cream",fg="black",bd=1,relief="solid",padx=15,pady=7,command=lambda:bclick("*"))
bs=Button(roo,text="-",bg="mint cream",fg="black",bd=1,relief="solid",padx=16,pady=6,command=lambda:bclick("-"))
ba=Button(roo,text="+",bg="mint cream",fg="black",padx=14,pady=6,command=lambda:bclick("+"))
be=Button(roo,text="=",bg="old lace",fg="black",bd=1,relief="solid",width=27,height=2,command=bequal)

b1.grid(row=3,column=1)
b2.grid(row=3,column=2)
b3.grid(row=3,column=3)
b4.grid(row=4,column=1)
b5.grid(row=4,column=2)
b6.grid(row=4,column=3)
b7.grid(row=5,column=1)
b8.grid(row=5,column=2)
b9.grid(row=5,column=3)
b.grid(row=6,column=1)
b0.grid(row=6,column=2)
bf.grid(row=6,column=3)
bd.grid(row=3,column=4)
bm.grid(row=4,column=4)
bs.grid(row=5,column=4)
ba.grid(row=6,column=4)
be.grid(row=7,column=0,columnspan=5)

roo.mainloop()

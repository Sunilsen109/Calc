from tkinter import *


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def click(event):
    global scvalue
    text = event.widget.cget("text")
    #print(text)
    if text == "C":
        scvalue.set("")
        screen.update()
    elif text == "<-x":
        if scvalue.get().isdigit():
            l = list(scvalue.get())
            l = l[:-1]
            t = listToString(l)

        # else:
        #     value = eval(screen.get())
        scvalue.set(t)
        screen.update()


    elif text == "=":
        if scvalue.get().isdigit():
            value =int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()


    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root=Tk()
root.title("Calc GUI")
root.geometry("350x500")
scvalue=StringVar()
scvalue.set("")
screen= Entry( font="lucida 35 bold",bg="yellow",fg="black" ,textvariable=scvalue)
screen.pack(padx=5,pady=5)
f1 = Frame(root)
b=Button(f1,text="7",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="8",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="9",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="*",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")

f1.pack()


f1 = Frame(root)
b=Button(f1,text="4",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="5",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="6",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="-",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")

f1.pack()


f1 = Frame(root)
b=Button(f1,text="1",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="2",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="3",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="+",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")

f1.pack()

f1 = Frame(root)
b=Button(f1,text="00",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="0",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text=".",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="=",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")

f1.pack()


f1 = Frame(root)
b=Button(f1,text="C",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="%",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="<-x",relief="groove",padx=12,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")
b=Button(f1,text="/",relief="groove",padx=16,pady=16)
b.bind("<Button-1>",click)
b.pack(side= "right",padx=16,pady=16,anchor="w")

f1.pack()

root.mainloop()
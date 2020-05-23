from tkinter import *
from tkinter.messagebox import *
#some usefull variable
font=('verdana',22,'bold')

#important function
def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)

def all_clear():
    textField.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='X':
        textField.insert(END,"*")
        return

    if text=='=':
        try:
            ex=textField.get()
            answer=eval(ex)
            textField.delete(0, END)
            textField.insert(0,answer)
        except Exception as e:
            print("Error..",e)
            showerror("Error",e)
        return
    textField.insert(END,text)
#creating a window
window=Tk()
window.title('my calculater')
window.geometry('510x550')
# picture label
pic = PhotoImage(file='img/cal1.png')
headingLable=Label(window,image=pic)
headingLable.pack(side=TOP,pady=15)

#heading label
heading= Label(window,text='my calculator',font=font)
heading.pack(side=TOP)

#textfield
textField = Entry(window, font=font,justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)
#button
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP,padx=10)
#adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
        btn.grid(row=i,column=j)
        temp= temp +1
        btn.bind('<Button-1>',click_btn_function)
ZeroBtn=Button(buttonFrame,text=0,font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
ZeroBtn.grid(row=3,column=1)

dotBtn=Button(buttonFrame,text='.',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
dotBtn.grid(row=3,column=0)

equalBtn=Button(buttonFrame,text='=',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
equalBtn.grid(row=3,column=2)

plusBtn=Button(buttonFrame,text='+',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
plusBtn.grid(row=0,column=3)

minsBtn=Button(buttonFrame,text='-',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
minsBtn.grid(row=1,column=3)

multBtn=Button(buttonFrame,text='X',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
multBtn.grid(row=2,column=3)

divBtn=Button(buttonFrame,text='/',font=font,width=5,relief='ridge',activebackground='skyblue',activeforeground='orange')
divBtn.grid(row=3,column=3)

clearBtn=Button(buttonFrame,text='<--',font=font,width=11,relief='ridge',activebackground='skyblue',activeforeground='orange',command=clear)
clearBtn.grid(row=4,column=0,columnspan=2)

allclearBtn=Button(buttonFrame,text='AC',font=font,width=11,relief='ridge',activebackground='skyblue',activeforeground='orange',command=all_clear)
allclearBtn.grid(row=4,column=2,columnspan=2,)

#binding all button
plusBtn.bind('<Button-1>',click_btn_function)
minsBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divBtn.bind('<Button-1>',click_btn_function)
ZeroBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)




window.mainloop()

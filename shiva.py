import tkinter as tk

def addition():
    global a
    global op
    a=entry2.get()
    entry2.delete(0,tk.END)
    entry1.insert(0,a)
    op='+'
     
def subtraction():
    global a
    global op
    a=entry2.get()
    entry2.delete(0,tk.END)
    entry1.insert(0,a)
    op='-'
def multiplication():
    global a
    global op
    a=entry2.get()
    entry2.delete(0,tk.END)
    entry1.insert(0,a)
    op='*'
def division():
    global a
    global op
    a=entry2.get()
    entry2.delete(0,tk.END)
    entry1.insert(0,a)
    op='/'

def num_entering(num):
    p=entry2.get()
    entry2.delete(0,tk.END)
    entry2.insert(0,p+num)
def math():
    b=entry2.get()
    entry1.delete(0,tk.END)
    entry1.insert(0,a+op+b)
    entry2.delete(0,tk.END)
    if op=='+':
        entry2.insert(0,int(a)+int(b))
    elif op=='-' :
        entry2.insert(0,int(a)-int(b))
    elif op=='*':
        entry2.insert(0,int(a)*int(b)) 
    elif op=='/':
        entry2.insert(0,int(a)/int(b))         
def clc():
    entry2.delete(0,tk.END)
    entry1.delete(0,tk.END)


calculator=tk.Tk()
entry1=tk.Entry(selectborderwidth=0,width=32)
entry2=tk.Entry(selectborderwidth=0,width=32)
entry2.insert(0,'Enter here')
add=tk.Button(calculator,text='+',command=addition,fg='black',bg='light cyan')
sub=tk.Button(calculator,text='-',command=subtraction,fg='black',bg='light cyan')
mul=tk.Button(calculator,text='*',command=multiplication,fg='black',bg='light cyan')
div=tk.Button(calculator,text='/',command=division,fg='black',bg='light cyan')
one=tk.Button(calculator,text='1',command=lambda:num_entering('1'),fg='black',bg='white')
two=tk.Button(calculator,text='2',command=lambda:num_entering('2'),fg='black',bg='white')
three=tk.Button(calculator,text='3',command=lambda:num_entering('3'),fg='black',bg='white')
four=tk.Button(calculator,text='4',command=lambda:num_entering('4'),fg='black',bg='white')
five=tk.Button(calculator,text='5',command=lambda:num_entering('5'),fg='black',bg='white')
six=tk.Button(calculator,text='6',command=lambda:num_entering('6'),fg='black',bg='white')
seven=tk.Button(calculator,text='7',command=lambda:num_entering('7'),fg='black',bg='white')
eight=tk.Button(calculator,text='8',command=lambda:num_entering('8'),fg='black',bg='white')
nine=tk.Button(calculator,text='9',command=lambda:num_entering('9'),fg='black',bg='white')
zero=tk.Button(calculator,text='0',command=lambda:num_entering('0'),fg='black',bg='white')
equal=tk.Button(calculator,text='=',command=math,fg='black',bg='light cyan')
clear=tk.Button(calculator,text='clear',command=clc,fg='black',bg='light cyan')



#packing
entry1.grid(ipady=10,row=0,column=0,columnspan=20)
entry2.grid(ipady=10,row=1,column=0,columnspan=20)
add.grid(row=2,column=0,ipadx=15,ipady=10)
sub.grid(row=2,column=1,ipadx=15,ipady=10)
mul.grid(row=2,column=2,ipadx=15,ipady=10)
div.grid(row=2,column=3,ipadx=15,ipady=10)
one.grid(row=3,column=0,ipadx=15,ipady=10)
two.grid(row=3,column=1,ipadx=15,ipady=10)
three.grid(row=3,column=2,ipadx=15,ipady=10)
four.grid(row=4,column=0,ipadx=15,ipady=10)
five.grid(row=4,column=1,ipadx=15,ipady=10)
six.grid(row=4,column=2,ipadx=15,ipady=10)
seven.grid(row=5,column=0,ipadx=15,ipady=10)
eight.grid(row=5,column=1,ipadx=15,ipady=10)
nine.grid(row=5,column=2,ipadx=15,ipady=10)
zero.grid(row=6,column=0,ipadx=65,ipady=10,columnspan=3)
equal.grid(row=4,column=3,ipadx=15,ipady=57,rowspan=3)
clear.grid(row=3,column=3,ipadx=7,ipady=10)

calculator.mainloop()





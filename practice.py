from tkinter import *
from tkinter import messagebox

player_turn=0
count=0
def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
def reset_button():
    b1.config(text='',state=NORMAL,fg='white',bg='black')
    b2.config(text='',state=NORMAL,fg='white',bg='black')
    b3.config(text='',state=NORMAL,fg='white',bg='black')
    b4.config(text='',state=NORMAL,fg='white',bg='black')
    b5.config(text='',state=NORMAL,fg='white',bg='black')
    b6.config(text='',state=NORMAL,fg='white',bg='black')
    b7.config(text='',state=NORMAL,fg='white',bg='black')
    b8.config(text='',state=NORMAL,fg='white',bg='black')
    b9.config(text='',state=NORMAL,fg='white',bg='black')
        
    


def entering(b):
    global player_turn,b1,b2,b3,b4,b5,b6,b7,b8,b9,count
    if b['text']=='':
        if player_turn==0:
            b['text']='X'
            player_turn+=1
            count+=1
        elif player_turn==1 :
            b['text']='O'
            player_turn-=1  
            count+=1 
    else:
        messagebox.showerror('error','There already exists a value')  
    if b1['text']==b2['text'] and b2['text']==b3['text'] and b1['text']!='' and b2['text']!='' and b3['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b1['text'])) 
        disable()
    elif b1['text']==b4['text'] and b4['text']==b7['text'] and b1['text']!='' and b4['text']!='' and b7['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b1['text'])) 
        disable()
    elif b2['text']==b5['text'] and b5['text']==b8['text'] and b2['text']!='' and b5['text']!='' and b8['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b2['text'])) 
        disable()
    elif b3['text']==b6['text'] and b6['text']==b9['text'] and b3['text']!='' and b6['text']!='' and b9['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b3['text'])) 
        disable()
    elif b4['text']==b5['text'] and b5['text']==b6['text'] and b4['text']!='' and b5['text']!='' and b6['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b4['text'])) 
        disable()
    elif b7['text']==b8['text'] and b8['text']==b9['text'] and b7['text']!='' and b7['text']!='' and b9['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b7['text']))  
        disable()
    elif b1['text']==b5['text'] and b5['text']==b9['text'] and b1['text']!='' and b5['text']!='' and b9['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b1['text'])) 
        disable()
    elif b7['text']==b5['text'] and b5['text']==b3['text'] and b7['text']!='' and b5['text']!='' and b3['text']!='':
        messagebox.showinfo('winner','{} is the winner'.format(b7['text']))   
        disable() 
    elif count==9:
        messagebox.showinfo('winner','Its a Tie! ')
        disable()

           


        


    

window=Tk()
b1=Button(window,text='',command=lambda: entering(b1),fg='white',bg='black',height=6,width=12)
b2=Button(window,text='',command=lambda: entering(b2),fg='white',bg='black',height=6,width=12)
b3=Button(window,text='',command=lambda: entering(b3),fg='white',bg='black',height=6,width=12)
b4=Button(window,text='',command=lambda: entering(b4),fg='white',bg='black',height=6,width=12)
b5=Button(window,text='',command=lambda: entering(b5),fg='white',bg='black',height=6,width=12)
b6=Button(window,text='',command=lambda: entering(b6),fg='white',bg='black',height=6,width=12)
b7=Button(window,text='',command=lambda: entering(b7),fg='white',bg='black',height=6,width=12)
b8=Button(window,text='',command=lambda: entering(b8),fg='white',bg='black',height=6,width=12)
b9=Button(window,text='',command=lambda: entering(b9),fg='white',bg='black',height=6,width=12)
reset=Button(window,text='Play Again',fg='white',bg='green',command=reset_button)
reset.grid(row=3,column=0,columnspan=3)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)



window.mainloop()

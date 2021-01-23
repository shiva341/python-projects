import tkinter as tk
def converter():
    i=var1.get()
    o=var2.get()
    val=int(entry_input.get())
    op_value=0
    entry_output.delete(0,tk.END)
    if i=='c':
        if o=='f':
            op_value=(val*(9/5))+32
        elif o=='k':
            op_value=val+273.15  
        else:
            op_value=val  
    elif i=='f':
        if o=='c':
            op_value=(val-32)*5/9  
        elif o=='k':   
            op_value= (val-32)*(5/9 ) + 273.15     
        else:
            op_value=val
    elif i=='k':
        if o=='c':
            op_value=val-273.15
        elif o=='f':
            op_value=(val-273.15)*9/5+32
        else:
            op_value=val
    entry_output.insert(0,op_value)                                 


window= tk.Tk()
window.geometry('600x300')
label1=tk.Label(text="Enter the Input and choose the input scale :")
entry_input= tk.Entry()
var1=tk.StringVar(value='c')
ip_c=tk.Radiobutton(text="centigrade",variable=var1,value='c')
ip_f=tk.Radiobutton(text="fahreheit",variable=var1,value='f')
ip_k=tk.Radiobutton(text="kelvin",variable=var1,value='k')

label1.grid(row=0,column=0,columnspan=2)
entry_input.grid(row=1,column=2)
ip_c.grid(row=1,column=4)
ip_f.grid(row=1,column=5)
ip_k.grid(row=1,column=6)



#output
label2=tk.Label(text="Choose the output format :")
entry_output=tk.Entry()
var2=tk.StringVar(value='x')
op_c=tk.Radiobutton(text="centigrade",variable=var2,value='c')
op_f=tk.Radiobutton(text="fahreheit",variable=var2,value='f')
op_k=tk.Radiobutton(text="kelvin",variable=var2,value='k')
submit=tk.Button(text='ENTER',command=converter)
op_label=tk.Label(text="Output :")
brk=tk.Label(text='')
brk2=tk.Label(text='')
brk3=tk.Label(text='')

label2.grid(row=2,column=0,columnspan=1)
entry_output.grid(row=8,column=2)
brk2.grid(row=3)
op_c.grid(row=4,column=1)
op_f.grid(row=4,column=2)
op_k.grid(row=4,column=3)
brk3.grid(row=5)
brk.grid(row=7)
submit.grid(row=6,column=2)
op_label.grid(row=8,column=1)

window.mainloop()



import customtkinter as ctk



Zeich='None'
def Zeichen(ZeichenInsert):
    He=En.get()
    if He[-1]=='+' or He[-1]=='-' or He[-1]=='/' or He[-1]=='*' :
        He=He[:-1]

    elif '+' in He or '-' in He or '/' in He or '*' in He:
        Rechner()
        He=En.get()

    En.delete(0, 'end')
    En.insert('end',He+ZeichenInsert)


def numbers(numbInsert):
    EE=En.get()

    if EE=='0':
        En.delete(0,'end')
        En.insert('end',numbInsert)
    if EE!='0':
        En.insert('end',numbInsert)


def X2():
    Mal=En.get()
    j=float(Mal)
    Answer=j*j
    En.delete(0,'end')
    En.insert('end',str(Answer))
def Rechner():
    Mal=En.get()
    Ergebnis=eval(Mal)
    En.delete(0, 'end')
    En.insert('end', Ergebnis)


def deleteAll():
    En.delete(0,'end')
    En.insert('end','0')
def delete():
    Anz=En.get()
    Df=Anz[:-1]
    if Df=='':
        Df='0'
    En.delete(0,'end')
    En.insert('end',Df)


Calculator=ctk.CTk()
Calculator.geometry('600x1000+2500+100')
Calculator._set_appearance_mode('dark')



En=ctk.CTkEntry(Calculator,width=500,height=70,text_color='#41640D',fg_color='#5CFC18',bg_color='#202020',font=('Terminal',50,'bold'),justify='right')
En.grid(row=0,column=0,sticky='snwe',columnspan=4)
En.insert('end','0')

for Wiederholung in range(1,10):

    ctk.CTkButton(Calculator,text= (str(Wiederholung)),font=('Courier',80,'bold'),fg_color='#5D891C',bg_color='#202020',
                  hover_color='#768B55',command=lambda Numb=Wiederholung:numbers(Numb)).grid(row=(Wiederholung-1)//3+1,column=(Wiederholung-1)%3,sticky='snwe',padx=5,pady=5)

A=ctk.CTkButton(Calculator,text='0',font=('Courier',80,'bold'),fg_color='#5D891C',bg_color='#202020',hover_color='#768B55',command=lambda:(numbers('0')))
A.grid(row=4,column=0,sticky='snwe',padx=5,pady=5)

K=ctk.CTkButton(Calculator,text='+',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=lambda:Zeichen('+'))
K.grid(row=1,column=3,sticky='snwe',padx=5,pady=5)

L=ctk.CTkButton(Calculator,text='-',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=lambda:Zeichen('-'))
L.grid(row=2,column=3,sticky='snwe',padx=5,pady=5)

M=ctk.CTkButton(Calculator,text='x',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=lambda:Zeichen('*'))
M.grid(row=3,column=3,sticky='snwe',padx=5,pady=5)

N=ctk.CTkButton(Calculator,text=':',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=lambda:Zeichen('/'))
N.grid(row=4,column=3,sticky='snwe',padx=5,pady=5)

O=ctk.CTkButton(Calculator,text='.',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=lambda:Zeichen('.'))
O.grid(row=4,column=1,sticky='snwe',padx=5,pady=5)

P=ctk.CTkButton(Calculator,text='=',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=Rechner)
P.grid(row=5,column=3,sticky='snwe',padx=5,pady=5)

Q=ctk.CTkButton(Calculator,text='x²',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=X2)
Q.grid(row=4,column=2,sticky='snwe',padx=5,pady=5)

R=ctk.CTkButton(Calculator,text='⌫',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=delete)
R.grid(row=5,column=2,sticky='snwe',padx=5,pady=5)

S=ctk.CTkButton(Calculator,text='AC',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=deleteAll)
S.grid(row=5,column=1,sticky='snwe',padx=5,pady=5)

T=ctk.CTkButton(Calculator,text='()',font=('Courier',80,'bold'),fg_color='#35C657',bg_color='#202020',hover_color='#768B55',command=Rechner)
T.grid(row=5,column=0,sticky='snwe',padx=5,pady=5)

for f in range(0,6):
    Calculator.grid_columnconfigure(f,minsize=150)
    Calculator.grid_rowconfigure(f,minsize=150)
Calculator.mainloop()
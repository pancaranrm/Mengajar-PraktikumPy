'''
    Buatlah kolom login ada nama,pw 
    check box pria/wanita
'''

from cgitb import text
import tkinter as tk
from tkinter import Entry,Text,ttk
from tkinter.messagebox import showinfo
from turtle import title

jendela = tk.Tk()
jendela.configure(bg="Pink")
jendela.geometry("700x500")
jendela.title("SignIn")

# Variablenya
NAMA = tk.StringVar()
PW = tk.StringVar()
AGREEMENT = tk.StringVar()


# fungsi agreement
def agreement_changed():
    tk.messagebox.showinfo(title='Result',
    message= AGREEMENT.get())

# fungsi tombol
def tombol_click():
    pesan = f"Halo {NAMA.get()} {PW.get()}, {AGREEMENT.get()},Verified!"
    showinfo(title="HASIL",message=pesan)

inputFrame = ttk.Frame(jendela)
inputFrame.pack(padx=8,pady=8,fill="x",expand=True)

# label nama
lnama = ttk.Label(inputFrame,text="Nama Depan")
lnama.pack(padx=10,fill="x",expand=True)

# entry nama
enama = ttk.Entry(inputFrame,textvariable=NAMA)
enama.pack(padx=10,fill="x",expand=True)

# label pw
lpw = ttk.Label(inputFrame,text="Password")
lpw.pack(padx=8,pady=8,fill="x",expand=True)

# entry pw
epw = ttk.Entry(inputFrame,textvariable=PW)
epw.pack(padx=8,pady=8,fill="x",expand=True)

ttk.Checkbutton(jendela,
                text='I agree',
                command=agreement_changed,
                variable=AGREEMENT,
                onvalue='agree',
                offvalue='disagree').pack()

# 3. Tombol
tombol_sapa = ttk.Button(inputFrame,text="Sapa saya",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# text = Text(jendela, height=4)
# text.pack()

jendela.mainloop()
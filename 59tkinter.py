# tkinter is a GUI in python
import tkinter as tk
from tkinter import Entry, ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white") 
window.geometry("700x300") 
window.resizable(False,False) 
window.title("Judulnya")

#  variable yang dibutuhkan
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''akan dipanggil tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},Cakepp!"
    showinfo(title= "What'sUp",message=pesan)


# frame input
input_frame  = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)


# komponen-komponen
# 1. Lebel nama depan
label_nama_depan = ttk.Label(input_frame,text="Nama depan:")
label_nama_depan.pack(padx=10,fill="x",expand=True)

# entry nama depan
entryDepan = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
entryDepan.pack(padx=10,fill="x",expand=True)

# 2. Lebel nama belakang
label_nama_belakang = ttk.Label(input_frame,text="Nama belakang:")
label_nama_belakang.pack(padx=10,fill="x",expand=True)

# entry nama belakang
entryBelakang = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
entryBelakang.pack(padx=10,fill="x",expand=True)

# 3. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa saya",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# main loop agar keluar 
window.mainloop()
from unittest import result
import os

def head():
    os.system("cls")
    print("===== PROGRAM RESTORAN =====")
    result = 0
    
    
def inputan():
    menu = int(input("Masukkan Nomor Menu"))
    nama_menu = int(input("Masukkan Nama Menu"))
    return menu, nama_menu

def message(massage,value):
    print(f"Hasilnya adalah {massage} = {value}")


    

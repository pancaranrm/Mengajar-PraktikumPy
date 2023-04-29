import os # build in
from signal import valid_signals

# program menghitung luas dan keliling persegi panjang
# buat headernya dulu

def header():
    os.system("cls")
    print(f"{'PROGRAM UNTUK MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def inputUser():
    a = int(input("Masukkan Input pertama"))
    b = int(input("Masukkan Input kedua"))
    return a,b

def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def bagi(a,b):
    return a/b

def kali(a,b):
    return a*b

def message(massage,value):
    print(f"Hasil perhitungan {massage} = {value}")


while True:
    header()
    A,B = inputUser()
    HITUNG = hitungLuas(LEBAR,PANJANG)
    KELILING = hitungKeliling(LEBAR,PANJANG)

    message("Luas",LUAS)
    message("Keliling",KELILING)

    isContinue = input("y/n")
    if isContinue == " n": 
        break

print("Program Selesai thnk u 3>")
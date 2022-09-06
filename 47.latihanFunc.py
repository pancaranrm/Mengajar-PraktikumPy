import os
from signal import valid_signals

# program menghitung luas dan keliling persegi panjang
# buat headernya dulu

def header():
    os.system("Clear")
    print(f"{'PROGRAM UNTUK MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def inputUser():
    lebar = int(input("Masukkan Lebar"))
    panjang = int(input("Masukkan Panjang"))
    return lebar,panjang

def hitungLuas(lebar,panjang):
    return lebar*panjang

def hitungKeliling(lebar,panjang):
    return 2*(lebar+panjang)

def message(massage,value):
    print(f"Hasil perhitungan {massage} + {value}")


while True:
    header()
    LEBAR,PANJANG = inputUser()
    LUAS = hitungLuas(LEBAR,PANJANG)
    KELILING = hitungKeliling(LEBAR,PANJANG)

    message("Luas",LUAS)
    message("Keliling",KELILING)

    isContinue = input("y/n")
    if isContinue == " n": 
        break

print("Program Selesai thnk u 3>")
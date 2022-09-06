# buat fungsi program menghitung luas lingkaran

import os

def head():
    os.system("cls")
    print("PROGRAM MENCARI LUAS")

result = 0

def phi():
    phi1 = 3.14
    phi2 = 22/7
    return phi1,phi2

def inputan():
    jari = int(input("Masukkan Jarijari"))
    return jari

def hitungan(jari,phi):

    if (jari % 7 == 0):
        hitung = jari * phi[1]
    else:
        hitung = jari * phi[0]
    return hitung

def message(massage,value):
    print(f"Hasil perhitungan {massage} = {value}")


while True:
    head()
    JARI = inputan()
    PHI = phi()
    LUAS = hitungan(JARI,PHI)

    message("Luas : ",LUAS)

    isContinue = input("y/n")
    if isContinue == " n": 
        break




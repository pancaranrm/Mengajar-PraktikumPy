"""
    Program menerima minimal 2 harga barang, menghitung nilai total yang harus dibayar, 
    dan menghitung nilai total pajak sebesar 11% dari nilai total yang harus dibayar,
    serta Total Pembayaran setelah ditambah pajak.
"""

import os

def head():
    os.system("cls")
    print("PROGRAM KALKULATOR KASIR")

result = 0

def diskon():
    diskon = 11/100
    return diskon
    
def inputan():
    baranga = int(input("Masukkan harga barang pertama"))
    barangb = int(input("Masukkan harga barang kedua"))
    return baranga, barangb

def hitung(baranga,barangb):
    hitung = baranga + barangb  * diskon
    return hitung
    
def pesan(pesan,hasil):
    print(f"Hasil perhitungan {pesan} = {hasil}")
    
while True:
    head()
    BARANG = inputan()
    DISKON = diskon()
    HITUNG = hitung(BARANG,DISKON)

    pesan("Hitung : ", HITUNG)

    isContinue = input("y/n")
    if isContinue == " n": 
        break
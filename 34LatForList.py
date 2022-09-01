# buatlah program untuk mendata buku tulis fan tampilkan datanya menggunakan list 

from ast import Break
from tkinter import END

list_buku = []
while True:
    print("Masukkan detail buku")
    nama = input("Masukkan nama buku :")
    pengarang = input("Masukkan pengarang buku :")
    kode = input("Masukkan kode buku :")

    bukunya = [nama,pengarang,kode]
    list_buku.append(bukunya)

    print(5*"#"*5)
    # menampilkan data buku
    for index,b in enumerate(list_buku):
        print(f"{index+1} | {b[0]} | {b[1]} | {b[2]}")
    
    print(5*"#"*5)
    # apakah sudah selesai
    isLanjut = input("Apkakah lanjut? y/n")

    if isLanjut == " `n":
        break
        

    print("PROGRAM SELESAI")

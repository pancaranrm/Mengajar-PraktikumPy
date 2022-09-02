# buat program untuk menginput dan menapilkan data mahasiswa 

import datetime
import os
# import random
# import string

datam = {
	'nama':'nama',
	'nim':'000000',
	'sks_lulus':0,
	'lahir':datetime.datetime(1111,1,11)
}

mhs = {}

while True:
    os.system("cls")
    print("SELAMAT DATANG MAHASISWA")
    print("Harap Isi Form Dibawah")
    print("-"*50)

    mahasiswa = dict.fromkeys(datam.keys())

    mahasiswa['nama'] = str(input("Masukkan nama anda"))
    mahasiswa['nim'] = int(input("Masukkan NIM anda"))
    mahasiswa['sks_lulus'] = int(input("Masukkan SKS anda"))
    TAHUN = int(input("Tahun lahir kamu"))
    BULAN = int(input("Bulan lahir kamu"))
    TANGGAL = int(input("Tanggal lahir kamu"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    print(mahasiswa)


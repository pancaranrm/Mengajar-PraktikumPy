import datetime
import os
import random
import string
# import pandas as pd

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
    print("-", 50)

    mahasiswa = dict.fromkeys(datam.keys())

    mahasiswa['nama'] = input("Masukkan nama anda")
    mahasiswa['nim'] = int(input("Masukkan NIM anda"))
    mahasiswa['sks_lulus'] = int(input("Masukkan SKS anda"))
    TAHUN = int(input("Tahun lahir kamu"))
    BULAN = int(input("Bulan lahir kamu"))
    TANGGAL = int(input("Tanggal lahir kamu"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)


    # mengenerate key yg random sebanyak 6kali
    # KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    KEY = ''

    for i in range(6):
        KEY = KEY + random.choice(string.ascii_uppercase)

    # KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    mhs.update({KEY: mahasiswa})
    print(mhs)

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print('-' * 60)

    for h in mhs:
        KEY = h
        NAMA = mhs[KEY]['nama']
        NIM = mhs[KEY]['nim']
        SKS = mhs[KEY]['sks_lulus']
        LAHIR = mhs[KEY]['lahir'].strftime("%x")
        print(f"\n{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:<10} {LAHIR:<10}")

    print('-' * 60)

    isDone = input("Sudah selesai y/n?")
    if isDone == "y":
        break
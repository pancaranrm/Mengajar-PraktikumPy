# Write a program to check whether a person is eligible for voting or not. (accept age from user)


import datetime as dt


tanggalan = int(input("Date : \t"))
bulan = int(input("Month : \t\t"))
tahun = int(input("Years : \t\t"))
tanggal_lahir = dt.date(tahun,bulan,tanggalan)

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print(f"Umur anda adalah : {umur_tahun}")

if umur_tahun > 17:
    print("You are eligible to vote new president")
elif umur_tahun < 17:
    print("You're not allowed to join")
else:
    print("none")


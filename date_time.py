
import datetime as dt

today = dt.date.today()
print(today)

print("Hi! Welcome to Computer")
print("Please input the data")

nama = str(input("Name : \t"))
tanggalan = int(input("Date : \t"))
bulan = int(input("Month : \t\t"))
tahun = int(input("Years : \t\t"))

print(f"HAI {nama}")

tanggal_lahir = dt.date(tahun,bulan,tanggalan)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari Ultah adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
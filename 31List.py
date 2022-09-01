# cara menghitung data pada list yang panjang
from tkinter import PIESLICE


data = [1,2,1,2,1,3,2,1,3,4,5,1,0]
# hitung angka 1 ada berapa
jumlahData1 = data.count(4)
print(f"Jumlah data angka 1 adalah... {jumlahData1} ")


data = ["anca","oke","siap","kaya"]
# cara ambil data pada list
# INDEXING

ambil = data.index("kaya")
print(f"Kita mengambil data {ambil}")

# cara mengurutkan data 
print(f"Sebelum diurutkan = \n {data}")
# setelah diurutkan
data.sort()
print(f"data sudah disort= \n {data}")

# mereverse data 
data.reverse()
print(f"data sudah direverse= \n {data}")


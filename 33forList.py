# RECAP LOOPING DENGAN BERBAGAI CARA

list_angka = [1,2,4,5,6,7]
for angka in list_angka:
    print(f"List angka = {angka}")

list_nama = ["Pancaran","Ratna","Mustika"]
print(5*"====")

for nama in list_nama:
    print(f"Nama = {nama}")

# ribet
print(5*"====")
kumpulan = 1,2,3,4
panjang = len(kumpulan)

for i in range(panjang):
    print(f"Pokoknya {kumpulan [i]}")

# while loop
print(5*"====")
print("WHILE LOOP")
panjang = len(kumpulan)
i = 0 
 
while i < panjang:
    print(f"Angka = {kumpulan[i]}")
    i+= 1

# list comperhension
# biar singkat
print(5*"====")
data = ["Pancaran",13,"September"]
[print(f"data = [i]") for i in data]

print(5*"====")
angka = [1,2,3,4,5,6]
akuadrat = [i**2 for i in angka]
print(akuadrat)

print(5*"====")

# enumarate
listan = ["Pancaran",13,"Desember"]
for index,data in enumerate(listan):
    print(f"Index = {index},data = {data}")
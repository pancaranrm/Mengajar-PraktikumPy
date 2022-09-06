# digunakan untuk membuat default var

def fDefault(angka = 1,angkab = 3):
    tambah = angka + angkab
    return tambah

print(fDefault(1,5))
print(fDefault())
print(fDefault(10)) # ini akan menambah 10 + 3 = 13


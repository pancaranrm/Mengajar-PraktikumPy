# digunakan untuk membuat default var

def fDefault(angka = 1,angkab = 3):
    tambah = angka + angkab
    return tambah

print(fDefault(1,5))
print(fDefault())
print(fDefault(10)) # ini akan menambah 10 + 3 = 13


def fungsi(a=4,b=5,c=6,d=7):
    hasil = a + b + c + d
    return hasil

print(5*"#")
print(fungsi()) # 4+5+6+7 =22 
print(fungsi(c = 2)) # 4+5+6+2+7 = 11
print(fungsi(1,1)) #1+1+6+7 = 15
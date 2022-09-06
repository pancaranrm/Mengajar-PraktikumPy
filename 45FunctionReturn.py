def fTambah(a,b):
    tambah = a + b
    return tambah

masukkan = fTambah(1,2)
print(masukkan)
print(fTambah(1,3)) #bisa kek gini

def fKuadrat(angkaI):
    outputKuadrat = angkaI**2
    return outputKuadrat

y = fKuadrat(5)
print(y)


def frumah(benda):
    barangYgada = benda
    return barangYgada

b = frumah("kursi")
print(f"Barang yang ada : {b}")

# yang banyak returnnya

def opMtk(angkaa,angkab):
    tambah = angkaa + angkab
    kurang = angkaa - angkab
    bagi = angkaa / angkab
    kali = angkaa * angkab
    return tambah,kurang,bagi,kali

# k,l,m,n = opMtk(10,5)


k,l,m,n = opMtk(10,5)

print(f"Hasil tambah {k}")
print(f"Hasil kurang {l}")
print(f"Hasil bagi {m}")
print(f"Hasil kali {n}")







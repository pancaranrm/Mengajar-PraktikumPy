'''
    yang dipelajari : 
    1. sort
    2. list
    3. lambda
    4. filter
    5. Anonymous Function = function without name
'''

# lambda py digunakan untuk menyingka penulisan kuadrat
# output = lambda argumen:expression

# kuadarat biasa
def kuadrat(angka):
    return angka**2

print(f"hasil kuadrat {kuadrat(3)}")

kuadrat = lambda angka : angka **2
print(f" hasil kuadrat = {kuadrat(5)}")

kuadratb = lambda num,pow : num**pow
print(f"hasiil kuadra num pow = {kuadratb(5,2)}") # 5 pangkat 2

# fungsinya buat apa sih?

# sorting datalist
data_list = ['Anca','Ngantuk','apah','iyah']
data_list.sort()
print(f"Sorted data {data_list}")

# sorting pake panjang /len()

def panjangData(nama):
    return len(nama)

data_list.sort(key = panjangData)
print(f"panjang nama {data_list}")

# sort pake list
# data_list = ['Anca','Ngantuk',1,3,4,4,5] no int in len!
data_list = ['Anca','Ngantuk','apah','iyah']
data_list.sort(key = lambda nama: len(nama))
print(f"panjang nama {data_list}")

# mengolah data/short data
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurangdari5(angka):
    return angka < 5

data_angkaa = list(filter(kurangdari5,data_angka))
data_angkab = list(filter(lambda x : x < 7,data_angka))

print(data_angkaa)
print(data_angkab)

# sorting data genap
data_genap = list(filter(lambda x: (x%2== 0), data_angka))
print(data_genap)

data_ganjil = list(filter(lambda b:(b%2 != 0),data_angka))
print(data_ganjil)

# sorting kelipatan 3
kelipatan3 = list(filter(lambda c: (c%3 == 0),data_angka))
print(kelipatan3)

#  map kelipatan 3
kelipatan3 = list(map(lambda c: (c%3 == 0),data_angka)) #hasilnya t/f
print(f"Shorting menggunakan map {kelipatan3}")

# ini fungsi normal yah
def pangkat(angka,n):
    hasil = angka **n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa {data_hasil}")


# menggunakan currying dapat membuat nam func sendiri
def pangkat(n):
    return lambda angka:angka**n

# buat nama func sendiri
# fungsi bisa dimasukkin argumen
pangkat2 = pangkat(2)
print(f"Pangkat 2 = {pangkat2(3)}") #3 ^ 2 

pangkat3 = pangkat(3)
print(f"Pangkat 3 = {pangkat3(2)}") # 2^3 

print(f"Pangkat bebas = {pangkat(4)(2)}") # 4 pangkat 2

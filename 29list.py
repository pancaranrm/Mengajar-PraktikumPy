# penggunaan list untuk mempersingkat 

i = [1,2,3,4]
print(1)

# bisa di mix antar tipe data = tipe data boolean,string dkk

b = ['Anca',"ok",12,True]
print(b)

# membuat list menggunakan for |  dalam range 
pake_for = [i for i in range(0,10)]
print(pake_for)

# membuat list menggunakan for | yang berpangkat
pangkat = [i**2 for i in range(1,10)]
print(pangkat)

# membuat list menggunakan for | bilangan genap
genap = [i for i in range(0,10) if i%2 == 0]
print(genap)

# membuat list menggunakan for | bilangan ganjil
ganjil = [i for i in range(0,10) if i%2 !=0]
print(ganjil)

# membuat list menggunakan for | pake if biasa
# jangan print ketika 5
p = [i for i in range(0,11)if i !=5]
print(p)
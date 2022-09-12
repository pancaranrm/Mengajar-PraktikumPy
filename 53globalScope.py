#  global scope ini universal 
'''
    cara agar dapat mengubah variable locale menjadi global = tulis global
'''

namaGlobal = "anca"
def panggil():
    print(f"Panggil saja aku {namaGlobal}")
    
panggil()

# manggil globlal di pengulangan
for i in range(2,3):
    print(f"loop in {i} - {namaGlobal} ")
    
# Percabangan
if True:
    print(namaGlobal)
    

# # VARIABLE LOCALE
# def flocal():
#     namaLocal = "Pancaran Ratna"  #local variable
# print(namaLocal) # ga bisa diakses

# Mengganti variable global
angka1 = 10
angka2 = 19

def ubah(angka_baru1,angka_baru2):
    global angka1
    global angka2
    angka1 = angka_baru1
    angka2 = angka_baru2
    
print(f"Angka sebelum didedit {angka1,angka2}")
ubah(4,5)
print(f"Angka sebelum didedit {angka1,angka2}")

# contoh ini masih bisa dibah 
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
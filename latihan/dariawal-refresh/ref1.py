"""
    buat program masukkan ipk jika ipk <= 4 maka maksimal ipk adalah 24
    jika ipk <= 3 maka minimal sks adalah 22
    <= 2,5 Maksimal 18 sks
    <= 2,00 Maksimal 15 SKS
    == dropout
"""

from ast import If


print("#"*3 ,"Selamat datang", "#"*3)
print("IPK", "\t\t\t" "SKS")
print("4.00", "\t\t\t" "24")
print("3.00", "\t\t\t" "22")
print("2.50", "\t\t\t" "18")
print("2.00", "\t\t\t" "15")


ipk = (float(input("Masukkan IPK ")))
if ipk == 4.0 :
    print("Kamu bisa ambil 24 SKS")
elif ipk < 4.0 :
    print("Kamu bisa ambil 22 SKS")
elif ipk <= 3.0 :
    print("Kamu bisa ambil 22 SKS")
elif ipk <= 2.5 :
    print("Kamu bisa ambil 18 SKS")
elif ipk <= 2.0 :
    print("Kamu bisa ambil 15 SKS")
else:
    print("Ya coba lagi tahun depan")









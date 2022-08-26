# buatlah kalkulator sederhana

from ast import operator


angkaa = float(input("Masukkan angka pertama... "))
operator = (input("+,-,*,/,% "))
angkab = float(input("Masukkan angka kedua... "))

if operator == "+" :
    hasil = angkaa + angkab
    print(f"Hasilnya adalah = ",hasil)
elif operator == "-" :
    hasil = angkaa - angkab
    print(f"Hasilnya adalah = ",hasil)
elif operator == "*" :
    hasil = angkaa * angkab
    print(f"Hasilnya adalah = ",hasil)
elif operator == "/" :
    hasil = angkaa / angkab
    print(f"Hasilnya adalah = ",hasil)
elif operator == "%" :
    hasil = angkaa % angkab
    print(f"Hasilnya adalah = ",hasil)
else:
    print("Bingung") 
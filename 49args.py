"""
Args digunakan untuk menjadikan parameter/argumen lebih dinamis
*args /nama args tuh bebas asal depannya ada *
bakal kepake buat filtering/mapping 
"""

# def fun(funa, *funb):
#     print("first argument is =",funa)
#     for nama in funb:
#         print("Next argument will = ",nama)

# fun("Hello","my","name")

# yang funa hanya akan nampilin  Hello
# yang print 2 hanya nampilin my,name 3>


from random import betavariate


def identitas(nama,tinggi,berat):
    print(f"Nama = {nama}, tinggi = {tinggi}, berat = {berat} ")
    
identitas("Anca",159,45)


def iden(datalist):
    data = datalist.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"Nama = {nama}, tinggi = {tinggi}, berat = {berat} ")

iden(["Anca",150,40])

# MENGGUNAKAN *ARGS

print(5*"#MENGGUNAKAN *ARGS")
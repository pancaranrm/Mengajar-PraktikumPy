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

print(2*"#")

def fungsi(*argum):
    # data = datalist.copy() ga usah pake ini yah
    nama = argum[0]
    tinggi = argum[1]
    berat = argum[2]
    print(f"Nama = {nama}, tinggi = {tinggi}, berat = {berat} ")
    
fungsi("Haura",160,46) #this is tauple


# Studi kasus mengenai *args
def tambah(*data):
    output = 0
    for angka in data:
        output += data
        return output
    
hasil = tambah(10,20,20)
print(f"Hasil = {hasil}")

#akan error jika
# hasil = tambah(operasi = "Hasilnya",12,2,3)
# mangkanya kita pake **args
# operasi memanipulasi string
# PENTING BGT GAN

nama_depan = "Pancaran"
nama_tengah = "Ratna"
nama_belakang = "Mustika"
nlp = nama_depan + " " + nama_tengah + " " + nama_belakang 
print(nlp)

print("=================")
# menghitung panjang string
panjangnya = len(nlp)
print("Panjang dari " + nlp ,"adalah", str(panjangnya))

print("=================")
# mengecek komponen yg ada pada suatu string
lihat = "Pancaran"
lihat2 = "Ucup"
status = lihat in nlp
print("Hasil pencarian",lihat, "di "+nlp + " = " +str(status))

status2 = lihat not in nlp
print("Hasil pencarian",lihat, "di "+nlp + " = " +str(status2))
 
# mengulang string
print(3* "How to win with yourself")

# indexing // mencari string pada angka tertentu
print("Kalimat ke 0 dari kalimat "+ nlp + "= " + nlp[0])
# mencari dari rentang ini hasilnya bakalan Panc p=0 
print("kalimat dari 0:3 "+ nlp + "= " + nlp[0:4]) 

print("index ke-[0,2,4,6,8] : " + nlp[0:10:2]) # diambil index 0,2,4,6,8

# item paling kecil
print("nilai terkecil : " + min(nlp))
# item paling besar
print("nilai terbesar : " + max(nlp))

ascii_code = ord(" ")
print("ASCII number dari spasi : " + str(ascii_code))
data = 117
print("Character dari ascii code 117 : " + chr(data))

# 4. operator dalam bentuk method

data = "ih surotong pararotong"
jumlah = data.count("o")
print("jumlah o di " + data + " : " + str(jumlah))

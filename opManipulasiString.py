# operasi memanipulasi string

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

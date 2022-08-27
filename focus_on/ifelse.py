# nama = "Pancaran"
# if nama == "Pancaran":
#     print(f"Halo {nama} 3>")
# else :
#     print(f"Kamu pasti bukan {nama}")

nama = str(input("Masukkan Nama"))
print(f"SELAMAT DATANG{nama}")

gender = input("Pilih Gender ")

if gender == "perempuan": # kondisi 1
	print("Kamu perempuan!! ") # aksi true 1
elif gender == "laki": # kondisi 2
	print("Kamu laki-laki!! ") # aksi true 2
else:
	print("au ah gak kenal!!!") # aksi false


kelas = input("IPA/IPS ")

if kelas == "IPA": 
	print("kamu cocok masuk di Informatika/dokter")
elif kelas == "IPS": 
	print("Kamu cocok masuk jurusan Hukum")
else:
	print("Anak SMK") 


# penting inputan "harus ada spasi "
makanan = input("Ayam/Ikan ") # setelah ikan 

if makanan == "Ayam":
    print("McD")
elif makanan == "Ikan":
    print("Sushi")
else: 
    print("Warteg")

transportasi = input("Mobil/Motor/AngkutanUmum ") # setelah ikan 

if transportasi == "Mobil":
    print("kamu beruntung")
elif transportasi == " Motor":
    print("kamu berada")
elif transportasi == " Angkutan Umum":
    print("kamu pejuang")
else: 
    print("melayang")



print(f"""
nama = {nama}
gender = {gender}
kelas = {kelas}
makanan = {makanan}
transportasi = {transportasi}
""")



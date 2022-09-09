# kalo menggunakan *args biasa
def funa(nama,tinggi,berat):
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")

funa("Pancaran",160,40)    


# Bisa dimix n match dgn dictionary 
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    # print(kwargs["nama"]) # seperti dictionary
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")
    
fungsi(nama = "Ucuplas",tinggi= 120, berat = 20)
    
    
def studik(*a,**b):
    if b["op"] == "tambah":
        print(f"Ini adalah operasi {a}")
    elif b["op"] == "kurang":
        print("Ini adalah operasi pengurangan")
    elif b["op"] == "bagi":
        print("Ini adalah operasi pembagian")
        return 0
    
hasil = studik(10,90,op = "tambah" )
hasil = studik(10,90,op = "kurang" )

# yey udah 
def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output
    
hasil = tambah(1,2,2,23,3)
print(f"Hasil = {hasil}")

hasil = tambah(12,3)
print(f"Hasil = {hasil}")


# INI MEMBUAT CREATE READ UPDATE DELATE
from operator import index

datalist = []

def menu():
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    
    kode = input("Masukkan kode")
    if kode == "1":
        tampil()
    elif kode == "2":
        tambah()
    
    elif kode == "3":
        edit()
    
    elif kode == "4":
        hapus()
    
    while(True):
        menu()

def tampil():
    index = 0
    if len(datalist)<=0:
        print("Data masih kosong")
    else:
        for list in datalist:
            print(str(index)+ "." +list())     
            index +=1

def tambah():
    judul = input('Masukkan Kucing')
    datalist.append((judul))
    print("Data berhasil ditambahkan")
    
def edit():
    tampil()
    index = int(input("Masukkan No data yang ingin diedit"))
    data_lama = datalist[index]
    data_baru = input("Masukkan Data baru")
    datalist[index] = data_baru
    print("Data Lama "+ data_lama +"Duganti menjadi "+ data_baru)
    

def hapus():
    tampil()
    index = int(input("Masukkan No data yang ingin dihapus"))
    judul = datalist[index]
    del datalist[index]
    print("Judul telah dihapus")
    
    
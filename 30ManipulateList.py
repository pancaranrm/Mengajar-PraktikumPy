from turtle import pen


data = ['A','B','C']

# total data list
total = len(data)
print(total)

# memanipulasi per list
list = data[2]
print("Outputnya adalah..",list)

# mengambil data terakhir
akhir = data[-1]
print("List data terakhir",akhir)

# menambah data pada list tertentu
data.insert(1,"Jajang")
print(data)

# menambah di akhir list
data.append("tambah akhir")
print("Data ditmbah lagi ",data)

# menggabungkan list
data_baru = ['Anca','okr','cape']
data.extend(data_baru)
print("Data baru",data)

# merubah data
data[1] = "Yaudah" 
print("Data diubah menjadi",data)

# menghapus data 
data.remove('cape')
print(f"data {data} terhapus")

# menghapus data paling belakang = pop
data.pop()
print(f"data terakhir dihapus jadinya tinggal.. {data}")
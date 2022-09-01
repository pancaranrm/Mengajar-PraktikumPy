# list dalam list


# data = ['will','you','study','with','me']
data1 = [1,2,3,4]
data2 = [4,5,6]
data3 = [1,2,3]

print(f"data list biasa {data1}")
# menggabungkannya
print(f"gabungannya{data1,data2,data3}")

# contoh penggunaannya
peserta0 = ['Pancaran',17,'P']
peserta1 = ['Ucup',18,'L']
peserta2 = ['Ani',20,'P']
peserta3 = ['dadang',17,'L']

total = [peserta0,peserta1,peserta2,peserta3]
print(f"List peserta sekarang {total}")

for peserta in total:
    print(f"Nama \t : {peserta[0]}")
    print(f"Umur \t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")


# tapi akan bermasalah jika mau ngecopy
list_copy = total.copy()
print(list_copy)
# ubah
list_copy[0] = "Ratna"
print(list_copy) #engga masuk ke dalam list,jadi dia keluar sendiri 
print(total)




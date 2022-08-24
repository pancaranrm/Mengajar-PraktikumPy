# menginput data via shell

# data yang dimasukkan pasti string
data = input("Masukkan data :")

print("data = ", data, "tipe datanya = ", type(data))

# # maka konversikan datanya 
datak = int(input("Masukkan datanya : "))
print("datanya : ", datak, "tipe datanya adalah = ",type(datak))

# agar bisa kebaca 1/0 maka utk boolean harus dikonversikan ke int dulu klo langsung kek gini g bisa kebaca
# misal biner = bopl(input("Maukkan dulu gan :"))

biner = bool(int(input("Massukkan biner anda : ")))
print("Hasilnya adalah : ", biner, "Tipe datanya adalah = ",type(biner))
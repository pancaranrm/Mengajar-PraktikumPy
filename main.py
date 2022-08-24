# variable
from xmlrpc.client import boolean


panjang = 10 
lebar = 50
tinggi = 20
luasnya = (panjang^lebar*tinggi)/2

# pemanggilan pertama
print("Luas layang-layang", luasnya )

# TIPE DATA yang suka lupa 

# bilangan kompleks
data_complex = complex(10,6) 
# hasilnya bakal 10+6j j= imajiner
print("data bool : ", data_complex)
print("data bertipe", type(data_complex))

# boolean
data_boolean=True
print("data bool : ", data_boolean)
print("data bertipe", type(data_boolean))


# tipe data yang ga ada di py bisa dipanggil dari bahasa c (karena py berasal dari bahasa c)

from ctypes import c_double 

data_c_double = c_double(10.6)
print("data doublenya : ", data_c_double)
print("data bertipe", type(data_c_double))

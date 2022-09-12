# mengubah dari tipe data a ke tipe data b

from xmlrpc.client import Boolean


tipedataA = 9
print("Datanya : ", tipedataA, "Dan tipe datanya adalah :", type(tipedataA))

# tinggal tulis tipe yg dituju dgn kurungan variablenya 3>
tipedataB = float(tipedataA)
tipedataC = str(tipedataA)
tipedataD = bool(tipedataA)


print("Datanya : ", tipedataB, "Dan tipe datanya berubah jadi :", type(tipedataB))
print("Datanya : ", tipedataC, "Dan tipe datanya berubah jadi :", type(tipedataC))
print("Datanya : ", tipedataD, "Dan tipe datanya berubah jadi :", type(tipedataD))




print("=====STRING=====")
data_str = "anca"
data_str2 = ""
print("Hasilnya adalah : ",data_str, "Tipe datanya: ", type(data_str))

# tapi kalo isinya "Anca" pindah ke int g bisa ya
# data_int = int(data_str)  ga bisa 

# data_float = float(data_str)  ga bisa

# akan true jika stringnya ga kosong
data_bool = bool(data_str)
data_bool2 = bool(data_str2)

# print("Hasilnya adalah : ",data_int, "Tipe datanya: ", type(data_int))
# print("Hasilnya adalah : ",data_float, "Tipe datanya: ", type(data_float))
print("Hasilnya adalah : ",data_bool, "Tipe datanya: ", type(data_bool))
print("Hasilnya adalah : ",data_bool, "Tipe datanya: ", type(data_bool2))


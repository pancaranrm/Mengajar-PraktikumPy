#  kita bisa CRUD

data_dict = {
    'Carl Marx':'Marxisme',
    'Max waber' : 'Kapitalisme-cita',
    'Ferdinand Tonnies' : 'Kelompok pengayuban & petambayan',
    'Chc' : 'Glasseffect',
}

# Panjang 
LENDICT = len(data_dict)
print(f"Panjang dictionary: {LENDICT}")

# mengecek ada/ tidak

KEY = "Marxisme"
CHECKK =  KEY in data_dict
print(f"Adakah kalimat {KEY} : {CHECKK}")

# mengecek data
print(data_dict["Chc"])
print(data_dict.get("Chc"))
print(data_dict.get("Coo","tidak diteukan"))

# mengupdate data
data_dict [1] = "Marxii"
print(f"diupdate secara biasa",data_dict)

# pake update saja
data_dict.update({"Marx":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"}) # kalau gak ada di key jadinya diadd 3>
print(data_dict)

del data_dict["Carl Marx"]
print(f"data dict yang sekarang{data_dict}")
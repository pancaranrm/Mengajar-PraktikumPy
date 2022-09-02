# bisa mengambil data value/key 
# ambil key dgn key
# ambil value dgn values

data_dict = {
    'Carl Marx':'Marxisme',
    'Max waber' : 'Kapitalisme-cita',
    'Ferdinand Tonnies' : 'Kelompok pengayuban & petambayan',
    'Chc' : 'Glasseffect',
}

# menggunakaan yang biasa
for data in data_dict:
    print(data)

# menggunakan key
ambilKey = data_dict.keys()
print(ambilKey)


# klo ambil valuenya
ambilValue = data_dict.values()
print(ambilValue)

# ambil item
ambilItem = data_dict.items()
print(ambilItem)

for item in data_dict.items():
    print(item)

for key,value in data_dict.items():
    print(f"Key: {key} | Value: {value}")
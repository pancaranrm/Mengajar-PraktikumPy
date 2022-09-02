# copy n pop py 
# pop item and pop berdasarkan key

from copy import copy


data_dict = {
    'Caca':'Marxisme',
    'Max' : 'Kapitalisme',
    'Ferdinand' : 'petambayan',
    'Chc' : 'Glasseffect',
}

data_dict2 = data_dict.copy()
print(f"Biasa {data_dict}\n")
print(f"Biasa copy {data_dict2}\n")


data_dict2["Caca"] = "Ganti"
print(f"Biasa {data_dict}\n")
print(f"Biasa copy {data_dict2}\n")


dataPop = data_dict2.pop("Ferdinand")
print(f"Pop {dataPop}\n")
print(f"Biasa copy {data_dict2}\n")

# data popItem hanya mengambil bagian list paling akhir
popit = data_dict2.popitem()
print(f"Biasa copy {data_dict2}\n")
print(f"Data terakhir {popit}\n")


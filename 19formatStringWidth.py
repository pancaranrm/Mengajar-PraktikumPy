# Width and multiline

data_nama = "Pancaran Ratna M"
kelas = "A"
tinggi = 150
nomor_sepatu = 38

data_string = f"nama = {data_nama}, kelas = {kelas},tinggi = {tinggi},Nomor Sepatu = {nomor_sepatu}"
print(5*"𓆩♡𓆪"+ " DATA SINGLE " + 5*"𓆩♡𓆪")
print(data_string)

# STRING MULTILINE
dMultiline = f"""nama = {data_nama}
kelas        = {kelas}
tinggi       = {tinggi}
nomor sepatu = {nomor_sepatu}
"""
print(5*"♡"+ " DATA MULTILINE " + 5*"♡")
print(dMultiline)


# Mengatur lebar
dWid = f"""nama = {data_nama:>1}
kelas        = {kelas:>2}
tinggi       = {tinggi:>2}
nomor sepatu = {nomor_sepatu:>2}
"""
print(5*"♡ "+ " DATA MULTILINE " + 5*" ♡")
print(dWid)

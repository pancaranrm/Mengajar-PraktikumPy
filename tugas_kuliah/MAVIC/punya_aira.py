# Konversi mata uang
# benerin punya aira
# Deklarasi variabel dengan nama, nim, dan kelas
nama = 'Nama : Aira Putri Deninta'
nim = 'NIM : 0102522006'
kelas = 'Kelas : IF22A'

# Mencetak informasi nama, nim, dan kelas
print(nama)
print(nim)
print(kelas)

# Menambahkan baris kosong
print()

# Deklarasi fungsi konversi mata uang dari IDR ke USD
def idrkeusd (idr):
  usd = 14932
  return idr/usd

# Deklarasi fungsi konversi mata uang dari IDR ke JPY
def idrkejpy (idr):
  jpy = 113
  return idr/jpy

# Deklarasi fungsi konversi mata uang dari IDR ke CNY
def idrkecny (idr):
  cny = 2171
  return idr/cny

# Deklarasi fungsi konversi mata uang dari IDR ke KRW
def idrkekrw (idr):
  krw = 11
  return idr/krw

# Menambahkan informasi header untuk konversi mata uang
print('Mengkonversi mata uang')
print('============================')

# Menambahkan informasi pilihan konversi mata uang
print('Pilihan Konversi mata uang')
print()
print('1. IDR ke USD')
print('2. IDR ke JPY')
print('3. IDR ke CNY')
print('4. IDR ke KRW')
print('============================')

# Menerima input pilihan konversi mata uang
pilihan = int(input('Silakan pilih yang ingin anda konversi : '))

# Menambahkan baris kosong
print()

# Menerima input nominal uang yang akan dikonversi
idr = int(input('Masukkan nominal : '))

# Menambahkan baris kosong
print()

# Melakukan pengecekan pilihan konversi mata uang dan mencetak hasil konversi
if pilihan == 1:
    print('IDR ke USD', idr, '=', idrkeusd(idr))
elif pilihan == 2:
   print('IDR ke JPY', idr, '=', idrkejpy(idr))
elif pilihan == 3:
   print('IDR ke CNY', idr, '=', idrkecny(idr))
elif pilihan == 4:
   print('IDR ke KRW', idr, '=', idrkekrw(idr))
else:
   print('Maaf yang anda masukkan salah!')

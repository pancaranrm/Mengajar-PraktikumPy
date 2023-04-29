# nama = 'Nama : Aira Putri Deninta'
# nim = 'NIM : 0102522006'
# kelas = 'Kelas : IF22A'

print(nama)
print(nim)
print(kelas)
print()

def idrkeusd(idr):
  usd = 14932
  return idr/usd

def idrkejpy(idr):
  jpy = 113
  return idr/jpy

def idrkecny(idr):
  cny = 2171
  return idr/cny

def idrkekrw(idr):
  krw = 11
  return idr/krw

print('Mengkonversi mata uang')
print('============================')
print('Pilihan Konversi mata uang')
print()

print('1. IDR ke USD')
print('2. IDR ke JPY')
print('3. IDR ke CNY')
print('4. IDR ke KRW')
print('============================')

pilihan = int(input('Silakan pilih yang ingin anda konversi : '))
print()

idr = int(input('Masukkan nominal : '))
print()

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

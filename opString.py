# memudahkan dalam penyingkatan kalimat

from operator import truediv


nama = "pancaran"
format = f"Hello {nama}"
print(format)

# boolean 
b = True
formatb = f"Boolean {b}"
print(formatb)

# angka
c = 2005.5
formatc = f"Decimal {c}"
print(formatc)

# bisa memisahkannya
d = 20000
formatd = f"RP. {d:,}"
print(formatc)

# bilangan desimal
e = 2200.0
formate = f"Decimal = {e:3f}" #nambahin angka inget klo komputer dari 0123 = jadi 6 angka 
print(formate)

# menampilkan leading zero
angka = 200.590
formatangka = f"Decimal = {angka:0,f}" #nambahin angka 0 kebelakangnya 
print(formatangka)

# manampilkan tanda minus
angka_minus = -10
angka_plus = +10
form_minus = f"minus = {angka_minus:+d}"
form_plus = f"plus = {angka_plus:+.2f}"

print(form_minus)
print(form_plus)

# memformaat presentase
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 2
total = f"Harga total = Rp. {harga *jumlah:,}"
print(total)

# format ke angka lain (binary,octal,dan hex)
angka = 1340
fb = f"binary = {bin(angka)}"
fo = f"Octalnya = {oct(angka)}"
fh = f"hexnya =  {hex(angka)}"

print(fb)
print(fo)
print(fh)
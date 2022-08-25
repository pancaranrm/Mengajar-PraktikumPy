# operator dalam bentuk methods

# menjadikan semua kalimat menjadi upper

from threading import main_thread


# nulis biar di tengah nih
tengah = "".center(20,'✧')
print("'"+ tengah + "Merubah ke besar" + "'")

# ke besar
salam = "anca cape banget"
print("No upper = ",salam)
salaman = salam.upper()
print("Upperd = "+salaman)


# Merubah ke kecil
print("'"+ tengah + "Merubah ke Kecil" + "'")

aneh = "HadEH CApek Oi"
print("No Lowered = ",salam)
salaman = aneh.lower()
print("Lowerd= "+salaman)

# Method pengecekan Upper/Lower Casenya

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

a = "SIST"
b = "sisster"
c = 'number 09109'
d = '1.2'
e = "THE JUNGLE BOOK"

apakah_upper = a.isupper()
print("Apakah a upper?... ",str(apakah_upper))

apakahLower = b.islower()
print("Apakah Lower?... ",str(apakah_upper))

apakahNumber = c.isalnum()
print("Apakah Number?... ",str(apakahNumber))

apakahDec = d.isdecimal()
print("Apakah Decimal?... ",str(apakahDec))

apakahTitle = e.istitle()
print("Apakah Title?... ",str(apakahTitle))









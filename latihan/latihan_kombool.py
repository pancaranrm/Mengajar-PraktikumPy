# buatlah inputan yang menghasilkan
#  soal A = ++++3----10++++
#  soal B = ----3++++10----

inputUser = (float(input("Masukkan nilai kurang dari-3 / lebih dari 10")))

# SOAL A
# ++++3---
isKurang = (inputUser < 3)
print("Kurang dari 3 = ", isKurang )

# ----10+++
isLebih = (inputUser > 10)
print("Lebih dari 10 = ", isLebih)

# Mengetahui kebenaran secara gabungan 
#  ++++3----10++++

isCorrect = isKurang or isLebih
print("angka yang anda masukkan = ", isCorrect)


#  SOAL B
#  ---3++++10--- 

inputUser = float(input("Masukkan angka lebih dari 3 / kurang dari 10"))

# ---3+++
isLebih = (inputUser > 3)
print("angka yang dimasukkan >3 = ", isLebih)

# ++++10---
isKurang = (inputUser < 10)
print("angka yang dimasukkan <10 = ",isKurang)

# gabungkan pake AND!
# ---3+++++10----

isCorrect = isKurang and isLebih
print("Angka yang dimasukkan anda = ", isCorrect)
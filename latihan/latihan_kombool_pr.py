# buatlah a = ---0+++5---8++++11---
# buatlah b = +++0---5+++8----11+++

# SOAL YG A

inputan = float(input("Maasukkan angka"))

angkaA = (inputan > 0)
print("inputan > 0 = ", angkaA)

angkaB = (inputan < 5)
print("inputan < 5 = ", angkaB)

angkaC = (inputan > 8)
print("inputan > 8 = ", angkaC)

angkaD = (inputan < 11)
print("inputan < 11 = ", angkaD)


isCorrect = angkaA and angkaB or angkaC and angkaD
print("Jadi hasilnya = ", isCorrect) 


# SOAL YG b = +++0---5+++8----11+++

inputanB = float(input("Inputan soal 2"))

angkaE = (inputanB < 0 )
print("Inputan < 0 = ",angkaE)

angkaF =(inputanB > 5 )
print("Inputan > 5", angkaF)

angkaG = (inputanB < 8 )
print("Inputan < 8 ", angkaG)

angkaH = (inputanB > 11)
print("Inputan > 11", angkaH)


# menguji 
isBenar = (angkaE or angkaF) or (angkaG and angkaH)
print ("Jadin hasilnya = ", isBenar)

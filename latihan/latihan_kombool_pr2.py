# versi ke dua gtw yg bener yg mana 3>

print('angka akan positif diantara 0 dan 5, 8 dan 11')
inputUser = float(input('masukan angka:'))

islebihdari   = (inputUser > 0)
iskurangdari  = (inputUser < 5)
islebih       = (inputUser > 8)
iskurang      = (inputUser < 11)
ishasildari   = islebihdari and iskurangdari
ishasil       = islebih and iskurang
isCorrect     = ishasildari or ishasil
print ('angka yang dimasukan:',isCorrect)


print('angka akan negatif diantara 0 dan 5, 8 dan 11')
inputUser = float(input('masukan angka:'))

iskurangdari  = (inputUser < 0)
islebihdari   = (inputUser > 5)
iskurang      = (inputUser < 8)
islebih       = (inputUser > 11)
ishasildari   = islebihdari and iskurang
isCorrect     = ishasildari or iskurangdari or islebih
print ('angka yang dimasukan:',isCorrect)
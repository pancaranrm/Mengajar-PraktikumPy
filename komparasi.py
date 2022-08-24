# penggunaan operator =,== 
# != 
# is hanya bisa membandingkan dengan variable yg udh dideklarasikan
# is not (pokonya sama dgn is cm ini versi not)
#  < > <= >=

# HARUS TELITI SAMA SYMBOLNYA ANJAY 3>

from ast import IsNot


a = 10
b = 10
c = 2

print('~~~~PENGGUNAAN~~~~')
hasilA = a > b
hasilB = b < c
hasilC = a == b
hasilD = c >= b
hasilE = a <= c
hasilF = a != c
hasilG = a is b
hasilH = a is not c


print( a, '>', b, 'hasilnya adalah..', hasilA)
print( a, '<', b, 'hasilnya adalah..', hasilB)
print( a, '==', b, 'hasilnya adalah..', hasilC)
print( c, '>=', b, 'hasilnya adalah..', hasilD)
print( a, '<=', c, 'hasilnya adalah..', hasilE)
print( a, '!=', b, 'hasilnya adalah..', hasilF)
print( a, 'is', b, 'hasilnya adalah..', hasilG)
print( a, 'is not', c, 'hasilnya adalah..', hasilH)






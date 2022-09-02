# operator khusus untuk menangani operasi logika bilangan biner dalam bentuk bit.
# jika nilai inputan bukan dari bilangan biner maka akan dikompilasi bahasa C menjadi bilangan biner

import binascii


a = 5
b = 9

# OR |
c = a | b
print("=======OR========")
print('nilai :',a, 'binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print("-------------(|)")
print('nilai biner :',c, 'binary :',format(c,'08b'))


# AND &
c = a & b
print("=======AND========")
print('nilai :',a, 'binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print("-------------(&)")
print('nilai biner :',c, 'binary :',format(c,'08b'))


# XOR
c = a ^ b
print("=======XOR========")
print('nilai :',a, 'binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print("-------------(^)")
print('nilai biner :',c, 'binary :',format(c,'08b'))


# bitwise NOT (~)
c = ~a
print('\n=========NOT========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('----------------------------- (^)')
# biner dari 9
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))


# shifting kanan/longkap ke kanan
# ini longkap ke kanan 2 kali
c = a >> 2
print('\n========= >> =======')
print('nilai :', a, ',binary :', format(a,'08b'))
print('========= >> =======')
print('nilai :', c, ',binary :', format(c,'08b'))


# shift left (<<)
c = a << 2
print('\n=========<<=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (<<)')
print('nilai :',c,' , binary :',format(c,'08b'))






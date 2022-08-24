# adalah penyingkatan agar lebih efisien anjay

a = 10
b = 5

a += 1
print("Hasilnya adalah : ",a)

b -= 3
print("Hasilnya adalah : ",b)

a *= b
print("Hasilnya adalah : ",a)

a /= b
print("Hasilnya adalah : ",a)

a %= 4
print("Hasilnya adalah : ",a)

a //= 4
print("Hasilnya adalah : ",a)

a **= 5
print("Hasilnya adalah : ",a)

a **= 3
print("nilai a **= 3, nilai a menjadi",a)

# operasi bitwise
# OR
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)
c = False
print("nilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))
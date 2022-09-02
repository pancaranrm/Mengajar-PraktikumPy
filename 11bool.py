# AND = keduanya harus true agar T
# OR = salah satu harus true
# XOR = Jika beda maka true
# NOT = kebalikan nilai


from operator import truediv, xor
from pickle import TRUE
from turtle import clear


a = TRUE
b = TRUE
c = False
d = False

print("===== OR ====")
p1 = a or b 
p2 = c or d
print(a , 'OR', b, '=', p1)
print(c , 'OR', c, '=', p2)


print("===== XOR ====")
bb = True
bc = False
xb = bb ^ bc
print(bb , 'XOR', bc, '=', xb)


print("===== AND ====")
p1 = a and b
p2 = c and d
p3 = a and c
print(a , 'AND', b, '=', p1)
print(c , 'AND', d, '=', p2)
print(a , 'AND', c, '=', p3)



print("===== NOT ====")
p1 = False
p2 = not p1
print('Data p1 =',p1)
print('Data p2 =',p2)


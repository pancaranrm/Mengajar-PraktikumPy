# membuat segitiga
"""
*
**
***
*****
"""

i = 5
c = 1
for i in range(i):
    print("*"*c)
    c+=1
sisi = 10
print("akhir dari for")


# # menggunakan while
d = 1
g = 10
while True:
    print("*"*d)
    d+= 1

    if d > g:
        break


# hanya ganjil saja
d = 1
g = 10
while True:
    if (d%2):
        print("*"*d)
        d+= 1   
    else:
        d+= 1   
        continue

    if d > g:
        break

# hanya genap
sisi = 10
print("awal while")
count = 1
spasi = int(sisi/2)

while True:
	if (count%2):
		# Print jika ganjil
		print(" "*spasi,"+"*count)
		spasi -= 1
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier while")


# buatlah ketupat
for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print("+ ", end = "")

    print()

for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()
# end digunakan untuk tidak adanya spasi


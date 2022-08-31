#  for loop disebut juga iterator

from calendar import month

# print(5* "*" *5)
# bulan = ["Januari","Februari","Desember"]

# for i in bulan:
#     print("nama bulan = ",i)
# print(5* "*" *5)

# dengan range 
# angka_range = range(5)

# for u in angka_range:
#     print("Hai saya Pancaran ke -",u)

# # 
# angka_range2 = range(5,10)
# for i in angka_range2:
#     print("Hai range ke -",i)

# print(5* "*" *5)
# print("akhir dari program 3 \n")

# # string 
# data_str = "saya ingin kurus"
# for i in data_str:
#     print(i)

print(5* "*" *5)
for i in range(2,22,2):
     print(i)

print("========")

for i in range(1,21,2):
      print(i)
print("========")

# reverse
for i in range(20,0,-2):
      print(i)
print("========")


# for x in range(10,15):
#     if (x==15):break
#     if (x % 2 == 0):continue
#     print(x)

# for i in '123':
#     print("anca",i)

for i in range(10,20):
    if (i==20):break
    if (i % 2 == 0):continue
    print(i)
# cara memngganti list yang tercopy
# dengan cara duplicate

from re import A


a = ["Anca","Lagi","Ngantuk","Banget"]
b = a

print(a)
print(b)

b.insert(1,"MASA")
print("Insert jadinya",b)
print("Insert jadinya",a) # bakalan sama hasilnya karena:

# mereka akan memiliki hex yang sama 
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
# jadi klo mau diedit bakal sama 

print("Membuat list dengan duplicate/copy")
c = a.copy()
print("Hasilnya adalah",c)

print("yang baru",a)

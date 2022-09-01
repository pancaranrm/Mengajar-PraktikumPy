# solusi untuk mengcopy pada nasted list utk ngecopynya 3>

data_0 = [1,2]
data_1 = [2,3,4]

dataGabung1 = data_0,data_1
dataGabungCopy = data_0,data_1.copy() #shallow copy /dangkal
print("ini adalah data...",dataGabung1)
print("ini adalah data...",dataGabungCopy)

data = dataGabungCopy[1][0] #mengambil data dari nasted list
print(f"data = {data}")

# adressing
print(f"addres asli = {hex(id(dataGabung1))}")
print(f"addres copy = {hex(id(dataGabungCopy))}")

dataGabung1[1][0] = 9
print("ini adalah data...",dataGabung1)
print("ini adalah data...",dataGabungCopy)

# deepcopy

from copy import deepcopy

dataGabung1 = [data_0,data_1]
dataDeep = deepcopy(dataGabung1) #

print(f"addres asli = {hex(id(dataGabung1))}")
print(f"addres Deep copy = {hex(id(dataDeep))}")

# add 
dataGabung1[1][0] = 20
print(f"data = {dataGabung1}")
print(f"data copy = {dataGabung1}")
print(f"data deep = {dataDeep}")
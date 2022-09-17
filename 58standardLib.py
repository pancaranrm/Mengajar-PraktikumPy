import collections
import datetime
import io

data_waktu = datetime.datetime.now()
print(data_waktu)
print(data_waktu.year)
print(data_waktu.month)
print(data_waktu.day) #tanggal
print(data_waktu.strftime('%A')) #day in english


from collections import Counter

data = ['A','B','C','A','B','C','A']
data_count = Counter(data)

print(f"Total data adalah {data_count}")
print(f"Total data A adalah {data_count['A']}")
print(f"Total data D adalah {data_count['D']}")


import io
file = io.open("text.txt","r")
print(file.read())  

# ada banyak cari aja di documentationnya
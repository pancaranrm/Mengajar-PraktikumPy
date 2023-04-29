import numpy as np

# INI PENTING UNTUK DATA SAINS
#  perbedaan list dan array
list_a = [1,2,3,4,5]
vector_a = np.array([1,2,3,4,5])

print(list_a)
print(f"list_a = {list_a}")
print(f"vector_a = {vector_a}")

#  matriks bisa dioprasikan matematika

matrix_b = np.array ([[1,2], [2,3]])
print(f"matrix b = \n {matrix_b}")


zeros_c = np.zeros((2,2))
print (f"Matriks kosong 2*2 = \n {zeros_c}")

# ones
ones_d = np.ones((2,2))
print (f"Matriks kosong 2*2 = \n {ones_d}") 

# pertambahan matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"Hasil penjumlahan matriks matriks yaitu = \n{jumlah}")
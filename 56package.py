'''
    package adalah sebuah tempat untuk naruh program
    diserbut folder
'''

import bImport.math #mengimport folder bImport dari file math

# jadi 
hasil_tambah = bImport.math.tambah(9,1)
print(f"hasil tambah dari package {hasil_tambah}")

hasil_perkalian = bImport.math.perkalian(2,3)
print(f"hasil kali dari package {hasil_perkalian}")


# import time
# t_start = time,time()

from bImport import fisika
gaya = fisika.gaya(10,2)
print(gaya)


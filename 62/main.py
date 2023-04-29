# Ini adalah top level code env

#  ini akan ngeprint file utama (pokoknya klo ditulis di suatu file itu akn dipanggil jadi program utama, klo diimport akan kepanggil file namanya contoh penggunaan import fungsi eksternal)
#  __name__ == "__main__"

print(f"Nilai pada __neme__ pada main.py adalah'{__name__}'")

# import __name__ pada fungsi eksternal 

import fungsi

# contoh penggunaan fungsinya

def fungsi_tambah(a:int, b:int)-> int:
    return a+b

# fungsi utama
if __name__ == '__main__':
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"Hasil tambah adalah = {hasil}")
    

# import dari folder package
import package
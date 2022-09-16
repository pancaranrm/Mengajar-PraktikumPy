from re import A


def tambah(*angka):
    hasil = 0
    
    for data in angka:
        hasil += data   
    return hasil


def kali(*angka):
    hasil = 1   
    
    for data in angka:
        hasil *= data   
    return hasil

def pangkat(n):
    return lambda angka:angka **2

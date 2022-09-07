"""
    fungsi untuk menentukan parameter
    lebih ke wawasan nih
"""

import string


def fungsi(parameter):
    hasil = parameter
    print(hasil)
    # print(hasil**2) jika kek gini akan eror ya

fungsi(True)
fungsi(2)

"""
    Olehakrena itu dibutuhkan Hint pada parameter
"""

def fungsiHint(parameter:int)->int:
    hasil = parameter + 2
    print(hasil)

fungsiHint(12)

def masukkanString(param:string):
    karakter = "Halo " + param
    print(karakter)

masukkanString("Anca")

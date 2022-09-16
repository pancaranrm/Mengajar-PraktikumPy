'''
    fungsinya untuk merapihkan folder
    ___init__.py
    seperti membuat path
'''
import packaging #manggil semuanya dari init
# import packaging.fisika #bisa ga pake ini asal tulis from di iniit
# import packaging.math 

# from packaging.math import kali, tambah

hasil_tambah = packaging.math.tambah(1,2,22)
hasil_kali = packaging.math.kali(2,4)

print(hasil_tambah)
print(hasil_kali) 

hasil_fisika = packaging.fisika.gaya(19,2)
print(f"Gayanya adalah {hasil_fisika}")

hasil_kali_super = packaging.kali(12,2) 
print(f"Hasil perkaliannya adalah {hasil_kali}") 
# aliasing
from buatimpor import pertambahan as add
from buatimpor import perkalian as kali
from buatimpor import pangkat as kuadrat


# klo udh pake from ga usah nulis file.func tinggal tulis func aja
hasil_tambah = add(10,2)
print(f"Hasil pertambahan {hasil_tambah}")

hasil_kali = kali(2,1)
print(f"Hasil perkalian {hasil_kali}")

pangkat3 = kuadrat(3)
print(f"Hasil pangkat {pangkat3(2)}")

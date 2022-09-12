# module mtk dgn import 
from buatimpor import pertambahan,perkalian,pangkat

from buatimpor import * # cara mengambil semua func


# klo udh pake from ga usah nulis file.func tinggal tulis func aja
hasil_tambah = pertambahan(10,2)
print(f"Hasil pertambahan {hasil_tambah}")

hasil_kali = perkalian(2,1)
print(f"Hasil perkalian {hasil_kali}")

pangkat3 = pangkat(3)
print(f"Hasil pangkat {pangkat3(2)}")

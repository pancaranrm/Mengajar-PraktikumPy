import packaging
from packaging.folderdalam import nyamnyam
from packaging.folderdalam.pangkat import pangkatan


pangkat_3 = pangkatan(3) # kita sudah impor semuanya dari packaging 
print(f"hasil pangkat 3 = {pangkat_3(5)}")

nyamnyam = nyamnyam.func("nyam","anggora","kuning")
print(nyamnyam)
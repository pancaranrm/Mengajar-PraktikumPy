# buatlah sebuah table seperti database mahasiswa
import datetime
from socket import NI_MAXHOST

mhs1 = {
    'nama' : 'Pancaran Ratna',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':True,    
	'lahir':datetime.datetime(2004,9,13)
}
mhs3 = {
    'nama' : 'Ratna Hadid',
	'nim':'1309090',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}
mhs2 = {
    'nama' : 'Yuna Proserus',
	'nim':'19022001',
	'sks_lulus':102,
	'beasiswa':True,
	'lahir':datetime.datetime(2001,4,10)
}

data_mhs = {
    'MHS01':mhs1,
    'MHS02':mhs2,
    'MHS03':mhs3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print(50*"=")

for mha in data_mhs:
    KEY = mha

    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks_lulus']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime("%x")
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")

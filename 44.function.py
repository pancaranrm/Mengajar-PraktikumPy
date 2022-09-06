# def fungsi(argument/parameter/input):/
    # badan fungsi 

def hi(nama):
    print(f"Hello {nama}")

hi("Anca")
hi("Abil")

def tambah(angkaa,angkab):
    hasil = angkaa + angkab
    print(f"{angkaa}+{angkab} = {hasil}")
tambah(1,33)


def salam(list_peserta):
    daftarPeserta = list_peserta.copy()
    for peserta in daftarPeserta:
        print(f"Yang terhormat {peserta}")

anggota = ['Anca','Arum','Miftah']
salam(anggota)

def fmusic(listMusic):
    dataM = listMusic.copy()
    for musik in dataM:
        print(f"Lagu keseukaan {musik}")

musiknya = ['pertified','Walk alone','Hurricane']
fmusic(musiknya)

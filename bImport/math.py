
def tambah(a:float, b:float)->float:
    return a+b

def pertambahan(*arg):
    hasil = 0
    for data in arg:
        hasil += data 
        return hasil
    
def perkalian(*kali):
    hasil = 1
    for data in kali:
        hasil *= data
        return hasil
        
def pangkat(n:int):
    return lambda a: a**n

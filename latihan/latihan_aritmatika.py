# konversikanlah daari  Farenheit ke Kelvin
'''
Farenheit ke Kelvin = (5/9)*(F - 32) + 273 
Kelvin ke Farenheit = (9/5)*(k-273)+32
'''

f = (5/9)
k = (9/5)
n = 32
o = 273

suhu_masukkanF = float(input('Masukkan suhu Farenheit ...'))
print ("suhu awal : ",suhu_masukkanF)

fK = (f)*(suhu_masukkanF - n) + o
print ("Hasil konversi ke Kelvin : ", fK)

print ("===Lanjut====")

suhu_masukkanK = float(input('Masukkan suhu Kelvin'))
kF = (k)*(suhu_masukkanK-o)+n
print("Hasil Konversi ke Farenheit =", kF)

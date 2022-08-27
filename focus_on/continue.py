# while untuk kondisi tertentu

anca = 0 # penting! masukkan angka dari 0 jika ingin mengulang dari angka 1
print("angka kamu",anca)

while anca  < 5 :
    anca += 1 
    print(f"angka sekarang -> {anca}")

    if anca == 3:
        print("nice")
        continue
    print("Kak")
print(5*"#"*5)


angka = 0

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") # aksi 1

	if angka == 3:
		pass # ini tidak akan dieksekusi kek dummy saja
		
	print("whassup!") # aksi 2

print("Pinish!")
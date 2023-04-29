# program resto

list_makanan = []
while True:
	print("\nMasukan data makanan")
 
	menu = input("No. Menu\t: ")
	makanan = input("Nama Makanan\t: ")

	menu_baru = [menu,makanan]
	list_makanan.append(menu_baru)

	print("\n\n","="*10,"Data Makanan","="*10)
	for index,makanan in enumerate(list_makanan):
		print(f"{index+1} | {makanan[0]} | {makanan[1]}")
	
	print("\n\n","="*20)
	isLanjut = input("Apakah dilanjutkan?(y/n) ")

	if isLanjut == "n":
			break

print("PROGRAM SELESAI")
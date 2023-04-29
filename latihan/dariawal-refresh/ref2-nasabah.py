"""
    Buat program jika nasabah baru masukan input nasabah, input setoran awal, simpan dan buat file tabungan baru 
    Jika nasabah lama -> baca data dan saldo nasabah   
"""

from random import choice


def head():
    print("========= HALO SELAMAT DATANG DI BANK KUCING =========")
    
    balance = 0
    while True:
        print("1. penabung lama\n 2. penabung baru \n 0. exit aplikasi\n  input anda:")
        choice = input(int("Input nomor yang dipilih"))
        
        if choice == 1:
            amount = int(input("Enter amount to be deposited: "))
            balance += amount
            print("Amount deposited successfully")
        elif choice == 2:
            amount = int(input("Enter amount to be withdrawn: "))
            
            if balance < amount:
                print("Insufficient balance")
            else:
                balance -= amount
                print("Amount withdrawn successfully")
                
        elif choice == 3:
            print("Your balance is:", balance)
        elif choice == 4:
            print("Thank you for using the banking system")
            break
        else:
            print("Invalid choice")
    

def nasabah_baru():
    i_nama = input("Input Nama Nasabah")
    i_jk = input("Jenis Kelamin")
    i_ttl = input(str("Tanggal lahir(yyyy-mm-dd hh:mm)"))
    i_strAwal = input(int("Setoran awal"))
    
    
    
    
    
    
    
    
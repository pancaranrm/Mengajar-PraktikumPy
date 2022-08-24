# beberapa penggunaan simbol pada string
'''
'...' | "..."
"\b" menjadikan teks terpisah jadi kegabung
"\t" untuk menjauh 
"\" untuk isn't [']
"\\" ketika ingin memakai slash biar ga kebaca slash '
"r" agar lebih aman pake slash untuk penamaan folder   

penggunaan '"jika ada kalimat yg ada Jum'at"' 

untuk new line kita pake 
 \r\n ini untuk windows CSRF
 \r ini macOs LF

 multiline string """ 
 hasilnya bakal ngikutin ke bawah gt
 """

'''

print('Ini quote satu saja kak')
print("quote dua")
print('"Hari ini adalah hari jum\'at"')
print('C:takut salah\\klo bisa jgn pake yg ini walau bisa')
print(r'Aku menaruh foldernya di C:ok/ok.com')
print("I\'m scared of being \r anjay testing")
print("""
Nama : Pancaran Ratna M
Fakultas : Psikologi
Cita-cita : sukses 
""")
	
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")


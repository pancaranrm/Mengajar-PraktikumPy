# Tutorial membaca file eksternal

print(3*"==", "Membaca File Text", 3*"==")
file = open("data.txt", mode= "r")

print(f"Status read = {file.readable()}")
print(f"Status read = {file.writable()}")

print(file.read())
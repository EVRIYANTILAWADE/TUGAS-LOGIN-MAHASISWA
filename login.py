# Database login mahasiswa
database = {
    "evriyanti": "3006",
}

# Authentikasi
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in database and database[username] == password:
    print("Login berhasil!")
    # Input mata kuliah
    mata_kuliah = input("Masukkan nama mata kuliah: ")
    dosen_pengampuh = input("Masukkan nama dosen pengampuh: ")
    
    print("mata kuliah:", mata_kuliah)
    print("dosen pengampuh:", dosen_pengampuh)
else:
    print("Username atau password salah.")
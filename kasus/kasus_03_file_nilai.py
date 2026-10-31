# Kasus 3: Penanganan File I/O Dasar (Materi Pertemuan 12)
try:
    with open("nilai.txt", "r") as file:
        data = file.read()
        print("Isi file:", data)
except FileNotFoundError:
    print("[Sistem] File 'nilai.txt' belum tersedia, silakan buat file terlebih dahulu.")
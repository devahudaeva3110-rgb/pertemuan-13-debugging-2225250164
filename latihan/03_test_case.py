# Latihan 3 - Bug Batas Kelulusan (Fixed)
def status_lulus(nilai):
    if nilai >= 60:  # Menggunakan >= sesuai perbaikan nilai batas
        return "Lulus"
    return "Tidak lulus"

# Menguji nilai batas 59, 60, dan 61
for n in [59, 60, 61]:
    print(f"Nilai: {n} -> Status: {status_lulus(n)}")
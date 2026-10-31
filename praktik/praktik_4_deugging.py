# Program Berhasil Diperbaiki - Tugas Pertemuan 13 NIM 2225250164
# =====================================================================
# PRAKTIK 4: KODE SETELAH PERBAIKAN (FIXED)
# S1 Pendidikan Matematika - Pertemuan 13
# =====================================================================

def hitung_rata_rata(nilai):
    # Penanganan list kosong agar tidak memicu ZeroDivisionError
    if len(nilai) == 0:
        return 0
    # PERBAIKAN: Pembagi dinamis menggunakan len(nilai) sesuai jumlah data
    return sum(nilai) / len(nilai)

def status(nilai):
    # PERBAIKAN: Menggunakan operator >= agar nilai batas (60) dinyatakan Lulus
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    # Penanganan jika list kosong
    if len(nilai) == 0:
        return None
    # PERBAIKAN: Inisialisasi diambil dari elemen pertama di dalam list nilai
    tertinggi = nilai[0]
    # PERBAIKAN: Memeriksa elemen berikutnya dengan operator > untuk mencari nilai terbesar
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

# Jalankan Pengujian Utama di Terminal
if __name__ == "__main__":
    nilai_uji = [80, 60, 90, 70]
    print("=" * 40)
    print("HASIL EVALUASI PROGRAM SETELAH PERBAIKAN")
    print("=" * 40)
    print("Rata-rata (Harapan: 75.0) -> Aktual:", hitung_rata_rata(nilai_uji))
    print("Status 60 (Harapan: Lulus) -> Aktual:", status(60))
    print("Tertinggi (Harapan: 90)   -> Aktual:", nilai_tertinggi(nilai_uji))
    print("=" * 40)
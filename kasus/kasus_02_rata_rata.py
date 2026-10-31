# Kasus 2: Perhitungan Rata-rata Kelas
def hitung_rerata(list_nilai):
    return sum(list_nilai) / len(list_nilai) if list_nilai else 0

print("Rata-rata:", hitung_rerata([80, 70, 90]))
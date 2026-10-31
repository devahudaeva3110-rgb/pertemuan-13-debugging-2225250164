# Latihan 2 - Menelusuri Fungsi Diskon
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

print("Hasil Akhir:", hitung_diskon(200000, 10))
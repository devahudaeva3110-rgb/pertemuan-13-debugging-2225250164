# Latihan 4 - Bug Rata-rata Dinamis
def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)  # Menggunakan len(data) bukan hardcoded 5

print("Rata-rata data:", rata_rata([80, 90, 70]))
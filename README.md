# Pertemuan 13 - Debugging dan Testing
**Nama:** Hudaeva 
**NIM:** 2225250164 
**Kelas:** 3E 

## Kasus
Program yang diuji adalah aplikasi pengolah data nilai mahasiswa untuk menghitung rata-rata kelas, menentukan status kelulusan berdasarkan standar nilai minimal 60, dan menyaring nilai ujian tertinggi di kelas.

## Test Case (Expected vs Actual)

| ID | Target | Input | Expected | Actual Awal | Status Awal | Actual Akhir | Status Akhir |
|---|---|---|---|---|---|---|---|
| T1 | Rata-rata | `[80, 60, 90, 70]` | 75.0 | 60.0 | **FAIL** | 75.0 | **PASS** |
| T2 | Rata-rata | `[100, 80]` | 90.0 | 36.0 | **FAIL** | 90.0 | **PASS** |
| T3 | Status | 60 | Lulus | Tidak lulus | **FAIL** | Lulus | **PASS** |
| T4 | Status | 59 | Tidak lulus | Tidak lulus | **PASS** | Tidak lulus | **PASS** |
| T5 | Tertinggi | `[80, 60, 90, 70]` | 90 | 0 | **FAIL** | 90 | **PASS** |

## Bug Report
### 1. Bug ID: B01 (Fungsi Rata-rata)
* **Gejala:** Hasil hitung rata-rata salah jika total data siswa bukan berjumlah 5.
* **Lokasi:** Fungsi `hitung_rata_rata()`.
* **Akar Penyebab:** Pembagi di-hardcode angka `5`, bukan berdasarkan panjang list data yang dimasukkan pengguna.
* **Perbaikan:** Mengubah nilai pembagi statis menjadi dinamis menggunakan `len(nilai)`.

### 2. Bug ID: B02 (Fungsi Status Kelulusan)
* **Gejala:** Mahasiswa dengan nilai tepat 60 dianggap "Tidak lulus".
* **Lokasi:** Fungsi `status()`.
* **Akar Penyebab:** Kondisi logika menggunakan `>` (lebih dari), sehingga nilai batas 60 tidak masuk kategori lulus.
* **Perbaikan:** Mengubah operator perbandingan menjadi `>=` (lebih dari atau sama dengan).

### 3. Bug ID: B03 (Fungsi Nilai Tertinggi)
* **Gejala:** Nilai tertinggi kelas selalu menghasilkan angka 0.
* **Lokasi:** Fungsi `nilai_tertinggi()`.
* **Akar Penyebab:** Variabel `tertinggi` diinisialisasi dari angka `0` dan logika pembanding di dalam loop terbalik menggunakan `<`.
* **Perbaikan:** Menginisialisasi `tertinggi = nilai[0]` dan mengubah tanda pengecekan menjadi `if x > tertinggi`.

## Retest
Setelah dilakukan perbaikan kode secara hati-hati, seluruh fungsi yang diuji dengan 5 test case utama kini sukses berstatus **PASS** tanpa memicu regresi.

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi
Teknik debugging yang paling membantu adalah kombinasi pelacakan manual (*tracing*) dan analisis nilai batas (*boundary values*). Menyusun rencana hasil (*expected result*) terlebih dahulu mencegah kita dari menebak-nebak kode tanpa arah.
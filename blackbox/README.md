# Black Box Testing - Document Generator

Script Python untuk generate dokumen Black Box Testing dalam format Word (.docx)

## Requirements

```bash
pip install python-docx
```

## Usage

1. Install dependencies terlebih dahulu:
```bash
pip install python-docx
```

2. Jalankan script:
```bash
python generate_blackbox_word.py
```

3. File Word akan ter-generate dengan nama: `Blackbox_Testing_Vendra_CRM_YYYYMMDD_HHMMSS.docx`

## Isi Dokumen

Dokumen yang di-generate mencakup:

### ✅ Cover Page
- Judul Black Box Testing
- Informasi produk
- Field untuk Tester dan Tanggal

### ✅ Informasi Umum
- Metode testing yang digunakan
- Tujuan testing

### ✅ Test Cases (45 Test Case)
1. **Authentication (7 TC)**
   - Login valid/invalid
   - Registrasi
   - Logout

2. **Manajemen Produk (8 TC)**
   - CRUD produk
   - Validasi input
   - Search & filter

3. **Transaksi POS (5 TC)**
   - Transaksi normal
   - Diskon
   - Validasi stock

4. **Import CSV (5 TC)**
   - Import valid
   - Validasi format
   - Handle duplikat produk

5. **RFM Analysis (3 TC)**
6. **AI Assistant (3 TC)**
7. **Laporan & Export (3 TC)**
8. **Role & Permission (3 TC)**
9. **Customer Management (3 TC)**
10. **Performance & Security (5 TC)**

### ✅ Summary
- Statistik testing (tabel)
- Critical/Major/Minor bugs
- Rekomendasi perbaikan
- Signature section

### ✅ Lampiran
- Decision Table
- Equivalence Partitioning
- Boundary Value Analysis

## Format Dokumen

- **Font:** Calibri 11pt
- **Heading:** Dark Blue (#003366)
- **Table Style:** Light Grid Accent 1
- **Checkbox:** ☐ Pass / Fail
- **Page Break:** Antar section

## Output

File Word siap print dan siap diisi untuk testing!

---

**Developed for Vendra AI CRM Project**

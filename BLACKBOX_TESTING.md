# Black Box Testing - Vendra AI CRM

## Informasi Umum Testing

**Produk:** Vendra AI CRM - Smart Business Management System  
**Metode Testing:** Black Box Testing  
**Tujuan:** Menguji fungsionalitas sistem tanpa melihat struktur internal kode  
**Tester:** _____________________  
**Tanggal Testing:** _____________________

---

## METODE BLACK BOX TESTING YANG DIGUNAKAN

### 1. **Equivalence Partitioning (EP)**
Membagi input menjadi kelompok valid dan invalid

### 2. **Boundary Value Analysis (BVA)**
Menguji nilai batas minimum, maksimum, dan di luar batas

### 3. **Decision Table Testing**
Menguji kombinasi kondisi dan aksi

### 4. **State Transition Testing**
Menguji perubahan state dalam sistem

### 5. **Error Guessing**
Menguji berdasarkan pengalaman error yang sering terjadi

---

## TEST CASE 1: AUTHENTICATION & AUTHORIZATION

### TC-AUTH-001: Login dengan Kredensial Valid
| **ID** | TC-AUTH-001 |
|--------|-------------|
| **Test Scenario** | User login dengan email dan password yang benar |
| **Pre-condition** | User sudah terdaftar di database |
| **Test Steps** | 1. Buka halaman login<br>2. Input email: `owner@test.com`<br>3. Input password: `password123`<br>4. Klik tombol "Login" |
| **Test Data** | Email: `owner@test.com`<br>Password: `password123` |
| **Expected Result** | ✅ Login berhasil<br>✅ Redirect ke dashboard<br>✅ Session tersimpan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-002: Login dengan Email Salah
| **ID** | TC-AUTH-002 |
|--------|-------------|
| **Test Scenario** | User login dengan email yang tidak terdaftar |
| **Test Steps** | 1. Input email: `tidakada@test.com`<br>2. Input password: `password123`<br>3. Klik "Login" |
| **Test Data** | Email: `tidakada@test.com`<br>Password: `password123` |
| **Expected Result** | ❌ Muncul error "Email tidak ditemukan"<br>❌ Login gagal<br>❌ Tetap di halaman login |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-003: Login dengan Password Salah
| **ID** | TC-AUTH-003 |
|--------|-------------|
| **Test Scenario** | User login dengan password yang salah |
| **Test Steps** | 1. Input email: `owner@test.com`<br>2. Input password: `salahpassword`<br>3. Klik "Login" |
| **Test Data** | Email: `owner@test.com`<br>Password: `salahpassword` |
| **Expected Result** | ❌ Muncul error "Password salah"<br>❌ Login gagal |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-004: Login dengan Input Kosong
| **ID** | TC-AUTH-004 |
|--------|-------------|
| **Test Scenario** | User submit form login tanpa mengisi email/password |
| **Test Steps** | 1. Biarkan email kosong<br>2. Biarkan password kosong<br>3. Klik "Login" |
| **Test Data** | Email: ` ` (kosong)<br>Password: ` ` (kosong) |
| **Expected Result** | ❌ Muncul validasi "Email wajib diisi"<br>❌ Muncul validasi "Password wajib diisi" |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-005: Registrasi User Baru
| **ID** | TC-AUTH-005 |
|--------|-------------|
| **Test Scenario** | User mendaftar akun baru sebagai Owner |
| **Test Steps** | 1. Buka halaman registrasi<br>2. Isi semua field yang required<br>3. Klik "Daftar" |
| **Test Data** | Name: `Test Owner`<br>Email: `newowner@test.com`<br>Password: `Test123!`<br>Store Name: `Toko Test`<br>Phone: `081234567890` |
| **Expected Result** | ✅ Registrasi berhasil<br>✅ User tersimpan di database<br>✅ Store otomatis dibuat<br>✅ Redirect ke login |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-006: Registrasi dengan Email Duplicate
| **ID** | TC-AUTH-006 |
|--------|-------------|
| **Test Scenario** | User mendaftar dengan email yang sudah terdaftar |
| **Test Steps** | 1. Input email yang sudah ada: `owner@test.com`<br>2. Isi data lainnya<br>3. Klik "Daftar" |
| **Expected Result** | ❌ Muncul error "Email sudah terdaftar"<br>❌ Registrasi gagal |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AUTH-007: Logout
| **ID** | TC-AUTH-007 |
|--------|-------------|
| **Test Scenario** | User logout dari sistem |
| **Test Steps** | 1. Login terlebih dahulu<br>2. Klik menu "Sign Out"<br>3. Konfirmasi logout |
| **Expected Result** | ✅ Session terhapus<br>✅ Redirect ke halaman login<br>✅ Tidak bisa akses halaman protected |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 2: MANAJEMEN PRODUK

### TC-PROD-001: Tambah Produk Valid
| **ID** | TC-PROD-001 |
|--------|-------------|
| **Test Scenario** | Admin menambahkan produk baru dengan data lengkap |
| **Test Steps** | 1. Login sebagai Owner<br>2. Klik "Manajemen Produk"<br>3. Klik "Tambah Produk"<br>4. Isi semua field<br>5. Klik "Simpan" |
| **Test Data** | Name: `Kopi Arabica`<br>SKU: `KOPI-001`<br>Price: `50000`<br>Stock: `100`<br>Category: `Minuman` |
| **Expected Result** | ✅ Produk tersimpan di database<br>✅ Muncul di list produk<br>✅ Notifikasi sukses muncul |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-002: Tambah Produk dengan SKU Duplicate
| **ID** | TC-PROD-002 |
|--------|-------------|
| **Test Scenario** | Admin menambahkan produk dengan SKU yang sudah ada |
| **Test Steps** | 1. Tambah produk dengan SKU: `KOPI-001`<br>2. Klik "Simpan" |
| **Expected Result** | ❌ Muncul error "SKU sudah digunakan"<br>❌ Produk tidak tersimpan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-003: Tambah Produk dengan Harga Negatif (BVA)
| **ID** | TC-PROD-003 |
|--------|-------------|
| **Test Scenario** | Admin input harga dengan nilai negatif |
| **Test Steps** | 1. Input harga: `-10000`<br>2. Klik "Simpan" |
| **Expected Result** | ❌ Validasi error "Harga harus lebih dari 0"<br>❌ Produk tidak tersimpan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-004: Tambah Produk dengan Stock 0 (BVA)
| **ID** | TC-PROD-004 |
|--------|-------------|
| **Test Scenario** | Admin input stock dengan nilai 0 |
| **Test Steps** | 1. Input stock: `0`<br>2. Klik "Simpan" |
| **Expected Result** | ✅ Produk tersimpan<br>✅ Status produk = "Out of Stock" |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-005: Edit Produk
| **ID** | TC-PROD-005 |
|--------|-------------|
| **Test Scenario** | Admin mengubah informasi produk |
| **Test Steps** | 1. Pilih produk yang ada<br>2. Klik "Edit"<br>3. Ubah harga dari 50000 → 55000<br>4. Klik "Update" |
| **Expected Result** | ✅ Produk terupdate di database<br>✅ Harga baru tampil di list produk |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-006: Hapus Produk
| **ID** | TC-PROD-006 |
|--------|-------------|
| **Test Scenario** | Admin menghapus produk |
| **Test Steps** | 1. Pilih produk<br>2. Klik "Hapus"<br>3. Konfirmasi hapus |
| **Expected Result** | ✅ Produk terhapus dari database<br>✅ Produk tidak muncul di list<br>✅ Notifikasi sukses muncul |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-007: Search Produk
| **ID** | TC-PROD-007 |
|--------|-------------|
| **Test Scenario** | User mencari produk dengan keyword |
| **Test Steps** | 1. Input keyword: "Kopi"<br>2. Tekan Enter atau klik Search |
| **Expected Result** | ✅ Menampilkan semua produk yang mengandung "Kopi"<br>✅ Hasil relevan dengan keyword |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PROD-008: Filter Produk by Category
| **ID** | TC-PROD-008 |
|--------|-------------|
| **Test Scenario** | User filter produk berdasarkan kategori |
| **Test Steps** | 1. Pilih kategori "Minuman"<br>2. Klik "Filter" |
| **Expected Result** | ✅ Hanya menampilkan produk kategori "Minuman" |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 3: TRANSAKSI POS (KASIR)

### TC-POS-001: Transaksi Cash Normal
| **ID** | TC-POS-001 |
|--------|-------------|
| **Test Scenario** | Kasir melakukan transaksi pembayaran cash |
| **Test Steps** | 1. Login sebagai Kasir<br>2. Tambah produk ke cart (2 item)<br>3. Input customer<br>4. Pilih payment method: Cash<br>5. Klik "Bayar" |
| **Test Data** | Product 1: Kopi Arabica (Qty: 2)<br>Product 2: Roti Bakar (Qty: 1)<br>Total: Rp 150.000<br>Payment: Cash |
| **Expected Result** | ✅ Transaksi tersimpan<br>✅ Stock produk berkurang<br>✅ Struk/Invoice generate<br>✅ Cart kosong kembali |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-POS-002: Transaksi dengan Diskon
| **ID** | TC-POS-002 |
|--------|-------------|
| **Test Scenario** | Kasir memberikan diskon pada transaksi |
| **Test Steps** | 1. Tambah produk (Total: Rp 100.000)<br>2. Apply diskon 10%<br>3. Klik "Bayar" |
| **Expected Result** | ✅ Total menjadi Rp 90.000<br>✅ Diskon tercatat di transaksi |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-POS-003: Transaksi dengan Stock Tidak Cukup
| **ID** | TC-POS-003 |
|--------|-------------|
| **Test Scenario** | Kasir mencoba transaksi dengan qty lebih besar dari stock |
| **Test Steps** | 1. Pilih produk dengan stock 5<br>2. Input qty: 10<br>3. Coba checkout |
| **Expected Result** | ❌ Muncul error "Stock tidak cukup"<br>❌ Transaksi tidak dapat dilanjutkan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-POS-004: Void/Cancel Transaksi
| **ID** | TC-POS-004 |
|--------|-------------|
| **Test Scenario** | Kasir membatalkan transaksi yang sudah diinput |
| **Test Steps** | 1. Tambah beberapa item ke cart<br>2. Klik "Cancel/Void"<br>3. Konfirmasi |
| **Expected Result** | ✅ Cart dikosongkan<br>✅ Tidak ada transaksi tersimpan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-POS-005: Scan Barcode
| **ID** | TC-POS-005 |
|--------|-------------|
| **Test Scenario** | Kasir scan barcode produk |
| **Test Steps** | 1. Klik input barcode<br>2. Scan barcode produk<br>3. Enter |
| **Expected Result** | ✅ Produk otomatis masuk ke cart<br>✅ Qty default = 1 |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 4: IMPORT DATA CSV

### TC-IMPORT-001: Import CSV Valid
| **ID** | TC-IMPORT-001 |
|--------|-------------|
| **Test Scenario** | Admin import file CSV dengan format benar |
| **Test Steps** | 1. Upload file CSV valid<br>2. Preview data<br>3. Klik "Import" |
| **Expected Result** | ✅ Data ter-import ke database<br>✅ Jumlah data sesuai file CSV<br>✅ Notifikasi sukses |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-IMPORT-002: Import CSV dengan Format Salah
| **ID** | TC-IMPORT-002 |
|--------|-------------|
| **Test Scenario** | Admin upload file CSV dengan kolom tidak sesuai |
| **Test Steps** | 1. Upload CSV dengan kolom berbeda<br>2. Coba import |
| **Expected Result** | ❌ Muncul error "Format file salah"<br>❌ Import gagal |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-IMPORT-003: Import File Non-CSV
| **ID** | TC-IMPORT-003 |
|--------|-------------|
| **Test Scenario** | Admin upload file selain CSV (Excel, PDF, dll) |
| **Test Steps** | 1. Upload file .xlsx atau .pdf<br>2. Coba import |
| **Expected Result** | ❌ Validasi "File harus format CSV"<br>❌ Import ditolak |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-IMPORT-004: Import CSV Kosong
| **ID** | TC-IMPORT-004 |
|--------|-------------|
| **Test Scenario** | Admin import CSV tanpa data (hanya header) |
| **Test Steps** | 1. Upload CSV kosong<br>2. Klik import |
| **Expected Result** | ❌ Error "File tidak ada data"<br>❌ Import gagal |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-IMPORT-005: Import CSV dengan Produk Duplikat
| **ID** | TC-IMPORT-005 |
|--------|-------------|
| **Test Scenario** | Import CSV yang berisi produk dengan nama yang sama |
| **Test Steps** | 1. Upload CSV dengan multiple rows produk "Almond Butter"<br>2. Klik import |
| **Expected Result** | ✅ Produk dengan nama sama hanya dibuat 1x<br>✅ Data lainnya tetap ter-import<br>✅ Tidak ada duplikat produk |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 5: ANALISIS RFM

### TC-RFM-001: View RFM Dashboard
| **ID** | TC-RFM-001 |
|--------|-------------|
| **Test Scenario** | Owner melihat dashboard RFM Analysis |
| **Test Steps** | 1. Login sebagai Owner<br>2. Klik menu "RFM Analysis" |
| **Expected Result** | ✅ Dashboard tampil<br>✅ Chart/Graph muncul<br>✅ Data segmentasi customer tampil |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-RFM-002: Filter Customer by Segment
| **ID** | TC-RFM-002 |
|--------|-------------|
| **Test Scenario** | Owner filter customer berdasarkan segmen RFM |
| **Test Steps** | 1. Pilih segment "Champions"<br>2. Klik "Filter" |
| **Expected Result** | ✅ Hanya tampil customer dengan segment Champions<br>✅ Data sesuai kriteria RFM |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-RFM-003: Export RFM Data
| **ID** | TC-RFM-003 |
|--------|-------------|
| **Test Scenario** | Owner export data RFM ke Excel/CSV |
| **Test Steps** | 1. Klik "Export Data"<br>2. Pilih format<br>3. Download |
| **Expected Result** | ✅ File berhasil didownload<br>✅ Data sesuai dengan tampilan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 6: AI ASSISTANT

### TC-AI-001: Tanya AI tentang Sales
| **ID** | TC-AI-001 |
|--------|-------------|
| **Test Scenario** | User bertanya ke AI tentang performa sales |
| **Test Steps** | 1. Buka AI Assistant<br>2. Ketik: "Bagaimana performa penjualan bulan ini?"<br>3. Send |
| **Expected Result** | ✅ AI merespons dalam < 5 detik<br>✅ Jawaban relevan dengan data sales<br>✅ Ada angka/statistik |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AI-002: Minta Rekomendasi Produk Restock
| **ID** | TC-AI-002 |
|--------|-------------|
| **Test Scenario** | User minta saran produk yang perlu restock |
| **Test Steps** | 1. Tanya: "Produk apa yang perlu di-restock?"<br>2. Send |
| **Expected Result** | ✅ AI memberi list produk dengan stock rendah<br>✅ Disertai jumlah stock saat ini |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-AI-003: Pertanyaan di Luar Konteks
| **ID** | TC-AI-003 |
|--------|-------------|
| **Test Scenario** | User bertanya hal di luar bisnis/CRM |
| **Test Steps** | 1. Tanya: "Siapa presiden Indonesia?"<br>2. Send |
| **Expected Result** | ✅ AI menolak/redirect ke topik bisnis<br>✅ Atau jawab singkat lalu kembali ke konteks |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 7: LAPORAN & EXPORT

### TC-REPORT-001: Generate Laporan Penjualan Harian
| **ID** | TC-REPORT-001 |
|--------|-------------|
| **Test Scenario** | Owner generate laporan penjualan hari ini |
| **Test Steps** | 1. Pilih filter "Hari Ini"<br>2. Klik "Generate Report" |
| **Expected Result** | ✅ Report tampil dengan data hari ini<br>✅ Total penjualan benar<br>✅ Jumlah transaksi sesuai |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-REPORT-002: Export Laporan ke Excel
| **ID** | TC-REPORT-002 |
|--------|-------------|
| **Test Scenario** | Owner export laporan dalam format Excel |
| **Test Steps** | 1. Pilih periode laporan<br>2. Klik "Export Excel"<br>3. Download |
| **Expected Result** | ✅ File Excel terdownload<br>✅ Data sesuai dengan laporan<br>✅ Format rapi dan readable |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-REPORT-003: Filter Laporan by Date Range
| **ID** | TC-REPORT-003 |
|--------|-------------|
| **Test Scenario** | Owner filter laporan dari tanggal tertentu |
| **Test Steps** | 1. Input start date: 01-11-2025<br>2. Input end date: 27-11-2025<br>3. Klik "Filter" |
| **Expected Result** | ✅ Hanya data dalam range tersebut yang tampil<br>✅ Calculation benar |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 8: ROLE & PERMISSION

### TC-ROLE-001: Akses Menu sesuai Role (Owner)
| **ID** | TC-ROLE-001 |
|--------|-------------|
| **Test Scenario** | Owner dapat akses semua menu |
| **Test Steps** | 1. Login sebagai Owner<br>2. Coba akses: Dashboard, Produk, RFM, Settings |
| **Expected Result** | ✅ Semua menu dapat diakses<br>✅ Tidak ada restriction |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-ROLE-002: Akses Menu sesuai Role (Cashier)
| **ID** | TC-ROLE-002 |
|--------|-------------|
| **Test Scenario** | Kasir hanya bisa akses menu POS |
| **Test Steps** | 1. Login sebagai Cashier<br>2. Coba akses menu Settings/RFM |
| **Expected Result** | ❌ Tidak dapat akses menu restricted<br>❌ Redirect atau error 403 |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-ROLE-003: SuperAdmin Approve Owner
| **ID** | TC-ROLE-003 |
|--------|-------------|
| **Test Scenario** | SuperAdmin approve pending owner |
| **Test Steps** | 1. Login sebagai SuperAdmin<br>2. Lihat pending owners<br>3. Klik "Approve" |
| **Expected Result** | ✅ Status owner berubah jadi "ACTIVE"<br>✅ Owner bisa login |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 9: MANAJEMEN CUSTOMER

### TC-CUST-001: Tambah Customer Baru
| **ID** | TC-CUST-001 |
|--------|-------------|
| **Test Scenario** | Admin menambahkan customer baru |
| **Test Steps** | 1. Buka menu Customer<br>2. Klik "Tambah Customer"<br>3. Isi data customer<br>4. Klik "Simpan" |
| **Test Data** | Name: `John Doe`<br>Phone: `081234567890`<br>Email: `john@mail.com`<br>Member: Yes |
| **Expected Result** | ✅ Customer tersimpan<br>✅ Unique ID ter-generate<br>✅ Muncul di list customer |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-CUST-002: Edit Data Customer
| **ID** | TC-CUST-002 |
|--------|-------------|
| **Test Scenario** | Admin mengubah data customer |
| **Test Steps** | 1. Pilih customer<br>2. Edit phone number<br>3. Update |
| **Expected Result** | ✅ Data customer terupdate<br>✅ Perubahan tersimpan |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-CUST-003: Hapus Customer
| **ID** | TC-CUST-003 |
|--------|-------------|
| **Test Scenario** | Admin menghapus customer |
| **Test Steps** | 1. Pilih customer<br>2. Klik "Hapus"<br>3. Konfirmasi |
| **Expected Result** | ✅ Customer terhapus dari database<br>✅ Tidak muncul di list |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## TEST CASE 10: PERFORMANCE & SECURITY

### TC-PERF-001: Load Time Homepage
| **ID** | TC-PERF-001 |
|--------|-------------|
| **Test Scenario** | Mengukur kecepatan loading homepage |
| **Test Steps** | 1. Clear cache browser<br>2. Akses homepage<br>3. Catat waktu loading |
| **Expected Result** | ✅ Loading < 3 detik |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-PERF-002: Load Time Dashboard (After Login)
| **ID** | TC-PERF-002 |
|--------|-------------|
| **Test Scenario** | Mengukur kecepatan loading dashboard |
| **Test Steps** | 1. Login<br>2. Catat waktu loading dashboard |
| **Expected Result** | ✅ Loading < 2 detik |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-SEC-001: Akses Halaman Protected tanpa Login
| **ID** | TC-SEC-001 |
|--------|-------------|
| **Test Scenario** | User mencoba akses halaman admin tanpa login |
| **Test Steps** | 1. Logout terlebih dahulu<br>2. Akses URL `/admin/products` |
| **Expected Result** | ❌ Redirect ke halaman login<br>❌ Tidak dapat akses halaman |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-SEC-002: SQL Injection Test
| **ID** | TC-SEC-002 |
|--------|-------------|
| **Test Scenario** | Test keamanan dari SQL injection |
| **Test Steps** | 1. Input di search: `' OR 1=1--`<br>2. Submit |
| **Expected Result** | ❌ Tidak ada error SQL<br>✅ Input di-sanitize |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

### TC-SEC-003: XSS (Cross-Site Scripting) Test
| **ID** | TC-SEC-003 |
|--------|-------------|
| **Test Scenario** | Test keamanan dari XSS attack |
| **Test Steps** | 1. Input di form: `<script>alert('XSS')</script>`<br>2. Submit |
| **Expected Result** | ❌ Script tidak dieksekusi<br>✅ Input di-escape |
| **Actual Result** | ________________ |
| **Status** | [ ] Pass [ ] Fail |

---

## SUMMARY HASIL TESTING

### Statistik Testing
| **Kategori** | **Total Test Case** | **Pass** | **Fail** | **% Pass Rate** |
|--------------|---------------------|----------|----------|-----------------|
| Authentication | 7 | ___ | ___ | ___% |
| Produk | 8 | ___ | ___ | ___% |
| POS/Transaksi | 5 | ___ | ___ | ___% |
| Import CSV | 5 | ___ | ___ | ___% |
| RFM Analysis | 3 | ___ | ___ | ___% |
| AI Assistant | 3 | ___ | ___ | ___% |
| Laporan | 3 | ___ | ___ | ___% |
| Role & Permission | 3 | ___ | ___ | ___% |
| Customer Management | 3 | ___ | ___ | ___% |
| Performance & Security | 5 | ___ | ___ | ___% |
| **TOTAL** | **45** | ___ | ___ | ___% |

---

### Critical Bugs Found
1. ______________________________________
2. ______________________________________
3. ______________________________________

### Major Bugs Found
1. ______________________________________
2. ______________________________________
3. ______________________________________

### Minor Bugs Found
1. ______________________________________
2. ______________________________________

---

### Rekomendasi Perbaikan
1. ______________________________________
2. ______________________________________
3. ______________________________________

---

**Tester Signature:** _____________________  
**Date:** _____________________

---

## LAMPIRAN A: DECISION TABLE

### Decision Table: Login Process

| **Condition** | TC1 | TC2 | TC3 | TC4 | TC5 |
|---------------|-----|-----|-----|-----|-----|
| Email Valid | ✅ | ❌ | ✅ | ✅ | ❌ |
| Password Valid | ✅ | ✅ | ❌ | ✅ | ❌ |
| User Active | ✅ | ✅ | ✅ | ❌ | ✅ |
| **Action** |
| Login Success | ✅ | ❌ | ❌ | ❌ | ❌ |
| Show Error | ❌ | ✅ | ✅ | ✅ | ✅ |
| Redirect Dashboard | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## LAMPIRAN B: EQUIVALENCE PARTITIONING

### EP untuk Input Harga Produk

| **Partition Class** | **Input Range** | **Valid/Invalid** | **Expected Result** |
|---------------------|-----------------|-------------------|---------------------|
| Valid Positive | 1 - 999,999,999 | Valid | ✅ Diterima |
| Zero | 0 | Valid | ✅ Diterima (Out of Stock) |
| Negative | < 0 | Invalid | ❌ Error |
| Too Large | > 999,999,999 | Invalid | ❌ Error |
| Non-numeric | "abc", "!@#" | Invalid | ❌ Error |

---

## LAMPIRAN C: BOUNDARY VALUE ANALYSIS

### BVA untuk Input Stock Produk

| **Test Value** | **Type** | **Expected Result** |
|----------------|----------|---------------------|
| -1 | Below Min | ❌ Error |
| 0 | Min Valid | ✅ Accepted (Out of Stock) |
| 1 | Min+1 | ✅ Accepted |
| 9999 | Max-1 | ✅ Accepted |
| 10000 | Max | ✅ Accepted |
| 10001 | Above Max | ❌ Error (Optional) |

---

**End of Black Box Testing Document**

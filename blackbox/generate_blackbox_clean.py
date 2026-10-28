from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def add_table_borders(table):
    """Add borders to table"""
    tbl = table._element
    tblPr = tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)
    
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), '000000')
        tblBorders.append(border)
    tblPr.append(tblBorders)

# Data test case berdasarkan implementasi web ASLI
test_cases = [
    # ============== AUTENTIKASI & REGISTRASI ==============
    {
        "no": 1,
        "fitur": "Registrasi Owner - Step 1 (Data Pribadi)",
        "skenario": "Input data pribadi lengkap pada step 1",
        "input": "Nama: 'John Doe', Email: 'john@test.com', Password: 'password123', Confirm Password: 'password123'",
        "hasil": "System mengirim OTP ke email, menampilkan form OTP verification (Step 2)",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 2,
        "fitur": "Registrasi Owner - Step 1 (Validasi Password)",
        "skenario": "Password tidak cocok dengan confirm password",
        "input": "Password: 'pass123', Confirm Password: 'pass456'",
        "hasil": "Muncul error: 'Password tidak cocok'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 3,
        "fitur": "Registrasi Owner - Step 1 (Validasi Panjang Password)",
        "skenario": "Password kurang dari 6 karakter",
        "input": "Password: '12345' (5 karakter)",
        "hasil": "Muncul error: 'Password minimal 6 karakter'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 4,
        "fitur": "Registrasi Owner - Step 2 (OTP Verification)",
        "skenario": "Input kode OTP yang valid",
        "input": "OTP code yang diterima di email (6 digit)",
        "hasil": "OTP terverifikasi, lanjut ke step 3 (Company Info) jika paket berbayar, atau auto-approve jika FREE",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 5,
        "fitur": "Registrasi Owner - Step 2 (OTP Invalid)",
        "skenario": "Input kode OTP yang salah/expired",
        "input": "OTP code: '000000' (salah)",
        "hasil": "Muncul error: 'Kode OTP tidak valid'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 6,
        "fitur": "Registrasi Owner - Step 3 (Data Perusahaan)",
        "skenario": "Input data perusahaan lengkap setelah OTP verified",
        "input": "Company Name: 'PT ABC', Company Email: 'info@abc.com', Phone: '081234567890', Address: 'Jl. Sudirman'",
        "hasil": "Data tersimpan, registrasi selesai dengan paket FREE, redirect ke success page",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 7,
        "fitur": "Registrasi Owner - Default FREE Tier",
        "skenario": "Semua registrasi baru otomatis mendapat paket FREE",
        "input": "Complete registration process",
        "hasil": "User terdaftar dengan subscriptionTier: 'FREE', auto-approved, bisa langsung login",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== LOGIN OWNER ==============
    {
        "no": 8,
        "fitur": "Login Owner",
        "skenario": "Login dengan credentials valid sebagai Owner setelah registrasi",
        "input": "Email: 'owner@test.com', Password: 'validpass123'",
        "hasil": "Login sukses, redirect ke '/admin' dashboard",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 9,
        "fitur": "Login Invalid Credentials",
        "skenario": "Login dengan email/password salah",
        "input": "Email: 'owner@test.com', Password: 'wrongpass'",
        "hasil": "Muncul error: 'Email atau password salah'",
        "valid": "",
        "tidak_valid": "✓"
    },

    # ============== UPGRADE SUBSCRIPTION ==============
    {
        "no": 10,
        "fitur": "Upgrade Akun - Pilih Paket BASIC",
        "skenario": "Owner FREE tier request upgrade ke BASIC",
        "input": "Select plan: 'BASIC', Upload payment proof, Payment method: 'Bank Transfer'",
        "hasil": "Request terkirim, status: PENDING, menunggu approval SuperAdmin",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 11,
        "fitur": "Upgrade Akun - Pilih Paket PREMIUM",
        "skenario": "Owner request upgrade ke PREMIUM",
        "input": "Select plan: 'PREMIUM', Upload payment proof, Payment method: 'E-Wallet'",
        "hasil": "Request terkirim, status: PENDING",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 12,
        "fitur": "Upgrade Akun - Pilih Paket ENTERPRISE",
        "skenario": "Owner request upgrade ke ENTERPRISE",
        "input": "Select plan: 'ENTERPRISE', Upload payment proof",
        "hasil": "Request terkirim, status: PENDING",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 13,
        "fitur": "Upgrade Akun - Tanpa Bukti Pembayaran",
        "skenario": "Submit upgrade request tanpa upload file",
        "input": "Select plan: 'BASIC', No payment proof",
        "hasil": "Error: 'Silakan upload bukti pembayaran'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 14,
        "fitur": "Upgrade Akun - File Terlalu Besar",
        "skenario": "Upload file lebih dari 5MB",
        "input": "Payment proof file: 6MB",
        "hasil": "Error: 'Ukuran file maksimal 5MB'",
        "valid": "",
        "tidak_valid": "✓"
    },

    # ============== SUPERADMIN - APPROVAL UPGRADE ==============
    {
        "no": 15,
        "fitur": "SuperAdmin Login",
        "skenario": "Login sebagai SuperAdmin untuk approve upgrade requests",
        "input": "Email: 'superadmin@vendra.com', Password: 'PASSWORD_BARU_ANDA'",
        "hasil": "Login sukses, redirect ke '/superadmin' dashboard",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 16,
        "fitur": "SuperAdmin - Approve Upgrade Request",
        "skenario": "SuperAdmin approve request upgrade owner",
        "input": "Upgrade request ID, Action: Approve",
        "hasil": "Owner subscription tier terupdate, email notification sent, fitur baru aktif",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 17,
        "fitur": "SuperAdmin - Reject Upgrade Request",
        "skenario": "SuperAdmin reject request upgrade owner",
        "input": "Upgrade request ID, Action: Reject, Reason: 'Bukti pembayaran tidak valid'",
        "hasil": "Request ditolak, owner tetap di tier lama, email notification sent",
        "valid": "",
        "tidak_valid": "✓"
    },

    # ============== MANAJEMEN EMPLOYEES (KASIR) ==============
    {
        "no": 18,
        "fitur": "Tambah Employee/Kasir Baru",
        "skenario": "Owner membuat akun kasir untuk cabang toko",
        "input": "Name: 'Budi Kasir', Email: 'budi@tokosaya.com', Password: 'kasir123', Role: 'KASIR', Store: 'Toko Cabang A'",
        "hasil": "Akun kasir berhasil dibuat, email notifikasi terkirim dengan credentials",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 19,
        "fitur": "Tambah Employee - Email Duplikat",
        "skenario": "Buat employee dengan email yang sudah ada",
        "input": "Email: 'budi@tokosaya.com' (already exists)",
        "hasil": "Error: 'Email sudah terdaftar'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 20,
        "fitur": "Edit Employee",
        "skenario": "Update data employee existing",
        "input": "Employee ID, New Name: 'Budi Updated', New Store: 'Toko Cabang B'",
        "hasil": "Data employee terupdate, perubahan tersimpan",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 21,
        "fitur": "Hapus Employee",
        "skenario": "Delete akun employee dengan konfirmasi",
        "input": "Employee ID, Confirm delete: Yes",
        "hasil": "Employee terhapus, tidak bisa login lagi",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== LOGIN KASIR ==============
    {
        "no": 22,
        "fitur": "Login Kasir",
        "skenario": "Kasir login dengan akun yang sudah dibuat Owner",
        "input": "Email: 'budi@tokosaya.com', Password: 'kasir123'",
        "hasil": "Login sukses, redirect ke '/kasir' dashboard POS",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== MANAJEMEN PRODUK ==============
    {
        "no": 23,
        "fitur": "Tambah Produk Baru",
        "skenario": "Input produk baru dengan data lengkap",
        "input": "Name: 'Sabun Mandi', SKU: 'SBN001', Barcode: '1234567890123', Price: 15000, Stock: 100, Min Stock: 10, Category: 'Toiletries', Unit: 'pcs'",
        "hasil": "Produk tersimpan, muncul di daftar produk",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 24,
        "fitur": "Tambah Produk - SKU Duplikat",
        "skenario": "Input produk dengan SKU yang sudah ada",
        "input": "SKU: 'SBN001' (already exists)",
        "hasil": "Muncul error: 'SKU sudah digunakan'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 25,
        "fitur": "Edit Produk",
        "skenario": "Update informasi produk existing",
        "input": "Product ID: 'xxx', New Price: 18000, New Stock: 150",
        "hasil": "Data produk terupdate, perubahan tersimpan",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 26,
        "fitur": "Hapus Produk",
        "skenario": "Delete produk dengan konfirmasi",
        "input": "Product ID: 'xxx', Confirm delete: Yes",
        "hasil": "Produk terhapus, hilang dari daftar produk",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 27,
        "fitur": "Search Produk - By Name",
        "skenario": "Cari produk berdasarkan nama",
        "input": "Search term: 'Sabun'",
        "hasil": "Menampilkan semua produk yang mengandung kata 'Sabun' di nama",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 28,
        "fitur": "Search Produk - By SKU",
        "skenario": "Cari produk berdasarkan SKU",
        "input": "Search term: 'SBN001'",
        "hasil": "Menampilkan produk dengan SKU 'SBN001'",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 29,
        "fitur": "Search Produk - By Barcode",
        "skenario": "Cari produk berdasarkan barcode",
        "input": "Search term: '1234567890123'",
        "hasil": "Menampilkan produk dengan barcode '1234567890123'",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 30,
        "fitur": "Filter Produk - By Category",
        "skenario": "Filter produk berdasarkan kategori",
        "input": "Category filter: 'Toiletries'",
        "hasil": "Menampilkan hanya produk kategori 'Toiletries'",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 31,
        "fitur": "Filter Produk - By Store",
        "skenario": "Filter produk berdasarkan toko tertentu",
        "input": "Store filter: 'Toko Cabang A'",
        "hasil": "Menampilkan hanya produk yang ada di 'Toko Cabang A'",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 32,
        "fitur": "Low Stock Alert",
        "skenario": "Produk dengan stock <= minimum stock",
        "input": "Stock: 5, Min Stock: 10",
        "hasil": "Produk muncul di 'Low Stock Products' warning list",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== TRANSAKSI POS KASIR ==============
    {
        "no": 33,
        "fitur": "Tambah Item ke Cart - POS",
        "skenario": "Kasir menambah produk ke keranjang",
        "input": "Product: 'Sabun Mandi', Quantity: 2",
        "hasil": "Item ditambahkan ke cart, subtotal: Price × 2",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 34,
        "fitur": "Tambah Item - Stok Tidak Cukup",
        "skenario": "Tambah qty lebih dari stock available",
        "input": "Product stock: 3, Quantity to add: 5",
        "hasil": "Quantity tetap max 3 (tidak bisa melebihi stock)",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 35,
        "fitur": "Edit Quantity Item di Cart",
        "skenario": "Ubah jumlah item di keranjang",
        "input": "Cart item quantity: 2 → 5",
        "hasil": "Quantity terupdate, subtotal recalculated",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 36,
        "fitur": "Hapus Item dari Cart",
        "skenario": "Remove item dari keranjang",
        "input": "Product ID di cart, action: remove",
        "hasil": "Item terhapus dari cart, total amount updated",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 37,
        "fitur": "Search Produk di POS - By Name",
        "skenario": "Kasir search produk by name",
        "input": "Search: 'Sabun'",
        "hasil": "Tampil produk yang mengandung 'Sabun' di nama",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 38,
        "fitur": "Search Produk di POS - By Barcode",
        "skenario": "Kasir scan barcode untuk search",
        "input": "Search: '1234567890123'",
        "hasil": "Tampil produk dengan barcode tersebut",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 39,
        "fitur": "Select Customer untuk Transaksi",
        "skenario": "Pilih customer dari database",
        "input": "Customer: 'Budi Santoso'",
        "hasil": "Customer terpilih, data customer tersimpan untuk transaksi",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 40,
        "fitur": "Checkout Transaksi - Cash",
        "skenario": "Proses pembayaran dengan metode Cash",
        "input": "Cart: 3 items, Total: 50000, Payment Method: 'CASH', Customer: selected",
        "hasil": "Transaksi berhasil disimpan, stock terupdate, cart kosong, muncul success notification",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 41,
        "fitur": "Checkout Transaksi - E-Wallet",
        "skenario": "Proses pembayaran dengan metode E-Wallet",
        "input": "Cart: 2 items, Total: 35000, Payment Method: 'E-WALLET'",
        "hasil": "Transaksi berhasil disimpan, payment method: 'E-WALLET'",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 42,
        "fitur": "Checkout - Cart Kosong",
        "skenario": "Coba checkout tanpa item di cart",
        "input": "Cart: empty",
        "hasil": "Muncul alert: 'Keranjang kosong!'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 43,
        "fitur": "Auto Update Stock After Checkout",
        "skenario": "Stock berkurang otomatis setelah checkout",
        "input": "Product stock sebelum: 100, Quantity sold: 5",
        "hasil": "Product stock setelah: 95, stock terupdate di database",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== SUBSCRIPTION & TIER MANAGEMENT ==============
    {
        "no": 44,
        "fitur": "FREE Tier - Limit Toko",
        "skenario": "Owner FREE tier coba buat toko ke-2",
        "input": "Current stores: 1, Action: Create new store",
        "hasil": "Error: 'Limit toko untuk FREE tier adalah 1'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 45,
        "fitur": "BASIC Tier - Limit Toko",
        "skenario": "Owner BASIC tier buat toko ke-3",
        "input": "Current stores: 2, Action: Create new store",
        "hasil": "Toko ke-3 berhasil dibuat (max 3 toko untuk BASIC)",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 46,
        "fitur": "PREMIUM Tier - Limit Toko",
        "skenario": "Owner PREMIUM tier buat toko ke-10",
        "input": "Current stores: 9, Action: Create new store",
        "hasil": "Toko ke-10 berhasil dibuat (max 10 toko untuk PREMIUM)",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 47,
        "fitur": "ENTERPRISE Tier - Unlimited Stores",
        "skenario": "Owner ENTERPRISE tier buat toko ke-100",
        "input": "Current stores: 99, Action: Create new store",
        "hasil": "Toko ke-100 berhasil dibuat (unlimited untuk ENTERPRISE)",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 48,
        "fitur": "Storage Monitoring",
        "skenario": "Cek penggunaan storage company",
        "input": "Company storage usage query",
        "hasil": "Menampilkan total storage used vs limit berdasarkan tier",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== AI FEATURES ==============
    {
        "no": 49,
        "fitur": "AI Assistant - BASIC Tier",
        "skenario": "Owner BASIC tier akses AI Assistant",
        "input": "Question: 'Berapa total penjualan bulan ini?'",
        "hasil": "AI menjawab dengan data analisis penjualan",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 50,
        "fitur": "AI Assistant - FREE Tier Blocked",
        "skenario": "Owner FREE tier coba akses AI Assistant",
        "input": "Action: Open AI Assistant menu",
        "hasil": "Error/Blocked: 'AI Features hanya untuk BASIC, PREMIUM, ENTERPRISE'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 51,
        "fitur": "RFM Analysis - BASIC Tier",
        "skenario": "Owner BASIC tier akses RFM Analysis",
        "input": "Action: View RFM Analysis report",
        "hasil": "Menampilkan customer segmentation (Recency, Frequency, Monetary)",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 52,
        "fitur": "RFM Analysis - FREE Tier Blocked",
        "skenario": "Owner FREE tier coba akses RFM Analysis",
        "input": "Action: Open RFM Analysis menu",
        "hasil": "Blocked: 'RFM Analysis tidak tersedia untuk FREE tier'",
        "valid": "",
        "tidak_valid": "✓"
    },

    # ============== IMPORT CSV ==============
    {
        "no": 53,
        "fitur": "Import CSV - Produk Valid",
        "skenario": "Upload CSV dengan data produk valid",
        "input": "CSV file: products.csv (valid format, all fields correct)",
        "hasil": "Semua produk berhasil diimport, muncul di daftar produk",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 54,
        "fitur": "Import CSV - Prevent Duplicate by Name",
        "skenario": "Import CSV dengan nama produk yang sudah ada",
        "input": "CSV contains: 'Almond Butter' (already exists in DB with same name)",
        "hasil": "System skip duplicate, hanya import produk baru, atau update existing by name",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 55,
        "fitur": "Import CSV - Invalid Format",
        "skenario": "Upload CSV dengan format kolom salah",
        "input": "CSV file: invalid_format.csv (missing required columns)",
        "hasil": "Error: 'Format CSV tidak valid, periksa kolom yang diperlukan'",
        "valid": "",
        "tidak_valid": "✓"
    },
    {
        "no": 56,
        "fitur": "Import CSV - Transaction Data",
        "skenario": "Upload CSV dengan data transaksi historical",
        "input": "CSV file: transactions.csv (transaction history)",
        "hasil": "Transaksi diimport, muncul di transaction history",
        "valid": "✓",
        "tidak_valid": ""
    },

    # ============== SUPERADMIN APPROVAL ==============
    {
        "no": 57,
        "fitur": "SuperAdmin - Approve Owner Registration",
        "skenario": "SuperAdmin approve pending owner",
        "input": "Owner status: PENDING, Action: Approve",
        "hasil": "Owner status → APPROVED, owner bisa login dan akses dashboard",
        "valid": "✓",
        "tidak_valid": ""
    },
    {
        "no": 58,
        "fitur": "SuperAdmin - Reject Owner Registration",
        "skenario": "SuperAdmin reject pending owner",
        "input": "Owner status: PENDING, Action: Reject",
        "hasil": "Owner status → REJECTED, owner tidak bisa login",
        "valid": "✓",
        "tidak_valid": ""
    }
]

# Buat dokumen Word
doc = Document()

# Set font default
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(11)

# Judul Dokumen
title = doc.add_paragraph()
title_run = title.add_run('LEMBAR UJI BLACKBOX\nVENDRA CRM - CUSTOMER RELATIONSHIP MANAGEMENT SYSTEM')
title_run.font.size = Pt(14)
title_run.font.bold = True
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Spasi
doc.add_paragraph()

# Informasi Penguji (seperti di PDF)
penguji_info = doc.add_paragraph()
penguji_info.add_run('Nama Penguji  : ').font.bold = False
penguji_info.add_run('_' * 60)
penguji_info.alignment = WD_ALIGN_PARAGRAPH.LEFT

profesi_info = doc.add_paragraph()
profesi_info.add_run('Profesi             : ').font.bold = False
profesi_info.add_run('_' * 60)
profesi_info.alignment = WD_ALIGN_PARAGRAPH.LEFT

website_info = doc.add_paragraph()
website_info.add_run('Alamat Website : https://vendra-crm.vercel.app')
website_info.alignment = WD_ALIGN_PARAGRAPH.LEFT

# Spasi
doc.add_paragraph()

# Informasi Dokumen
info_table = doc.add_table(rows=5, cols=2)
info_table.autofit = False
info_table.allow_autofit = False

# Set lebar kolom info
info_table.columns[0].width = Inches(1.5)
info_table.columns[1].width = Inches(5.0)

info_data = [
    ('Aplikasi', 'Vendra CRM - Customer Relationship Management System'),
    ('Versi', '1.0.0'),
    ('Teknologi', 'Next.js 15.2.3, React 19, TypeScript, Prisma ORM, MySQL'),
    ('Tanggal', '27 November 2024'),
    ('Tester', '_' * 50)
]

for idx, (label, value) in enumerate(info_data):
    row = info_table.rows[idx]
    row.cells[0].text = label
    row.cells[1].text = value
    
    # Bold untuk label
    row.cells[0].paragraphs[0].runs[0].font.bold = True
    
    # Set font size
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(11)

add_table_borders(info_table)

# Spasi
doc.add_paragraph()

# Keterangan
keterangan = doc.add_paragraph()
keterangan_run = keterangan.add_run('Keterangan:')
keterangan_run.font.bold = True
keterangan_run.font.size = Pt(11)

keterangan_text = doc.add_paragraph()
keterangan_text.add_run('Kolom "Valid" dan "Tidak Valid" akan diisi dengan tanda centang (✓) menggunakan pulpen saat melakukan pengujian.')
keterangan_text.paragraph_format.left_indent = Inches(0.25)

for run in keterangan_text.runs:
    run.font.size = Pt(10)

doc.add_paragraph()

# Tabel Test Cases - 7 kolom seperti PDF
table = doc.add_table(rows=2, cols=7)  # 2 rows untuk header dengan merge
table.style = 'Table Grid'
table.autofit = False
table.allow_autofit = False

# Set lebar kolom yang lebih rapi (total ~6.5 inches untuk A4)
table.columns[0].width = Inches(0.3)   # No
table.columns[1].width = Inches(1.0)   # Fitur yang Diuji
table.columns[2].width = Inches(1.0)   # Skenario Pengujian
table.columns[3].width = Inches(1.5)   # Input/Tindakan
table.columns[4].width = Inches(2.0)   # Hasil yang Diharapkan
table.columns[5].width = Inches(0.35)  # Valid
table.columns[6].width = Inches(0.35)  # Tidak Valid

# Header Row 1 - Merge cells untuk kolom yang tidak punya sub-header
header_row1 = table.rows[0].cells
header_row1[0].merge(table.rows[1].cells[0])  # No
header_row1[1].merge(table.rows[1].cells[1])  # Fitur yang Diuji
header_row1[2].merge(table.rows[1].cells[2])  # Skenario Pengujian
header_row1[3].merge(table.rows[1].cells[3])  # Input/Tindakan
header_row1[4].merge(table.rows[1].cells[4])  # Hasil yang Diharapkan

# Merge untuk "Hasil" header (kolom 5-6)
header_row1[5].merge(header_row1[6])

# Set text untuk row 1
header_row1[0].text = 'No'
header_row1[1].text = 'Fitur yang Diuji'
header_row1[2].text = 'Skenario Pengujian'
header_row1[3].text = 'Input/Tindakan'
header_row1[4].text = 'Hasil yang Diharapkan'
header_row1[5].text = 'Hasil'

# Header Row 2 - Sub-headers untuk "Hasil"
header_row2 = table.rows[1].cells
header_row2[5].text = 'Valid'
header_row2[6].text = 'Tidak Valid'

# Format semua header cells
for row_idx in [0, 1]:
    for cell in table.rows[row_idx].cells:
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.bold = True
                run.font.size = Pt(9)
        
        # Background color
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), 'D3D3D3')
        cell._element.get_or_add_tcPr().append(shading)

# Tambahkan data test cases
for test in test_cases:
    row = table.add_row()
    
    cells = row.cells
    cells[0].text = str(test['no'])
    cells[1].text = test['fitur']
    cells[2].text = test['skenario']
    cells[3].text = test['input']
    cells[4].text = test['hasil']
    cells[5].text = ''  # Valid - kosong untuk centang manual
    cells[6].text = ''  # Tidak Valid - kosong untuk centang manual
    
    # Center align nomor dan kolom hasil
    cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cells[6].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Format semua cell dengan font lebih kecil agar rapi
    for idx, cell in enumerate(cells):
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(8)  # Font lebih kecil agar muat
            
            # Set line spacing agar lebih compact
            paragraph.paragraph_format.line_spacing = 1.0
            paragraph.paragraph_format.space_before = Pt(2)
            paragraph.paragraph_format.space_after = Pt(2)

add_table_borders(table)

# Spasi setelah tabel
doc.add_paragraph()
doc.add_paragraph()

# Catatan / Masukan Penguji
catatan_section = doc.add_paragraph()
catatan_run = catatan_section.add_run('Catatan / Masukan Penguji:')
catatan_run.font.bold = True
catatan_run.font.size = Pt(11)

# Garis untuk catatan (3 baris)
for i in range(3):
    catatan_line = doc.add_paragraph()
    catatan_line.add_run('.' * 150)
    catatan_line.paragraph_format.left_indent = Inches(0)

# Spasi
doc.add_paragraph()
doc.add_paragraph()

# Tempat dan Tanggal
from datetime import datetime
today = datetime.now()
tanggal_text = doc.add_paragraph()
tanggal_text.add_run(f'Makassar, {today.day} November {today.year}')
tanggal_text.alignment = WD_ALIGN_PARAGRAPH.RIGHT

penguji_label = doc.add_paragraph()
penguji_label.add_run('Penguji')
penguji_label.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Spasi untuk tanda tangan
doc.add_paragraph()
doc.add_paragraph()
doc.add_paragraph()

# Nama dan NIP Penguji
nama_penguji = doc.add_paragraph()
nama_penguji_run = nama_penguji.add_run('_' * 40)
nama_penguji_run.font.underline = False
nama_penguji.alignment = WD_ALIGN_PARAGRAPH.RIGHT

nip_penguji = doc.add_paragraph()
nip_penguji.add_run('NIP. _________________________')
nip_penguji.alignment = WD_ALIGN_PARAGRAPH.RIGHT

# Simpan dokumen
output_file = 'Lembar_Uji_Blackbox_Vendra_CRM_Final_v3.docx'
doc.save(output_file)
print(f'✅ Dokumen berhasil dibuat: {output_file}')
print(f'📊 Total test cases: {len(test_cases)}')
print(f'🔄 ALUR YANG DIPERBAIKI:')
print(f'   1. Registrasi Owner (FREE tier)')
print(f'   2. Login Owner')
print(f'   3. Upgrade Subscription (BASIC/PREMIUM/ENTERPRISE)')
print(f'   4. SuperAdmin Approval Upgrade')
print(f'   5. Owner Membuat Akun Employee/Kasir')
print(f'   6. Login Kasir')
print(f'   7. Manajemen Produk & Transaksi POS')
print(f'✅ Alur sudah benar untuk user testing dari awal tanpa akun!')

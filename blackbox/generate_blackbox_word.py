"""
Script untuk generate dokumen Black Box Testing dalam format Word (.docx)
Vendra AI CRM - Smart Business Management System

Usage:
    python generate_blackbox_word.py
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime

def add_heading_custom(doc, text, level=1):
    """Add custom styled heading"""
    heading = doc.add_heading(text, level=level)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = heading.runs[0]
    run.font.color.rgb = RGBColor(0, 51, 102)  # Dark blue
    return heading

def create_test_case_table(doc, test_case_data):
    """Create formatted table for test case"""
    table = doc.add_table(rows=len(test_case_data), cols=2)
    table.style = 'Light Grid Accent 1'
    
    for idx, (label, value) in enumerate(test_case_data):
        row = table.rows[idx]
        cell_label = row.cells[0]
        cell_value = row.cells[1]
        
        # Label cell (bold)
        cell_label.text = label
        cell_label_paragraph = cell_label.paragraphs[0]
        cell_label_paragraph.runs[0].font.bold = True
        cell_label_paragraph.runs[0].font.size = Pt(10)
        
        # Value cell
        cell_value.text = value
        cell_value_paragraph = cell_value.paragraphs[0]
        cell_value_paragraph.runs[0].font.size = Pt(10)
    
    return table

def add_checkbox(paragraph, label):
    """Add checkbox to paragraph"""
    run = paragraph.add_run()
    run.add_text('☐ ')
    run.font.size = Pt(11)
    run = paragraph.add_run(label)
    run.font.size = Pt(10)

def generate_blackbox_document():
    """Generate complete Black Box Testing document"""
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # ========== COVER PAGE ==========
    title = doc.add_heading('BLACK BOX TESTING', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    subtitle = doc.add_paragraph('Vendra AI CRM')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].font.size = Pt(18)
    subtitle.runs[0].font.bold = True
    
    subtitle2 = doc.add_paragraph('Smart Business Management System')
    subtitle2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle2.runs[0].font.size = Pt(14)
    
    doc.add_paragraph()  # Spacing
    doc.add_paragraph()
    
    # Testing Info
    info_table = doc.add_table(rows=2, cols=2)
    info_table.style = 'Light List Accent 1'
    
    info_table.rows[0].cells[0].text = 'Tester:'
    info_table.rows[0].cells[1].text = '_' * 40
    info_table.rows[1].cells[0].text = 'Tanggal Testing:'
    info_table.rows[1].cells[1].text = '_' * 40
    
    doc.add_page_break()
    
    # ========== INFORMASI UMUM ==========
    add_heading_custom(doc, 'Informasi Umum Testing', 1)
    
    info_text = [
        ('Produk:', 'Vendra AI CRM - Smart Business Management System'),
        ('Metode Testing:', 'Black Box Testing'),
        ('Tujuan:', 'Menguji fungsionalitas sistem tanpa melihat struktur internal kode'),
    ]
    
    for label, value in info_text:
        p = doc.add_paragraph()
        p.add_run(f'{label} ').bold = True
        p.add_run(value)
    
    doc.add_paragraph()
    
    # ========== METODE TESTING ==========
    add_heading_custom(doc, 'Metode Black Box Testing Yang Digunakan', 1)
    
    methods = [
        ('Equivalence Partitioning (EP)', 'Membagi input menjadi kelompok valid dan invalid'),
        ('Boundary Value Analysis (BVA)', 'Menguji nilai batas minimum, maksimum, dan di luar batas'),
        ('Decision Table Testing', 'Menguji kombinasi kondisi dan aksi'),
        ('State Transition Testing', 'Menguji perubahan state dalam sistem'),
        ('Error Guessing', 'Menguji berdasarkan pengalaman error yang sering terjadi'),
    ]
    
    for idx, (method, desc) in enumerate(methods, 1):
        p = doc.add_paragraph()
        p.add_run(f'{idx}. {method}').bold = True
        doc.add_paragraph(desc, style='List Bullet')
    
    doc.add_page_break()
    
    # ========== TEST CASES ==========
    test_cases = [
        # AUTHENTICATION
        {
            'section': 'TEST CASE 1: AUTHENTICATION & AUTHORIZATION',
            'cases': [
                {
                    'id': 'TC-AUTH-001',
                    'scenario': 'Login dengan Kredensial Valid',
                    'precondition': 'User sudah terdaftar di database',
                    'steps': '1. Buka halaman login\n2. Input email: owner@test.com\n3. Input password: password123\n4. Klik tombol "Login"',
                    'test_data': 'Email: owner@test.com\nPassword: password123',
                    'expected': '✅ Login berhasil\n✅ Redirect ke dashboard\n✅ Session tersimpan',
                },
                {
                    'id': 'TC-AUTH-002',
                    'scenario': 'Login dengan Email Salah',
                    'precondition': '-',
                    'steps': '1. Input email: tidakada@test.com\n2. Input password: password123\n3. Klik "Login"',
                    'test_data': 'Email: tidakada@test.com\nPassword: password123',
                    'expected': '❌ Muncul error "Email tidak ditemukan"\n❌ Login gagal\n❌ Tetap di halaman login',
                },
                {
                    'id': 'TC-AUTH-003',
                    'scenario': 'Login dengan Password Salah',
                    'precondition': '-',
                    'steps': '1. Input email: owner@test.com\n2. Input password: salahpassword\n3. Klik "Login"',
                    'test_data': 'Email: owner@test.com\nPassword: salahpassword',
                    'expected': '❌ Muncul error "Password salah"\n❌ Login gagal',
                },
                {
                    'id': 'TC-AUTH-004',
                    'scenario': 'Login dengan Input Kosong',
                    'precondition': '-',
                    'steps': '1. Biarkan email kosong\n2. Biarkan password kosong\n3. Klik "Login"',
                    'test_data': 'Email: (kosong)\nPassword: (kosong)',
                    'expected': '❌ Muncul validasi "Email wajib diisi"\n❌ Muncul validasi "Password wajib diisi"',
                },
                {
                    'id': 'TC-AUTH-005',
                    'scenario': 'Registrasi User Baru',
                    'precondition': '-',
                    'steps': '1. Buka halaman registrasi\n2. Isi semua field yang required\n3. Klik "Daftar"',
                    'test_data': 'Name: Test Owner\nEmail: newowner@test.com\nPassword: Test123!\nStore Name: Toko Test\nPhone: 081234567890',
                    'expected': '✅ Registrasi berhasil\n✅ User tersimpan di database\n✅ Store otomatis dibuat\n✅ Redirect ke login',
                },
            ]
        },
        # PRODUK
        {
            'section': 'TEST CASE 2: MANAJEMEN PRODUK',
            'cases': [
                {
                    'id': 'TC-PROD-001',
                    'scenario': 'Tambah Produk Valid',
                    'precondition': 'User login sebagai Owner',
                    'steps': '1. Login sebagai Owner\n2. Klik "Manajemen Produk"\n3. Klik "Tambah Produk"\n4. Isi semua field\n5. Klik "Simpan"',
                    'test_data': 'Name: Kopi Arabica\nSKU: KOPI-001\nPrice: 50000\nStock: 100\nCategory: Minuman',
                    'expected': '✅ Produk tersimpan di database\n✅ Muncul di list produk\n✅ Notifikasi sukses muncul',
                },
                {
                    'id': 'TC-PROD-002',
                    'scenario': 'Tambah Produk dengan SKU Duplicate',
                    'precondition': 'Sudah ada produk dengan SKU KOPI-001',
                    'steps': '1. Tambah produk dengan SKU: KOPI-001\n2. Klik "Simpan"',
                    'test_data': 'SKU: KOPI-001',
                    'expected': '❌ Muncul error "SKU sudah digunakan"\n❌ Produk tidak tersimpan',
                },
                {
                    'id': 'TC-PROD-003',
                    'scenario': 'Tambah Produk dengan Harga Negatif (BVA)',
                    'precondition': '-',
                    'steps': '1. Input harga: -10000\n2. Klik "Simpan"',
                    'test_data': 'Price: -10000',
                    'expected': '❌ Validasi error "Harga harus lebih dari 0"\n❌ Produk tidak tersimpan',
                },
            ]
        },
        # POS
        {
            'section': 'TEST CASE 3: TRANSAKSI POS (KASIR)',
            'cases': [
                {
                    'id': 'TC-POS-001',
                    'scenario': 'Transaksi Cash Normal',
                    'precondition': 'User login sebagai Kasir',
                    'steps': '1. Login sebagai Kasir\n2. Tambah produk ke cart (2 item)\n3. Input customer\n4. Pilih payment method: Cash\n5. Klik "Bayar"',
                    'test_data': 'Product 1: Kopi Arabica (Qty: 2)\nProduct 2: Roti Bakar (Qty: 1)\nTotal: Rp 150.000\nPayment: Cash',
                    'expected': '✅ Transaksi tersimpan\n✅ Stock produk berkurang\n✅ Struk/Invoice generate\n✅ Cart kosong kembali',
                },
                {
                    'id': 'TC-POS-002',
                    'scenario': 'Transaksi dengan Diskon',
                    'precondition': '-',
                    'steps': '1. Tambah produk (Total: Rp 100.000)\n2. Apply diskon 10%\n3. Klik "Bayar"',
                    'test_data': 'Total: Rp 100.000\nDiskon: 10%',
                    'expected': '✅ Total menjadi Rp 90.000\n✅ Diskon tercatat di transaksi',
                },
            ]
        },
        # IMPORT CSV
        {
            'section': 'TEST CASE 4: IMPORT DATA CSV',
            'cases': [
                {
                    'id': 'TC-IMPORT-001',
                    'scenario': 'Import CSV Valid',
                    'precondition': '-',
                    'steps': '1. Upload file CSV valid\n2. Preview data\n3. Klik "Import"',
                    'test_data': 'File: transactions.csv (format benar)',
                    'expected': '✅ Data ter-import ke database\n✅ Jumlah data sesuai file CSV\n✅ Notifikasi sukses',
                },
                {
                    'id': 'TC-IMPORT-005',
                    'scenario': 'Import CSV dengan Produk Duplikat',
                    'precondition': '-',
                    'steps': '1. Upload CSV dengan multiple rows produk "Almond Butter"\n2. Klik import',
                    'test_data': 'File CSV dengan produk duplikat (nama sama)',
                    'expected': '✅ Produk dengan nama sama hanya dibuat 1x\n✅ Data lainnya tetap ter-import\n✅ Tidak ada duplikat produk',
                },
            ]
        },
    ]
    
    # Generate test cases
    for test_section in test_cases:
        add_heading_custom(doc, test_section['section'], 1)
        
        for case in test_section['cases']:
            add_heading_custom(doc, f"{case['id']}: {case['scenario']}", 2)
            
            test_data = [
                ('ID', case['id']),
                ('Test Scenario', case['scenario']),
                ('Pre-condition', case['precondition']),
                ('Test Steps', case['steps']),
                ('Test Data', case['test_data']),
                ('Expected Result', case['expected']),
                ('Actual Result', '_' * 50),
            ]
            
            create_test_case_table(doc, test_data)
            
            # Status checkboxes
            p = doc.add_paragraph()
            p.add_run('Status: ').bold = True
            add_checkbox(p, 'Pass    ')
            add_checkbox(p, 'Fail')
            
            doc.add_paragraph()  # Spacing
        
        doc.add_page_break()
    
    # ========== SUMMARY ==========
    add_heading_custom(doc, 'SUMMARY HASIL TESTING', 1)
    
    # Statistics table
    add_heading_custom(doc, 'Statistik Testing', 2)
    
    stats_table = doc.add_table(rows=12, cols=5)
    stats_table.style = 'Light Grid Accent 1'
    
    # Header
    headers = ['Kategori', 'Total Test Case', 'Pass', 'Fail', '% Pass Rate']
    for idx, header in enumerate(headers):
        cell = stats_table.rows[0].cells[idx]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True
    
    # Data rows
    categories = [
        ('Authentication', '7'),
        ('Produk', '8'),
        ('POS/Transaksi', '5'),
        ('Import CSV', '5'),
        ('RFM Analysis', '3'),
        ('AI Assistant', '3'),
        ('Laporan', '3'),
        ('Role & Permission', '3'),
        ('Customer Management', '3'),
        ('Performance & Security', '5'),
        ('TOTAL', '45'),
    ]
    
    for idx, (category, total) in enumerate(categories, 1):
        row = stats_table.rows[idx]
        row.cells[0].text = category
        row.cells[1].text = total
        row.cells[2].text = '___'
        row.cells[3].text = '___'
        row.cells[4].text = '___%'
        
        if category == 'TOTAL':
            for cell in row.cells:
                cell.paragraphs[0].runs[0].font.bold = True
    
    doc.add_paragraph()
    
    # Bugs section
    add_heading_custom(doc, 'Critical Bugs Found', 2)
    for i in range(1, 4):
        doc.add_paragraph(f'{i}. ' + '_' * 70)
    
    add_heading_custom(doc, 'Major Bugs Found', 2)
    for i in range(1, 4):
        doc.add_paragraph(f'{i}. ' + '_' * 70)
    
    add_heading_custom(doc, 'Minor Bugs Found', 2)
    for i in range(1, 3):
        doc.add_paragraph(f'{i}. ' + '_' * 70)
    
    doc.add_paragraph()
    
    add_heading_custom(doc, 'Rekomendasi Perbaikan', 2)
    for i in range(1, 4):
        doc.add_paragraph(f'{i}. ' + '_' * 70)
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    # Signature
    sig_table = doc.add_table(rows=2, cols=2)
    sig_table.rows[0].cells[0].text = 'Tester Signature:'
    sig_table.rows[0].cells[1].text = '_' * 40
    sig_table.rows[1].cells[0].text = 'Date:'
    sig_table.rows[1].cells[1].text = '_' * 40
    
    doc.add_page_break()
    
    # ========== LAMPIRAN ==========
    add_heading_custom(doc, 'LAMPIRAN A: DECISION TABLE', 1)
    add_heading_custom(doc, 'Decision Table: Login Process', 2)
    
    decision_table = doc.add_table(rows=7, cols=6)
    decision_table.style = 'Light Grid Accent 1'
    
    # Headers
    decision_headers = ['Condition', 'TC1', 'TC2', 'TC3', 'TC4', 'TC5']
    for idx, header in enumerate(decision_headers):
        cell = decision_table.rows[0].cells[idx]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True
    
    # Conditions
    decision_data = [
        ['Email Valid', '✅', '❌', '✅', '✅', '❌'],
        ['Password Valid', '✅', '✅', '❌', '✅', '❌'],
        ['User Active', '✅', '✅', '✅', '❌', '✅'],
        ['Action', '', '', '', '', ''],
        ['Login Success', '✅', '❌', '❌', '❌', '❌'],
        ['Show Error', '❌', '✅', '✅', '✅', '✅'],
        ['Redirect Dashboard', '✅', '❌', '❌', '❌', '❌'],
    ]
    
    for row_idx, row_data in enumerate(decision_data, 1):
        for col_idx, cell_data in enumerate(row_data):
            decision_table.rows[row_idx].cells[col_idx].text = cell_data
            if col_idx == 0:
                decision_table.rows[row_idx].cells[col_idx].paragraphs[0].runs[0].font.bold = True
    
    doc.add_paragraph()
    
    # ========== SAVE DOCUMENT ==========
    filename = f'Blackbox_Testing_Vendra_CRM_{datetime.now().strftime("%Y%m%d_%H%M%S")}.docx'
    doc.save(filename)
    
    return filename

if __name__ == '__main__':
    print('=' * 60)
    print('Black Box Testing Document Generator')
    print('Vendra AI CRM - Smart Business Management System')
    print('=' * 60)
    print()
    
    print('🚀 Generating Black Box Testing document...')
    
    try:
        filename = generate_blackbox_document()
        print(f'✅ Document berhasil dibuat: {filename}')
        print()
        print('📄 Dokumen siap digunakan untuk testing!')
        print('📝 Silakan isi kolom "Actual Result" dan "Status" saat melakukan testing')
        
    except Exception as e:
        print(f'❌ Error: {e}')
        print()
        print('💡 Pastikan library python-docx sudah terinstall:')
        print('   pip install python-docx')

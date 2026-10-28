"""
Script untuk generate dokumen Black Box Testing dalam format Word (.docx)
Vendra AI CRM - Smart Business Management System
Format: Lembar Uji Blackbox Sistem Informasi Berbasis Website

Usage:
    python generate_blackbox_vendra.py
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime
import os

def set_cell_border(cell, **kwargs):
    """Set cell borders"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    
    for edge in ('top', 'left', 'bottom', 'right'):
        if edge in kwargs:
            edge_el = OxmlElement(f'w:{edge}')
            edge_el.set(qn('w:val'), 'single')
            edge_el.set(qn('w:sz'), '12')
            edge_el.set(qn('w:space'), '0')
            edge_el.set(qn('w:color'), '000000')
            tcBorders.append(edge_el)
    
    tcPr.append(tcBorders)

def set_cell_shading(cell, fill):
    """Set cell background color"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), fill)
    cell._element.get_or_add_tcPr().append(shading_elm)

def merge_cells_vertically(table, col, start_row, end_row):
    """Merge cells vertically"""
    cell = table.cell(start_row, col)
    for row in range(start_row + 1, end_row + 1):
        cell.merge(table.cell(row, col))

def create_blackbox_document():
    """Create Black Box Testing document"""
    doc = Document()
    
    # Set margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3)
        section.right_margin = Cm(2)
    
    # ===== HEADER / TITLE =====
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title.add_run('LEMBAR UJI BLACKBOX SISTEM INFORMASI BERBASIS WEBSITE\nVENDRA AI CRM - SMART BUSINESS MANAGEMENT SYSTEM')
    title_run.font.size = Pt(14)
    title_run.font.bold = True
    title_run.font.name = 'Times New Roman'
    
    doc.add_paragraph()  # Spacing
    
    # ===== INFORMASI PENGUJI =====
    info = doc.add_paragraph()
    info_run = info.add_run('Nama Penguji\t: A.Balqis Mutiara Asizah')
    info_run.font.size = Pt(12)
    info_run.font.name = 'Times New Roman'
    
    info2 = doc.add_paragraph()
    info2_run = info2.add_run('Profesi\t\t: Mahasiswa / Developer')
    info2_run.font.size = Pt(12)
    info2_run.font.name = 'Times New Roman'
    
    info3 = doc.add_paragraph()
    info3_run = info3.add_run('Alamat Website\t: https://vendra-crm.vercel.app')
    info3_run.font.size = Pt(12)
    info3_run.font.name = 'Times New Roman'
    
    doc.add_paragraph()  # Spacing
    
    # ===== TABEL TEST CASE =====
    # Test cases data
    test_cases = [
        {
            'no': '1',
            'fitur': 'Registrasi & Login',
            'skenario': 'User mengisi Step 1 (Informasi Personal) dengan data lengkap',
            'input': 'Nama Lengkap: "John Doe"\nEmail: "balqismdi00@gmail.com"\nPassword: "Test123!"\nKonfirmasi Password: "Test123!"',
            'hasil': 'Validasi berhasil, tombol "Daftar Sekarang" aktif, berpindah ke Step 2',
            'valid': True
        },
        {
            'no': '2',
            'fitur': 'Registrasi & Login',
            'skenario': 'User mengisi Step 2 (Informasi Perusahaan) untuk paket FREE',
            'input': 'Nama Perusahaan: "PT. Contoh Perusahaan"\nEmail Perusahaan: "info@perusahaan.com"\nNomor Telepon: "+62812345678"\nAlamat: "Jl. Contoh No. 123, Jakarta"',
            'hasil': 'Registrasi berhasil, akun FREE langsung aktif, redirect ke halaman sukses',
            'valid': True
        },
        {
            'no': '3',
            'fitur': 'Registrasi & Login',
            'skenario': 'User input password dan konfirmasi password tidak cocok',
            'input': 'Password: "Test123!"\nKonfirmasi Password: "Test456!"',
            'hasil': 'Muncul error "Password tidak cocok", form tidak bisa submit',
            'valid': False
        },
        {
            'no': '4',
            'fitur': 'Registrasi & Login',
            'skenario': 'User input password kurang dari 6 karakter',
            'input': 'Password: "123"',
            'hasil': 'Muncul error "Password minimal 6 karakter"',
            'valid': False
        },
        {
            'no': '5',
            'fitur': 'Registrasi & Login',
            'skenario': 'User mendaftar dengan email yang sudah terdaftar',
            'input': 'Email: "balqismdi00@gmail.com" (sudah ada di database)',
            'hasil': 'Muncul error "Email sudah terdaftar"',
            'valid': False
        },
        {
            'no': '6',
            'fitur': 'Registrasi & Login',
            'skenario': 'User login dengan email dan password yang benar',
            'input': 'Email: "balqismdi00@gmail.com"\nPassword: "Test123!"',
            'hasil': 'Login berhasil, session tersimpan, redirect ke dashboard sesuai role',
            'valid': True
        },
        {
            'no': '7',
            'fitur': 'Registrasi & Login',
            'skenario': 'User login dengan password yang salah',
            'input': 'Email: "balqismdi00@gmail.com"\nPassword: "salahpassword"',
            'hasil': 'Muncul error "Password salah", login gagal',
            'valid': False
        },
        {
            'no': '8',
            'fitur': 'Registrasi & Login',
            'skenario': 'User login dengan email yang tidak terdaftar',
            'input': 'Email: "tidakada@test.com"',
            'hasil': 'Muncul error "Email tidak ditemukan"',
            'valid': False
        },
        },
        {
            'no': '9',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin menambahkan produk baru dengan data lengkap',
            'input': 'Nama: "Kopi Arabica"\nSKU: "KOPI-001"\nHarga: 50000\nCost: 35000\nStock: 100\nKategori: "Minuman"\nBrand: "Arabica Coffee"',
            'hasil': 'Produk tersimpan di database, muncul di list produk, notifikasi sukses muncul',
            'valid': True
        },
        {
            'no': '10',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin menambahkan produk dengan SKU yang sudah ada',
            'input': 'SKU: "KOPI-001" (sudah ada di database)',
            'hasil': 'Muncul error "SKU sudah digunakan", produk tidak tersimpan',
            'valid': False
        },
        {
            'no': '11',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin input harga produk dengan nilai negatif',
            'input': 'Harga: -10000',
            'hasil': 'Muncul validasi error "Harga harus lebih dari 0", produk tidak tersimpan',
            'valid': False
        },
        {
            'no': '12',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin input stock produk dengan nilai 0',
            'input': 'Stock: 0',
            'hasil': 'Produk tersimpan, status produk berubah menjadi "Out of Stock"',
            'valid': True
        },
        {
            'no': '13',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin mencari produk dengan keyword',
            'input': 'Keyword: "Kopi" di search box',
            'hasil': 'Menampilkan semua produk yang nama/SKU mengandung kata "Kopi"',
            'valid': True
        },
        {
            'no': '14',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin filter produk berdasarkan kategori',
            'input': 'Pilih kategori: "Minuman"',
            'hasil': 'Hanya menampilkan produk dengan kategori "Minuman"',
            'valid': True
        },
        {
            'no': '15',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin edit informasi produk',
            'input': 'Pilih produk, klik Edit, ubah harga dari 50000 → 55000',
            'hasil': 'Produk terupdate di database, harga baru tampil di list produk',
            'valid': True
        },
        {
            'no': '16',
            'fitur': 'Manajemen Produk',
            'skenario': 'Admin hapus produk',
            'input': 'Pilih produk, klik tombol hapus, konfirmasi penghapusan',
            'hasil': 'Produk terhapus dari database, tidak muncul di list, notifikasi sukses',
            'valid': True
        },
            'hasil': 'Produk terhapus dari database, tidak muncul di list',
            'valid': True
        },
        {
            'no': '9',
            'fitur': 'Transaksi POS',
            'skenario': 'Kasir melakukan transaksi pembayaran cash',
            'input': 'Tambah 2 produk, pilih customer, metode: Cash, total: Rp 150.000',
            'hasil': 'Transaksi tersimpan, stock berkurang, struk ter-generate',
            'valid': True
        },
        {
            'no': '10',
            'fitur': 'Transaksi POS',
            'skenario': 'Kasir memberikan diskon pada transaksi',
            'input': 'Total: Rp 100.000, diskon 10%',
            'hasil': 'Total menjadi Rp 90.000, diskon tercatat di database',
            'valid': True
        },
        {
            'no': '11',
            'fitur': 'Transaksi POS',
            'skenario': 'Kasir input qty lebih besar dari stock',
            'input': 'Stock produk: 5, input qty: 10',
            'hasil': 'Muncul error "Stock tidak cukup"',
            'valid': False
        },
        {
            'no': '12',
            'fitur': 'Transaksi POS',
            'skenario': 'Kasir scan barcode produk',
            'input': 'Scan barcode produk',
            'hasil': 'Produk otomatis masuk ke cart dengan qty 1',
            'valid': True
        },
        {
            'no': '13',
            'fitur': 'Import Data CSV',
            'skenario': 'Admin import file CSV dengan format benar',
            'input': 'Upload file CSV valid dengan data transaksi',
            'hasil': 'Data ter-import ke database, jumlah sesuai file CSV',
            'valid': True
        },
        {
            'no': '14',
            'fitur': 'Import Data CSV',
            'skenario': 'Admin upload file CSV dengan kolom tidak sesuai',
            'input': 'Upload CSV dengan format kolom berbeda',
            'hasil': 'Muncul error "Format file salah"',
            'valid': False
        },
        {
            'no': '15',
            'fitur': 'Import Data CSV',
            'skenario': 'Admin upload file selain CSV',
            'input': 'Upload file .xlsx atau .pdf',
            'hasil': 'Validasi "File harus format CSV"',
            'valid': False
        },
        {
            'no': '16',
            'fitur': 'Import Data CSV',
            'skenario': 'Import CSV dengan produk nama duplikat',
            'input': 'CSV berisi multiple rows produk "Almond Butter"',
            'hasil': 'Produk dengan nama sama hanya dibuat 1x, tidak ada duplikat',
            'valid': True
        },
        {
            'no': '17',
            'fitur': 'Analisis RFM',
            'skenario': 'Owner melihat dashboard RFM Analysis',
            'input': 'Klik menu "RFM Analysis"',
            'hasil': 'Dashboard tampil dengan chart dan segmentasi customer',
            'valid': True
        },
        {
            'no': '18',
            'fitur': 'Analisis RFM',
            'skenario': 'Owner filter customer berdasarkan segment',
            'input': 'Pilih segment "Champions"',
            'hasil': 'Hanya tampil customer dengan segment Champions',
            'valid': True
        },
        {
            'no': '19',
            'fitur': 'Analisis RFM',
            'skenario': 'Owner export data RFM',
            'input': 'Klik "Export Data", pilih format Excel',
            'hasil': 'File Excel berhasil didownload dengan data sesuai',
            'valid': True
        },
        {
            'no': '20',
            'fitur': 'AI Assistant',
            'skenario': 'User bertanya tentang performa sales',
            'input': 'Tanya: "Bagaimana performa penjualan bulan ini?"',
            'hasil': 'AI merespons < 5 detik dengan jawaban relevan dan statistik',
            'valid': True
        },
        {
            'no': '21',
            'fitur': 'AI Assistant',
            'skenario': 'User minta rekomendasi produk restock',
            'input': 'Tanya: "Produk apa yang perlu di-restock?"',
            'hasil': 'AI memberi list produk dengan stock rendah',
            'valid': True
        },
        {
            'no': '22',
            'fitur': 'Laporan Penjualan',
            'skenario': 'Owner generate laporan harian',
            'input': 'Pilih filter "Hari Ini"',
            'hasil': 'Report tampil dengan data hari ini, total penjualan benar',
            'valid': True
        },
        {
            'no': '23',
            'fitur': 'Laporan Penjualan',
            'skenario': 'Owner export laporan ke Excel',
            'input': 'Klik "Export Excel"',
            'hasil': 'File Excel terdownload dengan format rapi',
            'valid': True
        },
        {
            'no': '24',
            'fitur': 'Laporan Penjualan',
            'skenario': 'Owner filter laporan by date range',
            'input': 'Start: 01-11-2025, End: 27-11-2025',
            'hasil': 'Hanya data dalam range tersebut yang tampil',
            'valid': True
        },
        {
            'no': '25',
            'fitur': 'Role & Permission',
            'skenario': 'Owner akses semua menu',
            'input': 'Login sebagai Owner, akses Dashboard, Produk, RFM, Settings',
            'hasil': 'Semua menu dapat diakses tanpa restriction',
            'valid': True
        },
        {
            'no': '26',
            'fitur': 'Role & Permission',
            'skenario': 'Kasir coba akses menu restricted',
            'input': 'Login sebagai Cashier, coba akses Settings/RFM',
            'hasil': 'Tidak dapat akses, redirect atau error 403',
            'valid': False
        },
        {
            'no': '27',
            'fitur': 'Role & Permission',
            'skenario': 'SuperAdmin approve pending owner',
            'input': 'Login SuperAdmin, klik "Approve" pada pending owner',
            'hasil': 'Status owner berubah jadi ACTIVE, owner bisa login',
            'valid': True
        },
        {
            'no': '28',
            'fitur': 'Manajemen Customer',
            'skenario': 'Admin tambah customer baru',
            'input': 'Nama: "John Doe", Phone: "081234567890", Member: Yes',
            'hasil': 'Customer tersimpan, unique ID ter-generate',
            'valid': True
        },
        {
            'no': '29',
            'fitur': 'Manajemen Customer',
            'skenario': 'Admin edit data customer',
            'input': 'Edit phone number customer',
            'hasil': 'Data customer terupdate di database',
            'valid': True
        },
        {
            'no': '30',
            'fitur': 'Manajemen Customer',
            'skenario': 'Admin hapus customer',
            'input': 'Klik hapus, konfirmasi penghapusan',
            'hasil': 'Customer terhapus dari database',
            'valid': True
        },
        {
            'no': '31',
            'fitur': 'Performance',
            'skenario': 'Mengukur kecepatan loading homepage',
            'input': 'Clear cache, akses homepage',
            'hasil': 'Loading time < 3 detik',
            'valid': True
        },
        {
            'no': '32',
            'fitur': 'Performance',
            'skenario': 'Mengukur kecepatan loading dashboard',
            'input': 'Login, catat waktu loading dashboard',
            'hasil': 'Loading time < 2 detik',
            'valid': True
        },
        {
            'no': '33',
            'fitur': 'Security',
            'skenario': 'Akses halaman protected tanpa login',
            'input': 'Logout, akses URL /admin/products',
            'hasil': 'Redirect ke halaman login, tidak dapat akses',
            'valid': False
        },
        {
            'no': '34',
            'fitur': 'Security',
            'skenario': 'Test SQL Injection',
            'input': 'Input di search: \' OR 1=1--',
            'hasil': 'Tidak ada error SQL, input di-sanitize',
            'valid': False
        },
        {
            'no': '35',
            'fitur': 'Security',
            'skenario': 'Test XSS Attack',
            'input': 'Input: <script>alert(\'XSS\')</script>',
            'hasil': 'Script tidak dieksekusi, input di-escape',
            'valid': False
        },
    ]
    
    # Create table with headers
    table = doc.add_table(rows=1, cols=7)
    table.style = 'Table Grid'
    
    # Header row
    header_cells = table.rows[0].cells
    headers = ['No', 'Fitur yang\nDiuji', 'Skenario\nPengujian', 'Input /\nTindakan', 'Hasil yang\nDiharapkan', 'Hasil', '']
    
    for idx, header_text in enumerate(headers[:-1]):
        cell = header_cells[idx]
        cell.text = header_text
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(10)
        cell.paragraphs[0].runs[0].font.name = 'Times New Roman'
        set_cell_shading(cell, 'D9D9D9')
        set_cell_border(cell, top={}, bottom={}, left={}, right={})
    
    # Merge cells for "Hasil" column (Valid/Tidak Valid)
    header_cells[5].text = 'Hasil'
    header_cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_cells[5].paragraphs[0].runs[0].font.bold = True
    header_cells[5].paragraphs[0].runs[0].font.size = Pt(10)
    header_cells[5].paragraphs[0].runs[0].font.name = 'Times New Roman'
    set_cell_shading(header_cells[5], 'D9D9D9')
    set_cell_border(header_cells[5], top={}, bottom={}, left={}, right={})
    
    header_cells[6].text = ''
    set_cell_shading(header_cells[6], 'D9D9D9')
    set_cell_border(header_cells[6], top={}, bottom={}, left={}, right={})
    
    # Sub-header row for Valid/Tidak Valid
    subheader_row = table.add_row()
    for i in range(5):
        subheader_row.cells[i].text = ''
        set_cell_shading(subheader_row.cells[i], 'D9D9D9')
        set_cell_border(subheader_row.cells[i], top={}, bottom={}, left={}, right={})
    
    subheader_row.cells[5].text = 'Valid'
    subheader_row.cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    subheader_row.cells[5].paragraphs[0].runs[0].font.bold = True
    subheader_row.cells[5].paragraphs[0].runs[0].font.size = Pt(9)
    subheader_row.cells[5].paragraphs[0].runs[0].font.name = 'Times New Roman'
    set_cell_shading(subheader_row.cells[5], 'D9D9D9')
    set_cell_border(subheader_row.cells[5], top={}, bottom={}, left={}, right={})
    
    subheader_row.cells[6].text = 'Tidak\nValid'
    subheader_row.cells[6].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    subheader_row.cells[6].paragraphs[0].runs[0].font.bold = True
    subheader_row.cells[6].paragraphs[0].runs[0].font.size = Pt(9)
    subheader_row.cells[6].paragraphs[0].runs[0].font.name = 'Times New Roman'
    set_cell_shading(subheader_row.cells[6], 'D9D9D9')
    set_cell_border(subheader_row.cells[6], top={}, bottom={}, left={}, right={})
    
    # Add test cases
    for tc in test_cases:
        row = table.add_row()
        
        # No
        row.cells[0].text = tc['no']
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[0].paragraphs[0].runs[0].font.size = Pt(10)
        row.cells[0].paragraphs[0].runs[0].font.name = 'Times New Roman'
        
        # Fitur yang Diuji
        row.cells[1].text = tc['fitur']
        row.cells[1].paragraphs[0].runs[0].font.size = Pt(10)
        row.cells[1].paragraphs[0].runs[0].font.name = 'Times New Roman'
        
        # Skenario Pengujian
        row.cells[2].text = tc['skenario']
        row.cells[2].paragraphs[0].runs[0].font.size = Pt(10)
        row.cells[2].paragraphs[0].runs[0].font.name = 'Times New Roman'
        
        # Input / Tindakan
        row.cells[3].text = tc['input']
        row.cells[3].paragraphs[0].runs[0].font.size = Pt(9)
        row.cells[3].paragraphs[0].runs[0].font.name = 'Times New Roman'
        
        # Hasil yang Diharapkan
        row.cells[4].text = tc['hasil']
        row.cells[4].paragraphs[0].runs[0].font.size = Pt(9)
        row.cells[4].paragraphs[0].runs[0].font.name = 'Times New Roman'
        
        # Valid checkbox
        if tc['valid']:
            row.cells[5].text = '✓'
        else:
            row.cells[5].text = ''
        row.cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[5].paragraphs[0].runs[0].font.size = Pt(14)
        
        # Tidak Valid checkbox
        if not tc['valid']:
            row.cells[6].text = '✓'
        else:
            row.cells[6].text = ''
        row.cells[6].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[6].paragraphs[0].runs[0].font.size = Pt(14)
        
        # Set borders for all cells
        for cell in row.cells:
            set_cell_border(cell, top={}, bottom={}, left={}, right={})
    
    # Set column widths
    table.columns[0].width = Cm(1)    # No
    table.columns[1].width = Cm(3)    # Fitur
    table.columns[2].width = Cm(4)    # Skenario
    table.columns[3].width = Cm(3.5)  # Input
    table.columns[4].width = Cm(4)    # Hasil Diharapkan
    table.columns[5].width = Cm(1.5)  # Valid
    table.columns[6].width = Cm(1.5)  # Tidak Valid
    
    # Merge header cells for "No" column
    merge_cells_vertically(table, 0, 0, 1)
    merge_cells_vertically(table, 1, 0, 1)
    merge_cells_vertically(table, 2, 0, 1)
    merge_cells_vertically(table, 3, 0, 1)
    merge_cells_vertically(table, 4, 0, 1)
    
    doc.add_page_break()
    
    # ===== HALAMAN 2: CATATAN & TANDA TANGAN =====
    catatan = doc.add_paragraph()
    catatan_run = catatan.add_run('Catatan / Masukan Penguji:')
    catatan_run.font.size = Pt(12)
    catatan_run.font.bold = True
    catatan_run.font.name = 'Times New Roman'
    
    for i in range(3):
        doc.add_paragraph('.' * 100)
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    # Tanda tangan
    ttd = doc.add_paragraph()
    ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    ttd_run = ttd.add_run(f'Makassar, {datetime.now().strftime("%d %B %Y")}\nPenguji')
    ttd_run.font.size = Pt(12)
    ttd_run.font.name = 'Times New Roman'
    
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    nama_ttd = doc.add_paragraph()
    nama_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    nama_ttd_run = nama_ttd.add_run('A.Balqis Mutiara Asizah\nNIM: 220907502036')
    nama_ttd_run.font.size = Pt(12)
    nama_ttd_run.font.name = 'Times New Roman'
    nama_ttd_run.font.underline = True
    
    return doc

def main():
    """Main function"""
    print("=" * 60)
    print("BLACK BOX TESTING DOCUMENT GENERATOR")
    print("Vendra AI CRM - Smart Business Management System")
    print("=" * 60)
    print()
    
    try:
        print("📝 Generating document...")
        doc = create_blackbox_document()
        
        # Save document
        output_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(output_dir, 'Lembar_Uji_Blackbox_Vendra_CRM.docx')
        
        doc.save(output_file)
        
        print(f"✅ Document berhasil dibuat!")
        print(f"📄 Lokasi file: {output_file}")
        print()
        print("📊 Ringkasan:")
        print("   - Total Test Case: 35")
        print("   - Format: Lembar Uji Blackbox")
        print("   - Kategori: 10 fitur utama")
        print()
        print("✨ Dokumen siap digunakan untuk pengujian!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, GOV_LEGAL, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from utils.fungsi.pdf_function import *
from reportlab.platypus import (Paragraph,Frame, Table, TableStyle)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import sys



class TemplateRapor:
    def __init__(self, parent=None, papersize=A4, data=None):
        self.papersize = papersize
        self.width, self.height = self.papersize
        # self.width = self.width
        # self.height = self.height
        self.w_center = self.width/2
        self.logo_persis = "resources/images/logo mi.jpg"
        self.logo_kemenag = "resources/images/logo kemenag.jpg"
        self.data = data

    def create_rapor(self):
        buffer = BytesIO()
        self.c = canvas.Canvas(buffer, A4)
        for index, row_data in enumerate(self.data):
            cleaned_data = format_cell_data(row_data)
            self.cover(cleaned_data)
        self.c.save()
        content = buffer.getvalue()
        buffer.close()
        return content

    def cover(self, data):
        tengah = self.w_center/mm - 20
        teks1 = "KEMENTERIAN AGAMA REPUBLIK INDONESIA"
        teks2 = "LAPORAN HASIL BELAJAR"
        teks3 = "MADRASAH IBTIDAIYAH"
        teks4 = "(MI)"
        nama_lengkap = data['nama_lengkap'] if data else 'NAMA LENGKAP'
        nis_lokal = data['nis_lokal'] if data else 'NIS LOKAL'
        nis_kemenag = data['nis_kemenag'] if data else 'NIS KEMENAG'
        nisn = data['nisn'] if data else 'NISN'
        nama = Paragraph(f"<para font face='Aptos Bold' size=14 leading=20>{nama_lengkap}</para>")
        nis = f"{nis_lokal} / {nis_kemenag}"
        nisn = f"{nisn}"
        teks5 = "MIS PERSIS RAHAYU"
        teks6 = "KABUPATEN BANDUNG"
        teks7 = "PROVINSI JAWA BARAT"
        data_tabel = [
            ["Nama Lengkap",    ":",    nama],
            ["NIS Madrasah",    ":",    nis],
            ["NISN",            ":",    nisn],
        ]
        style_tabel = TableStyle(
            [
                ("FONTNAME", (0, 0), (1, -1), "Aptos"),
                ("FONTNAME", (2, 0), (2, -1), "Aptos Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 14),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 12),
            ]
        )
        gambar(self.c, self.height, self.logo_kemenag, x=tengah, y=60, h=40)

        paragraf(self.c, self.height, teks1, x=20, y=80, w=170, h=9, size=14)
        paragraf(self.c, self.height, teks2, x=20, y=90, w=170, h=10, size=18)
        paragraf(self.c, self.height, teks3, x=20, y=100, w=170, h=10, size=18)
        paragraf(self.c, self.height, teks4, x=20, y=110, w=170, h=10, size=20)

        gambar(self.c, self.height, self.logo_persis, tengah, 165, 40)
        tabel(self.c, self.width, self.height, x= 30, y=180, data=data_tabel, col_width=[45*mm, 5*mm, 110*mm], styles=style_tabel)

        paragraf(self.c, self.height, teks5, x=20, y=257, w=170, h=9, size=18)
        paragraf(self.c, self.height, teks6, x=20, y=264, w=170, h=8, size=14)
        paragraf(self.c, self.height, teks7, x=20, y=271, w=170, h=8, size=14)
        self.c.showPage()


    def halaman_identitas_siswa(self, data):
        self.kop_madrasah()
        teks = "IDENTITAS PESERTA DIDIK"
        ttd_kamad = "resources/images/ttd_kamad.png"
        alamat = Paragraph(f"<para font face='Aptos' size=11 leading=16>{data['alamat_full']}</para>")
        if data['ayah_telp'] == '':
            telp_ayah = ''
        else:
            telp_ayah = data['ayah_telp']
        if data['ibu_telp'] == '':
            telp_ibu = ''
        else:
            if data['ayah_telp'] == '':
                telp_ibu = f"{data['ibu_telp']}"
            else:
                telp_ibu = f" / {data['ibu_telp']}"
        no_telp_ortu = f"{telp_ayah}{telp_ibu}"
        data1 = [
            ["Nama Peserta Didik",          ":",        f"{data['nama_lengkap']}"],
            ["NIS",                         ":",        f"{data['nis_lokal']}"],
            ["NISN",                        ":",        f"{data['nisn']}"],
            ["Tempat Tanggal Lahir",        ":",        f"{data['tmp_lahir']}, {data['tgl_lahir']}"],
            ["Jenis Kelamin",               ":",        f"{'Laki-laki' if data['jk']=='L' else 'Perempuan'}"],
            ["Agama",                       ":",        f"{data['agama']}"],
            ["Status Dalam Keluarga",       ":",        "Anak Kandung"],
            ["Anak Ke",                     ":",        f"{data['anak_ke']}"],
            ["Alamat Peserta Didik",        ":",        alamat],
            ["Nomor Telepon Rumah/HP",      ":",        no_telp_ortu],
            ["Sekolah Asal",                ":",        f"{data['nama_sekolah_asal']}"],
            ["Diterima di sekolah ini",     "",         ""],
            ["       a. Di Kelas",          ":",        f"{data['kls_masuk']}"],
            ["       b. Pada tanggal",      ":",        f"{data['tgl_masuk']}"],
            ["Nama Orang Tua",              "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_nama']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_nama']}"],
            ["Alamat Orang Tua",            ":",        alamat],
            ["Pekerjaan Orang Tua",         "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_pekerjaan']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_pekerjaan']}"]
        ]
        titimangsa = f"Bandung, {data['tgl_masuk']}"
        data2 = [
            [titimangsa],
            ["Kepala Madrasah"],
            [""],
            [""],
            [""],
            ["Ahmad Buldani, S.Ag., M.I.Kom"],
        ]

        style1 = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                    ("ALIGN", (0, 0), (-1, 1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                    
                    ("FONTSIZE", (0, 0), (-1, -1), 11),
                    ("VALIGN", (0, 1), (-1, -1), "TOP"),
                    ])
        style2 = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                    ("FONTNAME", (0, -1), (-1, -1), "Aptos Bold"),
                    ("SIZE", (0,0), (-1,-1), 11)])
        
        paragraf(teks, x = self.width/2/mm-50, y=60, w= 100, h=8, font='Aptos Bold', size=16)
        tabel(20, 65 , data1, (50*mm, 5*mm, 115*mm), None, style1)
        self.c.setLineWidth(1)
        self.c.rect(77*mm, 30*mm, 30*mm, 40*mm)
        gambar(ttd_kamad, 110, 263, 14)
        tabel(120, 228, data2,[70*mm], None, styles=style2)
        self.c.showPage()

    
    def kop_madrasah(self, margin_top=20, margin_left=20):
        margin_top = margin_top * mm
        margin_left = margin_left * mm
        # isi
        logo_kemenag = "resources/images/logo kemenag.jpg"
        logo_persis = "resources/images/logo mi.jpg"
        teks1 = "KEMENTERIAN AGAMA REPUBLIK INDONESIA"
        teks2 = "MIS PERSIS RAHAYU"
        teks3 = "Jl. Mahmud No. 271 Kp. Curug RT 04 RW 08 Ds. Rahayu"
        teks4 = "Kec. Margasasih Kab. Bandung - Jawa Barat"

        # posisi
        gambar(logo_kemenag, 20, 38, 24)
        gambar(logo_persis, 170, 38, 24)
        paragraf(teks1, self.w_center/mm-57.5, 18, 120, 6, size= 14)
        paragraf(teks2, self.w_center/mm-57.5, 28, 120, 10, size=24)
        paragraf(teks3, self.w_center/mm-57.5, 35, 120, 6, size=11, font='TNRI')
        paragraf(teks4, self.w_center/mm-57.5, 40, 120, 6, size=11, font='TNRI')
        self.c.setLineWidth(2)
        self.c.line(x1=20*mm, y1=self.height-42*mm, x2=195*mm, y2=self.height - 42*mm)
    

    def identitas(self, data):
        style1 = TableStyle([
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
            ("FONTNAME", (2, 0), (2, 0), "Aptos Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 6),
            ("LINEBELOW", (0, -1), (-1, -1), 2, colors.black),
        ])
        data_tabel = [
            ["Nama", ":", data["nama_singkat"], "Madrasah", ": ", "MIS Persis Rahayu"],
            ["NIS", ":", data["nis_lokal"], "Kelas/Semester",": ", f"{data['kelas']}/{self.data_header['semester']}"],
            ["NISN", ":", data["nisn"], "Tahun Pelajaran",": ", data['tapel']],
        ]
        tabel(20, 42, data_tabel, [15 * mm, 4 * mm, 80 * mm, 32 * mm,4*mm, 40 * mm],None,  style1)
        
    def identitas_md(self, data):
        logo = "resources/images/logo_persis.png"
        style1 = TableStyle([
            ("LINEABOVE", (0, 0), (-1, 0), 2, colors.black),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
            ("FONTNAME", (3, 0), (3, 0), "Aptos Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("BOTTOMPADDING", (0, -1), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 6),
            ("LINEBELOW", (0, -1), (-1, -1), 2, colors.black),
        ])
        data_tabel = [
            ["", "Nama", ":", data["nama_singkat"], "Madrasah", ": ", "MD Persis Rahayu"],
            ["", "NIS", ":", data["nis_lokal"], "Semester",": ", f"{self.data_header['semester']}"],
            ["", "Kelas", ":", data['kelas'], "Tahun Pelajaran",": ", data['tapel']],
        ]
        gambar(logo, 20, 32, 18)
        tabel(20, 12, data_tabel, [22*mm, 15 * mm, 2 * mm, 67 * mm, 30 * mm, 2*mm, 37 * mm],None,  style1)
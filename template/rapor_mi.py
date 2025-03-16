from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, GOV_LEGAL, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from io import BytesIO
from utils.fungsi.general_functions import *
from reportlab.platypus import (Paragraph,TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from models.nilai.cetak_rapor import CetakRapor
import string

class TemplateRapor:
    def __init__(self, parent=None, papersize=A4, data=None):
        self.parent = parent
        self.papersize = papersize
        self.width, self.height = self.papersize
        self.w_center = self.width/2
        self.logo_persis = "resources/images/logo mi.jpg"
        self.logo_kemenag = "resources/images/logo kemenag.jpg"
        self.SQL = CetakRapor()
        self.data_rapor = data['data_rapor']
        self.setting = data['setting']
        self.ttd_mudir = f'{value_from_db("DOKUMEN_PATH")}/guru/{self.data_rapor[0]['ttd_mudir']}'
        if self.data_rapor[0]['ttd_walas'] not in ['', None] and self.setting['show_ttd_walas']:
            self.ttd_walikelas = f'{value_from_db("DOKUMEN_PATH")}/guru/{self.data_rapor[0]["ttd_walas"]}'
        else:
            self.ttd_walikelas = 'resources/images/no_ttd.png'

    def create_rapor(self):
        buffer = BytesIO()
        self.c = canvas.Canvas(buffer, A4)
        for row_data in self.data_rapor:
            cleaned_data = format_cell_data(row_data)
            id_kelas = cleaned_data['id_kelas']
            id_kegiatan = cleaned_data['id_kegiatan']
            nis_lokal = cleaned_data['nis_lokal']
            data_nilai = format_cell_data(self.SQL.data_nilai(id_kelas, id_kegiatan, nis_lokal))
            if self.parent.opsi_cover.isChecked():
                self.cover(cleaned_data)
            if self.parent.opsi_id_madrasah.isChecked():
                self.identitas_madrasah()
            if self.parent.opsi_id_siswa.isChecked():
                self.identitas_siswa(cleaned_data)
            if self.parent.opsi_nilai.isChecked():
                self.halaman_nilai(cleaned_data, data_nilai)
            if self.parent.opsi_catatan.isChecked():
                self.halaman_catatan(cleaned_data)
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
        gambar(self, self.logo_kemenag, x=tengah, y=60, h=40)

        paragraf(self, teks1, x=20, y=80, w=170, h=9, size=14)
        paragraf(self,teks2, x=20, y=90, w=170, h=10, size=18)
        paragraf(self, teks3, x=20, y=100, w=170, h=10, size=18)
        paragraf(self,teks4, x=20, y=110, w=170, h=10, size=20)

        gambar(self, self.logo_persis, tengah, 165, 40)
        tabel(self, x= 30, y=180, data=data_tabel, col_width=[45*mm, 5*mm, 110*mm], styles=style_tabel)

        paragraf(self, teks5, x=20, y=257, w=170, h=9, size=18)
        paragraf(self,  teks6, x=20, y=264, w=170, h=8, size=14)
        paragraf(self, teks7, x=20, y=271, w=170, h=8, size=14)
        self.c.showPage()


    def identitas_siswa(self, data):
        self.kop_madrasah()
        teks = "IDENTITAS PESERTA DIDIK"
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
        titimangsa = f"Bandung, {date_to_text(data['tgl_masuk'],'lengkap')}"
        data2 = [
            [titimangsa],
            ["Kepala Madrasah"],
            [""],
            [""],
            [data['mudir']],
        ]

        style1 = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                    ("ALIGN", (0, 0), (-1, 1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                    
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("VALIGN", (0, 1), (-1, -1), "TOP"),
                    ])
        style2 = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                    ("FONTNAME", (0, -1), (-1, -1), "Aptos Bold"),
                    ("FONTSIZE", (0,0), (-1,-1), 10)])
        
        paragraf(self, teks, x = self.width/2/mm-50, y=60, w= 100, h=8, font='Aptos Bold', size=16)
        tabel(self, 20, 65 , data1, (50*mm, 5*mm, 115*mm), 8, style1)
        self.c.setLineWidth(1)
        self.c.rect(77*mm, 30*mm, 30*mm, 40*mm)
        tabel(self, 120, 228, data2,[70*mm], self.setting['tinggi_baris']*10, styles=style2)
        gambar(self, self.ttd_mudir, 143 + self.setting['x_mudir']*10, 258 + self.setting['y_mudir']*10, self.setting['size_mudir']*10)
        
        self.c.showPage()


# HALAMAN NILAI
    def halaman_nilai(self, data_siswa, data_nilai_db):
        setting = self.setting
        teks = "CAPAIAN HASIL BELAJAR"
        
        # Tentukan tanda tangan wali kelas

        
        # Tentukan peringkat berdasarkan radio button
        if self.setting['10_besar']:
            if data_siswa['ranking'] != '':
                if int(data_siswa['ranking']) <= 10:
                    ranking = data_siswa['ranking']
                else:
                    ranking = ""
            else:
                ranking = ""
        else:
            if data_siswa['ranking'] != "":
                ranking = data_siswa['ranking']
            else:
                ranking = ''
        
        # Bangun data_nilai secara dinamis dari data_nilai_db (list of dicts)
        data_nilai = [["#", "MATA PELAJARAN", "NILAI\nAKHIR", "TERBILANG"]]  # Header
        
        # Tambahkan baris untuk setiap mata pelajaran
        for i, item in enumerate(data_nilai_db, start=1):
            mata_pelajaran = Paragraph(f"""
                    <para  alignment='LEFT' leading=10>
                    <font name='Aptos' size='11'>{item['mata_pelajaran']}</font><br/>
                    <font name='Aptos Italic' size='8'>Guru: {string.capwords(item['nama_guru'])}</font>
                    </para>
            """)
            # Paragraph(f"<para font size 10>{item['mata_pelajaran']}</para>") if item['mata_pelajaran'] else item['mapel']
            nilai = item['nilai']
            data_nilai.append([str(i), mata_pelajaran, str(nilai), angka_ke_teks(nilai)])
        
        # Hitung jumlah dan rata-rata
        total_nilai = sum(float(item['nilai']) for item in data_nilai_db)
        rata_rata = round(total_nilai / len(data_nilai_db), 2) if data_nilai_db else 0
        teks_rt = Paragraph(f"<para font='Aptos Italic' size=11 alignment='LEFT' leading=12>{angka_ke_teks(rata_rata)}</para>")
        
        # Tambahkan baris untuk Jumlah, Rata-Rata, dan Peringkat
        data_nilai.append(["Jumlah", "", str(total_nilai), angka_ke_teks(total_nilai)])
        data_nilai.append(["Rata-Rata", "", str(rata_rata), teks_rt])
        data_nilai.append(["Peringkat", "", str(ranking), terbilang_peringkat(ranking)])
        
        # Data untuk tabel tanda tangan
        data_tabel_ttd = [
            ["Mengetahui", "", f"Bandung, {date_to_text(data_siswa['tgl_titimangsa'], 'lengkap')}"],
            ["Kepala Madrasah", "", "Wali Kelas"],
            ["", ""],
            ["", ""],
            ["", ""],
            [data_siswa['mudir'], "", data_siswa['walas']],
        ]
        
        # Style untuk tabel nilai
        style1 = TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),
                # ("TOPPADDING", (0, 0), (-1, 0), 0),
                # ("BOTTOMPADDING", (1, 1), (1, -3), 20),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (1, 1), (1, -1), "LEFT"),
                ("ALIGN", (-1, 1), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 1), (-1, -1), "Aptos"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("LINEABOVE", (0, 0), (-1, 0), 1.5, colors.black),
                ("LINEBELOW", (0, 0), (-1, 0), 1.5, colors.black),
                ("LINEABOVE", (0, -3), (-1, -3), 1.5, colors.black),
                ("LINEBELOW", (0, -1), (-1, -1), 1.5, colors.black),
                ("SPAN", (0, -3), (1, -3)),
                ("SPAN", (0, -2), (1, -2)),
                ("SPAN", (0, -1), (1, -1)),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
                ("TOPPADDING", (0, 1), (-1, -1), 2),
                ("ALIGN", (0, -3), (1, -1), "LEFT"),
                ("FONTNAME", (0, -3), (-1, -1), "Aptos Bold"),
                ("FONTNAME", (2, 0), (2, -1), "Aptos Bold"),
                ("FONTNAME", (-1, 1), (-1, -1), "Aptos Italic"),
            ]
        )
        
        # Style untuk tabel tanda tangan
        style2 = TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 1), "Aptos"),
                ("FONTNAME", (0, -1), (-1, -1), "Aptos Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BOTTOMPADDING", (0, 2), (-1, 2), 0),
                ("TOPPADDING", (0, 2), (-1, 2), 0),
            ]
        )
        self.kop_madrasah()
        self.identitas(data_siswa)
        paragraf(self, teks, x=self.width/2/mm-50, y=83, w=100, h=8, font='Aptos Bold', size=16)
        tinggi_tabel = tabel(self, 20, 85, data_nilai, [10 * mm, 85 * mm, 15 * mm, 65*mm], 
                            #  self.setting['tinggi_baris']*10
                            None
                             , style1)
        gambar(self, self.ttd_mudir, 50+setting['x_mudir']*10, tinggi_tabel/mm + 133 + setting['y_mudir']*10, setting['size_mudir']*10)
        gambar(self, self.ttd_walikelas, 155+setting['x_walas']*10, tinggi_tabel/mm + 133 + setting['y_walas']*10, setting['size_walas']*10)
        tabel(self, 30, tinggi_tabel/mm+100, data_tabel_ttd, [60 * mm, 37 * mm, 60 * mm], None, style2)
        self.c.showPage()
        
    def halaman_catatan(self, data):
        setting = self.setting
        self.kop_madrasah()
        self.identitas(data)
        teks1 = "Ekstrakurikuler"
        teks2 = "Ketidakhadiran"
        teks3 = "Catatan Wali Kelas"
        teks4 = "Tanggapan Orang Tua/Wali"
        teks5 = "Status Kenaikan Kelas"
        size_catatan = self.setting['ukuran_catatan']
        jarak_baris = self.setting['jarak_catatan']
        teks_catatan = Paragraph(
            f"""<para 
                font face='Aptos Narrow Italic' 
                size={size_catatan} leading={jarak_baris} 
                alignment='justify'>{data['catatan_walas']}
                </para>
            """)
        catatan_wali_kelas = [[teks_catatan]]
        data_ekskul = [
            ["#", "Kegiatan Ekstrakurikuler", "Nilai", "Keterangan"],
            ["1", "", "", ""],
            ["2", "", "", ""],
        ]
        data_absensi = [
            ["Sakit", f"   -    Hari" if data["sakit"] == "" else f"   {data['sakit']}   Hari"],
            ["Izin", f"   -    Hari" if data["ijin"] == "" else f"   {data['ijin']}   Hari"],
            ["Alpa", f"   -    Hari" if data["alpa"] == "" else f"   {data['alpa']}   Hari"],
        ]
        # data_kenaikan = [
        #     [f"{data['status_naik']}"],
        # ]
        data_tabel_ttd = [
            ["", "", f"Bandung, {date_to_text(data['tgl_titimangsa'], "lengkap")}"],
            ["Orang Tua/Wali", "", "Wali Kelas"],
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
            ["_________________", "", data['walas']],
            ["", "Mengetahui", ""],
            ["", "Kepala Madrasah", ""],
            ["", "", ""],
            ["", "", ""],
     
            ["", data['mudir'], ""],
        ]
        style_ekstra =TableStyle(
            [   
            ("TOPPADDING", (0, 0), (-1, 0), 3),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Aptos"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ])
        style_kehadiran = TableStyle(
            
            [   ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ])
        style_kenaikan = TableStyle(
            [("GRID", (0, 0), (-1, -1), 0.5, colors.black),
             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
             ("FONTNAME", (0, 0), (-1, -1), "Aptos Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 18),
            ("TOPPADDING", (0, 0), (-1, -1), -12),
            ])
        
        style_catatan = TableStyle(
            [("GRID", (0, 0), (-1, -1), 0.5, colors.black),
             ("TOPPADDING", (0,0), (-1,0), 2*mm),
             ("LEFTPADDING", (0,0), (0,-1), 5*mm),
             ("RIGHTPADDING", (-1,0), (-1,-1), 5*mm),
             ("BOTTOMPADDING", (0,-1), (-1,-1), 2*mm),
            ("FONTSIZE", (0, 0), (-1, -1), 12),]
        )
        style_ttd = TableStyle([
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                ("FONTNAME", (0, 5), (-1, 5), "Aptos Bold"),
                ("FONTNAME", (0, -1), (-1, -1), "Aptos Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ])
        
        if data['semester'] == "Genap":
            paragraf(teks5, x = 132, y=107, w= 70, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
            tabel(self, 120, 107, "HARD KODE",[75*mm],[19*mm], style_kenaikan)
        
        paragraf(self, teks1, x = 20, y=77, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tabel(self, 22, 77, data_ekskul, [10*mm , 80*mm , 20*mm, 63*mm], None, style_ekstra)
        paragraf(self, teks2, x = 20, y=107, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tabel(self, 22, 107, data_absensi, [30 * mm, 60 * mm], None, style_kehadiran)
        
        paragraf(self, teks3, x = 20, y=138, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tinggi_catatan = tabel(self, 22, 138, catatan_wali_kelas, [173 * mm], None, style_catatan)
        paragraf(self, teks4, x = 20, y=150 + tinggi_catatan/mm, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        self.c.setLineWidth(1)
        self.c.rect(22*mm, self.height-165*mm-tinggi_catatan, 173*mm, 15*mm)

        gambar(
            self, self.ttd_mudir, 
            90 + setting['x_mudir']*10, 
            239 + tinggi_catatan/mm + setting['y_mudir']*10, 
            setting['size_mudir']*10
        )

        gambar(self, self.ttd_walikelas, 
               155+ setting['x_walas']*10, 
               203 + setting['y_walas']*10 + tinggi_catatan/mm, 
               setting['size_walas']*10
            )
        tabel(self, 22, 
              170 + tinggi_catatan/mm, data_tabel_ttd, 
              [50 * mm, 60 * mm, 50 * mm], 
              None, style_ttd
        )
        self.c.showPage()

    def identitas_madrasah(self):
        teks1 = "RAPOR"
        teks2 = "PESERTA DIDIK"
        teks3 = "MADRASAH IBTIDAIYAH"
        teks4 = "(MI)"
        data_tabel1 = [
            ["Nama Madrasah",   ":",    "MIS PERSIS RAHAYU"],
            ["NSM",             ":",    "111232040082"],
            ["NPSN",            ":",    "60707798"],
            ["Alamat Madrasah", ":",    "Kp. Curug RT 04 RW 08"],
            ["Kelurahan/Desa",  ":",    "Ds. Rahayu"],
            ["Kecamatan",       ":",    "Margaasih"],
            ["Kabupaten/Kota",  ":",    "Kab. Bandung"],
            ["Provinsi",        ":",    "Jawa Barat"],
            ["Kodepos",         ":",    "40218"],
            ["Email",           ":",    "mipersisrahayu@gmail.com"],
        ]
        style_table1 = TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                ("FONTNAME", (2, 0), (-1, -1), "Aptos Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 14),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
             ]
        )
        center = self.width/2/mm-50
        gambar(self, path=self.logo_persis, x=self.width/2/mm-20, y=90, h=40)
        paragraf(self, teks1, x = center, y=110, w= 100, h=10, font='TNRB', size=22, alignment=TA_CENTER)
        paragraf(self, teks2, x = center, y=120, w= 100, h=10, font='TNRB', size=22, alignment=TA_CENTER)
        paragraf(self, teks3, x = center, y=130, w= 100, h=10, font='TNRB', size=22, alignment=TA_CENTER)
        paragraf(self, teks4, x = center, y=140, w= 100, h=10, font='TNRB', size=22, alignment=TA_CENTER)
        tabel(self, x=30, y=150, data=data_tabel1, col_width=[60*mm, 5*mm, 90*mm], styles=style_table1)
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
        gambar(self, logo_kemenag, 20, 38, 24)
        gambar(self, logo_persis, 170, 38, 24)
        paragraf(self, teks1, self.w_center/mm-57.5, 18, 120, 6, size= 14)
        paragraf(self, teks2, self.w_center/mm-57.5, 28, 120, 10, size=24)
        paragraf(self, teks3, self.w_center/mm-57.5, 35, 120, 6, size=11, font='TNRI')
        paragraf(self, teks4, self.w_center/mm-57.5, 40, 120, 6, size=11, font='TNRI')
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
            ["NIS", ":", data["nis_lokal"], "Kelas/Semester",": ", f"{data['kelas']}/{data['semester']}"],
            ["NISN", ":", data["nisn"], "Tahun Pelajaran",": ", data['tapel']],
        ]
        tabel(self, 20, 42, data_tabel, [15 * mm, 4 * mm, 80 * mm, 32 * mm,4*mm, 40 * mm],None,  style1)
        
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
        gambar(self, logo, 20, 32, 18)
        tabel(self, 20, 12, data_tabel, [22*mm, 15 * mm, 2 * mm, 67 * mm, 30 * mm, 2*mm, 37 * mm],None,  style1)


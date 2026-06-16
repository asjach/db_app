from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, GOV_LEGAL, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from io import BytesIO
from utils.fungsi.general_functions import *
from reportlab.platypus import (Paragraph,TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from models.model_nilai import Model_Nilai
from utils.app_config import DIREKTORI_DOKUMEN
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

class TemplateRapor:
    def __init__(self, parent=None, papersize=A4, data=None):
        self.parent = parent
        self.papersize = papersize
        self.width, self.height = self.papersize
        self.w_center = self.width/2
        self.logo_persis = "resources/images/logo mi.jpg"
        self.logo_kemenag = "resources/images/logo kemenag.jpg"
        self.logo_diniyah = "resources/images/logo_md.png"
        self.SQL = Model_Nilai()
        self.data_rapor = data['data_rapor']
        self.setting = data['setting']
        self.ttd_mudir = str(DIREKTORI_DOKUMEN / "guru" / self.data_rapor[0]["ttd_mudir"]) if self.data_rapor and self.data_rapor[0].get('ttd_mudir') else None
        if self.data_rapor and self.data_rapor[0].get('ttd_walas') not in ['', None] and self.setting.get('show_ttd_walas'):
            self.ttd_walikelas = str(DIREKTORI_DOKUMEN / "guru" / self.data_rapor[0]["ttd_walas"])
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
            jenjang = cleaned_data['jenjang']
            data_nilai = format_cell_data(self.SQL.data_nilai(id_kelas, id_kegiatan, nis_lokal))
            data_ekskul = self.SQL.data_ekskul(nis_lokal, id_kegiatan)
            data_prestasi = self.SQL.data_prestasi(nis_lokal, id_kegiatan)
            if jenjang == 'MI':
                if self.parent.opsi_cover.isChecked():
                    self.cover_mi(cleaned_data)
                if self.parent.opsi_id_madrasah.isChecked():
                    self.identitas_madrasah_mi()
                if self.parent.opsi_id_siswa.isChecked():
                    self.identitas_siswa_mi(cleaned_data)
                if self.parent.opsi_nilai.isChecked():
                    self.halaman_nilai_mi(cleaned_data, data_nilai)
                if self.parent.opsi_catatan.isChecked():
                    self.halaman_catatan_mi(cleaned_data, data_ekskul, data_prestasi)
            else:
                if self.parent.opsi_cover.isChecked():
                    self.cover_md(cleaned_data)
                if self.parent.opsi_id_madrasah.isChecked():
                    self.identitas_madrasah_md()
                if self.parent.opsi_id_siswa.isChecked():
                    self.identitas_siswa_md(cleaned_data)
                if self.parent.opsi_nilai.isChecked():
                    self.halaman_nilai_md(cleaned_data, data_nilai)
                if self.parent.opsi_catatan.isChecked():
                    self.halaman_catatan_md(cleaned_data)
        self.c.save()
        content = buffer.getvalue()
        buffer.close()
        return content
    
# ================
# HALAMAN RAPOR MI
# ================
    def cover_mi(self, data):
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

    def identitas_madrasah_mi(self):
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
        paragraf(self, teks1, x = center, y=110, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks2, x = center, y=120, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks3, x = center, y=130, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks4, x = center, y=140, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        tabel(self, x=30, y=150, data=data_tabel1, col_width=[60*mm, 5*mm, 90*mm], styles=style_table1)
        self.c.showPage()

    def identitas_siswa_mi(self, data):
        self.kop_mi()
        teks = "IDENTITAS PESERTA DIDIK"
        alamat = Paragraph(f"<para font face='Aptos' size=10 leading=12>{data['alamat_full']}</para>")
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
            ["Tempat Tanggal Lahir",        ":",        f"{data['tmp_lahir']}, {date_to_text(data['tgl_lahir'], 'lengkap')}"],
            ["Jenis Kelamin",               ":",        f"{'Laki-laki' if data['jk']=='L' else 'Perempuan'}"],
            ["Agama",                       ":",        f"{data['agama']}"],
            ["Status Dalam Keluarga",       ":",        "Anak Kandung"],
            ["Anak Ke",                     ":",        f"{data['anak_ke']}"],
            ["Alamat Peserta Didik",        ":",        alamat],
            ["",                            "",                  ],
            ["Nomor Telepon Rumah/HP",      ":",        no_telp_ortu],
            ["Sekolah Asal",                ":",        f"{data['nama_sekolah_asal']}"],
            ["Diterima di sekolah ini",     "",         ""],
            ["       a. Di Kelas",          ":",        f"{data['kls_masuk']}"],
            ["       b. Pada tanggal",      ":",        f"{date_to_text(data['tgl_masuk'], 'lengkap')}"],
            ["Nama Orang Tua",              "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_nama']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_nama']}"],
            ["Alamat Orang Tua",            ":",        alamat],
            ["",                            "",                  ],
            ["Pekerjaan Orang Tua",         "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_pekerjaan']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_pekerjaan']}"]
        ]
        titimangsa = f"Bandung, {date_to_text(data['tgl_masuk'],'lengkap')}"
        data2 = [
            [titimangsa],
            ["Kepala Madrasah"],
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
        tabel(self, 20, 65 , data1, (50*mm, 5*mm, 125*mm), self.setting['bio_tinggi']*10, style1)
        self.c.setLineWidth(1)
        self.c.rect(77*mm, 30*mm, 30*mm, 40*mm)
        tabel(self, 120, 228, data2,[70*mm], 10, styles=style2)
        gambar_mid(
            self, 
            self.ttd_mudir, 
            143 + self.setting['bio_x_mudir']*10, 
            258 + self.setting['bio_y_mudir']*10, 
            self.setting['size_mudir']*10
        )
        self.c.showPage()

    def halaman_nilai_mi(self, data_siswa, data_nilai_db):
        setting = self.setting
        teks = "CAPAIAN HASIL BELAJAR"
        # Tentukan tanda tangan wali kelas
        # Tentukan peringkat berdasarkan radio button
        if self.setting['show_peringkat'] == '10 Besar':
            if data_siswa['ranking'] != '':
                if int(data_siswa['ranking']) <= 10:
                    ranking = data_siswa['ranking']
                else:
                    ranking = ""
            else:
                ranking = ""
        elif self.setting['show_peringkat'] == 'Tidak Ditampilkan':
            ranking = ''
        else:
            if data_siswa['ranking'] != "":
                ranking = data_siswa['ranking']
            else:
                ranking = ''
        # Bangun data_nilai secara dinamis dari data_nilai_db (list of dicts)
        data_nilai = [["NO", "MATA PELAJARAN", "NILAI\nAKHIR", "TERBILANG"]]  # Header
        # Tambahkan baris untuk setiap mata pelajaran
        for i, item in enumerate(data_nilai_db, start=1):
            mata_pelajaran = Paragraph(f"""
                    <para  alignment='LEFT' leading=10>
                    <font name='Aptos Bold' size='10'>{item['mata_pelajaran']}</font><br/>
                    <font name='Aptos Italic' size='8'>Guru: {item['nama_guru']}</font>
                    </para>
            """)
            # Paragraph(f"<para font size 10>{item['mata_pelajaran']}</para>") if item['mata_pelajaran'] else item['mapel']
            nilai = item['nilai']
            data_nilai.append([str(i), mata_pelajaran, str(nilai), angka_ke_teks(nilai)])
        
        # Hitung jumlah dan rata-rata
        total_nilai = 0
        for item in data_nilai_db:
            nilai = item['nilai']
            total_nilai += float(nilai) if nilai not in('', None) else 0
        # total_nilai = sum(float(item['nilai']) for item in data_nilai_db)
        rata_rata = round(total_nilai / len(data_nilai_db), 2) if data_nilai_db else 0
        teks_rt = Paragraph(f"<para font='Aptos Italic' size=11 alignment='LEFT' leading=12>{angka_ke_teks(rata_rata)}</para>")
        
        # Tambahkan baris untuk Jumlah, Rata-Rata, dan Peringkat
        data_nilai.append(["Jumlah", "", str(int(total_nilai)), angka_ke_teks(int(total_nilai))])
        data_nilai.append(["Rata-Rata", "", str(rata_rata).replace(".", ","), teks_rt])
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
        self.kop_mi()
        self.identitas_mi(data_siswa)
        paragraf(self, teks, x=self.width/2/mm-50, y=83, w=100, h=8, font='Aptos Bold', size=16)
        tinggi_tabel = tabel(
            obj = self, 
            x = 20, 
            y = 85, 
            data = data_nilai, 
            col_width = [10 * mm, 85 * mm, 15 * mm, 65*mm], 
            row_height = [10, self.setting['nilai_tinggi']*10], 
            styles = style1
        )
        
        gambar_mid(
            obj = self, 
            path = self.ttd_mudir, 
            x = 50+setting['nilai_x_mudir']*10, 
            y = tinggi_tabel/mm + 123 + setting['nilai_y_mudir']*10, 
            h = setting['size_mudir']*10
        )

        gambar_mid(
            obj = self, 
            path = self.ttd_walikelas, 
            x = 155+setting['nilai_x_walas']*10, 
            y = tinggi_tabel/mm + 123 + setting['nilai_y_walas']*10, 
            h = setting['size_walas']*10
        )
        tabel(
            obj = self, 
            x = 30, 
            y = tinggi_tabel/mm + 90, 
            data=data_tabel_ttd, 
            col_width=[60 * mm, 37 * mm, 60 * mm], 
            row_height=None, 
            styles=style2
        )
        self.c.showPage()

    def halaman_catatan_mi(self, data, ekskul_list, prestasi_list):
        setting = self.setting
        self.kop_mi()
        self.identitas_mi(data)
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

        # EKSTRAKURIKULER
        DESKRIPSI = {
            "A": "Baik Sekali",
            "B": "Baik",
            "C": "Cukup",
            "D": "Kurang",
            "E": "Sangat Kurang",
            "F": "Salah memilih Ekskul"
        }
        header = ["#", "Ekstrakurikuler", "Pembimbing", "Predikat", "Deskripsi"]
        if not ekskul_list:
            data_ekskul = [header,
                ["1", "", "", "", ""],
                ["2", "", "", "", ""],
            ]
        else:
            data_ekskul = [header]
            for i, item in enumerate(ekskul_list, start=1):
                predikat = item.get("predikat", "")
                deskripsi = DESKRIPSI.get(predikat, "")
                data_ekskul.append([
                    str(i),
                    item.get("nama_ekskul", ""),
                    item.get("pembimbing", ""),
                    predikat,
                    deskripsi
                ])
            if len(ekskul_list) == 1:
                data_ekskul.append(["2", "", "", "", ""])

        # PRESTASI
        header_prestasi = ["#", "Jenis Prestasi", "Keterangan"]
        if not prestasi_list:
            data_prestasi = [
                header_prestasi,
                ["1", "", ""],] 
        else:
            data_prestasi = [header_prestasi]
            for i, item in enumerate(prestasi_list, start=1):
                data_prestasi.append([
                    str(i),
                    item.get("jenis_prestasi", ""),
                    item.get("keterangan", ""),
                ])

        # ABSENSI
        data_absensi = [
            ["Sakit", f"   0    Hari" if data["sakit"] == "" else f"   {data['sakit']}   Hari"],
            ["Izin", f"   0    Hari" if data["ijin"] == "" else f"   {data['ijin']}   Hari"],
            ["Alpa", f"   0    Hari" if data["alpa"] == "" else f"   {data['alpa']}   Hari"],
        ]
        data_kenaikan = [[f"{data['status_naik']}"],]
        data_tabel_ttd = [
            ["", "", f"Bandung, {date_to_text(data['tgl_titimangsa'], "lengkap")}"],
            ["Orang Tua/Wali", "", "Wali Kelas"],
            ["", "", ""],
            ["", "", ""],
            ["_________________", "", data['walas']],
            ["", "Mengetahui", ""],
            ["", "Kepala Madrasah", ""],
            ["", "", ""],
            ["", "", ""],
     
            ["", data['mudir'], ""],
        ]
        style_ekstra = TableStyle(
            [
                # Padding header
                ("TOPPADDING", (0, 0), (-1, 0), 3),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 6),

                # Warna & grid
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),

                # Vertical alignment
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                # Font
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),   # header
                ("FONTNAME", (0, 1), (-1, -1), "Aptos"),      # body
                ("FONTSIZE", (0, 0), (-1, -1), 11),

                # ===== ALIGNMENT =====

                # Header tetap rata tengah
                ("ALIGN", (0, 0), (-1, 0), "CENTER"),

                # Body default rata kiri
                ("ALIGN", (0, 1), (-1, -1), "CENTER"),

                # Kolom nomor (#) rata tengah
                ("ALIGN", (1, 1), (1, -1), "LEFT"),

                # Kolom predikat rata tengah
                ("ALIGN", (2, 1), (2, -1), "LEFT"),
            ]
        )

        style_prestasi = TableStyle(
            
            [   ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (1, 1), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
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
                ("FONTNAME", (0, 4), (-1, 4), "Aptos Bold"),
                ("FONTNAME", (0, -1), (-1, -1), "Aptos Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ])
        
        if data['semester'] == "Genap":
            paragraf(self, teks5, x = 132, y=128, w= 70, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
            tabel(
                obj=self, 
                x=120, 
                y=128, 
                data=data_kenaikan,
                col_width=[75*mm],
                row_height=19, 
                styles=style_kenaikan
            )
        tinggi = 75
        #  TABEL EKSKUL
        paragraf(self, teks1, x = 20, y=tinggi, w= 100, h=8, font='Aptos Bold', size=12, alignment=TA_LEFT)
        h_tabel = tabel(self, 22, tinggi, data_ekskul, [10*mm , 55*mm, 55*mm, 20*mm, 35*mm], None, style_ekstra)
        tinggi += 10 + h_tabel/mm

        # TABEL PRESTASI
        paragraf(self, "Prestasi", x = 20, y=tinggi, w= 100, h=8, font='Aptos Bold', size=12, alignment=TA_LEFT)
        h_tabel = tabel(self, 22, tinggi, data_prestasi, [10 * mm, 55 * mm, 110*mm], None, style_prestasi) 

        tinggi += 10 + h_tabel/mm
        # # TABEL ABSENSI
        paragraf(self, teks2, x = 20, y=tinggi, w= 100, h=8, font='Aptos Bold', size=12, alignment=TA_LEFT)
        h_tabel = tabel(self, 22, tinggi, data_absensi, [30 * mm, 60 * mm], None, style_kehadiran)
        tinggi += 10 + h_tabel/mm
        # # tulisan catatan wali kelas
        paragraf(self, teks3, x = 20, y=tinggi, w= 100, h=8, font='Aptos Bold', size=12, alignment=TA_LEFT)
        h_tabel = tabel(self, 22, tinggi, catatan_wali_kelas, [175 * mm], None, style_catatan)
        tinggi += 10 + h_tabel/mm

        # TANGGAPAN ORTU
        paragraf(self, teks4, x = 20, y=tinggi, w= 100, h=8, font='Aptos Bold', size=12, alignment=TA_LEFT)

        h_tabel = tabel(self, 22, tinggi, [[""]], [175 * mm], [15,0], style_catatan)
        tinggi += 17
        h_tabel = tabel(self, 22, 
              tinggi, 
              data_tabel_ttd, 
              [50 * mm, 60 * mm, 50 * mm], 
              None, style_ttd
        )
        tinggi += h_tabel/mm

        gambar_mid(
            self, 
            self.ttd_walikelas, 
            setting['catatan_x_walas']*10 + 160, 
            tinggi - 33 + setting['catatan_y_walas']*10, 
            setting['size_walas']*10
            )
        
        gambar_mid(
            self, 
            self.ttd_mudir, 
            setting['catatan_x_mudir']*10 + 90, 
            tinggi  + setting['catatan_y_mudir']*10, 
            setting['size_mudir']*10
        )
        self.c.showPage()


# ================
# HALAMAN RAPOR MD
# ================
    def cover_md(self, data):
        tengah = self.w_center/mm - 20
        teks1 = "PESANTREN PERSATUAN ISLAM 45 RAHAYU"
        teks2 = "LAPORAN HASIL BELAJAR"
        teks3 = "MADRASAH DINIYAH"
        teks4 = "(MD)"
        nama_lengkap = data['nama_lengkap'] if data else 'NAMA LENGKAP'
        nis_lokal = data['nis_lokal'] if data else 'NIS LOKAL'
        nisn = data['nisn'] if data else 'NISN'
        nama = Paragraph(f"<para font face='Aptos Bold' size=14 leading=20>{nama_lengkap}</para>")
        nis = f"{nis_lokal}"
        nisn = f"{nisn}"
        teks5 = "MD PERSIS RAHAYU"
        teks6 = "KABUPATEN BANDUNG"
        teks7 = "PROVINSI JAWA BARAT"
        data_tabel = [
            ["Nama Lengkap",    ":",    nama],
            ["NIS Madrasah",    ":",    nis],

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

        paragraf(self, teks1, x=20, y=50, w=170, h=9, size=14)
        paragraf(self,teks2, x=20, y=60, w=170, h=10, size=18)
        paragraf(self, teks3, x=20, y=70, w=170, h=10, size=18)
        paragraf(self,teks4, x=20, y=80, w=170, h=10, size=20)

        gambar(self, self.logo_diniyah, tengah, 145, 40)
        tabel(self, x= 30, y=180, data=data_tabel, col_width=[45*mm, 5*mm, 110*mm], styles=style_tabel)

        paragraf(self, teks5, x=20, y=257, w=170, h=9, size=18)
        paragraf(self,  teks6, x=20, y=264, w=170, h=8, size=14)
        paragraf(self, teks7, x=20, y=271, w=170, h=8, size=14)
        self.c.showPage()

    def identitas_madrasah_md(self):
        self.watermark_text_md()
        teks1 = "RAPOR"
        teks2 = "PESERTA DIDIK"
        teks3 = "MADRASAH DINIYAH"
        teks4 = "(MD)"
        data_tabel1 = [
            ["Nama Madrasah",   ":",    "MD PERSIS RAHAYU"],
            ["Alamat Madrasah", ":",    "Kp. Curug RT 04 RW 08"],
            ["Kelurahan/Desa",  ":",    "Ds. Rahayu"],
            ["Kecamatan",       ":",    "Margaasih"],
            ["Kabupaten/Kota",  ":",    "Kab. Bandung"],
            ["Provinsi",        ":",    "Jawa Barat"],
            ["Kodepos",         ":",    "40218"],
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
        gambar(self, path=self.logo_diniyah, x=self.width/2/mm-20, y=90, h=40)
        paragraf(self, teks1, x = center, y=110, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks2, x = center, y=120, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks3, x = center, y=130, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        paragraf(self, teks4, x = center, y=140, w= 100, h=10, font='Times New Roman Bold', size=22, alignment=TA_CENTER)
        tabel(self, x=30, y=150, data=data_tabel1, col_width=[60*mm, 5*mm, 90*mm], styles=style_table1)
        self.c.showPage()

    def identitas_siswa_md(self, data):
        self.watermark_md()
        self.kop_md()
        teks = "IDENTITAS PESERTA DIDIK"
        alamat = Paragraph(f"<para font face='Aptos' size=10 leading=12>{data['alamat_full']}</para>")
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
            ["Tempat Tanggal Lahir",        ":",        f"{data['tmp_lahir']}, {date_to_text(data['tgl_lahir'], 'lengkap')}"],
            ["Jenis Kelamin",               ":",        f"{'Laki-laki' if data['jk']=='L' else 'Perempuan'}"],
            ["Agama",                       ":",        f"{data['agama']}"],
            ["Status Dalam Keluarga",       ":",        "Anak Kandung"],
            ["Anak Ke",                     ":",        f"{data['anak_ke']}"],
            ["Alamat Peserta Didik",        ":",        alamat],
            ["",                            "",                  ],
            ["Nomor Telepon Rumah/HP",      ":",        no_telp_ortu],
            ["Sekolah Asal",                ":",        f"{data['nama_sekolah_asal']}"],
            ["Diterima di sekolah ini",     "",         ""],
            ["       a. Di Kelas",          ":",        f"{data['kls_masuk']}"],
            ["       b. Pada tanggal",      ":",        f"{date_to_text(data['tgl_masuk'], 'lengkap')}"],
            ["Nama Orang Tua",              "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_nama']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_nama']}"],
            ["Alamat Orang Tua",            ":",        alamat],
            ["",                            "",                  ],
            ["Pekerjaan Orang Tua",         "",         ""],
            ["       a. Ayah",              ":",        f"{data['ayah_pekerjaan']}"],
            ["       b. Ibu",               ":",        f"{data['ibu_pekerjaan']}"]
        ]
        titimangsa = f"Bandung, {date_to_text(data['tgl_masuk'],'lengkap')}"
        data2 = [
            [titimangsa],
            ["Kepala Madrasah"],
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
        tabel(self, 20, 65 , data1, (50*mm, 5*mm, 125*mm), self.setting['bio_tinggi']*10, style1)
        self.c.setLineWidth(1)
        self.c.rect(77*mm, 30*mm, 30*mm, 40*mm)
        tabel(self, 120, 228, data2,[70*mm], 10, styles=style2)
        gambar_mid(
            self, 
            self.ttd_mudir, 
            143 + self.setting['bio_x_mudir']*10, 
            258 + self.setting['bio_y_mudir']*10, 
            self.setting['size_mudir']*10
        )
        self.c.showPage()

    def halaman_nilai_md(self, data_siswa, data_nilai_db):
        self.watermark_md()
        setting = self.setting
        teks = "CAPAIAN HASIL BELAJAR"
        # Tentukan tanda tangan wali kelas
        # Tentukan peringkat berdasarkan radio button
        if self.setting['show_peringkat'] == '10 Besar':
            if data_siswa['ranking'] != '':
                if int(data_siswa['ranking']) <= 10:
                    ranking = data_siswa['ranking']
                else:
                    ranking = ""
            else:
                ranking = ""
        elif self.setting['show_peringkat'] == 'Tidak Ditampilkan':
            ranking = ''
        else:
            if data_siswa['ranking'] != "":
                ranking = data_siswa['ranking']
            else:
                ranking = ''
        # Bangun data_nilai secara dinamis dari data_nilai_db (list of dicts)
        data_nilai = [["NO", "MATA PELAJARAN", "NILAI\nAKHIR", "TERBILANG"]]  # Header
        # Tambahkan baris untuk setiap mata pelajaran
        for i, item in enumerate(data_nilai_db, start=1):
            mata_pelajaran = Paragraph(f"""
                    <para  alignment='LEFT' leading=10>
                    <font name='Aptos Bold' size='11'>{item['mata_pelajaran']}</font><br/>
                    <font name='Aptos Italic' size='8'>Guru: {item['nama_guru']}</font>
                    </para>
            """)
            # Paragraph(f"<para font size 10>{item['mata_pelajaran']}</para>") if item['mata_pelajaran'] else item['mapel']
            nilai = item['nilai']
            data_nilai.append([str(i), mata_pelajaran, str(nilai), angka_ke_teks(nilai)])
        
        # Hitung jumlah dan rata-rata
        total_nilai = 0
        for item in data_nilai_db:
            nilai = item['nilai']
            total_nilai += float(nilai) if nilai not in('', None) else 0
        # total_nilai = sum(float(item['nilai']) for item in data_nilai_db)
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
        self.kop_md()
        self.identitas_md(data_siswa)
        paragraf(self, teks, x=self.width/2/mm-50, y=83, w=100, h=8, font='Aptos Bold', size=16)
        tinggi_tabel = tabel(
            obj = self, 
            x = 20, 
            y = 85, 
            data = data_nilai, 
            col_width = [10 * mm, 85 * mm, 15 * mm, 65*mm], 
            row_height = [10, self.setting['nilai_tinggi']*10], 
            styles = style1
        )
        
        gambar_mid(
            obj = self, 
            path = self.ttd_mudir, 
            x = 50+setting['nilai_x_mudir']*10, 
            y = tinggi_tabel/mm + 123 + setting['nilai_y_mudir']*10, 
            h = setting['size_mudir']*10
        )

        gambar_mid(
            obj = self, 
            path = self.ttd_walikelas, 
            x = 155+setting['nilai_x_walas']*10, 
            y = tinggi_tabel/mm + 123 + setting['nilai_y_walas']*10, 
            h = setting['size_walas']*10
        )
        tabel(
            obj = self, 
            x = 30, 
            y = tinggi_tabel/mm + 90, 
            data=data_tabel_ttd, 
            col_width=[60 * mm, 37 * mm, 60 * mm], 
            row_height=None, 
            styles=style2
        )
        self.c.showPage()

    def halaman_catatan_md(self, data):
        setting = self.setting
        self.watermark_md()
        self.kop_md()
        self.identitas_md(data)
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
            ["Sakit", f"       Hari" if data["sakit"] == "" else f"   {data['sakit']}   Hari"],
            ["Izin", f"       Hari" if data["ijin"] == "" else f"   {data['ijin']}   Hari"],
            ["Alpa", f"       Hari" if data["alpa"] == "" else f"   {data['alpa']}   Hari"],
        ]
        data_kenaikan = [
            [f"{data['status_naik']}"],
        ]
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
            paragraf(self, teks5, x = 132, y=107, w= 70, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
            tabel(
                obj=self, 
                x=120, 
                y=107, 
                data=data_kenaikan,
                col_width=[75*mm],
                row_height=19, 
                styles=style_kenaikan
            )
        
        paragraf(self, teks1, x = 20, y=77, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tabel(self, 22, 77, data_ekskul, [10*mm , 80*mm , 20*mm, 63*mm], None, style_ekstra)
        paragraf(self, teks2, x = 20, y=107, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tabel(self, 22, 107, data_absensi, [30 * mm, 60 * mm], None, style_kehadiran)
        
        paragraf(self, teks3, x = 20, y=138, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        tinggi_catatan = tabel(self, 22, 138, catatan_wali_kelas, [173 * mm], None, style_catatan)
        paragraf(self, teks4, x = 20, y=150 + tinggi_catatan/mm, w= 100, h=8, font='Aptos Bold', size=14, alignment=TA_LEFT)
        self.c.setLineWidth(1)
        self.c.rect(22*mm, self.height-165*mm-tinggi_catatan, 173*mm, 15*mm)

        gambar_mid(
            self, self.ttd_mudir, 
            90 + setting['catatan_x_mudir']*10, 
            239 + tinggi_catatan/mm + setting['catatan_y_mudir']*10, 
            setting['size_mudir']*10
        )

        gambar_mid(self, self.ttd_walikelas, 
               155+ setting['catatan_x_walas']*10, 
               203 + setting['catatan_y_walas']*10 + tinggi_catatan/mm, 
               setting['size_walas']*10
            )
        tabel(self, 22, 
              170 + tinggi_catatan/mm, data_tabel_ttd, 
              [50 * mm, 60 * mm, 50 * mm], 
              None, style_ttd
        )
        self.c.showPage()


# ================
# TAMBAHAN/PEMBANTU
# ================
    def kop_mi(self, margin_top=20, margin_left=20):
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
        paragraf(self, teks3, self.w_center/mm-57.5, 35, 120, 6, size=11, font='Times New Roman Italic')
        paragraf(self, teks4, self.w_center/mm-57.5, 40, 120, 6, size=11, font='Times New Roman Italic')
        self.c.setLineWidth(2)
        self.c.line(x1=20*mm, y1=self.height-42*mm, x2=195*mm, y2=self.height - 42*mm)

    def kop_md(self, margin_top=20, margin_left=20):
        margin_top = margin_top * mm
        margin_left = margin_left * mm
        # isi
        teks1 = "PESANTREN PERSATUAN ISLAM 45 RAHAYU"
        teks2 = "MD PERSIS RAHAYU"
        teks3 = "Jl. Mahmud No. 271 Kp. Curug RT 04 RW 08 Ds. Rahayu"
        teks4 = "Kec. Margasasih Kab. Bandung - Jawa Barat"

        # posisi
        gambar(self, self.logo_diniyah, 30, 38, 24)
        paragraf(self, teks1, self.w_center/mm-47.5, 18, 120, 6, size= 14)
        paragraf(self, teks2, self.w_center/mm-47.5, 28, 120, 10, size=24)
        paragraf(self, teks3, self.w_center/mm-47.5, 35, 120, 6, size=11, font='Times New Roman Italic')
        paragraf(self, teks4, self.w_center/mm-47.5, 40, 120, 6, size=11, font='Times New Roman Italic')
        self.c.setLineWidth(2)
        self.c.line(x1=20*mm, y1=self.height-42*mm, x2=195*mm, y2=self.height - 42*mm)

    def identitas_mi(self, data):
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
            ["NIS", ":", data["nis_lokal"], "Kelas/Semester",": ", f"{data['kelas']} MI /{data['semester']}"],
            ["NISN", ":", data["nisn"], "Tahun Pelajaran",": ", data['tapel']],
        ]
        tabel(self, 20, 42, data_tabel, [15 * mm, 4 * mm, 80 * mm, 32 * mm,4*mm, 40 * mm],None,  style1)
        
    def identitas_md(self, data):
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
            ["", "NIS", ":", data["nis_lokal"], "Semester",": ", f"{data['semester']}"],
            ["", "Kelas", ":", f"{data['kelas']} MD", "Tahun Pelajaran",": ", data['tapel']],
        ]
        tabel(self, 20, 42, data_tabel, [5*mm, 15 * mm, 2 * mm, 77 * mm, 30 * mm, 2*mm, 37 * mm],None,  style1)



    def watermark_md(self, logo_path=None, ukuran=100, alpha=0.2):
        """
        Watermark logo transparan di tengah halaman
        """
        if logo_path is None:
            logo_path = self.logo_diniyah

        try:
            self.c.saveState()

            # transparansi
            self.c.setFillAlpha(alpha)

            # posisi tengah halaman
            x = (self.width - ukuran * mm) / 2
            y = (self.height - ukuran * mm) / 2

            self.c.drawImage(
                ImageReader(logo_path),
                x,
                y,
                width=ukuran * mm,
                height=ukuran * mm,
                preserveAspectRatio=True,
                mask='auto'
            )

            self.c.restoreState()

        except Exception as e:
            print(f"Watermark gagal dibuat: {e}")

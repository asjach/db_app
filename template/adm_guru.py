import os
import sys
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import GOV_LEGAL, landscape, A4
from reportlab.lib.units import mm, cm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.platypus.flowables import Flowable
from reportlab.platypus import Paragraph, Frame, Table, TableStyle, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

import PyPDF2
from utils.fungsi.general_functions import *

class TemplateAdmGuru:
    def __init__(self, setting:dict={}, data:dict={}) -> None:
        self.setting = setting
        self.data = data
        self.papersize = A4 if self.setting['kertas'] == 'A4' else GOV_LEGAL
        width, height = self.papersize
        self.width = width 
        self.height = height 
        self.logo_persis = "resources/images/logo mi.jpg"
        # self.data_siswa = data['data_siswa']

    def create_pdf(self):
        from_canvas = self.created_by_canvas()
        from_build = self.create_by_simple_doc_template()
        merger = PyPDF2.PdfMerger()
        output_buffer = BytesIO()
        pdfs = (from_canvas, from_build)
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(output_buffer)
        merger.close()
        pdf_data = output_buffer.getvalue()
        output_buffer.close()
        return pdf_data
        
    def created_by_canvas(self):
        buffer = BytesIO()
        self.c = canvas.Canvas(buffer, self.papersize)
        if self.setting['cover']:
            self.lembar_cover()
        if self.setting['agenda']:
            for _ in range(self.setting['jml_agenda']):
                self.lembar_agenda_harian()
        if self.setting['presensi']:
            for _ in range(self.setting['jml_presensi']):
                self.lembar_presensi()
        if self.setting['daftar_nilai']:
            for _ in range(self.setting['jml_daftar_nilai']):
                self.lembar_nilai()
        if self.setting['pengembalian']:
            self.lembar_pengembalian_rapor()
        if self.setting['penyerahan']:
            self.lembar_penyerahan_rapor()
        self.c.save()
        buffer.seek(0)
        return buffer

    def create_by_simple_doc_template(self):
        orientasi = landscape(self.papersize)
        buffer = BytesIO()
        pdf = SimpleDocTemplate(
            buffer, 
            pagesize = orientasi,
            topMargin = self.setting['sisi_jilid'] * cm,
            rightMargin = 1 * cm,
            bottomMargin = 1 * cm,
            leftMargin =  self.setting['sisi_lain'] * cm
        )
        self.elemen = []
        if self.setting['identitas']:
            self.lembar_identitas()
        pdf.build(self.elemen)
        buffer.seek(0)
        return buffer
    
    def lembar_cover(self):
        half = self.width/2
        teks = [
            "BUKU ADMINISTRASI", 
            "ASATIDZAH", 
            "Nama Guru:", 
            f"{self.data['nama_guru']}",
            "Kelas:",
            f"{self.data['kelas']} {self.data['jenjang']}",
            "MI-MD PERSIS RAHAYU",
            "PESANTREN PERSIS 45 RAHAYU",
            f"{self.data['semester'].upper()} - {self.data['tapel']}"
            ]
        self.paragraf(teks[0], x=half-7.0*cm, y= 4*cm, w=14*cm, h=1.2*cm, size=24)
        self.paragraf(teks[1], x=half-7.0*cm, y= 5.2*cm, w=14*cm, h=1.2*cm, size=24)
        self.image(path = self.logo_persis, x = half-2.5*cm, y = 13.2*cm, h = 50*mm)
        self.paragraf(teks[2], x=half-7.0*cm, y= 17*cm, w=14*cm, h=0.8*cm, size=16)
        self.paragraf(teks[3], x=half-7.0*cm, y= 18*cm, w=14*cm, h=1*cm, size=22)
        self.paragraf(teks[4], x=half-7.0*cm, y= 19.5*cm, w=14*cm, h=0.8*cm, size=16)
        self.paragraf(teks[5], x=half-7.0*cm, y= 20.5*cm, w=14*cm, h=1*cm, size=22)
        self.paragraf(teks[6], x=half-7.0*cm, y= 25*cm, w=14*cm, h=0.8*cm, size=18)
        self.paragraf(teks[7], x=half-7.0*cm, y= 25.8*cm, w=14*cm, h=0.8*cm, size=18)
        self.paragraf(teks[8], x=half-7.0*cm, y= 26.6*cm, w=14*cm, h=0.8*cm, size=18)
        self.c.showPage()

    def lembar_agenda_harian(self):
        # VARIABEL
        table_data = []
        header_table1 = ["PERTEMUAN", "", "Pelajaran", "Materi/Pembahasan", "Tugas"]
        header_table2 = ["Ke-", "Hari/Tanggal", "", "", ""]
        table_style_command = [("FONTNAME", (0, 0), (-1, -1), "Aptos Bold"),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("SPAN", (0, 0), (1, 0)),
                ("SPAN", (2, 0), (2, 1)),
                ("SPAN", (3, 0), (3, 1)),
                ("SPAN", (4, 0), (4, 1)),
                ("SPAN", (0, 2), (0, 3)),
                ("SPAN", (1, 2), (1, 3))]
        
        kali = 36
        table_data.append(header_table1)
        table_data.append(header_table2)
        for row in range(kali):
            table_data.append([""])

        baris_agenda = self.setting['baris_agenda']
        baris_pelajaran = 2 if baris_agenda == '2 baris' else 3
        
        for row in range(int(kali/baris_pelajaran)):
            baris_ke = row * baris_pelajaran
            table_style_command.append(("SPAN", (0, baris_ke + 2), (0, baris_ke + baris_pelajaran + 1)))
            table_style_command.append(("SPAN", (1, baris_ke + 2), (1, baris_ke + baris_pelajaran + 1)))
        tabel_style = TableStyle(table_style_command)
        col_width = [8*mm, 30*mm, 25*mm, 70*mm, 40*mm]
        tinggi_baris = self.setting['tinggi_baris_agenda']
        row_height = [6*mm, 6*mm] + [tinggi_baris*mm]*kali
        
        #POSISI
        x = self.setting['sisi_jilid'] * cm
        y = self.setting['sisi_lain'] * cm
        h = 10*mm
        self.paragraf("AGENDA HARIAN GURU", x=x, y= y, w=140*mm, h=h, size=20, alignment=TA_LEFT)
        y += h + 3*mm
        h = 7*mm
        self.paragraf("KELAS: ....................", x=x, y= y, w=70*mm, h=h, font='Aptos', size=11, alignment=TA_LEFT)
        self.paragraf("NAMA GURU: ..............................", x=x + 95*mm, y= y, w=70*mm, h=h, font='Aptos', size=11, alignment=TA_LEFT)
        y += h 
        self.tabel(x = x, y= y, data=table_data, col_width=col_width, row_height=row_height, styles=tabel_style)
        self.c.showPage()

    def lembar_presensi(self):
        # STYLE
        style_tabel_header = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos Narrow"),
                    ("SIZE", (0,0), (-1,-1), 11),
                    ])     

        style_tabel_detail = TableStyle([
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                    ("FONTNAME", (0, 0), (-1, -1), "Aptos Narrow"),
                    ("SIZE", (0,0), (-1,-1), 10),
                    ("SIZE", (2,0), (-6,0), 9),
                    ("SIZE", (0,2), (1,-1), 9),
                    ("SPAN", (-1, 0), (-1, 1)),
                    ("SPAN", (0,0), (0, 1)),
                    ("SPAN", (1,0), (1, 1)),
                    ("SPAN", (-5,0), (-2, 0)),
                    ("ALIGN", (0,0), (-1,-1), "CENTER"),
                    ("ALIGN", (1,2), (1,-1), "LEFT"),
                    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                    ("LINEBEFORE", (0,0), (0,-1), 1, colors.black),
                    ("LINEBELOW", (0,1), (-1,1), 1, colors.black),
                    ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                    ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                    ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                    ("LINEAFTER", (1,0), (1,-1), 1, colors.black),
                    ("LINEBEFORE", (-1,0), (-1,-1), 1, colors.black),
                    ])


        # CONTENT/DATA
        kelas = f"{self.data['kelas']} {self.data['jenjang']}"
        tapel_semester = f"{self.data['tapel']}/{self.data['semester']}"
        pelajaran = "1. ....................  2. ....................  3. ...................."
        data_tabel_header = [
            ["Kelas",           ":",    kelas,          "Hari",         ":",    ""],
            ["Tapel/Semester",  ":",    tapel_semester, "Pelajaran",    ":",    pelajaran],
        ]
        lebar_kolom_nama = self.setting['lebar_nama_singkat'] * mm
        tinggi_baris = self.setting['tinggi_baris'] * mm
        col_width = [6*mm, lebar_kolom_nama] + [self.setting['lebar_tanggal']*mm]*18 + [7*mm]*4 + [9*mm]
        data_tabel_detail = [["#", "Nama Lengkap", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "TIDAK HADIR", "","", "", "%"],]
        header2 = ['' for _ in range(20)] + ["S", "I","A", RotatedParagraph("JML", w=5*mm, h=15*mm), "%"]
        data_tabel_detail.append(header2)
        data_siswa = self.data['data_siswa']
        for row_data in data_siswa:
            new_row = [row_data['no_urut'], row_data['nama_singkat']]
            data_tabel_detail.append(new_row)
        
        no_urut = len(data_siswa)
        if self.setting['jumlah_baris'] < len(data_siswa):
            rentang = 0
            row_height = [None, 15*mm] + [tinggi_baris]*len(data_siswa)
        else:
            rentang = self.setting['jumlah_baris'] - len(data_siswa)
            row_height = [None, 15*mm] + [tinggi_baris]*self.setting['jumlah_baris']
        if self.setting['jumlah_baris'] > len(data_siswa):
            for _ in range(rentang):
                no_urut = no_urut + 1
                new_row = [no_urut]
                data_tabel_detail.append(new_row)


        # POSISI
        sisi_jilid = self.setting['sisi_jilid'] * cm
        sisi_lain = self.setting['sisi_lain'] * cm
        y = sisi_lain
        h = 10 * mm
        self.paragraf("PRESENSI HARIAN", x=sisi_jilid, y=y, w=140*mm, h=h, size=20, alignment=TA_LEFT)
        y += h
        h_header = self.tabel(x = sisi_jilid, y=y, data=data_tabel_header, col_width=[30*mm, 5*mm, 35*mm, 20*mm, 5*mm, 80*mm], styles=style_tabel_header)
        y += h_header + 2 *mm
        self.tabel(x = sisi_jilid, y = y, data=data_tabel_detail, col_width=col_width, styles=style_tabel_detail,row_height=row_height)
        self.c.showPage()

    def lembar_nilai(self):
        # STYLE / VARIABEL
        style_header = TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos Narrow"),
                ("SIZE", (0,0), (-1,-1), 11),
            ]
        )
        style_detail_mi = TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 1), "Aptos Bold"),
                ("FONTNAME", (0, 2), (-1, -1), "Aptos"),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.black),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("ALIGN", (1,2), (1,-1), "LEFT"),
                ("SIZE", (0,2), (1,-1), 9),
                ("SPAN", (0, 0), (0, 1)),
                ("SPAN", (1, 0), (1, 1)),
                ("SPAN", (2, 0), (10, 0)),
                ("SPAN", (11, 0), (11, 1)),
                ("SPAN", (12,0), (14,0)),
                ("SPAN", (-1,0), (-1,1)),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black),
                ("LINEBELOW", (0,1), (-1,1), 1, colors.black),
                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEAFTER", (1,0), (1,-1), 1, colors.black),
                ("LINEBEFORE", (11,0), (11,-1), 1, colors.black),
                ("LINEBEFORE", (15,0), (15,-1), 1, colors.black),
                ("TOPPADDING", (0,2), (-1,-1), 4)
            ]
        ) 
        style_detail_md = TableStyle(
            [   
                ("FONTNAME", (0, 0), (-1, 1), "Aptos Bold"),
                ("FONTNAME", (0, 2), (-1, -1), "Aptos"),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("ALIGN", (1,2), (1,-1), "LEFT"),
                ("SIZE", (0,2), (1,-1), 9),
                ("SPAN", (0, 0), (0, 1)),
                ("SPAN", (1, 0), (1, 1)),
                ("SPAN", (2, 0), (7, 0)),
                ("SPAN", (8, 0), (8, 1)),
                ("SPAN", (9, 0), (9, 1)),
                ("SPAN", (10, 0), (10, 1)),
                ("SPAN", (11, 0), (11, 1)),
                ("SPAN", (12, 0), (12, 1)),
                ("SPAN", (13, 0), (13, 1)),
                ("SPAN", (14, 0), (14, 1)),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black),
                ("LINEBELOW", (0,1), (-1,1), 1, colors.black),
                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBEFORE", (8,0), (8,-1), 1, colors.black),
                ("LINEBEFORE", (12,0), (12,-1), 1, colors.black),
                ("LINEAFTER", (1,0), (1,-1), 1, colors.black),
                ("TOPPADDING", (0,2), (-1,-1), 4)
            ])

        col_width_header = [30*mm, 5*mm, 65*mm, 20*mm, 5*mm, 50*mm]
             

        # CONTENT / DATA
        ## HEADER
        kelas = f"{self.data['kelas']} {self.data['jenjang']}"
        tapel_semester = f"{self.data['tapel']}/{self.data['semester']}"
        pas_pat = "PAS" if self.data['semester'] == "Ganjil" else "PAT"
        data_header = [
            ["Kelas", ":",kelas , "", "", ""],
            ["Tapel/Semester", ":", tapel_semester, "Pelajaran", ":", ".............................."],
        ]

        data_detail = []
        ## TABEL MI
        if self.data['jenjang'] == 'MI':
            header1 = ["#", "Nama Lengkap", "NILAI HARIAN DAN TUGAS", "", "", "", "", "", "", "", "", RotatedParagraph("RT HARIAN", w = 5*mm, h=22*mm, ), f"NILAI {pas_pat}","", "", RotatedParagraph("NILAI AKHIR", h=20*mm, w=5*mm, showBoundary=0)]
            header2 = ["", "", "1", "2", "3", "4", "5", "6", "7", "8", RotatedParagraph("HADIR", w=5*mm, h=18*mm),"", RotatedParagraph("PRAKTEK", w=5*mm, h=18*mm), RotatedParagraph("TULIS", w=5*mm, h=18*mm), RotatedParagraph("RATA2", w=5*mm, h=18*mm), ""]
            data_detail.append(header1)
            data_detail.append(header2)
            data_siswa = self.data['data_siswa']
            for row_data in data_siswa:
                new_row = [row_data['no_urut'], row_data['nama_singkat']]
                data_detail.append(new_row)
            no_urut = len(data_siswa)
            tinggi_kolom_nama = self.setting['tinggi_baris'] * mm
            if self.setting['jumlah_baris'] < len(data_siswa):
                rentang = 0
                row_height = [None, 18*mm] + [tinggi_kolom_nama]*len(data_siswa)
            else:
                rentang = self.setting['jumlah_baris'] - len(data_siswa)
                row_height = [None, 18*mm] + [tinggi_kolom_nama]*self.setting['jumlah_baris']
            if self.setting['jumlah_baris'] > len(data_siswa):
                for _ in range(rentang):
                    no_urut = no_urut + 1
                    new_row = [no_urut]
                    data_detail.append(new_row) 
            style_detail = style_detail_mi
            col_width_detail = [6*mm, self.setting['lebar_nama_singkat'] * mm] + [8*mm]*9 + [10*mm] + [8*mm]*3 + [12*mm]  

        ## TABEL MD
        elif self.data['jenjang'] == 'MD':
            rt_harian = RotatedParagraph("RT HARIAN", w = 5*mm, h=20*mm)
            hadir = RotatedParagraph("KEHADIRAN", w = 5*mm, h=22*mm)
            pas_pat = "PAS" if self.data['semester'] == "Ganjil" else "PAT"
            lisan = RotatedParagraph(f"{pas_pat} LISAN", w = 5*mm, h=20*mm)
            tulis = RotatedParagraph(f"{pas_pat} TULIS", w = 5*mm, h=20*mm)
            jumlah = RotatedParagraph("JUMLAH", w = 5*mm, h=20*mm)
            rata2 = RotatedParagraph("RATA2", w = 5*mm, h=20*mm)
            nilai_akhir = RotatedParagraph("NILAI AKHIR", w=5*mm, h=20*mm, )
            header1 = ["#", "Nama Lengkap", "NILAI HARIAN DAN TUGAS", "", "", "", "", "", rt_harian, hadir , lisan,tulis, jumlah, rata2, nilai_akhir]
            header2 = ["", "", "1", "2", "3", "4", "5", "6", "","", "", "", "", ""]
            data_detail.append(header1)
            data_detail.append(header2)
            data_siswa = self.data['data_siswa']
            for row_data in data_siswa:
                new_row = [row_data['no_urut'], row_data['nama_singkat']]
                data_detail.append(new_row)
            
            no_urut = len(data_siswa)
            tinggi_kolom_nama = self.setting['tinggi_baris'] * mm
            if self.setting['jumlah_baris'] < len(data_siswa):
                rentang = 0
                row_height = [None, 18*mm] + [tinggi_kolom_nama]*len(data_siswa)
            else:
                rentang = self.setting['jumlah_baris'] - len(data_siswa)
                row_height = [None, 18*mm] + [tinggi_kolom_nama]* self.setting['jumlah_baris']
            if self.setting['jumlah_baris'] > len(data_siswa):
                for _ in range(rentang):
                    no_urut = no_urut + 1
                    new_row = [no_urut]
                    data_detail.append(new_row)   
            style_detail = style_detail_md
            col_width_detail = [6*mm, self.setting['lebar_nama_singkat'] * mm] + [8*mm]*6 + [10*mm]*7

        # POSISI
        sisi_jilid = self.setting['sisi_jilid'] * cm
        sisi_lain = self.setting['sisi_lain'] * cm 
        h = 10*mm
        y = sisi_lain
        self.paragraf("DAFTAR NILAI", x=sisi_jilid, y= y, w=140*mm, h=h, size=20, alignment=TA_LEFT)
        y += h
        h_header = self.tabel(x = sisi_jilid, y=y, data=data_header, col_width=col_width_header, styles=style_header)
        y += h_header + 2*mm # 3mm adalah jarak dari header ke tabel
        self.tabel(x = sisi_jilid, y=y, data=data_detail, col_width=col_width_detail, row_height=row_height, styles=style_detail)
        self.c.showPage()
        
    def lembar_pengembalian_rapor(self):
        # STYLE / VARIABEL
        sisi_jilid = self.setting['sisi_jilid'] * cm
        sisi_lain = self.setting['sisi_lain'] * cm
        style_tabel_header = TableStyle(
            [   ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                ("SIZE", (0,0), (-1,-1), 10),
            ])
        
        style_tabel_detail = TableStyle(
            [   ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Aptos"),
                ("SIZE", (0,0), (-1,0), 10),
                ("SIZE", (0,1), (-1,-1), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("TOPPADDING", (0,1), (-1,-1), 4),

                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black), 
                ("LINEBELOW", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (1,0), (1,-1), 1, colors.black), 
            ])   
             
        # CONTENT
        kelas = f"{self.data['kelas']} {self.data['jenjang']}"
        tapel_semester = f"{self.data['tapel']}/{self.data['semester']}"
        data_tabel_header = [
            ["Kelas", ":",kelas],
            ["Tapel/Semester", ":", tapel_semester],]
        
        data_siswa = self.data['data_siswa']
        data_detail = [["#", "Nama Lengkap", "Tanggal", "Dikembalikan Oleh", "Keterangan"]]
        for row_data in data_siswa:
            new_row = [row_data['no_urut'], row_data['nama_singkat']]
            data_detail.append(new_row)
        
        no_urut = len(data_siswa)
        tinggi_kolom_nama = self.setting['tinggi_baris'] * mm
        if self.setting['jumlah_baris'] < len(data_siswa):
            rentang = 0
            row_height = [10*mm] + [tinggi_kolom_nama]*len(data_siswa)
        else:
            rentang = self.setting['jumlah_baris'] - len(data_siswa)
            row_height = [10*mm] + [tinggi_kolom_nama]*self.setting['jumlah_baris']
        if self.setting['jumlah_baris'] > len(data_siswa):
            for _ in range(rentang):
                no_urut = no_urut + 1
                new_row = [no_urut]
                data_detail.append(new_row)  

        # POSISI
        x = sisi_jilid
        y = sisi_lain
        h = 10*mm
        self.paragraf("PENGEMBALIAN RAPOR", font="Aptos Bold", x=x, y= y, w=140*mm, h=h, size=20, alignment=TA_LEFT)
        y += h
        h = self.tabel(x = x, y=y, data=data_tabel_header, col_width=[30*mm, 5*mm, 50*mm], styles=style_tabel_header)
        y += h
        self.tabel(x = x, y=y, data=data_detail, col_width=[8*mm, 55*mm] + [36*mm]*3, row_height=row_height, styles=style_tabel_detail)
        self.c.showPage()
    
    def lembar_penyerahan_rapor(self):
        # STYLE
        sisi_jilid = self.setting['sisi_jilid'] * cm
        sisi_lain = self.setting['sisi_lain'] * cm
        style_tabel_header = TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos"),
                ("SIZE", (0,0), (-1,-1), 10),
            ]
        )

        style_detail = TableStyle(
            [   ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Aptos"),
                ("SIZE", (0,0), (-1,0), 10),
                ("SIZE", (0,1), (-1,-1), 8),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("TOPPADDING", (0,1), (-1,-1), 4),

                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black), 
                ("LINEBELOW", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (1,0), (1,-1), 1, colors.black), 
            ])

        # KONTEN
        data_siswa = self.data['data_siswa']

        kelas = f"{self.data['kelas']} {self.data['jenjang']}"
        tapel_semester = f"{self.data['tapel']}/{self.data['semester']}"
        data_tabel_header = [
            ["Kelas", ":",kelas],
            ["Tapel/Semester", ":", tapel_semester],
        ]

        data_detail = [["#", "Nama Lengkap", "Tanggal", "Dikembalikan Oleh", "Keterangan"]]
        for row_data in data_siswa:
            new_row = [row_data['no_urut'], row_data['nama_singkat']]
            data_detail.append(new_row)
        no_urut = len(data_siswa)
        tinggi_kolom_nama = self.setting['tinggi_baris'] * mm
        if self.setting['jumlah_baris'] < len(data_siswa):
            rentang = 0
            row_height = [10*mm] + [tinggi_kolom_nama]*len(data_siswa)
        else:
            rentang = self.setting['jumlah_baris'] - len(data_siswa)
            row_height = [10*mm] + [tinggi_kolom_nama]*self.setting['jumlah_baris']
        if self.setting['jumlah_baris'] > len(data_siswa):
            for _ in range(rentang):
                no_urut = no_urut + 1
                new_row = [no_urut]
                data_detail.append(new_row)

        # POSISI
        x = sisi_jilid
        y = sisi_lain
        h = 10*mm
        self.paragraf("PENYERAHAN RAPOR", font="Aptos Bold", x=x, y= y, w=140*mm, h=h, size=20, alignment=TA_LEFT)
        y += h
        h = self.tabel(x = x, y=y, data=data_tabel_header, col_width=[30*mm, 5*mm, 47*mm], styles=style_tabel_header)
        y += h
        self.tabel(x = x, y=y, data=data_detail, col_width=[8*mm, 55*mm] + [36*mm]*3, row_height=row_height, styles=style_detail)
        self.c.showPage()

    def lembar_identitas(self):
        kelas = f"{self.data['kelas']} {self.data['jenjang']}"
        judul = para(f"IDENTITAS SISWA KELAS {kelas}", font='Aptos Bold', size=16)
        lebar_kolom_nama = self.setting['lebar_nama_lengkap']

        col_width = [8*mm, 23*mm, lebar_kolom_nama * mm, 8*mm, 30*mm, self.setting['lebar_nama_ayah']*mm, self.setting['lebar_nama_ibu']*mm, self.setting['lebar_alamat']*mm, 22*mm]
        tinggi_kolom_nama = self.setting['tinggi_baris'] * mm
        row_height = [7*mm] + [tinggi_kolom_nama]*len(self.data['data_siswa'])
        header_table = ["#", "NIS Lokal", "Nama Lengkap", "JK", "Tanggal Lahir","Ayah", "Ibu", "Alamat", "Status Awal"]
        table_data = []
        table_data.append(header_table)
        no = 1
        for row_data in self.data['data_siswa']:
            ttl = f"{date_to_text(row_data['tgl_lahir'], 'lengkap')}"
            no_urut = row_data['no_urut'] if row_data['no_urut'] else no
            nis = row_data['nis_lokal']
            nama = row_data['nama_lengkap']
            jk = row_data['jk']
            ayah = row_data['ayah_nama']
            ibu = row_data['ibu_nama']
            kp = row_data['kampung']
            status_awal = row_data['status_awal']
            new_row = [no_urut, nis, nama, jk, ttl, ayah, ibu, kp, status_awal]
            table_data.append(new_row)
            no += 1
        
        table_style = TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (2, 1), (-1, -1), "LEFT"),
                ("ALIGN", (3, 1), (3, -1), "CENTER"),
                ("ALIGN", (-1, 1), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Aptos Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Aptos Narrow"),
                ("SIZE", (0,0), (-1,0), 10),
                ("SIZE", (0,1), (-1,-1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("TOPPADDING", (0,1), (-1,-1), 4),
                ("BOTTOMPADDING", (0,1), (-1,-1), 4),
                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black), 
                ("LINEBELOW", (0,0), (-1,0), 1, colors.black),
            ])
        
        tabel = Table(
            data=table_data,
            colWidths=col_width,
            rowHeights=row_height,
            hAlign="LEFT",
            repeatRows=1,
            style = table_style
        )
        elemen = [judul,v_spacer(5), tabel,PageBreak()]
        self.elemen.extend(elemen)

    def tabel(self, x, y, data, col_width = None, row_height=None, styles=None)->float:
        table = Table(data, colWidths=col_width, rowHeights=row_height)
        if styles is None:
            styles = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
        table.setStyle(styles)
        table.wrapOn(self.c, aW=self.width, aH=self.height)
        table_height = table._height
        y_new = self.height - (y) - table_height
        table.drawOn(self.c, x = x, y = y_new)
        return table_height  

    def paragraf(self, text, x=0, y=0, w=100*mm, h=5*mm, font= 'Aptos Bold',size=12, alignment=TA_CENTER, leading=0, showBoundary= 0):
        style = ParagraphStyle(name='Normal', fontName=font, fontSize=size, leading=leading, alignment=alignment)
        paragraph = Paragraph(text, style)
        frame = Frame(x, self.height - y-h, w, h, showBoundary=showBoundary, topPadding=0, bottomPadding=0)
        frame.addFromList([paragraph], self.c)

    def image(self, path, x=0, y=0, h=2.0*cm):
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else: 
            base_path = os.path.abspath(".")
        path = os.path.join(base_path, path)
        x = x
        y = self.height - y
        h = h
        image = ImageReader(path)
        image_w, image_h = image.getSize()
        ratio = h / (image_h)
        w = (image_w)*ratio
        gambar = self.c.drawImage(path, x, y, w, h)
        
        return gambar


class RotatedText(Flowable):
    """Flowable to create rotated text."""
    def __init__(self, text, x = 0, y = 0, size = 10, font='TNR'):
        Flowable.__init__(self)
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.font = font

    def draw(self):
        self.canv.saveState()
        self.canv.translate(0, 0)
        self.canv.rotate(90)
        self.canv.setFont(self.font, self.size)
        self.canv.drawString(self.x, self.y, self.text)
        self.canv.restoreState()


class RotatedParagraph(Flowable):
    """Flowable untuk membuat paragraf berotasi dengan boundary."""
    def __init__(self, text, x=0, y=0, w=5*mm, h=20*mm, font='Aptos Bold', size=10, alignment=TA_CENTER, leading=0, showBoundary=0):
        Flowable.__init__(self)
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.size = size
        self.alignment = alignment
        self.leading = leading or 1.2 * size  # default leading if not provided
        self.showBoundary = showBoundary


        # Set up paragraph style
        self.style = ParagraphStyle(
            name='RotatedParagraphStyle',
            fontName=self.font,
            fontSize=self.size,
            leading=self.leading,
            alignment=self.alignment,
            # borderWidth = 1,
            # borderColor = colors.red
        )

    def wrap(self, *args):
        return self.w, self.h

    def draw(self):
        # Buat objek Paragraph
        paragraph = Paragraph(self.text, self.style)
        width, height = self.wrap(0, 0)

        self.canv.saveState()
        self.canv.translate((self.x - self.h + self.w), self.y)
        self.canv.rotate(90)
        self.canv.translate(0, -height)

        # Buat Frame untuk membatasi area paragraf
        frame = Frame(0, 0,  height, width, showBoundary=self.showBoundary, topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
        frame.addFromList([paragraph], self.canv)
        self.canv.restoreState()

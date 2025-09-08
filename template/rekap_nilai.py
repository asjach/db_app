from reportlab.lib.pagesizes import A4, landscape, GOV_LEGAL
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.units import cm, mm
from io import BytesIO
import decimal
from utils.fungsi.pdf_function import *

class TemplateRekapNilai:
    def __init__(self, parent=None):
        self.parent = parent

    
    def build_pdf_peringkat(
            self, top = 1*cm, left=1*cm, bottom = 1*cm, right = 1*cm, 
            orientasi = 'Portrait', 
            kertas=GOV_LEGAL, 
            data_peringkat=None,
            opsi_peringkat = None,
            ):
        if orientasi == "Landscape":
            pagesize = landscape(kertas)
        else:
            pagesize = kertas
        jenjang = self.parent.jenjang
        tapel = self.parent.tapel
        semester = self.parent.semester
        JENJANG = 'IBTIDAIYAH' if jenjang == 'MI' else 'DINIYAH ULA'
        if semester:
            semester = para(f"SEMESTER {semester.upper()}", font='Aptos Bold', size=16)
        buffer = BytesIO()
        pdf = SimpleDocTemplate(
            buffer,
            pagesize=pagesize,
            topMargin=top * cm,
            leftMargin=left * cm,
            rightMargin=right * cm,
            bottomMargin=bottom * cm,
        )
        tapel = para(f"TAHUN PELAJARAN {tapel}", font='Aptos Bold', size=16)
        col_width = [1*cm, 1*cm, 6*cm, 4.2*cm, 4.2*cm, 3*cm, 1.2*cm]
        style = TableStyle(
            [   ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (2, 1), (-1, -1), "LEFT"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("FONTNAME", (0,0), (-1,0), "Aptos Bold"),
                ("FONTNAME", (0,1), (-1,-1), "Aptos Narrow"),
                ("FONTSIZE", (0,0), (-1,-1), 9),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
            ]
        )
        style = style
        if opsi_peringkat == 1:
            judul = para("DAFTAR PERINGKAT PERTAMA PERKELAS", font='Aptos Bold', size=16)
            judul_jenjang = para(f"JENJANG {JENJANG}", font='Aptos Bold', size=14)
            tabel_nilai = Table(data_peringkat, repeatRows=1, hAlign="LEFT", colWidths=col_width, style=style)
            elements = [
                judul, v_spacer(2),
                tapel, v_spacer(2), 
                semester, v_spacer(10), 
                judul_jenjang, v_spacer(2),  
                tabel_nilai
            ]
            
        elif opsi_peringkat == 3:
            judul = para("DAFTAR PERINGKAT 3 BESAR", font='Aptos Bold', size=16)
            judul_jenjang = para("JENJANG IBTIDAIYAH", font='Aptos Bold', size=14)
            row_height = [1*cm] + [5*mm] * (len(data_peringkat)-1)
            tabel_nilai = Table(data_peringkat, repeatRows=1, hAlign="LEFT", colWidths=col_width, rowHeights=row_height)
            for i in range(1, len(data_peringkat)):
                if i % 3 == 0:
                    style.add("LINEBELOW", (0, i), (-1, i), 1, colors.black)
                    if not i < 3:
                        style.add("SPAN", (0, i-2), (0, i))
            tabel_nilai.setStyle(style)
            elements = [
                judul, 
                v_spacer(2),
                tapel, 
                v_spacer(2), 
                semester, 
                v_spacer(10), 
                judul_jenjang, 
                v_spacer(2),  
                tabel_nilai
            ]
        pdf.build(elements)
        pdf_value = buffer.getvalue()
        buffer.close()
        return pdf_value
        
    def build_pdf(
            self, top=1 * cm, left=1 * cm, bottom=1 * cm, right=1 * cm, 
            orientasi="Portrait", kertas=GOV_LEGAL, data_detail = None):
        if orientasi == "Landscape": pagesize = landscape(kertas)
        else: pagesize = kertas
        buffer = BytesIO()
        pdf = SimpleDocTemplate(
            buffer,
            pagesize=pagesize,
            topMargin=top * cm,
            leftMargin=left * cm,
            rightMargin=right * cm,
            bottomMargin=bottom * cm,
        )
        jenjang = self.parent.jenjang
        tapel = self.parent.tapel
        kegiatan = self.parent.kegiatan
        judul = para("REKAP NILAI RAPOR", font='Aptos Bold', size=16)
        header_data = [
            ["Jenjang", ":", jenjang, "", "Kelas", ":", f"{self.parent.kelas}"],
            ["Tapel", ":", tapel, "", "Wali Kelas", ":", f"{self.parent.wali_kelas}"],
            ["Kegiatan Evaluatif", ":", kegiatan, "", "Titimangsa Rapor", ":", f"{self.parent.tgl_titimangsa}"],
        ]
        style_header = TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos Narrow"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("FONTNAME", (2, 0), (2, -1), "Aptos Narrow Bold"),
                ("FONTNAME", (6, 0), (6, -1), "Aptos Narrow Bold"),

            ]
        )
        col_width = [30*mm, 3*mm, 50*mm, 10*mm, 30*mm, 3*mm, 30*mm]
        table_header = Table(header_data, style=style_header, colWidths=col_width, hAlign="LEFT")
        # Create a table with the data
        header = data_detail[0]
        row_height = [12*mm] + [self.parent.tinggi_baris_spin.value()*cm]*(len(data_detail)-1)
        col_width = [8*mm, self.parent.kolom_nama_spin.value()*cm, 10*mm] + [self.parent.kolom_pelajaran_spin.value()*cm] * (len(header)-6) + [10*mm, 10*mm, 9*mm]
        
        for index in range(3, len(header)):
            pelajaran = RotatedParagraph(header[index], h=10, font='Aptos Bold', size=9)
            data_detail[0][index] = pelajaran
        table = Table(data_detail, repeatRows=1, hAlign="LEFT", rowHeights=row_height, colWidths=col_width)
        # Add style to the table
        style = TableStyle(
            [   ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("ALIGN", (1, 1), (1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, -1), "Aptos Narrow"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("SPAN", (0, -1), (2, -1)),
                ("FONTNAME", (0,0), (-1,0), "Aptos Bold"),
                ("FONTNAME", (0,-1), (-1,-1), "Aptos Bold"),
                ("FONTNAME", (-3,1), (-2,-2), "Aptos Bold"),
                ("LINEABOVE", (0,0), (-1,0), 1, colors.black),
                ("LINEBELOW", (0,0), (-1,0), 1, colors.black),
                ("LINEABOVE", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBELOW", (0,-1), (-1,-1), 1, colors.black),
                ("LINEBEFORE", (0,0), (0,-1), 1, colors.black),
                ("LINEBEFORE", (3,0), (3,-1), 1, colors.black),
                ("LINEBEFORE", (-3,0), (-3,-1), 1, colors.black),
                ("LINEAFTER", (-1,0), (-1,-1), 1, colors.black),
            ]
        )
        for i in range(1, len(data_detail)):
            if i % 2 == 0:
                bg_color = colors.white
            else:
                bg_color = colors.HexColor('#cbf2f1')
            style.add("BACKGROUND", (0, i), (-1, i), bg_color)

        for row_idx, row in enumerate(data_detail):
            if row_idx == 0:
                continue  # Skip header row
            for col_idx in range(len(row)-1, len(row)):
                cell = row[col_idx]
                if cell == "1":
                    style.add("BACKGROUND", (0, row_idx), (col_idx, row_idx), colors.lightgreen)
                    style.add("FONTNAME", (0, row_idx), (col_idx, row_idx), "Aptos Bold")
                if cell == "2":
                    style.add("BACKGROUND", (0, row_idx), (col_idx, row_idx), colors.yellow)
                    style.add("FONTNAME", (0, row_idx), (col_idx, row_idx), "Aptos Bold")
                if cell == "3":
                    style.add("BACKGROUND", (0, row_idx), (col_idx, row_idx), colors.lightsalmon)
                    style.add("FONTNAME", (0, row_idx), (col_idx, row_idx), "Aptos Bold")

                
            for col_idx in range(3, len(row) - 1):  # Iterate from column 4 to the second last column
                cell = row[col_idx]
                if isinstance(cell, str) and cell.isdigit():
                    cell = int(cell)
                try:
                    if isinstance(cell, (int, float, decimal.Decimal)) and cell < self.parent.nilai_merah_spin.value():
                        style.add("BACKGROUND", (col_idx, row_idx), (col_idx, row_idx), colors.HexColor('#fdb3b3'))
                        style.add("TEXTCOLOR", (col_idx, row_idx), (col_idx, row_idx), colors.black)
                        style.add("FONTSIZE", (col_idx, row_idx), (col_idx, row_idx), 10)
                except ValueError:
                    pass
        table.setStyle(style)
        elements = [judul, v_spacer(5), table_header, v_spacer(2) , table]
        pdf.build(elements)

        pdf_value = buffer.getvalue()
        buffer.close()
        return pdf_value
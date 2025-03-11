from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.platypus import Paragraph, Spacer, Frame, Table, TableStyle
from reportlab.platypus.flowables import Flowable
from utils.fungsi.table_functions import header_for_table, format_cell_data
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
from PySide6.QtPdf import QPdfDocument
import sys, os
from reportlab.lib.utils import ImageReader

pdfmetrics.registerFont(TTFont("TNR", "times.ttf"))
pdfmetrics.registerFont(TTFont("TNRB", "timesbd.ttf"))
pdfmetrics.registerFont(TTFont("TNRI", "timesi.ttf"))
pdfmetrics.registerFont(TTFont("Aptos Bold", "C:/APP/DB App/resources/font/Aptos Bold.ttf"))
pdfmetrics.registerFont(TTFont("Aptos Narrow", "C:/APP/DB App/resources/font/Aptos Narrow.ttf"))
pdfmetrics.registerFont(TTFont("Aptos Narrow Bold", "C:/APP/DB App/resources/font/Aptos Narrow Bold.ttf"))
pdfmetrics.registerFont(TTFont("Aptos", "C:/APP/DB App/resources/font/Aptos.ttf"))
pdfmetrics.registerFont(TTFont("Aptos Italic", "C:/APP/DB App/resources/font/Aptos Italic.ttf"))
pdfmetrics.registerFont(TTFont("Aptos Narrow Italic", "C:/APP/DB App/resources/font/Aptos Narrow Italic.ttf"))


def para(teks, font='Aptos', size=12, leading=12, color=colors.black, bg_color=colors.white, alignment=0):
    '''
    alignment: 
        0 = left, 
        1 = center, 
        2 = right, 
        4 = justify
    '''
    style = ParagraphStyle(
        'Judul', 
        fontName = font,
        fontSize = size,
        leading = leading,
        textColor = color,
        backColor = bg_color,
        alignment = alignment
    )
    paragraf = Paragraph(text = teks, style = style)
    return paragraf

def v_spacer(tinggi=0):
    '''dalam mm'''
    return Spacer(0, tinggi*mm)

def h_spacer(lebar=0):
    '''dalam mm'''
    return Spacer(lebar*mm, 0)



class RotatedParagraph(Flowable):
    """Flowable untuk membuat paragraf berotasi dengan boundary."""
    def __init__(self, text, x=0, y=0, w=5, h=20, font='Times-Roman', size=10, alignment=1, leading=0, showBoundary=0):
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
        return self.w * mm, self.h * mm

    def draw(self):
        # Buat objek Paragraph
        paragraph = Paragraph(self.text, self.style)
        width, height = self.wrap(0, 0)

        self.canv.saveState()
        self.canv.translate((self.x - self.h + self.w) *mm, self.y * mm)
        self.canv.rotate(90)
        self.canv.translate(0, -height)

        # Buat Frame untuk membatasi area paragraf
        frame = Frame(0, 0,  height, width, showBoundary=self.showBoundary, topPadding=0, bottomPadding=0, leftPadding=0, rightPadding=0)
        frame.addFromList([paragraph], self.canv)
        self.canv.restoreState()
        
def tabel_template(data, style=None, col_width=None, h_align = "LEFT"):
    if len(data) > 0:
        data = convert_mysql_to_reportlab(data)
        if style is None:
            style = TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Aptos Narrow'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ])
        tabel = Table(
            data=data,
            style=style,
            colWidths=col_width,
            hAlign=h_align,
        )    
        return tabel    

def tabel(canvas, x, y, width, height, data, col_width = None, row_height=None, styles=None):
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
        table.wrapOn(canvas, aW=width, aH=height)
        table_height = table._height
        y_new = height - (y * mm) - table_height
        table.drawOn(canvas, x = x*mm, y = y_new)
        return table_height
    
def paragraf(canvas, text='', x=0, y=0, height=None, w=100, h=5, font= 'TNRB',size=11, alignment=2, leading=0, showBoundary= 0):
        style = ParagraphStyle(name='Normal', fontName=font, fontSize=size, leading=leading, alignment=alignment)
        paragraph = Paragraph(text, style)
        frame = Frame(x*mm, height - y*mm, w*mm, h*mm, showBoundary=showBoundary, topPadding=0, bottomPadding=0)
        frame.addFromList([paragraph], canvas)
        
def convert_mysql_to_reportlab(data):
    if not data:
        return []
    header = list(data[0].keys())
    header_tbl = header_for_table(header)
    table_data = [header_tbl]
    for row in data:
        table_data.append([format_cell_data(row[key], zero="") for key in header])
    return table_data

def tabel_style_grid():
    style = TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            # ('TOPPADDING', (0, 0), (-1, -1), 6),
            # ('VOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('FONTNAME', (0, 1), (-1, -1), 'Aptos Narrow'),
            ('SIZE', (0, 1), (-1, -1), 10),
        ]
    )
    return style

def tabel_style_nogrid():
    style = TableStyle(
        [
            ('FONTNAME', (0, 0), (-1, -1), 'Aptos Narrow'),
            ('FONTNAME', (-1, 0), (-1, -1), 'Aptos Bold'),
            ('SIZE', (0, 0), (-1, -1), 10),
        ]
    )
    return style

def paragraf(c, height, text, x=0, y=0, w=100, h=5, font= 'TNRB',size=11, alignment=1, leading=0, showBoundary= 0):
    style = ParagraphStyle(name='Normal', fontName=font, fontSize=size, leading=leading, alignment=alignment)
    paragraph = Paragraph(text, style)
    frame = Frame(x*mm, height - y*mm, w*mm, h*mm, showBoundary=showBoundary, topPadding=0, bottomPadding=0)
    frame.addFromList([paragraph], c)

def gambar(c, height, path, x=0, y=0, h=20):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else: 
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, path)
    x = x * mm
    y = height - y * mm
    h = h * mm
    image = ImageReader(path)
    image_w, image_h = image.getSize()
    ratio = h / (image_h*mm)
    w = (image_w *mm)*ratio
    gambar = c.drawImage(path, x, y, w, h)
    return gambar

def tabel(c, width, height, x, y, data, col_width = None, row_height=None, styles=None):
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
    table.wrapOn(c, aW=width, aH=height)
    table_height = table._height
    y_new = height - (y * mm) - table_height
    table.drawOn(c, x = x*mm, y = y_new)
    return table_height
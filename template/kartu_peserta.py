from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter, landscape, portrait
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from utils.fungsi.general_functions import *
from reportlab.lib.colors import HexColor

class TemplateKartuPeserta:
    def __init__(self, parent=None, data=None):
        self.parent = parent
        self.data = data
        self.height = 0
        self.width = 0
        self.init_data()
    
    def init_data(self):
        self.setting_kartu = self.data.get('setting_kartu', {})
        self.lebar_kartu = self.setting_kartu.get('lebar_kartu', 1) * cm
        self.tinggi_kartu = self.setting_kartu.get('tinggi_kartu', 1) * cm
        self.horizontal_gap = self.setting_kartu.get('horizontal_gap', 0.05) * cm
        self.vertical_gap = self.setting_kartu.get('vertical_gap', 0.05) * cm
        self.left_margin = self.setting_kartu.get('left_margin', 1) * cm
        self.top_margin = self.setting_kartu.get('top_margin', 1) * cm
        self.page_size = self.setting_kartu.get('page_size', 'A4')
        self.orientation = self.setting_kartu.get('orientation', 'portrait').lower()
        self.peserta_data = self.data.get('data_peserta', [])
    
    def calculate_grid(self, page_width, page_height):
        """Menghitung jumlah kartu yang muat dalam satu halaman"""
        # Hitung jumlah kartu horizontal
        available_width = page_width - 2 * self.left_margin
        cards_per_row = int((available_width + self.horizontal_gap) / 
                           (self.lebar_kartu + self.horizontal_gap))
                          
        # Hitung jumlah kartu vertikal
        available_height = page_height - 2 * self.top_margin
        cards_per_col = int((available_height + self.vertical_gap) / 
                         (self.tinggi_kartu + self.vertical_gap))
        
        return cards_per_row, cards_per_col
    
    def draw_card(self, c, x, y, peserta):
        """Menggambar satu kartu peserta pada posisi x,y"""
        setting = self.data.get('setting_kartu')
        # Gambar border kartu
        

        if setting['font'] != '':
            font = setting['font']
        else:
            font = 'Times New Roman Bold'
        # BACKGROUND KARTU
        if setting['background'] != '':

            background = setting['background']
            img = ImageReader(background)
            c.drawImage(img, x, y, 
                        width = self.lebar_kartu, 
                        height=self.tinggi_kartu, 
                        preserveAspectRatio=True
            )
        else:
            c.rect(x, y, self.lebar_kartu, self.tinggi_kartu)

        # NAMA
        if setting['nama']:
            paragraf(
                obj=self,
                text=f"{peserta.get('nama_lengkap', '')}",
                x=(x + setting['x_nama']*cm)/mm,
                y=( - y  + self.tinggi_kartu*mm + setting['y_nama']*cm -12*mm)/mm,
                w=75,
                h=12,
                showBoundary=0,
                font=font,
                size=setting['size_nama'],
                leading=12,
            )

        # TTL
        if setting['ttl']:
            c.setFont(font, setting['size_ttl'])
            c.drawString(x + setting['x_ttl']*cm, y + self.tinggi_kartu - setting['y_ttl']*cm, f"{peserta.get('ttl', '')}")

        # NOPES
        if setting['nopes']:
            c.setFont(font, setting['size_nopes'])
            c.drawString(x + setting['x_nopes']*cm, y + self.tinggi_kartu - setting['y_nopes']*cm, f"{peserta.get('no_peserta', '')}")
        
        # KELAS
        if setting['kelas']:
            c.setFont(font, setting['size_kelas'])
            c.drawString(x + setting['x_kelas']*cm, y + self.tinggi_kartu - setting['y_kelas']*cm, f"{peserta['kelas']}")
        
        # NO INDUK
        if setting['no_induk']: 
            c.setFont(font, setting['size_no_induk'])
            c.drawString(x + setting['x_no_induk']*cm, y + self.tinggi_kartu - setting['y_no_induk']*cm, f"{peserta.get('nis_lokal', '')}")
        # NISN
        if setting['nisn']: 
            c.setFont(font, setting['size_nisn'])
            c.drawString(x + setting['x_nisn']*cm, y + self.tinggi_kartu - setting['y_nisn']*cm, f"{peserta.get('nisn', '')}")
        # FOTO
        if setting['foto']:
            # if peserta.get('foto') not in [None, '']:
            if peserta.get('foto'):
                path = f'{value_from_db('DOKUMEN_PATH')}/siswa/{peserta.get('foto')}'
                foto = ImageReader(path)
                c.drawImage(foto, 
                            x + setting['x_foto']*cm, 
                            y + self.tinggi_kartu - setting['y_foto']*cm - setting['h_foto']*cm, 
                            width= setting['w_foto']*cm, 
                            height= setting['h_foto']*cm, 
                            preserveAspectRatio=True)

    def build_pdf(self):
        """Membuat PDF dengan semua kartu peserta"""
        if self.peserta_data:
            # Tentukan ukuran halaman
            if self.page_size.upper() == 'A4':
                page_size = A4
            elif self.page_size.upper() == 'F4':
                page_size = (215*mm, 330*mm)
            else:
                page_size = letter
            if self.orientation == 'landscape':
                page_width, page_height = landscape(page_size)
                self.width, self.height = landscape(page_size)
            else:
                page_width, page_height = portrait(page_size)
                self.width, self.height = portrait(page_size)
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=(page_width, page_height))
            self.c = c
            # Hitung jumlah kartu per halaman
            cards_per_row, cards_per_col = self.calculate_grid(page_width, page_height)
            cards_per_page = cards_per_row * cards_per_col
            
            for i, peserta in enumerate(self.peserta_data):
                # Hitung posisi kartu dalam halaman
                page_position = i % cards_per_page
                if page_position == 0 and i > 0:
                    c.showPage()  # Buat halaman baru
                
                row = (page_position // cards_per_row)
                col = page_position % cards_per_row
                
                x = self.left_margin + col * (self.lebar_kartu + self.horizontal_gap)
                y = page_height - self.top_margin - (row + 1) * self.tinggi_kartu - row * self.vertical_gap
                
                # Gambar kartu
                self.draw_card(c, x, y, peserta)
            
            c.save()
            buffer.seek(0)
            return buffer

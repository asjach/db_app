from PySide6.QtWidgets import QWidget, QMainWindow, QFileDialog, QMessageBox
from utils.fungsi.general_functions import *
from utils.fungsi.functions import read_excel
from ui.ui_page_input_nilai import Ui_Form
from models.nilai.input_nilai import InputNilai
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
from collections import defaultdict
import os


class PageInputNilai(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = InputNilai()
        self.cbo_kegiatan.currentIndexChanged.connect(self.cbo_kegiatan_selected)
        self.btn_template_nilai.clicked.connect(lambda:self.create_template('nilai'))
        self.btn_template_walas.clicked.connect(lambda:self.create_template('walas'))
        self.btn_template_rekap.clicked.connect(lambda:self.create_template('rekap'))
        self.btn_browse.clicked.connect(self.browse_btn_clicked)
        self.btn_save.clicked.connect(self.save_btn_clicked)
        self.btn_new_default_path.clicked.connect(self.browse_save_folder)
        self.cbo_jenjang = self.parent.cbo_jenjang
        self.cbo_tapel = self.parent.cbo_tapel
        self.cbo_tingkat = self.parent.cbo_tingkat
        self.cbo_kelas = self.parent.cbo_kelas
        
    def init_default_folder(self):
        default_path = self.SQL.get_path(
            jenjang=self.cbo_jenjang.currentText(),
            tapel = self.cbo_tapel.currentText(),
            kegiatan=self.cbo_kegiatan.currentText(),
            kolom="path_folder_nilai")
        if default_path:
            self.pte_default_path.setPlainText(default_path[0]['path_folder_nilai'])
        else:
            self.pte_default_path.clear()

    def init_file_rekap_nilai(self):
        file_rekap_nilai = self.SQL.get_path(
            jenjang=self.cbo_jenjang.currentText(),
            tapel = self.cbo_tapel.currentText(),
            kegiatan=self.cbo_kegiatan.currentText(),
            kolom="path_file_rekap")
        if file_rekap_nilai:
            self.pte_excel_path.setPlainText(file_rekap_nilai[0]['path_file_rekap'])
        else:
            self.pte_excel_path.clear()

    def browse_save_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Pilih Folder Penyimpanan Template",
            self.pte_default_path.toPlainText())
        if folder_path:
            self.pte_default_path.setPlainText(folder_path)
            self.SQL.update_path(
                jenjang=self.cbo_jenjang.currentText(),
                tapel=self.cbo_tapel.currentText(),
                kegiatan=self.cbo_kegiatan.currentText(),
                kolom="path_folder_nilai",
                nilai=self.pte_default_path.toPlainText())
    
    def browse_btn_clicked(self):
        open_dialog(self, self.pte_excel_path)
        if self.pte_excel_path.toPlainText() !='':
            self.SQL.update_path(
                jenjang=self.cbo_jenjang.currentText(),
                tapel = self.cbo_tapel.currentText(),
                kegiatan=self.cbo_kegiatan.currentText(),
                kolom="path_file_rekap",
                nilai=self.pte_excel_path.toPlainText())

    def get_template_filename(self, opsi):
        save_path = self.pte_default_path.toPlainText()
        if opsi == 'nilai':
            filename = f"Blanko Input Nilai {self.cbo_kegiatan.currentText()}_{self.cbo_kelas.currentText()} {self.cbo_jenjang.currentText()}.xlsx"
        elif opsi == 'walas':
            filename = f"Blanko Input Catatan Walas_{self.cbo_kegiatan.currentText()}_{self.cbo_kelas.currentText()} {self.cbo_jenjang.currentText()}.xlsx"
        elif opsi == 'rekap':
            filename = f"Rekap Nilai_{self.cbo_kegiatan.currentText()} {self.cbo_jenjang.currentText()} {self.cbo_tapel.currentText()}.xlsx"
        else:
            return None
        return os.path.join(save_path, filename)

    def show_page(self): 
        self.fill_kegiatan_cbo()

    def fill_kegiatan_cbo(self):
        data = self.SQL.get_id_kegiatan(
            jenjang=self.cbo_jenjang.currentText(),
            tapel=self.cbo_tapel.currentText())
        self.cbo_kegiatan.clear()
        for item in data:
            self.cbo_kegiatan.addItem(item['kegiatan'], userData=item['id'])
        
    def cbo_kegiatan_selected(self):
        self.init_default_folder()
        self.init_file_rekap_nilai()
        self.fill_table()

    def template_nilai(self, data):
        jenjang = self.cbo_jenjang.currentText()
        kolom = ["no_urut", "nis_lokal", "nama_lengkap", "kelas"]
        filename = self.get_template_filename('nilai')
        if jenjang == "MI":
            kolom_tambahan = [f"nh{i}" for i in range(1, 9)] + ["nrh", "tulis", "lisan", "nilai"]
        elif jenjang == "MD":
            kolom_tambahan = [f"nh{i}" for i in range(1, 7)] + ["nrh", "harian", "tulis", "lisan", "nilai"]
        df = pd.DataFrame(data, columns=kolom)
        for col in kolom_tambahan:
            df[col] = ""
        df.to_excel(filename, index=False)
        wb = load_workbook(filename)
        ws = wb.active
        if jenjang == "MI":
            for row in range(2, len(df) + 2):
                ws[f"M{row}"] = f"=AVERAGE(E{row}:L{row})"  # nrh
                ws[f"P{row}"] = f"=(M{row} * 0.6) + (AVERAGE(N{row}:O{row}) * 0.4)"
        elif jenjang == "MD":
            for row in range(2, len(df) + 2):
                ws[f"K{row}"] = f"=AVERAGE(E{row}:J{row})"
                ws[f"O{row}"] = f"=AVERAGE(K{row}:N{row})"
        exclude_column = ['nrh', 'nilai']
        all_columns = kolom + kolom_tambahan
        for col_idx, col_name in enumerate(all_columns, start=1):
            if col_name in exclude_column:
                continue
            max_length = max(
                len(str(col_name)),  
                *(len(str(ws.cell(row=row_idx, column=col_idx).value)) for row_idx in range(1, len(df) + 2)))
            ws.column_dimensions[get_column_letter(col_idx)].width = max_length + 2
        wb.save(filename)

    def template_walas(self, data):
        filename = self.get_template_filename('walas')
        kolom = ["no_urut", "nis_lokal", "nama_lengkap", "kelas"]
        kolom_tambahan = ['sakit', 'ijin', 'alpa', 'catatan_walas']
        df = pd.DataFrame(data, columns=kolom)
        for col in kolom_tambahan:
            df[col] = ""
        df.to_excel(filename, index=False)
        wb = load_workbook(filename)
        ws = wb.active
        all_columns = kolom + kolom_tambahan
        for col_idx, col_name in enumerate(all_columns, start=1):
            max_length = max(
                len(str(col_name)),  
                *(len(str(ws.cell(row=row_idx, column=col_idx).value)) for row_idx in range(1, len(df) + 2)))
            ws.column_dimensions[get_column_letter(col_idx)].width = max_length + 2
        wb.save(filename)

    def template_rekap(self, data):
        filename = self.get_template_filename('rekap')
        jenjang = self.cbo_jenjang.currentText()
        tapel = self.cbo_tapel.currentText()
        tingkat = self.cbo_tingkat.currentText()
        kelas = self.cbo_kelas.currentText()
        kegiatan = self.cbo_kegiatan.currentText()
        kolom = ["id_kelas", "id_kegiatan", "no_urut", "id_peserta", "nis_lokal", "nama_lengkap", "kelas"]
        list_of_dict_mapel = self.SQL.get_list_mapel(jenjang, tapel, kegiatan, '', '')
        merge_mapel = list(dict.fromkeys(d['mapel'] for d in list_of_dict_mapel))
        kolom_tambahan = merge_mapel + ['rata_rata', 'jumlah', 'ranking', 'sakit', 'ijin', 'alpa', 'ranking', 'catatan_walas']
        df = pd.DataFrame(data, columns=kolom)
        for col in kolom_tambahan:
            df[col] = ""
        df.to_excel(filename, index=False)
        wb = load_workbook(filename)
        ws = wb.active
        all_columns = kolom + kolom_tambahan
        kolom_pelajaran_awal = get_column_letter(all_columns.index('kelas')+2)
        end_kolom = get_column_letter(all_columns.index('rata_rata'))
        kolom_jumlah = get_column_letter(all_columns.index('jumlah')+1)
        kolom_rata_rata = get_column_letter(all_columns.index('rata_rata')+1)
        kolom_ranking = get_column_letter(all_columns.index('ranking')+1)
        kelas_ranges = defaultdict(list)
        for row in range(2, len(df) + 2):
            ws[f"{kolom_rata_rata}{row}"] = f"=AVERAGE({kolom_pelajaran_awal}{row}:{end_kolom}{row})"
            ws[f"{kolom_jumlah}{row}"] = f"=SUM({kolom_pelajaran_awal}{row}:{end_kolom}{row})"
        for row_idx, row in enumerate(df.itertuples(), start=2):
            kelas_ranges[row.kelas].append(row_idx)
        for kelas, rows in kelas_ranges.items():
            start_row = rows[0]
            end_row = rows[-1]
            for row in rows:
                ws[f"{kolom_ranking}{row}"] = f"=RANK({kolom_jumlah}{row},${kolom_jumlah}${start_row}:${kolom_jumlah}${end_row})"
        exclude_column = ['rata_rata', 'jumlah', 'ranking']
        all_columns = kolom + kolom_tambahan
        for col_idx, col_name in enumerate(all_columns, start=1):
            if col_name in exclude_column:
                continue
            max_length = max(
                len(str(col_name)),  
                *(len(str(ws.cell(row=row_idx, column=col_idx).value)) for row_idx in range(1, len(df) + 2)))
            ws.column_dimensions[get_column_letter(col_idx)].width = max_length + 2
        wb.save(filename)

    def create_template(self, opsi):
        data_siswa = self.SQL.data_siswa(
            jenjang=self.cbo_jenjang.currentText(), 
            tapel= self.cbo_tapel.currentText(), 
            tingkat= self.cbo_tingkat.currentText(), 
            kelas= self.cbo_kelas.currentText(), 
            kegiatan= self.cbo_kegiatan.currentText()
        )
        if not data_siswa:
            print("Tidak ada data siswa untuk kegiatan ini.")
            return
        if opsi == 'nilai': self.template_nilai(data_siswa)
        elif opsi == 'walas': self.template_walas(data_siswa)
        elif opsi == 'rekap': self.template_rekap(data_siswa)
        print('Template berhasil dibuat')

    def save_btn_clicked(self):
        if self.pte_excel_path.toPlainText() != '':
            data = read_excel(self.pte_excel_path.toPlainText())
            self.save_operation(data)
        else:
            print("Tidak ada file excel yang dipilih")

    def fill_table(self):
        path_rekap = self.pte_excel_path.toPlainText()
        if path_rekap:
            df = pd.read_excel(path_rekap)
            generate_table(
                data=df,
                table=self.input_tbl
            )
        else:
            self.input_tbl.clear()
            self.input_tbl.setRowCount(0)
            self.input_tbl.setColumnCount(0)

    @measure_time
    def save_operation(self, data):
        # Menyimpan data nilai
        MAPEL_NILAI = self.SQL.all_mapel()  # Daftar mata pelajaran yang valid, misalnya ['PAI', 'QDS', 'FKH', ...]
        KEGIATAN_FIELDS = ['no_urut', 'sakit', 'ijin', 'alpa', 'catatan_walas']
        
        # 1. Proses untuk nilai_angka (mata pelajaran)
        # Kumpulkan semua kombinasi kunci untuk pengecekan bulk di nilai_angka
        nilai_keys = [(row['id_peserta'], mapel) for row in data for mapel in MAPEL_NILAI if mapel in row]
        # Cek data yang sudah ada di nilai_angka
        existing_nilai_dict = self.SQL.cek_nilai_bulk(nilai_keys)
        
        # 2. Proses untuk kegiatan_peserta
        # Kumpulkan semua id_peserta untuk pengecekan di kegiatan_peserta
        peserta_keys = [row['id_peserta'] for row in data]
        # Cek data yang sudah ada di kegiatan_peserta
        existing_peserta_dict = self.SQL.cek_peserta_bulk(peserta_keys)
        # Proses setiap baris data dari Excel
        insert_nilai_data = []
        update_nilai_data = []
        insert_peserta_data = []
        update_peserta_data = []
        for row in data:
            id_peserta = int(row['id_peserta'])  # Pastikan integer
            id_kelas = int(row['id_kelas'])
            id_kegiatan = int(row['id_kegiatan'])
            # a. Proses mata pelajaran untuk nilai_angka
            mapel_keys = [key for key in row.keys() if key in MAPEL_NILAI]
            for nama_mapel in mapel_keys:
                nilai = row[nama_mapel]
                if isinstance(nilai, str):
                    nilai = nilai.strip()
                if not nilai or nilai == '':  # Kosong, langsung None
                    nilai = None
                else:  # Cek apakah angka valid
                    try:
                        nilai = float(str(nilai))
                    except ValueError:
                        nilai = None
                # Kunci untuk mencocokkan data yang ada di nilai_angka
                nilai_key = (id_peserta, nama_mapel)
                print(f"Processing nilai key: {nilai_key}, input_nilai={nilai}")
                
                if nilai_key in existing_nilai_dict:
                    id, nilai_db = existing_nilai_dict[nilai_key]
                    print(f"Found in nilai_angka: id={id}, nilai_db={nilai_db}")
                    if nilai != nilai_db:  # Hanya update jika nilai berbeda
                        update_nilai_data.append((nilai, id))
                        print("UPDATE queued for nilai_angka", id, nilai)
                    else:
                        print("No update needed for nilai_angka, values are the same")
                else:
                    insert_nilai_data.append((id_peserta, nama_mapel, nilai))
                    print("INSERT queued for nilai_angka", id_peserta, nama_mapel, nilai)
            
            # b. Proses kolom tambahan untuk kegiatan_peserta
            peserta_data = {field: row.get(field) for field in KEGIATAN_FIELDS}
            peserta_key = id_peserta
            print(f"Processing peserta key: {peserta_key}, input_data={peserta_data}")
            
            if peserta_key in existing_peserta_dict:
                existing_data = existing_peserta_dict[peserta_key]
                # Bandingkan setiap field, update jika ada perbedaan
                if any(peserta_data[field] != existing_data[field] for field in KEGIATAN_FIELDS):
                    update_peserta_data.append((
                        peserta_data['no_urut'], peserta_data['sakit'], peserta_data['ijin'],
                        peserta_data['alpa'], peserta_data['catatan_walas'], 
                        id_peserta
                    ))
                    print("UPDATE queued for kegiatan_peserta", id_peserta, peserta_data)
                else:
                    print("No update needed for kegiatan_peserta, values are the same")
            else:
                insert_peserta_data.append((
                    id_peserta, id_kelas, id_kegiatan,  # id_kelas dan id_kegiatan tidak ada di Excel, set None
                    peserta_data['no_urut'], peserta_data['sakit'], peserta_data['ijin'],
                    peserta_data['alpa'], peserta_data['catatan_walas']
                ))
                print("INSERT queued for kegiatan_peserta", id_peserta, peserta_data)
        
        if insert_nilai_data:
            self.SQL.insert_nilai_bulk(insert_nilai_data)
            pesan_insert_nilai= "Bulk inserted {len(insert_nilai_data)} records to nilai_angka"
        if update_nilai_data:
            self.SQL.update_nilai_bulk(update_nilai_data)
            pesan_update_nilai = f"Bulk updated {len(update_nilai_data)} records in nilai_angka"
        if insert_peserta_data:
            self.SQL.insert_peserta_bulk(insert_peserta_data)
            pesan_insert_peserta = f"Bulk inserted {len(insert_peserta_data)} records to kegiatan_peserta"
        if update_peserta_data:
            self.SQL.update_peserta_bulk(update_peserta_data)
            pesan_update_peserta = f"Bulk updated {len(update_peserta_data)} records in kegiatan_peserta"
        pesan_sukses(
            judul="Berhasil Insert Data",
            pesan=f'{pesan_insert_nilai}\n{pesan_update_nilai}\n{pesan_insert_peserta}\n{pesan_update_peserta}'
            )
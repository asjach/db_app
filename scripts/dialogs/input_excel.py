from PySide6.QtWidgets import QDialog
from ui.ui_dialog_input_excel import Ui_Form
from models.input_excel import ModelInputExcel
from utils.static_values import *
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from utils.fungsi.general_functions import *
import os
import pandas as pd

class DialogInputExcel(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setSizeGripEnabled(True)
        self.SQL = ModelInputExcel()
        self.init_slot_signals()

    def init_slot_signals(self):
        self.cbo_db.currentIndexChanged.connect(self.cbo_db_selected)
        self.cbo_table.currentIndexChanged.connect(self.cbo_table_selected)
        self.btn_no_filter.clicked.connect(self.btn_no_filter_clicked)
        self.btn_browse.clicked.connect(self.on_btn_browse_clicked)
        self.cbo_sheet.currentIndexChanged.connect(self.cbo_sheet_selected)
        self.insert_btn.clicked.connect(self.execute_insert)

    def init_attributes(self):
        self.nama_db = self.cbo_db.currentText()
        self.nama_tabel = self.cbo_table.currentText()

    def show_dialog(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.resize(screen_geometry.width()*0.9, screen_geometry.height()*0.9)
        self.move(
            (screen_geometry.width()-self.width()) // 2,
            (screen_geometry.height()-self.height()) // 2,)
        self.init_attributes()
        self.fill_cbo_db()
    

### BAGIAN TEMPLATE TANPA FILTER
    # mengisi cbo db
    def fill_cbo_db(self):
        daftar_database = self.SQL.get_databases()
        daftar_database.insert(0, "")
        fill_combobox(self.cbo_db, daftar_database)
        fill_combobox(self.cbo_save_to_db, daftar_database)

    # ketika combobox db dipilih
    def cbo_db_selected(self):
        self.SQL.set_db(self.cbo_db.currentText())
        self.fill_cbo_tabel()
        self.generate_namafile_no_filter()
    
    # mengisi cbo tabel
    def fill_cbo_tabel(self):
        daftar_tabel = ["All"]
        daftar_tabel.extend(self.SQL.get_all_tables())
        fill_combobox(self.cbo_table, daftar_tabel)

    def cbo_table_selected(self):
        self.generate_namafile_no_filter()

    # membuat nama file untuk excel no filter
    def generate_namafile_no_filter(self):
        database = self.cbo_db.currentText()
        tabel = self.cbo_table.currentText()
        namafile = f'{database}_{tabel}.xlsx'
        self.line_filename_nofilter.setText(namafile)

    # ketika tombol template no filter ditekan
    def btn_no_filter_clicked(self):
        sukses = False
        nama_file = self.line_filename_nofilter.text()
        namafile = save_as_path(self, nama_file)
        if namafile:
            try:
                sukses = self.create_not_filtered_template(namafile)
                folder_terakhir = os.path.dirname(namafile)
                save_value_to_db("LAST_SELECTED_FOLDER", folder_terakhir)
            except Exception as e:
                print(f"Error creating template: {str(e)}")
                return
        if sukses:
            QMessageBox.information(self.parent, "Sukses", "Template berhasil dibuat", QMessageBox.Ok)
            # open_in_explorer(namafile)
            open_with_default_app(namafile)

    # fungsi membuat file excel berdasarkan pilihan db dan tabel 
    def create_not_filtered_template(self, namafile=None):
        align_center = Alignment(horizontal='center', vertical='center')
        align_left = Alignment(horizontal='left', vertical='center', indent=1)
        font = Font(name='Aptos', size=10)
        bold_font = Font(name='Aptos', size=10, bold=True)
        left_column_set = set(LEFT_COLUMN)
        database_name = self.cbo_db.currentText()
        current_table = self.cbo_table.currentText()
        if current_table == 'All':
            list_nama_tabel = self.SQL.get_all_tables()
        else:
            list_nama_tabel = [current_table]
        wb = Workbook()
        ws_nav = wb.active
        ws_nav.title = "navigasi"
        ws_nav["A1"] = "MENUJU SHEET"
        ws_nav["A1"].font = Font(bold=True, size=12)

        for index, nama_tabel in enumerate(list_nama_tabel, start=2):
            cell = ws_nav.cell(row=index, column=1, value=nama_tabel)
            cell.hyperlink = f"#'{nama_tabel}'!A1"
            cell.font = Font(color="0000FF", underline="single")
            cell.alignment = align_left

        for nama_tabel in list_nama_tabel:
            columns = self.SQL.get_column_names(nama_tabel)
            data = self.SQL.get_table_data(nama_tabel)

            ws = wb.create_sheet(title=nama_tabel)
            for col_num, key in enumerate(columns, 1):
                header_cell = ws.cell(row=1, column=col_num, value=key)
                header_cell.font = bold_font
                header_cell.fill = PatternFill(start_color="FFFFCC", fill_type="solid")
                header_cell.alignment = align_center

            ws["A1"].hyperlink = "#'navigasi'!A1"
            ws["A1"].font = Font(underline="single")
            ws["A1"].fill = PatternFill(start_color="4215FF", fill_type="solid")
            ws.freeze_panes = "A2"

            if self.radio_filled.isChecked():
                if data:
                    for row_num, row_data in enumerate(data, 2):
                        for col_num, key in enumerate(columns, 1):
                            cell = ws.cell(row=row_num, column=col_num, value=row_data.get(key, ""))
                            cell.alignment = align_left if key in left_column_set else align_center
                            cell.font = font

            for col_num, column_name in enumerate(columns, 1):
                column_letter = get_column_letter(col_num)
                max_length = len(column_name)
                if data:
                    for row in range(2, len(data) + 2):
                        cell_value = ws.cell(row=row, column=col_num).value
                        if cell_value:
                            max_length = max(max_length, len(str(cell_value)))
                ws.column_dimensions[column_letter].width = max_length + 2
        wb.save(namafile)
        return True


### BAGIAN UPDATE INSERT DARI EXCEL
    def on_btn_browse_clicked(self):
        # self.cbo_sheet.clear()
        # self.line_namafile.clear()
        # self.cbo_key.clear()
        file_dipilih = open_dialog(parent=self.parent, text_widget=self.line_source)        
        if file_dipilih:
            path= self.line_source.text()
            namafile = os.path.basename(path)
            self.line_namafile.setText(namafile)
            sheet_names = pd.ExcelFile(path).sheet_names
            fill_combobox(self.cbo_sheet, sheet_names[1:])
        else:
            self.cbo_sheet.clear()
            self.line_namafile.clear()
            self.cbo_key.clear()

    def cbo_sheet_selected(self):
        filepath = self.line_source.text()
        sheet_name = self.cbo_sheet.currentText()
        if filepath != '':
            df = pd.read_excel(filepath, sheet_name, nrows=0)
            headers = df.columns.tolist()
            fill_combobox(self.cbo_key, headers)
        
    def create_insert_query(self):
        tabel_db = self.cbo_sheet.currentText()
        query = generate_insert_queries(
            tabel_db=tabel_db,
            excel_file_path=self.line_source.text()
        )
        return query
    
    def execute_insert(self):
        """Eksekusi query dengan progress bar dan tampilkan pesan setelah selesai"""
        db_name = self.cbo_save_to_db.currentText()
        con = ConnectDB(db_name)
        con.connect()  # Memastikan koneksi ke database aktif
        cursor = con.my_cursor

        queries = self.create_insert_query()
        total_queries = len(queries)
        if total_queries == 0:
            QMessageBox.information(self, "Informasi", "Tidak ada data yang perlu disimpan.")
            return
        self.progress_save.setMinimum(0)
        self.progress_save.setMaximum(total_queries)
        self.progress_save.setValue(0)
        try:
            insert_queries = [q for q in queries if q[0].startswith("INSERT")]
            if len(insert_queries) > 1000:
                sql_statement = insert_queries[0][0]  # Query dasar INSERT
                values_list = [q[1] for q in insert_queries]  # List parameter
                cursor.executemany(sql_statement, values_list)
                self.progress_save.setValue(len(insert_queries))  # Langsung penuh
            else:
                for i, (query, params) in enumerate(insert_queries, 1):
                    cursor.execute(query, params)
                    self.progress_save.setValue(i)
            con.my_connector.commit()  # Commit setelah semua eksekusi berhasil
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan ke database.")
        except Exception as e:
            con.my_connector.rollback()  # Rollback jika ada error
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {str(e)}")
        finally:
            cursor.close()
            con.close_connection()




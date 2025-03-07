from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui.ui_page_rekap_siswa import Ui_Form
from models.siswa.rekap_siswa import RekapSiswa
from utils.fungsi.general_functions import *


class PageRekapSiswa(QWidget, Ui_Form):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = RekapSiswa()

    def show_page(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.rekap_pertapel()
        self.fill_rekap_pertingkat()
        self.fill_rekap_perrombel()
        self.fill_rekap_usia()

    def rekap_pertapel(self):
            fill_table(
                table_name=self.tbl_rekap_all, 
                get_function=self.SQL.rekap_pertapel, 
                get_params=[self.txt_jenjang], 
            )
        
    def fill_rekap_pertingkat(self):
        self.tbl_rekap_tingkat.setRowCount(0) 
        fill_table(
            table_name=self.tbl_rekap_tingkat,
            get_function=self.SQL.rekap_pertingkat,
            get_params=[self.txt_jenjang, self.txt_tapel], 
        )
        self.hitung_total(self.tbl_rekap_tingkat, 3, 6)

    def fill_rekap_perrombel(self):
        self.tbl_rekap_rombel.setRowCount(0)
        fill_table(
            table_name=self.tbl_rekap_rombel,
            get_function= self.SQL.rekap_perrombel,
            get_params= (self.txt_jenjang, self.txt_tapel),
        )
        self.hitung_total(self.tbl_rekap_rombel, 4, 7)

    def fill_rekap_usia(self):
        self.tbl_rekap_umur.setRowCount(0)
        fill_table(
            table_name=self.tbl_rekap_umur,
            get_function=self.SQL.rekap_umur,
            get_params=(self.txt_jenjang, self.txt_tapel),
        )
        self.hitung_total(self.tbl_rekap_umur, 3, 16)

    def hitung_total(self, table, start_col, end_col):
        try:
            row_count = table.rowCount()
            if row_count == 0:
                return
            
            # Hapus "Total" yang mungkin sudah ada di akhir
            last_row_text = table.item(row_count - 1, 0)
            if last_row_text and last_row_text.text() == "Total":
                table.removeRow(row_count - 1)
                row_count = table.rowCount()  # Perbarui row_count setelah penghapusan

            total_rows = []
            sums = None
            current_jenjang = None

            for row in range(row_count):
                jenjang_value = table.item(row, 0).text() if table.item(row, 0) else None

                if jenjang_value != current_jenjang:
                    if sums is not None and any(sums):
                        total_rows.append((row, sums))
                    sums = [0] * (end_col - start_col + 1)
                    current_jenjang = jenjang_value

                for col in range(start_col, end_col + 1):
                    item = table.item(row, col)
                    text_value = item.text().strip() if item else ""
                    if text_value.lstrip("-").isdigit():
                        sums[col - start_col] += int(text_value)

            if sums is not None and any(sums):
                total_rows.append((row_count, sums))

            for insert_pos, sums in reversed(total_rows):
                table.insertRow(insert_pos)
                total_item = QTableWidgetItem("Total")
                total_item.setTextAlignment(Qt.AlignCenter)
                table.setItem(insert_pos, 0, total_item)

                if start_col > 0:
                    table.setSpan(insert_pos, 0, 1, start_col)

                for i, total in enumerate(sums, start=start_col):
                    item = QTableWidgetItem(str(total))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(insert_pos, i, item)

        except Exception as e:
            print(f"Error calculating totals: {e}")




    
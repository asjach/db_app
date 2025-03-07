from ui.ui_page_pindah_kelas import Ui_Form
from models.siswa.pindah_kelas import PindahKelas
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import PINDAH_KELAS
from PySide6.QtWidgets import QMainWindow, QWidget

class PagePindahKelas(Ui_Form, QWidget):
    def __init__(self, parent=QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = PindahKelas()
        self.tbl_a.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_a, self, self.parent, ['id', 'nis_lokal', 'tingkat']))
        self.tbl_b.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_b, self, self.parent, ['id', 'nis_lokal', 'tingkat']))
        self.tbl_c.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_c, self, self.parent, ['id', 'nis_lokal', 'tingkat']))
     
    def show_page(self):
        self.fill_tabel(
            table=self.tbl_a, 
            kelas="A", 
            fungsi_awal= lambda: self.pindah_kelas("C",self.tbl_a),
            fungsi_akhir= lambda: self.pindah_kelas("B",self.tbl_a))
        
        self.fill_tabel(
            table=self.tbl_b, 
            kelas="B", 
            fungsi_awal= lambda: self.pindah_kelas("A",self.tbl_b),
            fungsi_akhir= lambda: self.pindah_kelas("C",self.tbl_b),)
        
        self.fill_tabel(
            table=self.tbl_c, 
            kelas="C", 
            fungsi_awal= lambda: self.pindah_kelas("B",self.tbl_c),
            fungsi_akhir= lambda: self.pindah_kelas("A",self.tbl_c))
        
        jml_l_a = count_column(self.tbl_a, 6, "L")
        jml_p_a = count_column(self.tbl_a, 6, "P")
        jml_l_b = count_column(self.tbl_b, 6, "L")
        jml_p_b = count_column(self.tbl_b, 6, "P")
        jml_l_c = count_column(self.tbl_c, 6, "L")
        jml_p_c = count_column(self.tbl_c, 6, "P")
        self.lbl_a.setText(f"\tL: {jml_l_a}\tP: {jml_p_a}\tJ: {jml_l_a+jml_p_a}")
        self.lbl_b.setText(f"\tL: {jml_l_b}\tP: {jml_p_b}\tJ: {jml_l_b+jml_p_b}")
        self.lbl_c.setText(f"\tL: {jml_l_c}\tP: {jml_p_c}\tJ: {jml_l_c+jml_p_c}")

    def fill_tabel(self, table, kelas, fungsi_awal, fungsi_akhir):
        fill_table(
            table_name=table,
            get_function=self.SQL.list_siswa_pindah_kelas,
            get_params={
                'jenjang':self.parent.cbo_jenjang.currentText(),
                'tapel':self.parent.cbo_tapel.currentText(),
                'tingkat':f"%{self.parent.cbo_tingkat.currentText()}%",
                'order_by':self.parent.cbo_order_by.currentText(),
                'kelas':f"%{self.parent.cbo_tingkat.currentText()}{kelas}%",
                'search_by':self.parent.cbo_search_by.currentText(),
                'search_text':f"%{self.parent.line_search.text()}%",
                'kolom':self.kolom,
            },
            table_params={
                'hidden_column':[1, 2, 3], 
                'stretch_column':4, 
                'icon_awal':":/icon/resources/icon/less_than.svg", 
                'icon_akhir':":/icon/resources/icon/more_than.svg", 
                'fungsi_awal':fungsi_awal, 
                'fungsi_akhir':fungsi_akhir
            }
        )

    def pindah_kelas(self, kelas_target, tabel):
        scroll_position = tabel.verticalScrollBar().value()
        kelas = f"{self.tingkat}{kelas_target}"
        self.SQL.update_kelas_siswa(self.id, kelas)
        self.show_page()
        tabel.verticalScrollBar().setValue(scroll_position)

    @property
    def kolom(self):
        return PINDAH_KELAS.get(
            self.parent.cbo_kolom.currentText().lower(), PINDAH_KELAS['default'])
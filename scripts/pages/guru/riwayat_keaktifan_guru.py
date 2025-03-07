from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_riwayat_keaktifan_guru import Ui_Form
from models.guru.guru import ModelGuru
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import GURU

class PageKeaktifanGuru(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = ModelGuru()
        self.tbl_keaktifan.currentItemChanged.connect(lambda: 
            table_selected(self.tbl_keaktifan, self, self.parent))
        self.tbl_keaktifan.itemChanged.connect(self.update_from_table)

    def show_page(self):
        fill_table(
            table_name=self.tbl_keaktifan, 
            get_function=self.SQL.get_keaktifan_guru, 
            get_params={
                'jenjang':self.parent.cbo_jenjang.currentText(),
                'tapel':self.parent.cbo_tapel.currentText(),
                'kolom': self.kolom(),
                'order_by':self.parent.cbo_order_by.currentText(),
                'search_by':self.parent.cbo_search_by.currentText(),
                'search_text':self.parent.line_search.text(),
            },
            table_params={
                'hidden_column': [0, 1,],
            }
        )

    def update_from_table(self):
        tabel = self.tbl_keaktifan
        params_biodata = {
            'tabel_ui': self.tbl_keaktifan,
            'tabel_sql': 'guru',
            'not_updatable_column': ['id_guru'],
            'key': 'id_guru', 
            'key_value': self.id_guru
        }
        params_riwayat = {
            'tabel_ui': self.tbl_keaktifan,
            'tabel_sql': 'guru_keaktifan',
            'not_updatable_column': ['id_guru', 'id'],
            'key': 'id', 
            'key_value': self.id
        }
        cur_col = tabel.currentColumn()
        header = tabel.horizontalHeaderItem(cur_col)
        if header is not None:
            nama_kolom = header_for_db(header.text())
        else: nama_kolom=None
        if nama_kolom in ['fungsi_jabatan', 'nomor_sk', 'tgl_sk', 'namafile', 'kelas', 'status_keaktifan']:
            update_from_table(**params_riwayat)
        else:
            update_from_table(**params_biodata)
        

    def kolom(self):
        return GURU.get(self.parent.cbo_kolom.currentText().lower(), GURU['default'])

        
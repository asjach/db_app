from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_riwayat_keaktifan_guru import Ui_Form
from models.model_guru import Model_Guru
from utils.fungsi.general_functions import *
from utils.key_value.kolom_sql import GURU

class PageKeaktifanGuru(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Model_Guru()
        self.tbl_keaktifan.itemSelectionChanged.connect(self.table_guru_selected)
        self.tbl_keaktifan.itemChanged.connect(self.update_from_table)
        self.cbo_guru.textActivated.connect(self.cbo_guru_selected)
        self.btn_tapel_sebelumnya.clicked.connect(self.btn_tapel_sebelumnya_clicked)

    def show_page(self):
        self.fill_table_guru()
        self.fill_cbo_guru()

    def fill_table_guru(self):
        data = self.SQL.get_keaktifan_guru(
            jenjang=self.parent.str_jenjang,
            tapel = self.parent.str_tapel,
            kolom = self.kolom(),
            order_by=self.parent.str_order_by,
            search_by=self.parent.str_search_by,
            search_text=self.parent.last_search_text
        )
        generate_table(
            data=data,
            table=self.tbl_keaktifan,
            hidden_column=[0, 1,],
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_guru

        )
    
    def table_guru_selected(self):
        table_selected(self.tbl_keaktifan, self, self.parent)

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

    def delete_guru(self):
        try:
            delete_by_id('guru_keaktifan', 'id', self.id)
            self.show_page()
        except Exception as e:
            print(e)

    def kolom(self):
        return GURU.get(self.parent.cbo_kolom.currentText().lower(), GURU['default'])
    
    def fill_cbo_guru(self):
        data=self.SQL.get_pegawai_aktif()
        self.cbo_guru.blockSignals(True)
        populate_combobox(
            cbo_widget=self.cbo_guru,
            data=data,
            text_data='nama_lengkap',
            user_data='id_guru'
        )
        self.cbo_guru.blockSignals(False)
    
    
    def cbo_guru_selected(self):
        try:
            self.SQL.aktifkan_guru(
                id_guru=self.cbo_guru.currentData(),
                jenjang = self.parent.str_jenjang,
                tapel=self.parent.str_tapel
            )
            self.show_page()
        except Exception as e:
            print(e)

    def btn_tapel_sebelumnya_clicked(self):
        try:
            self.SQL.aktivasi_dari_tapel_sebelumnya(
                jenjang = self.parent.str_jenjang,
                tapel=self.parent.str_tapel,
            )
            self.show_page()
        except Exception as e:
            print(e)
        

    

        
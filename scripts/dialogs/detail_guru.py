
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QDialog, QMessageBox
from models.model_guru import Model_Guru
from ui.ui_dialog_detail_guru import Ui_Form
from utils.static_values import *
from utils.fungsi.general_functions import *


class DialogDetailGuru(QDialog, Ui_Form):
    def __init__(self, parent=None, id_guru=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setSizeGripEnabled(True)
        self.SQL = Model_Guru()
        self.parent = parent
        self.id_guru = id_guru
        self.id = None
        self.init_detail_controls()
        self.setup_connection()
        self.fill_cbo_data_guru()

    def setup_connection(self):
        combo_detail_guru = {
            self.cbo_jk:JK,
            self.cbo_agama: AGAMA,
            self.cbo_status_tmp_tinggal: STATUS_TEMPAT_TINGGAL,
            self.cbo_jarak:JARAK,
            self.cbo_transportasi:TRANSPORTASI,
            self.cbo_waktu_tempuh:WAKTU_TEMPUH,
            self.cbo_status_kepegawaian:STATUS_KEPEGAWAIAN,
            self.cbo_goldar:GOLONGAN_DARAH,
            self.cbo_status_sertifikasi:STATUS_SERTIFIKASI,
            self.cbo_jenjang_sertifikasi: JENJANG_SERTIFIKASI,
            self.cbo_status_kawin:STATUS_MENIKAH,
        }
        for combo, values in combo_detail_guru.items():
            combo.clear()
            combo.addItems(values() if callable(values) else values)
        for combo_box in self.findChildren(QComboBox):
            combo_box.installEventFilter(self)
        self.btn_save_detail.clicked.connect(self.btn_save_clicked)
        self.line_search.textChanged.connect(self.fill_cbo_data_guru)
        self.cbo_daftar_guru.textActivated.connect(self.cbo_daftar_guru_selected)
        self.tbl_daftar_keluarga.itemChanged.connect(self.update_keluarga)
        self.tbl_pendidikan_formal.itemChanged.connect(self.update_riwayat_pendidikan)
        self.tbl_daftar_keluarga.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_daftar_keluarga, self, self.parent, ("id","id_guru")))
        self.tbl_pendidikan_formal.itemSelectionChanged.connect(
            lambda: table_selected(self.tbl_pendidikan_formal, self, self.parent, ("id","id_guru")))
    
    def show_dialog(self, id_guru):
        self.fill_detail_guru(id_guru)
        self.fill_tbl_keluarga(id_guru)
        self.fill_tbl_pendidikan_formal(id_guru)
        
    def fill_cbo_data_guru(self):
        data = self.SQL.get_daftar_guru(
            search_by=self.cbo_search_by.currentText(),
            search_text=self.line_search.text()
        )
        self.cbo_daftar_guru.clear()
        if data:
            self.cbo_daftar_guru.blockSignals(True)
            for item in data:
                self.cbo_daftar_guru.addItem(f"{item['nama_lengkap']} | {item['is_active']}", userData=item['id_guru'])
            self.cbo_daftar_guru.blockSignals(False)
        self.show_dialog(self.cbo_daftar_guru.itemData(self.cbo_daftar_guru.currentIndex()))

    def cbo_daftar_guru_selected(self):
        index = self.cbo_daftar_guru.currentIndex()
        id_guru = self.cbo_daftar_guru.itemData(index)
        self.show_dialog(id_guru)

    def fill_detail_guru(self, id_guru):
        self.db_data = self.SQL.get_detail_guru(id_guru)
        data = self.db_data
        if data:
            self.id_guru = data['id_guru']
            controls = self.detail_controls
            self.setWindowTitle(data['nama_lengkap'])
            insert_data_to_controls(data, controls)

    def save_to_db(self):
        try:
            save_to_db(self.detail_controls, self.db_data, self.SQL.update_identitas_guru)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {e}")

    def fill_tbl_keluarga(self, id_guru):
        data, headers = self.SQL.get_keluarga(id_guru)
        generate_table(
            data = data,
            table = self.tbl_daftar_keluarga,
            icon_awal= ":/icon/resources/icon/multiply.svg",
            fungsi_awal = self.delete_keluarga,
            mode_input=True,
            column_names=headers,
        )

    def update_keluarga(self, item):
        sukses = handle_item_changed_v2(
            tabel_ui=self.tbl_daftar_keluarga,
            tabel_sql='guru_keluarga',
            primary_key='id',
            item=item,
            must_insert=['id_guru', 'nama_lengkap'],
            not_updatable_column=['id', 'id_guru'],
        )
        if sukses:
            self.fill_tbl_keluarga(self.id_guru)

    def delete_keluarga(self):
        sukses = delete_by_id("guru_keluarga", "id", self.id)
        if sukses:
           self.fill_tbl_keluarga(self.id_guru)

    def fill_tbl_pendidikan_formal(self, id_guru):
        data, headers = self.SQL.get_pendidikan_formal(id_guru)
        generate_table(
            data=data,
            table=self.tbl_pendidikan_formal,
            icon_awal= ":/icon/resources/icon/multiply.svg",
            fungsi_awal=self.delete_riwayat_pendidikan,
            mode_input=True, 
            column_names=headers,
        )
        
    def update_riwayat_pendidikan(self, item):
        sukses = handle_item_changed_v2(
            tabel_ui=self.tbl_pendidikan_formal,
            tabel_sql='guru_pendidikan',
            primary_key='id',
            item=item,
            must_insert=['id_guru', 'jenjang'],
            not_updatable_column=['id', 'id_guru'],
        )
        if sukses:
            self.fill_tbl_pendidikan_formal(self.id_guru)
    
    def delete_riwayat_pendidikan(self):
        sukses = delete_by_id("guru_pendidikan", "id", self.id)
        if sukses:
            self.fill_tbl_pendidikan_formal(self.id_guru)
        
    def btn_save_clicked(self):
        self.save_to_db()
        self.close()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel and isinstance(obj, QComboBox):
            return True
        return super().eventFilter(obj, event)
    
    def init_detail_controls(self):
        # (control, field db)
        self.detail_controls = [
            (self.line_id_guru, 'id_guru'),
            (self.line_nama_lengkap, 'nama_lengkap'),
            (self.cbo_jk, 'jk'),
            (self.line_tmp_lahir, 'tmp_lahir'),
            (self.line_tgl_lahir, 'tgl_lahir'),
            (self.line_ayah, 'ayah'),
            (self.line_ibu_kandung, 'ibu'),
            (self.line_nik, 'nik'),
            (self.line_niat_npa, 'niat_npa'),
            (self.line_no_kk, 'no_kk'),
            (self.cbo_agama, 'agama'),
            (self.cbo_status_tmp_tinggal, 'status_tmp_tinggal'),
            (self.line_alamat, 'alamat'),
            (self.line_kodepos, 'kodepos'),
            (self.line_rt, 'rt'),
            (self.line_rw, 'rw'),
            (self.line_kel_desa, 'kel_desa'),
            (self.line_kecamatan, 'kecamatan'),
            (self.line_kab_kota, 'kab_kota'),
            (self.line_provinsi, 'provinsi'),
            (self.cbo_jarak, 'jarak'),
            (self.cbo_transportasi, 'transportasi'),
            (self.cbo_waktu_tempuh, 'waktu_tempuh'),
            (self.cbo_status_kepegawaian, 'status_kepegawaian'),
            (self.line_nuptk, 'nuptk'),
            (self.line_npk, 'npk'),
            (self.line_peg_id, 'peg_id'),
            (self.line_tmt_guru, 'tmt_guru'),
            (self.line_tmt_pegawai, 'tmt_pegawai'),
            (self.line_no_hp, 'no_telp'),
            (self.line_email_pribadi, 'email'),
            (self.line_email_hebat, 'email_hebat'),
            (self.line_password_hebat, 'pw_email_hebat'),
            (self.line_bpjs, 'no_bpjs'),
            (self.line_npwp, 'npwp'),
            (self.cbo_goldar, 'goldar'),
            (self.line_nama_pemilik_rekening, 'nama_rekening'),
            (self.line_norek, 'nomor_rekening'),
            (self.line_nama_bank, 'nama_bank'),
            (self.cbo_status_sertifikasi, 'status_sertifikasi'),
            (self.cbo_jenjang_sertifikasi, 'jenjang_sertifikasi'),
            (self.line_mapel_sertifikasi, 'mapel_sertifikasi'),
            (self.line_kode_mapel_sertifikasi, 'kode_mapel_sertifikasi'),
            (self.line_nopes_sertifikasi, 'nopes_sertifikasi'),
            (self.line_lptk_sertifikasi, 'lptk_sertifikasi'),
            (self.line_no_sertifikasi, 'no_sertifikasi'),
            (self.line_tgl_lulus_sertifikasi, 'tgl_lulus_sertifikasi'),
            (self.line_tahun_sertifikasi, 'tahun_lulus_sertifikasi'),
            (self.line_model_sertifikasi, 'model_sertifikasi'),
            (self.line_jalur_sertifikasi, 'jalur_sertifikasi'),
            (self.line_naungan_sertifikasi, 'naungan_sertifikasi'),
            (self.cbo_status_kawin, 'status_perkawinan'),
            (self.line_nama_istri_suami, 'suami_istri'),
            (self.line_jumlah_anak, 'jumlah_anak'),
        ]

    
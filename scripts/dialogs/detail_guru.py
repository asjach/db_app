
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QDialog, QMessageBox
from models.guru.guru import ModelGuru
from ui.ui_dialog_detail_guru import Ui_Form
from utils.static_values import *
from utils.fungsi.general_functions import *


class DialogDetailGuru(QDialog, Ui_Form):
    def __init__(self, parent=None, id_guru=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setSizeGripEnabled(True)
        self.SQL = ModelGuru()
        self.parent = parent
        self.id_guru = id_guru
        self.id = None
        self.input_keluarga = (
            self.line_nik_anak, self.line_nama_anak, self.cbo_jk_anak,
            self.line_tmp_lahir_anak, self.line_tgl_lahir_anak, self.cbo_pendidikan_anak, 
            self.cbo_pekerjaan_anak, self.cbo_status_anak,
        )
        self.input_riwayat_pendidikan = ( 
            self.cbo_jenjang_sekolah, self.cbo_status_sekolah, self.line_nama_sekolah, 
            self.line_alamat_sekolah, self.line_tahun_masuk, self.line_tahun_lulus, 
            self.line_tgl_ijazah, self.line_nomor_ijazah, self.line_nem_ipk,
        )
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
            self.cbo_pendidikan_anak:PENDIDIKAN,

            self.cbo_pekerjaan_anak:PEKERJAAN,
            self.cbo_jk_anak:JK,
            self.cbo_status_anak: STATUS_ANAK,
            self.cbo_jenjang_sekolah:JENJANG_SEKOLAH,
            self.cbo_status_sekolah:STATUS_SEKOLAH,
        }
        for combo, values in combo_detail_guru.items():
            combo.clear()
            combo.addItems(values() if callable(values) else values)
        for combo_box in self.findChildren(QComboBox):
            combo_box.installEventFilter(self)
        self.btn_save_detail.clicked.connect(self.btn_save_clicked)
        self.line_search.textChanged.connect(self.fill_cbo_data_guru)
        self.cbo_daftar_guru.textActivated.connect(self.cbo_daftar_guru_selected)
        self.btn_tambah_anak.clicked.connect(self.tambah_keluarga)
        self.btn_tambah_sekolah.clicked.connect(self.tambah_riwayat_pendidikan)
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

    def tambah_keluarga(self):
        parameter = {
            "id_guru": self.line_id_guru.text(),
            "nik": self.line_nik_anak.text(),
            "nama_lengkap": self.line_nama_anak.text(),
            "jk": self.cbo_jk_anak.currentText(),
            "tmp_lahir": self.line_tmp_lahir_anak.text(),
            "tgl_lahir": text_to_date(self.line_tgl_lahir_anak.text()),
            "pendidikan": self.cbo_pendidikan_anak.currentText(),
            "pekerjaan": self.cbo_pekerjaan_anak.currentText(),
            "status_keluarga": self.cbo_status_anak.currentText(),
        }
        sukses = self.SQL.insert_keluarga(**parameter)
        if sukses:
            self.fill_tbl_keluarga(self.id_guru)
            clear_inputs(self.input_keluarga)

    def tambah_riwayat_pendidikan(self):
        parameter = {
            "id_guru": self.line_id_guru.text(),
            "jenjang": self.cbo_jenjang_sekolah.currentText(),
            "nama_sekolah": self.line_nama_sekolah.text(),
            "status_sekolah": self.cbo_status_sekolah.currentText(),
            "alamat_sekolah": self.line_alamat_sekolah.text(),
            "tahun_masuk": self.line_tahun_masuk.text(),
            "tahun_lulus": self.line_tahun_lulus.text(),
            "ip_ijazah": self.line_nem_ipk.text(),
            "tgl_ijazah": text_to_date(self.line_tgl_ijazah.text()),
            "nomor_ijazah":self.line_nomor_ijazah.text()
        }
        sukses = self.SQL.insert_riwayat_pendidikan(**parameter)
        if sukses:
            self.fill_tbl_pendidikan_formal(self.id_guru)
            clear_inputs(self.input_riwayat_pendidikan)

    def update_keluarga(self):
        parameter = {
            "tabel_ui": self.tbl_daftar_keluarga,
            "tabel_sql": "guru_keluarga",
            "not_updatable_column": ['id','id_guru'],
            "key": 'id',
            "key_value": self.id
        }
        sukses = update_from_table(**parameter)
        if sukses:
            self.fill_tbl_keluarga(self.id_guru)

    def update_riwayat_pendidikan(self):
        parameter = {
            "tabel_ui": self.tbl_pendidikan_formal,
            "tabel_sql": 'guru_riwayat_pendidikan',
            "not_updatable_column": ['id','id_guru'],
            "key": 'id',
            "key_value": self.id
        }
        sukses = update_from_table(**parameter)
        if sukses:
            self.fill_tbl_pendidikan_formal(self.id_guru)
    
    def delete_riwayat_pendidikan(self):
        sukses = delete_by_id("guru_riwayat_pendidikan", "id", self.id)
        if sukses:
            self.fill_tbl_pendidikan_formal(self.id_guru)

    def delete_keluarga(self):
        sukses = delete_by_id("guru_keluarga", "id", self.id)
        if sukses:
           self.fill_tbl_keluarga(self.id_guru)
        
    def btn_save_clicked(self):
        self.save_to_db()
        self.close()

    def fill_tbl_keluarga(self, id_guru):
        get_params = {'id_guru': id_guru}
        table_params = {
            'icon_awal': ":/icon/resources/icon/multiply.svg",
            'fungsi_awal':self.delete_keluarga
        }
        fill_table(
            table_name=self.tbl_daftar_keluarga, 
            get_function=self.SQL.get_keluarga, 
            get_params=get_params, 
            table_params=table_params)

    def fill_tbl_pendidikan_formal(self, id_guru):
        get_params = {'id_guru': id_guru}
        table_params = {
            'icon_awal': ":/icon/resources/icon/multiply.svg",
            'fungsi_awal':self.delete_riwayat_pendidikan
        }
        fill_table(
            table_name=self.tbl_daftar_keluarga, 
            get_function=self.SQL.get_pendidikan_formal, 
            get_params=get_params, 
            table_params=table_params)

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

    
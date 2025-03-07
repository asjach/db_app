from PySide6.QtWidgets import QComboBox, QLineEdit, QDialog, QCompleter
from ui.ui_dialog_detail_siswa import Ui_Form
from PySide6.QtPdf import QPdfDocument
from utils.fungsi.general_functions import *
from models.siswa.biodata_siswa import BiodataSiswa
from scripts.widgets.image_viewer import Widget_Image_Viewer
from PySide6.QtCore import QEvent, Qt


class CustomCompleter(QCompleter):
    def __init__(self, *args, **kwargs):
        super(CustomCompleter, self).__init__(*args, **kwargs)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.setFilterMode(Qt.MatchContains)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.Type.KeyPress and event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Tab]):
            # Jika hanya ada satu item yang cocok, pilih item tersebut
            if self.completionCount() == 1:
                self.setCurrentRow(0)
                self.activated.emit(self.currentCompletion())
                self.popup().hide()
                return True
        return super(CustomCompleter, self).eventFilter(source, event)


class DialogDetailSiswa(QDialog, Ui_Form):
    def __init__(self, parent=None, tabel=None, nis_lokal=None, nis_index=None, ):
        super().__init__(None)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setSizeGripEnabled(True)
        self.parent = parent
        self.tabel = tabel
        self.nis_lokal = nis_lokal
        self.nis_index = nis_index
        
        self.image_viewer = Widget_Image_Viewer()
        self.grid_viewer.addWidget(self.image_viewer)
        self.SQL = BiodataSiswa()
        self.fill_combobox()
        self.set_data_cbo_alamat()
        self.set_data_cbo_sekolah()
        list_alamat = [
            self.jalan_le,
            self.kampung_le,
            self.rt_le,
            self.rw_le,
            self.kel_desa_le,
            self.kecamatan_le,
            self.kab_kota_le,
            self.provinsi_le,
            self.kodepos_le,
        ]
        for widget in list_alamat:
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(self.create_alamat)
        for combo_box in self.findChildren(QComboBox):
            combo_box.installEventFilter(self)
        self.setup_connections()
        self.connect_btn_to_text_widget()

    def setup_connections(self):
        self.init_controls()
        self.line_search.textChanged.connect(self.set_data_cbo_nama_lengkap)
        self.cbo_nama_lengkap.textActivated.connect(self.cbo_nama_lengkap_item_selected)
        self.prev_btn.clicked.connect(self.btn_prev_table_item_clicked)
        self.next_btn.clicked.connect(self.btn_next_table_item_clicked)
        
        self.cbo_daftar_dokumen.currentIndexChanged.connect(self.show_dokumen)
        self.btn_prev_dok.clicked.connect(lambda: prev_item(self.cbo_daftar_dokumen))
        self.btn_next_dok.clicked.connect(lambda: next_item(self.cbo_daftar_dokumen))
        self.alamat_cbo.activated.connect(self.cbo_alamat_activated)
        self.cbo_daftar_sekolah.activated.connect(self.cbo_daftar_sekolah_activated)
        self.save_btn.clicked.connect(self.btn_save_clicked)

    def show_dialog(self, nis_lokal, tabel=None, nis_index=1):
        self.tabel = tabel
        self.nis_index = nis_index
        self.fill_detail_siswa(nis_lokal)

    def fill_detail_siswa(self, nis_lokal):
        self.db_data = self.SQL.get_detail_siswa(nis_lokal)
        data = self.db_data
        if data:
            self.nis_lokal = data['nis_lokal']
            self.setWindowTitle(data['nama_lengkap'])
            insert_data_to_controls(data, self.controls)
            count_len(self.label_no_kk, self.nomor_kk_le)
            count_len(self.label_nisn, self.nisn_le)
            count_len(self.label_nik, self.nik_le)
            count_len(self.label_nik_ibu, self.ibu_nik_le)
            count_len(self.label_nik_ayah, self.ayah_nik_le)
            self.label_ibu62.setText(format_telp_62(data["ibu_telp"]))
            self.label_ayah62.setText(format_telp_62(data["ayah_telp"]))
            self.set_data_cbo_dokumen(nis_lokal)
            self.create_alamat()
            self.show_dokumen()

    def save_to_db(self):
        sukses = False
        try:
            sukses = save_to_db(self.controls, self.db_data, self.SQL.update_identitas_siswa)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {e}")
        if sukses:
            self.blockSignals(True)
            self.alamat_cbo.setCurrentIndex(-1)
            self.cbo_daftar_sekolah.setCurrentIndex(-1)
            self.blockSignals(False)
                
    def search_data(self):
        data = self.SQL.cari_siswa(self.cbo_search_by.currentText(), self.line_search.text())
        return data
    
    def set_data_cbo_nama_lengkap(self):
        search_text = self.line_search.text()
        if  search_text!= '' and len(search_text) >= 3:
            self.cbo_nama_lengkap.clear()
            data = self.search_data()
            if data:
                for item in data:
                    self.cbo_nama_lengkap.blockSignals(True)
                    self.cbo_nama_lengkap.addItem(f"""{item['nama_lengkap']} | {item['ayah_nama']} | {item['ibu_nama']}""", userData=f'{item['nis_lokal']}')
                    self.cbo_nama_lengkap.blockSignals(False)
        elif len(search_text) < 3:
            self.cbo_nama_lengkap.clear()
    
    def set_data_cbo_dokumen(self, nis_lokal):
        combo = self.cbo_daftar_dokumen
        combo.clear()
        data = self.SQL.get_dokumen_path(nis_lokal)
        if data:
            for item in data:
                folder = value_from_db("FOLDER_DOKUMEN_SISWA")
                filepath = f"{folder}/{item['namafile']}"
                combo.blockSignals(True)
                combo.addItem(f'{item['jenis_dokumen']}', userData=filepath)
                combo.blockSignals(False)

    def set_data_cbo_alamat(self):
        alamat = self.SQL.list_alamat()
        for item in alamat:
            alamat = item["kampung"]
            self.alamat_cbo.addItem(alamat)
            self.alamat_cbo.setItemData(self.alamat_cbo.count() - 1, item)
        self.alamat_cbo.setCurrentIndex(-1)
    
    def set_data_cbo_sekolah(self):
        daftar_sekolah = self.SQL.list_sekolah()
        for item in daftar_sekolah:
            nama_sekolah = item["nama_sekolah"]
            self.cbo_daftar_sekolah.addItem(nama_sekolah)
            self.cbo_daftar_sekolah.setItemData(self.cbo_daftar_sekolah.count() - 1, item)
        self.cbo_daftar_sekolah.setCurrentIndex(-1)

    def show_dokumen(self):
        index = self.cbo_daftar_dokumen.currentIndex()
        self.filepath = self.cbo_daftar_dokumen.itemData(index)
        self.image_viewer.loadImage(self.filepath)
        
    def cbo_nama_lengkap_item_selected(self):
        index = self.cbo_nama_lengkap.currentIndex()
        nis_lokal = self.cbo_nama_lengkap.itemData(index)
        self.fill_detail_siswa(nis_lokal)

    def btn_prev_table_item_clicked(self):
        self.save_to_db()
        if self.tabel:
            prev_table_item(self.tabel)
            nis_lokal = self.tabel.item(self.tabel.currentRow(), self.nis_index).text()
            self.fill_detail_siswa(nis_lokal)

    def btn_next_table_item_clicked(self):
        self.save_to_db()
        if self.tabel:
            next_table_item(self.tabel)
            nis_lokal = self.tabel.item(self.tabel.currentRow(), self.nis_index).text()
            self.fill_detail_siswa(nis_lokal)

    def connect_btn_to_text_widget(self):
        btn_widget = {
            self.copy_nama_lengkap:self.nama_lengkap_le,
            self.copy_nis_lokal:self.nis_lokal_le,
            self.copy_nisn:self.nisn_le,
            self.copy_nik:self.nik_le,
            self.copy_tmp:self.tmp_lahir_le,
            self.copy_anak_ke:self.anak_ke_le,
            self.copy_saudara:self.jumlah_saudara_le,
            self.copy_nis_kemenag:self.nis_kemenag_le,
            self.copy_kampung:self.kampung_le,
            self.copy_kodepos:self.kodepos_le,
            self.copy_alamat:self.alamat_le,
            self.copy_alamat_full:self.alamat_full_pte,
            self.copy_ayah:self.ayah_nama_le,
            self.copy_nik_ayah:self.ayah_nik_le,
            self.copy_tmp_ayah:self.ayah_tmp_lahir_le,
            self.copy_telp_ayah:self.ayah_telp_le,
            self.copy_telp_ayah62:self.label_ayah62,
            self.copy_ibu:self.ibu_nama_le,
            self.copy_nik_ibu:self.ibu_nik_le,
            self.copy_tmp_ibu:self.ibu_tmp_lahir_le,
            self.copy_telp_ibu:self.ibu_telp_le,
            self.copy_telp_ibu62:self.label_ibu62,
            self.copy_no_kk:self.nomor_kk_le,
        }
        for btn, text_widget in btn_widget.items():
            btn.clicked.connect(lambda _, tw=text_widget:copy_value(tw))

    def create_alamat(self):
        jalan = self.jalan_le.text()
        kampung = self.kampung_le.text()
        rt = self.rt_le.text()
        rw = self.rw_le.text()
        desa = self.kel_desa_le.text()
        kec = self.kecamatan_le.text()
        kabkota = self.kab_kota_le.text()
        prov = self.provinsi_le.text()
        kodepos = self.kodepos_le.text()
        alamat = ""
        if jalan != "":
            alamat += f"Jl. {jalan} "
        if kampung != "":
            alamat += f"Kp. {kampung} "
        if rt != "":
            alamat += f"RT {rt} "
        if rw != "":
            alamat += f"RW {rw} "
        self.alamat_le.setText(alamat.strip())
        if desa != "":
            if "Kel." in desa:
                alamat += f"{desa} "
            else:
                alamat += f"Ds. {desa} "
        if kec != "":
            alamat += f"Kec. {kec} "
        if kabkota != "":
            if "Kota" in kabkota:
                alamat += f"{kabkota} "
            else:
                alamat += f"Kab. {kabkota} "
        if prov != "":
            alamat += f"Prov. {prov} "
        if kodepos != "":
            alamat += f"{kodepos}"
        self.alamat_full_pte.setPlainText(alamat.strip())   

    def cbo_alamat_activated(self):
        index = self.alamat_cbo.currentIndex()
        if index != -1:
            data = self.alamat_cbo.itemData(index)
            self.jalan_le.setText(data["jalan"])
            self.kampung_le.setText(data["kampung"])
            self.kel_desa_le.setText(data["kel_desa"])
            self.kecamatan_le.setText(data["kecamatan"])
            self.kab_kota_le.setText(data["kab_kota"])
            self.provinsi_le.setText(data["provinsi"])
            self.kodepos_le.setText(data["kodepos"])
            self.transportasi_cbo.setCurrentText(data["transportasi"])
            self.jarak_cbo.setCurrentText(data["jarak"])
            self.waktu_cbo.setCurrentText(data["waktu_tempuh"])
    
    def cbo_daftar_sekolah_activated(self):
        index = self.cbo_daftar_sekolah.currentIndex()
        if index != -1:
            data = self.cbo_daftar_sekolah.itemData(index)
            self.nama_sekolah_le.setText(data["nama_sekolah"])
            self.npsn_le.setText(data["npsn"])
            self.nss_le.setText(data["nss"])
            self.plain_alamat_sekolah.setPlainText(data["alamat_sekolah"])    


    def cbo_status_wali_selected(self):
        if self.wali_status_cbo.currentText() == "Sama Dengan Ayah":
            self.wali_nik_le.setText(self.ayah_nik_le.text())
            self.wali_nama_le.setText(self.ayah_nama_le.text())
            self.wali_tmp_lahir_le.setText(self.ayah_tmp_lahir_le.text())
            self.wali_tgl_lahir_le.setText(self.ayah_tgl_lahir_le.text())
            self.wali_pendidikan_cbo.setCurrentText(self.ayah_pendidikan_cbo.currentText())
            self.wali_pekerjaan_cbo.setCurrentText(self.ayah_pekerjaan_cbo.currentText())
            self.wali_telp_le.setText(self.ayah_telp_le.text())
        elif self.wali_status_cbo.currentText() == "Sama Dengan Ibu":
            self.wali_nik_le.setText(self.ibu_nik_le.text())
            self.wali_nama_le.setText(self.ibu_nama_le.text())
            self.wali_tmp_lahir_le.setText(self.ibu_tmp_lahir_le.text())
            self.wali_tgl_lahir_le.setText(self.ibu_tgl_lahir_le.text())
            self.wali_pendidikan_cbo.setCurrentText(self.ibu_pendidikan_cbo.currentText())
            self.wali_pekerjaan_cbo.setCurrentText(self.ibu_pekerjaan_cbo.currentText())
            self.wali_telp_le.setText(self.ibu_telp_le.text())
        elif self.wali_status_cbo.currentText() == "":
            self.wali_nik_le.setText("")
            self.wali_nama_le.setText("")
            self.wali_tmp_lahir_le.setText("")
            self.wali_tgl_lahir_le.setText("")
            self.wali_pendidikan_cbo.setCurrentIndex(-1)
            self.wali_pekerjaan_cbo.setCurrentIndex(-1)
            self.wali_telp_le.setText("")
        else:
            return

    def btn_save_clicked(self):
        self.save_to_db()
        self.close() 
    

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel and isinstance(obj, QComboBox):
            return True
        if event.type() == QEvent.Wheel and isinstance(obj, QComboBox):
            return True
        return super().eventFilter(obj, event)
    
    def closeEvent(self, event):
        self.parent.delayed_requery()
        return super().closeEvent(event)
    
    def init_controls(self):
        self.controls = [
        (self.nis_lokal_le, "nis_lokal"),
            (self.nama_lengkap_le, "nama_lengkap"),
            (self.nisn_le, "nisn"),
            (self.nis_kemenag_le, 'nis_kemenag'),
            (self.nik_le, "nik"),
            (self.nama_singkat_le, "nama_singkat"),
            (self.tmp_lahir_le, "tmp_lahir"),
            (self.tgl_lahir_le,"tgl_lahir"),
            (self.jk_cbo,"jk"),
            (self.jumlah_saudara_le, "j_saudara"),
            (self.anak_ke_le, "anak_ke"),
            (self.agama_cbo,"agama"),
            (self.cita_cita_cbo,"cita_cita"),
            (self.hobi_cbo,"hobi"),
            (self.pembiayaan_cbo,"yang_membiayai"),
            (self.keb_khusus_cbo,"kebutuhan_khusus"),
            (self.no_kip_le, "nomor_kip"),
            (self.ayah_status_cbo,"ayah_status"),
            (self.ayah_nama_le, "ayah_nama"),
            (self.ayah_nik_le, "ayah_nik"),
            (self.ayah_tmp_lahir_le, "ayah_tmp_lahir"),
            (self.ayah_tgl_lahir_le,"ayah_tgl_lahir"),
            (self.ayah_pendidikan_cbo,"ayah_pendidikan"),
            (self.ayah_pekerjaan_cbo,"ayah_pekerjaan"),
            (self.ayah_penghasilan_cbo,"ayah_penghasilan"),
            (self.ayah_telp_le, "ayah_telp"),
            (self.ibu_status_cbo,"ibu_status"),
            (self.ibu_nama_le, "ibu_nama"),
            (self.ibu_nik_le, "ibu_nik"),
            (self.ibu_tmp_lahir_le, "ibu_tmp_lahir"),
            (self.ibu_tgl_lahir_le,"ibu_tgl_lahir"),
            (self.ibu_pendidikan_cbo,"ibu_pendidikan"),
            (self.ibu_pekerjaan_cbo,"ibu_pekerjaan"),
            (self.ibu_penghasilan_cbo,"ibu_penghasilan"),
            (self.ibu_telp_le, "ibu_telp"),
            (self.wali_status_cbo,"status_wali"),
            (self.wali_nama_le, "wali_nama"),
            (self.wali_nama_le, "wali_nama"),
            (self.wali_nik_le, "wali_nik"),
            (self.wali_tmp_lahir_le, "wali_tmp_lahir"),
            (self.wali_tgl_lahir_le,"wali_tgl_lahir"),
            (self.wali_pendidikan_cbo,"wali_pendidikan"),
            (self.wali_pekerjaan_cbo,"wali_pekerjaan"),
            (self.wali_telp_le, "wali_telp"),
            (self.nomor_kk_le, "no_kk"),
            (self.kepala_kk_le, "kepala_keluarga"),
            (self.tgl_kk_le,"tgl_kk"),
            (self.alamat_le, "alamat"),
            (self.jalan_le, "jalan"),
            (self.kampung_le, "kampung"),
            (self.rt_le, "rt"),
            (self.rw_le, "rw"),
            (self.kel_desa_le, "kel_desa"),
            (self.kecamatan_le, "kecamatan"),
            (self.kab_kota_le, "kabkota"),
            (self.provinsi_le, "provinsi"),
            (self.kodepos_le, "kodepos"),
            (self.alamat_full_pte,"alamat_full"),
            (self.transportasi_cbo,"transportasi"),
            (self.jarak_cbo,"jarak"),
            (self.waktu_cbo,"waktu_tempuh"),
            (self.tgl_masuk_le,"tgl_masuk"),
            (self.tapel_masuk_le, "tapel_masuk"),
            (self.kls_masuk_le, "kls_masuk"),
            (self.no_urut_le,"no_urut"),
            (self.jenis_sekolah_cbo,"jenis_sekolah_asal"),
            (self.nama_sekolah_le, "nama_sekolah_asal"),
            (self.npsn_le,"npsn_sekolah_asal"),
            (self.nss_le,"nss_sekolah_asal"),
            (self.plain_alamat_sekolah,"alamat_sekolah_asal"),
            (self.pilihan_jenjang_cbo,"pilihan_jenjang"),
            (self.pilihan_jenjang_cbo2,"pilihan_jenjang"),
            (self.emis_cbo,"status_emis"),
            (self.vervalpd_cbo,"status_vervalpd"),
        ]

    def fill_combobox(self):
        combo_edit_biodata = {
            self.jk_cbo:list_from_db("JK"),
            self.agama_cbo:list_from_db("AGAMA"),
            self.cita_cita_cbo:list_from_db("CITA_CITA"),
            self.hobi_cbo:list_from_db("HOBI"),
            self.pembiayaan_cbo:list_from_db("BIAYA"),
            self.keb_khusus_cbo:list_from_db("KEB_KHUSUS"),
            self.ayah_status_cbo:list_from_db("STATUS_ORTU"),
            self.ayah_pendidikan_cbo:list_from_db("PENDIDIKAN"),
            self.ayah_pekerjaan_cbo:list_from_db("PEKERJAAN"),
            self.ayah_penghasilan_cbo:list_from_db("PENGHASILAN"),
            self.ibu_status_cbo:list_from_db("STATUS_ORTU"),
            self.ibu_pendidikan_cbo:list_from_db("PENDIDIKAN"),
            self.ibu_pekerjaan_cbo:list_from_db("PEKERJAAN"),
            self.ibu_penghasilan_cbo:list_from_db("PENGHASILAN"),
            self.wali_status_cbo:list_from_db("STATUS_WALI"),
            self.wali_pendidikan_cbo:list_from_db("PENDIDIKAN"),
            self.wali_pekerjaan_cbo:list_from_db("PEKERJAAN"),
            self.transportasi_cbo:list_from_db("TRANSPORTASI"),
            self.jarak_cbo:list_from_db("JARAK"),
            self.waktu_cbo:list_from_db("WAKTU_TEMPUH"),
            self.jenis_sekolah_cbo:list_from_db("JENIS_SEKOLAH"),
            self.pilihan_jenjang_cbo:list_from_db("PILIHAN_JENJANG"),
            self.pilihan_jenjang_cbo2:list_from_db("PILIHAN_JENJANG"),
        }
        for combo, values in combo_edit_biodata.items():
            combo.clear()
            combo.addItems(values() if callable(values) else values)
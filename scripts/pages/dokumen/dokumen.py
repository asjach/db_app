from PySide6.QtWidgets import QWidget, QMainWindow
from ui.ui_page_dokumen import Ui_Form
from models.dokumen import ModelDokumen
# from utils.app_config import *
from scripts.widgets.dokumen_viewer import DokumenViewer
from utils.fungsi.general_functions import *
from utils.static_values import TEMPLATE_KETERANGAN


class PageDokumen(QWidget, Ui_Form):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.dokumen_viewer = DokumenViewer()
        self.dokumen_container.addWidget(self.dokumen_viewer)
        self.SQL = ModelDokumen()
        self.cbo_filter_dokumen.setCurrentIndex(-1)
        self.frames = [
            self.frame_dokumen, self.frame_parameter, self.frame_browse,
            self.frame_copy_move, self.frame_eksekusi
        ]
        
        self._setup_connections()
        self.update_cbo_daftar2()

    def _setup_connections(self):
        # Radio buttons
        for radio in [self.radio_view, self.radio_input, self.radio_rename, 
                      self.radio_replace, self.radio_copy, self.radio_move, 
                      self.radio_delete]:
            radio.toggled.connect(self.radio_toggled)
        self.radio_tapel_aktif.toggled.connect(self.update_cbo_daftar)
        self.radio_all.toggled.connect(self.update_cbo_daftar)
        # Buttons
        self.btn_eksekusi.clicked.connect(self.btn_execute_clicked)
        self.btn_prev_nama.clicked.connect(lambda: prev_item(self.cbo_daftar))
        self.btn_next_nama.clicked.connect(lambda: next_item(self.cbo_daftar))
        self.btn_browse.clicked.connect(self.btn_browse_clicked)

        # Combo boxes
        self.cbo_filter_dokumen.currentIndexChanged.connect(self.update_tbl_dokumen)
        self.cbo_target.currentTextChanged.connect(self.show_page)
        self.cbo_daftar.currentIndexChanged.connect(self.cbo_daftar_selected)
        self.cbo_daftar2.currentIndexChanged.connect(self.cbo_daftar2_selected)
        self.cbo_jenis_dokumen.currentTextChanged.connect(self.cbo_jenis_dokumen_selected)
        self.cbo_template_keterangan.textActivated.connect(self.cbo_template_keterangan_selected)

        # Line edits
        self.line_search1.textChanged.connect(self.update_cbo_daftar)
        self.line_search2.textChanged.connect(self.update_cbo_daftar2)
        self.line_input_keterangan.editingFinished.connect(self.create_namafile)
        self.plain_path_source.textChanged.connect(self.create_namafile)

        # Table
        self.tbl_daftar_dokumen.itemSelectionChanged.connect(self.tbl_dokumen_selected)
        self.tbl_daftar_dokumen.itemClicked.connect(self.tbl_dokumen_selected)

    def show_page(self):
        self.update_cbo_daftar()

    def update_cbo_daftar(self):
        target = self.cbo_target.currentText()
        self.cbo_daftar.clear()
        data = self._get_data_for_target(target, self.line_search1.text())
        self._populate_combo(self.cbo_daftar, data)

    def update_tbl_dokumen(self):
        index = self.cbo_daftar.currentIndex()
        nomor_induk = self.cbo_daftar.itemData(index)
        self.tbl_daftar_dokumen.blockSignals(True)
        data = self.SQL.get_dokumen_by_nomor_induk(nomor_induk, self.cbo_filter_dokumen.currentText())
        generate_table(
            data=data,
            table=self.tbl_daftar_dokumen,
            hidden_column=[0, 1, 4],
            stretch_column=3,
            left_column=["jenis_dokumen", "keterangan"]
        )
        self.tbl_daftar_dokumen.blockSignals(False)
        self.tbl_daftar_dokumen.selectRow(0)

    def update_template_keterangan(self, selected_dokumen):
        self.cbo_template_keterangan.clear()
        self.cbo_template_keterangan.addItems(TEMPLATE_KETERANGAN.get(selected_dokumen, []))

    def update_cbo_daftar2(self):
        target = self.cbo_target.currentText()
        self.cbo_daftar2.clear()
        data = self._get_data_for_target(target, self.line_search2.text())
        self._populate_combo(self.cbo_daftar2, data)

    def _get_data_for_target(self, target, search_text):
        if target == 'Siswa':
            if self.radio_tapel_aktif.isChecked():
                return self.SQL.get_data_siswa_aktif(
                    jenjang=self.parent.cbo_jenjang.currentText(),
                    tapel=self.parent.cbo_tapel.currentText(),
                    tingkat=self.parent.cbo_tingkat.currentText(),
                    kelas=self.parent.cbo_kelas.currentText(),
                    search_text=search_text,
                )
            else:
                return self.SQL.get_data_siswa(search_text)
        elif target == 'Guru':
            return self.SQL.get_data_guru(search_text=search_text)
        return []

    def _populate_combo(self, combo, data):
        for item in data:
            if isinstance(item, dict):
                id_value = item.get('id_guru') or item.get('nis_lokal')
                nama_lengkap = item.get('nama_lengkap', 'Unknown Name')
                combo.addItem(nama_lengkap, id_value)
            else:
                combo.addItem(str(item))

    def cbo_daftar_selected(self):
        nomor_induk = self.cbo_daftar.currentData()
        self.line_input_nomor_induk.setText(nomor_induk)
        self.update_tbl_dokumen()
        self.create_namafile()
        if self.tbl_daftar_dokumen.rowCount() > 0 and not self.radio_input.isChecked():
            self.dokumen_viewer.loadFile(self.path)
        else:
            self.dokumen_viewer.close_file()
            self.dokumen_viewer.image_viwer_label.clear()

    def cbo_jenis_dokumen_selected(self):
        self.line_input_keterangan.clear()
        self.update_template_keterangan(self.cbo_jenis_dokumen.currentText())
        self.create_namafile()

    def tbl_dokumen_selected(self):
        set_attributes_values(self, self.tbl_daftar_dokumen)
        if self.tbl_daftar_dokumen.rowCount() > 0:
            self.line_id.setText(self.id)
            self.line_nomor_induk.setText(self.nomor_induk)
            self.line_jenis_dokumen_db.setText(self.jenis_dokumen)
            self.cbo_jenis_dokumen.setCurrentText(self.jenis_dokumen)
            self.line_keterangan_db.setText(self.keterangan)
            self.line_input_keterangan.setText(self.keterangan)
            self.line_namafile_db.setText(self.namafile)
            target = self.cbo_target.currentText().lower()
            self.path = f"{value_from_db('DOKUMEN_PATH')}/{target}/{self.namafile}"
            self.plain_path_db.setPlainText(self.path)
            if not self.radio_input.isChecked():
                self.dokumen_viewer.loadFile(self.path)
        else:
            self.dokumen_viewer.close_file()
            self.dokumen_viewer.image_viwer_label.clear()
        self.create_namafile()

    def cbo_template_keterangan_selected(self):
        keterangan = self.cbo_template_keterangan.currentText()
        self.line_input_keterangan.setText(keterangan)
        self.create_namafile()

    def cbo_daftar2_selected(self):
        nomor_induk = self.cbo_daftar2.currentData()
        self.line_nomor_induk2.setText(nomor_induk)
        self.create_namafile()

    def btn_browse_clicked(self):
        open_dialog(self, self.plain_path_source)
        self.dokumen_viewer.loadFile(self.plain_path_source.toPlainText())

    def btn_execute_clicked(self):
        currentIndex = self.cbo_daftar.currentIndex()
        self.dokumen_viewer.close_file()
        operations = {
            self.radio_input: self.input_operations,
            self.radio_rename: self.rename_operations,
            self.radio_replace: self.replace_operations,
            self.radio_copy: self.copy_operations,
            self.radio_move: self.move_operations,
            self.radio_delete: self.delete_operations,
        }
        for radio, operation in operations.items():
            if radio.isChecked():
                operation()
                break
        if currentIndex:
            self.clear_controls()
            self.cbo_daftar.setCurrentIndex(currentIndex)
        # self.clear_controls()

    def radio_toggled(self):
        self.create_namafile()
        self.update_tbl_dokumen()
        if self.tbl_daftar_dokumen.rowCount() > 0:
            self.dokumen_viewer.loadFile(self.path)
        else: 
            self.dokumen_viewer.close_file()
            self.dokumen_viewer.image_viwer_label.clear()

        operations = {
            self.radio_view: self.view_selected,
            self.radio_input: self.input_selected,
            self.radio_rename: self.rename_selected,
            self.radio_replace: self.replace_selected,
            self.radio_copy: self.copy_selected,
            self.radio_move: self.move_selected,
            self.radio_delete: self.delete_selected,
        }
        for radio, operation in operations.items():
            if radio.isChecked():
                operation()
                break

    def view_selected(self):
        self.set_frame_visibility([self.frame_dokumen])
        
    def input_selected(self):
        self.set_frame_visibility([
            self.frame_parameter, 
            self.frame_browse, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("TAMBAH")
        self.path = None
        self.dokumen_viewer.image_viwer_label.clear()
        self.dokumen_viewer.close_file()
        self.create_namafile()

    def rename_selected(self):
        self.set_frame_visibility([
            self.frame_dokumen, 
            self.frame_parameter, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("RENAME")
        self.create_namafile()

    def replace_selected(self):
        self.set_frame_visibility([
            self.frame_dokumen, 
            self.frame_browse, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("REPLACE")
        self.create_namafile()

    def copy_selected(self):
        self.set_frame_visibility([
            self.frame_dokumen, 
            self.frame_parameter, 
            self.frame_copy_move, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("COPY")
        self.update_cbo_daftar2()
        self.create_namafile()

    def move_selected(self):
        self.set_frame_visibility([
            self.frame_dokumen, 
            self.frame_parameter, 
            self.frame_copy_move, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("MOVE")
        self.update_cbo_daftar2()
        self.create_namafile()

    def delete_selected(self):
        self.set_frame_visibility([
            self.frame_dokumen, 
            self.frame_eksekusi
        ])
        self.btn_eksekusi.setText("DELETE")
        self.create_namafile()

    def input_operations(self): 
        source = self.plain_path_source.toPlainText()
        if source != "":
            sukses = self.add_dokumen()
            if sukses:
                self._handle_file_operation("copy", self.path_asal, self.path_tujuan)
                self._handle_file_operation("move", self.path_asal, self.path_delete, 
                                            "Pindahkan file yang sudah diinput?")
                
    def rename_operations(self):
        sukses = self.rename_dokumen()
        if sukses:
            self._handle_file_operation("move", self.path_asal, self.path_tujuan)

    def replace_operations(self):
        source = self.plain_path_source.toPlainText()
        sukses = self.replace_dokumen()
        if sukses:
            self._handle_file_operation("move", self.path_asal, self.path_delete)
            self._handle_file_operation("copy", source, self.path_tujuan)
            sudah = os.path.join(os.path.dirname(source), "sudah", os.path.basename(source))
            self._handle_file_operation("move", source, sudah, "Pindahkan file yang sudah diinput?")

    def copy_operations(self):
        sukses = self.copy_dokumen()
        if sukses:
            self._handle_file_operation("copy", self.path_asal, self.path_tujuan)

    def move_operations(self):
        sukses = self.move_dokumen()
        if sukses:
            self._handle_file_operation("move", self.path_asal, self.path_tujuan)

    def delete_operations(self):
        sukses = self.delete_dokumen()
        if sukses:
            self._handle_file_operation("move", self.path_asal, self.path_delete)
            
    def _handle_file_operation(self, operation, source, destination, confirm_message=None):
        create_folder(os.path.dirname(destination))
        if operation == "copy":
            shutil.copy(source, destination)
        elif operation == "move":
            shutil.move(source, destination)
        if confirm_message:
            aksi = pesan_konfirmasi("Konfirmasi", confirm_message)
            if aksi:
                shutil.move(source, os.path.join(os.path.dirname(source), "sudah", os.path.basename(source)))

    def add_dokumen(self):
        parameter = {
            'nomor_induk' : self.line_input_nomor_induk.text(),
            'jenis_dokumen' : self.cbo_jenis_dokumen.currentText(),
            'sub_folder' : self.cbo_target.currentText().lower(),
            'keterangan' : self.line_input_keterangan.text(),
            'namafile' : self.namafile_tujuan
        }
        return self.SQL.input_dokumen(**parameter)
    
    def rename_dokumen(self):
        parameter = {
            'jenis_dokumen': self.cbo_jenis_dokumen.currentText(),
            'keterangan':self.line_input_keterangan.text(),
            'namafile': self.namafile_tujuan,
        }
        return update_from_controls(
            tabel_sql='dokumen', 
            key_column='id', 
            key_value=self.line_id.text(), 
            **parameter)
    
    def replace_dokumen(self):
        parameter = {'namafile': self.namafile_tujuan,}
        return update_from_controls(
            tabel_sql='dokumen', 
            key_column='id', 
            key_value=self.line_id.text(), 
            **parameter)

    def copy_dokumen(self):
        parameter = {
            'nomor_induk' : self.line_nomor_induk2.text(),
            'jenis_dokumen' : self.cbo_jenis_dokumen.currentText(),
            'sub_folder' : self.cbo_target.currentText().lower(),
            'keterangan' : self.line_input_keterangan.text(),
            'namafile' : self.namafile_tujuan
        }
        return self.SQL.input_dokumen(**parameter)

    def move_dokumen(self):
        parameter = {
            'nomor_induk' : self.line_nomor_induk2.text(),
            'namafile' : self.namafile_tujuan
        }
        return update_from_controls(
            tabel_sql='dokumen',
            key_column= 'id',
            key_value=self.line_id.text(),
            **parameter)
    
    def delete_dokumen(self):
        return delete_by_id('dokumen', 'id', self.line_id.text())

    def create_namafile(self):
        jenis_dok_db = self.line_jenis_dokumen_db.text()
        keterangan_db = self.line_keterangan_db.text()
        namafile_db = self.line_namafile_db.text()
        path_db = self.plain_path_db.toPlainText()
        nama = self.cbo_daftar.currentText()
        jenis_dok_input = self.cbo_jenis_dokumen.currentText()
        keterangan_input = self.line_input_keterangan.text()
        source = self.plain_path_source.toPlainText()
        target = self.cbo_target.currentText().lower()
        folder_tujuan_save = f"{value_from_db('DOKUMEN_PATH')}/{target}/"
        folder_tujuan_delete = f"{value_from_db('DOKUMEN_PATH')}/{target}/delete/"
        nama_baru = self.cbo_daftar2.currentText()
        path_browse_input = source
        jenis_dok = self.cbo_jenis_dokumen.currentText()
        self.btn_eksekusi.setEnabled(False)
        # if self.radio_view.isChecked():
        #     ...
        if self.radio_input.isChecked():
            if source != '' and jenis_dok != '':
                namafile_asal = os.path.basename(path_browse_input)
                namafile_tujuan = create_filename(
                    nama, 
                    jenis_dok_input, 
                    keterangan_input, 
                    path_browse_input, 
                    folder_tujuan_save
                )
                path_tujuan = folder_tujuan_save + namafile_tujuan
                path_delete = f"{os.path.dirname(path_browse_input)}/sudah/"+namafile_asal     
                self.create_attributes(
                    namafile_asal, 
                    path_browse_input, 
                    namafile_tujuan, 
                    path_tujuan,
                    namafile_asal, 
                    path_delete
                )           
                self.btn_eksekusi.setEnabled(True)
        elif self.radio_rename.isChecked():
            namafile_tujuan = create_filename(nama, jenis_dok_input, keterangan_input, path_db, folder_tujuan_save)
            if namafile_tujuan!= namafile_db :
                namafile_tujuan = create_filename(nama, jenis_dok_input, keterangan_input, path_db, folder_tujuan_save)
                path_tujuan = folder_tujuan_save + namafile_tujuan
                self.create_attributes(namafile_db, path_db, namafile_tujuan, path_tujuan, None, None)               
                self.btn_eksekusi.setEnabled(True)
        elif self.radio_replace.isChecked():
            if source != '':
                namafile_tujuan = create_filename(nama, jenis_dok_input, keterangan_input, 
                    path_browse_input, folder_tujuan_save)
                path_tujuan = folder_tujuan_save + namafile_tujuan
                path_delete = folder_tujuan_delete + namafile_db
                self.create_attributes(
                    namafile_db, 
                    path_db, 
                    namafile_tujuan, 
                    path_tujuan,
                    namafile_db, 
                    path_delete
                )
                self.btn_eksekusi.setEnabled(True)
        elif self.radio_copy.isChecked():
            namafile_baru = create_filename(
                    nama_baru, 
                    jenis_dok_db, 
                    keterangan_db,
                    path_db, 
                    folder_tujuan_save
                )
            if self.namafile != namafile_baru:
                path_asal = folder_tujuan_save + namafile_db
                namafile_tujuan = create_filename(
                    nama_baru, 
                    jenis_dok_db, 
                    keterangan_db,
                    path_db, 
                    folder_tujuan_save
                )
                path_tujuan = folder_tujuan_save + namafile_tujuan
                self.create_attributes(namafile_db, path_asal, namafile_tujuan, path_tujuan, None, None)
                self.btn_eksekusi.setEnabled(True)
        elif self.radio_move.isChecked():
            if self.cbo_daftar.currentText() != self.cbo_daftar2.currentText():
                path_asal = folder_tujuan_save + namafile_db
                namafile_tujuan = create_filename(nama_baru,jenis_dok_db,
                    keterangan_db, path_db, folder_tujuan_save)
                path_tujuan = folder_tujuan_save + namafile_tujuan
                self.create_attributes(namafile_db, path_asal, namafile_tujuan, path_tujuan, None, None)
                self.btn_eksekusi.setEnabled(True)
        elif self.radio_delete.isChecked():
            if self.plain_path_db.toPlainText() != '':
                path_delete = folder_tujuan_delete + namafile_db
                self.create_attributes(namafile_db, path_db, None, None, namafile_db, path_delete)
                self.btn_eksekusi.setEnabled(True)

    def create_attributes(self, nama_asal, path_asal, file_tujuan, path_tujuan, file_delete, path_delete):
        self.namafile_asal = nama_asal
        self.path_asal = path_asal
        self.namafile_tujuan = file_tujuan
        self.path_tujuan = path_tujuan
        self.namafile_delete = file_delete
        self.path_delete = path_delete
        
    def set_frame_visibility(self, frame_to_show):
        for frame in self.frames:
            frame.hide()
        for frame in frame_to_show:
            frame.show()

    def clear_controls(self):
        controls = [
            self.line_id, self.line_nomor_induk, self.line_jenis_dokumen_db,
            self.line_keterangan_db, self.line_namafile_db, self.plain_path_db,
            self.cbo_jenis_dokumen, self.line_input_keterangan, self.cbo_template_keterangan,
            self.plain_path_source, self.cbo_daftar2
        ]
        clear_inputs(controls)
        self._reset_attributes()
        self.update_cbo_daftar()
        self.update_tbl_dokumen()
        self.dokumen_viewer.close_file()
        self.dokumen_viewer.image_viwer_label.clear()

    def _reset_attributes(self):
        self.id = None
        self.namafile = None
        self.nis_lokal = None
        self.keterangan = None
        self.sub_folder = None
        self.path = None
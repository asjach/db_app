from ui.ui_main import Ui_MainWindow
# from ui.ui_main2 import Ui_MainWindow
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from scripts import *
from utils.fungsi.general_functions import *
from models.main import ModelMain
from utils.tab_config import *
from PySide6.QtCore import QEvent, Qt

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_property_for_qss()
        self.showMaximized()
        self.apply_style()
        self._is_processing_tab_change = False 
        self.is_window_maximized = True
        self.nis_lokal = None
        self.nis_index = None
        self.id_guru = None
        # Properties
        self._last_search_text = ''
        self.model_main = ModelMain()
        # Context menu
        self.cmenu = QMenu()
        self.hideshow_frame_action = QAction("Show/Hide Left Frame")
        self.detail_siswa_action = QAction("Detail Siswa")
        self.detail_guru_action = QAction("Detail Guru")
        
        # Initialize components
        self.initialize_components()
        
    def initialize_components(self):
        self.filter_connections()
        self.setup_timer()
        self.class_init()
        self.installEventFilters()
        self.add_combo_value()
        self.connect_signals()
        self.actionDaftar_Kelas.trigger()
        # self.actionInput_By_Excel.trigger()
        
    def connect_signals(self):
        # Combobox signals
        for combo in [self.cbo_order_by, self.cbo_kolom, self.cbo_kelas]:
            combo.currentIndexChanged.connect(self.delayed_requery)
        for combo in [self.cbo_jenjang, self.cbo_tapel, self.cbo_tingkat]:
            combo.currentIndexChanged.connect(self.requery_kelas)

        # Tab and search signals
        self.line_search.textChanged.connect(self.delayed_search)
        self.main_tab.currentChanged.connect(self.tab_index_changed)
        self.main_tab.tabCloseRequested.connect(self.close_tab)
        self.actionShow_Filter.toggled.connect(self.show_hide_filter)

        # Action signals
        self.actionDaftar_Kelas.triggered.connect(lambda: self.add_tab(self.DK, "Daftar Kelas"))
        self.actionRekap_Santri.triggered.connect(lambda: self.add_tab(self.REKAP_SISWA, "Rekap Siswa"))
        self.actionPindah_Kelas.triggered.connect(lambda: self.add_tab(self.PINDAH_KELAS, "Pindah Kelas"))
        self.actionMutasiMasuk.triggered.connect(lambda: self.add_tab(self.MUTASI_MASUK, "Mutasi Masuk"))
        self.actionMutasiKeluar.triggered.connect(lambda: self.add_tab(self.MUTASI_KELUAR, "Mutasi Keluar"))
        self.actionKenaikan.triggered.connect(lambda: self.add_tab(self.NAIK, "Kenaikan"))
        self.actionKelulusan.triggered.connect(lambda: self.add_tab(self.LULUS, "Kelulusan"))
        self.actionMI_ke_MD.triggered.connect(lambda: self.add_tab(self.MI2MD, "MI ke MD"))
        
        self.actionBukuIndukGuru.triggered.connect(lambda: self.add_tab(self.BUKUINDUKGURU, "Buku Induk Guru"))
        self.actionRiwayatKeaktifan.triggered.connect(lambda: self.add_tab(self.KEAKTIFANGURU, "Keaktifan Guru"))
        self.actionRiwayat_Mengajar.triggered.connect(lambda: self.add_tab(self.RIWAYAT_MENGAJAR, "Riwayat Mengajar"))
        self.actionInput_Dokumen.triggered.connect(lambda: self.add_tab(self.DOKUMEN, "Dokumen"))
        self.actionPengaturanKegiatan.triggered.connect(lambda:self.add_tab(self.PENGATURAN_KEGIATAN, "Pengaturan Kegiatan"))
        self.actionInput_Nilai.triggered.connect(lambda: self.add_tab(self.INPUT_NILAI, "Input Nilai"))
        self.actionRekap.triggered.connect(lambda: self.add_tab(self.REKAP_NILAI, 'Rekap Nilai'))

        self.actionRiwayatKelas.triggered.connect(lambda: self.add_tab(self.RIWAYAT_KELAS, "Riwayat Kelas"))
        self.actionAlamat.triggered.connect(lambda: self.add_tab(self.ALAMAT, "Alamat"))
        self.actionInput_By_Excel.triggered.connect(self.show_input_excel)
        self.actionCari.triggered.connect(self.show_detail_siswa)
        self.actionInput_Preferensi.triggered.connect(self.show_input_preferensi)
    
    def filter_connections(self):
        fungsi_filter_buttons(self.cbo_jenjang, self.prev_jenjang, self.next_jenjang,self.label_jenjang)
        fungsi_filter_buttons(self.cbo_tapel, self.prev_tapel, self.next_tapel, self.label_tapel)
        fungsi_filter_buttons(self.cbo_tingkat, self.prev_tingkat, self.next_tingkat, self.label_tingkat)
        fungsi_filter_buttons(self.cbo_kelas, self.prev_kelas, self.next_kelas, self.label_kelas)
        fungsi_filter_buttons(self.cbo_order_by, self.prev_order_by, self.next_order_by)
        fungsi_filter_buttons(self.cbo_kolom, self.prev_kolom, self.next_kolom, )

    def setup_timer(self):
        self.requery_timer = QTimer(self)
        self.requery_timer.setInterval(400)
        self.requery_timer.setSingleShot(True)
        # self.requery_timer.timeout.connect(self.tab_index_changed)
        self.requery_timer.timeout.connect(self.requery_page)

    def class_init(self):
        # PAGE SISWA
        self.DK = PageDaftarKelas(self)
        self.REKAP_SISWA = PageRekapSiswa(self)
        self.PINDAH_KELAS = PagePindahKelas(self)
        self.MUTASI_MASUK = PageMutasiMasuk(self)
        self.MUTASI_KELUAR = PageMutasiKeluar(self)
        self.NAIK = PageKenaikan(self)
        self.LULUS = PageKelulusan(self)
        self.MI2MD = PageMI2MD(self)
        
        #PAGE GURU
        self.BUKUINDUKGURU=PageBukuIndukGuru(self)
        self.KEAKTIFANGURU=PageKeaktifanGuru(self)
        self.RIWAYAT_MENGAJAR = PageRiwayatMengajar(self)

        #PAGE DOKUMEN
        self.DOKUMEN = PageDokumen(self)

        #PAGE NILAI
        self.PENGATURAN_KEGIATAN = PagePengaturanKegiatan(self)
        self.INPUT_NILAI = PageInputNilai(self)
        self.REKAP_NILAI = PageRekapNilai(self)

        # PREFERENSI
        self.RIWAYAT_KELAS = PageRiwayatKelas(self)
        self.ALAMAT = PageAlamat(self)


    def add_combo_value(self):
        combo_values = {
            self.cbo_jenjang: JENJANG,
            self.cbo_tapel: self.model_main.get_list_tapel,
            self.cbo_tingkat: TINGKAT,
            self.DOKUMEN.cbo_jenis_dokumen:JENIS_DOKUMEN,
            self.DOKUMEN.cbo_filter_dokumen:JENIS_DOKUMEN
        }
        for combo, values in combo_values.items():
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(values() if callable(values) else values)
            combo.blockSignals(False)
        self.requery_kelas()

    def requery_kelas(self):
        data_kelas = self.model_main.get_list_kelas(
            jenjang=self.cbo_jenjang.currentText(),
            tapel=self.cbo_tapel.currentText(),
            tingkat=self.cbo_tingkat.currentText()
        )
        # self.cbo_kelas.blockSignals(True)
        self.cbo_kelas.clear()
        self.cbo_kelas.addItem("")
        self.cbo_kelas.addItems(data_kelas or [self.cbo_tingkat.currentText()])
        self.cbo_kelas.setCurrentIndex(0)
        # self.cbo_kelas.blockSignals(False)

    def add_tab(self, page_class, title):
        existing_tabs = [self.main_tab.tabText(i) for i in range(self.main_tab.count())]
        if title in existing_tabs:
            self.main_tab.setCurrentIndex(existing_tabs.index(title))
            return

        if isinstance(page_class, type):
            page_instance = page_class(self)
        else:
            page_instance = page_class
        self.main_tab.addTab(page_instance, title)
        self.main_tab.setCurrentWidget(page_instance)

    def close_tab(self, index):
        self.main_tab.removeTab(index)

    def tab_index_changed(self):
        current_index = self.main_tab.currentIndex()
        if current_index == -1:
            return
        tab_name = self.main_tab.tabText(current_index)
        config = TAB_CONFIG.get(tab_name, {})
        self.cbo_kolom.blockSignals(True)
        self.cbo_order_by.blockSignals(True)
        self.cbo_kolom.clear()
        self.cbo_order_by.clear()
        self.cbo_search_by.clear()
        frames = {
            "jenjang": self.frame_jenjang,
            "tapel": self.frame_tapel,
            "tingkat": self.frame_tingkat,
            "kelas": self.frame_kelas,
            "order_by": self.frame_order_by,
            "search_by": self.frame_search,
            "kolom": self.frame_kolom,
        }
        default_visible_frames = {"jenjang", "tapel", "tingkat", "kelas"}
        for key, frame in frames.items():
            is_default_visible = key in default_visible_frames
            is_visible = is_default_visible or (config.get(key) and config[key])
            frame.setVisible(bool(is_visible))
            if is_visible and key not in default_visible_frames:
                combo_box = getattr(self, f"cbo_{key}")
                combo_box.addItems(config.get(key, []))
        hidden_frames = config.get("hidden_frame", set())
        for frame_name in hidden_frames:
            frame = frames.get(frame_name.lower())
            if frame:
                frame.setVisible(False)
        self.cbo_kolom.blockSignals(False)
        self.cbo_order_by.blockSignals(False)
        self.cbo_search_by.blockSignals(False)
        self.requery_page()

    def requery_page(self):
        tab_name = self.main_tab.tabText(self.main_tab.currentIndex())
        config = TAB_CONFIG.get(tab_name)
        if config and hasattr(self, config["show_page"]):
            getattr(self, config["show_page"]).show_page()


    def delayed_action(self, interval=200, update_text=None, is_search=False):
        if is_search and update_text != self.last_search_text:
            self.last_search_text = update_text
            interval = 100 if update_text == "" else 200

        self.requery_timer.setInterval(interval)
        self.requery_timer.stop()
        self.requery_timer.start()

    def delayed_requery(self):
        self.delayed_action()

    def delayed_search(self):
        self.delayed_action(update_text=self.line_search.text(), is_search=True)

    @property
    def last_search_text(self):
        return self._last_search_text

    @last_search_text.setter
    def last_search_text(self, value):
        if value != getattr(self, "_last_search_text", None):
            self._last_search_text = value

    def show_detail_siswa(self, tabel):
        print(self.nis_lokal)
        self.EDIT_BIODATA = DialogDetailSiswa(self)
        self.EDIT_BIODATA.setStyleSheet(self.style)
        self.EDIT_BIODATA.show_dialog(
            tabel= tabel, 
            nis_lokal=self.nis_lokal, 
            nis_index=self.nis_index)
        self.EDIT_BIODATA.showMaximized()

    def show_detail_guru(self):
        self.DETAIL_GURU = DialogDetailGuru(self)
        self.DETAIL_GURU.show_dialog(self.id_guru)
        self.DETAIL_GURU.showMaximized()

    def show_input_excel(self):
        self.INPUT_EXCEL = DialogInputExcel(self)
        self.INPUT_EXCEL.show_dialog()
        self.INPUT_EXCEL.show()

    def show_input_preferensi(self):
        self.INPUT_PREFERENSI = DialogInputPreferensi(self)
        self.INPUT_PREFERENSI.show_dialog()
        self.INPUT_PREFERENSI.show()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu:
            self.handle_context_menu(source)
            action = self.cmenu.exec(source.mapToGlobal(event.pos()))
            if action == self.detail_siswa_action:
                self.show_detail_siswa(source)
            if action == self.detail_guru_action:
                self.show_detail_guru()
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                copyCells(source)
                print("COPIED")
                return True
        return super().eventFilter(source, event)
    
    def handle_context_menu(self, source):
        self.cmenu.clear()
        if source in self.tabel_siswa:
            self.cmenu.addActions([
                self.detail_siswa_action,
            ])
        elif source in self.tabel_guru:
            self.cmenu.addActions([
                self.detail_guru_action,
            ])
        
    def installEventFilters(self):
        self.tabel_tabel()
        for tabel in self.findChildren(QTableWidget):
            tabel.installEventFilter(self)

    def tabel_tabel(self):
        sub_class_siswa = [
            self.DK, self.NAIK, self.LULUS, self.MUTASI_KELUAR, self.PINDAH_KELAS, self.MI2MD, self.REKAP_SISWA
        ]
        self.tabel_siswa = []
        for parent_class in sub_class_siswa:
            self.tabel_siswa.extend(parent_class.findChildren(QTableWidget))

        sub_class_guru = [self.BUKUINDUKGURU, self.KEAKTIFANGURU, self.RIWAYAT_MENGAJAR]
        self.tabel_guru = []
        for parent_class in sub_class_guru:
            self.tabel_guru.extend(parent_class.findChildren(QTableWidget))

        sub_class_nilai = [self.PENGATURAN_KEGIATAN, self.INPUT_NILAI]
        self.tabel_nilai = []
        for parent_class in sub_class_nilai:
            self.tabel_nilai.extend(parent_class.findChildren(QTableWidget))

    def show_hide_filter(self):
        if self.actionShow_Filter.isChecked():
            self.frame_filter.show()
        else:
            self.frame_filter.hide()

    def apply_style(self):
        with open('resources/style.qss', 'r') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)

    def set_property_for_qss(self):...
        # self.frame_filter.setProperty("class", 'judul')


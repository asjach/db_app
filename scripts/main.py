from functools import partial
from ui.ui_main import Ui_MainWindow
from PySide6.QtCore import QTimer, QEvent, Qt
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from scripts import *
from models.model_main import Model_Main
from scripts.tab_config import TAB_CONFIG
from utils.static_values import *
from utils.fungsi.general_functions import *
from resources.color_var import THEMES

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.list_tingkat.setItemDelegate(CenteredDelegate())
        self.list_kelas.setItemDelegate(CenteredDelegate())
        self.list_jenjang.setItemDelegate(CenteredDelegate())
        centerize_combo(self.cbo_tapel)
        self.showMaximized()
        # ThemeManager.apply_theme(self, 'dark', './resources/style.qss')
        register_all_windows_fonts()
        self.static_values = get_json_data(os.path.join("D:/APP/DB App", "utils", "static_values.json"))
        self.toggle_theme()
        ## VARIABEL INITIALIZATION
        self.str_jenjang = None
        self._last_search_text = ''
        # Tingkat
        self.quoted_daftar_tingkat =None  ## list tingkat berupa string dengan tanda petik -> "'1', '2', '3'" untuk IN di sql
        self.not_quoted_daftar_tingkat=None ## list tingkat berupa string tanpa tanda petik -> "1, 2, 3" untuk IN di sql
        self.list_daftar_tingkat = None ## list tingkat -> ['1', '2', '3']
        self.quoted_tingkat = None # '1'
        self.not_quoted_tingkat = None  # 1
        # Kelas
        self.quoted_daftar_kelas =None  ## list kelas berupa string dengan tanda petik -> "'1', '2', '3'" untuk IN di sql
        self.str_kelas=None
  
        self.nis_lokal = None
        self.nis_index = None
        self.model_main = Model_Main()
        self.cmenu = QMenu()
        self.detail_siswa_action = QAction("Detail Siswa")
        self.detail_guru_action = QAction("Detail Guru")
        self.tidak_naik_action = QAction("Tidak Naik")

        self.requery_timer = QTimer(self)
        self.requery_timer.setInterval(400)
        self.requery_timer.setSingleShot(True)
        self.requery_timer.timeout.connect(self.requery_page)
        self.initialize_components()
        
    def initialize_components(self):
        self.list_kelas.setFixedWidth(0)
        self.add_combo_value()
        self.connect_signals()
        self.list_jenjang.setCurrentRow(0)
        self.list_tingkat.setCurrentRow(0)
        self.actionDaftar_Kelas.trigger()
    
    def connect_signals(self):
        # INIT CLASSES
        for config in TAB_CONFIG.values():
            attr_name = config["show_page"]
            page_class = config["page_class"]
            setattr(self, attr_name, page_class(self))
        self.tabel_tabel()
        for tabel in self.findChildren(QTableWidget):
            tabel.installEventFilter(self)
        # fungsi_filter_buttons(self.cbo_jenjang, self.prev_jenjang, self.next_jenjang,self.label_jenjang)
        fungsi_filter_buttons(self.cbo_tapel)
        fungsi_filter_buttons(self.cbo_order_by)
        fungsi_filter_buttons(self.cbo_kolom)
        combobox_mapping = {
            "delayed_requery": [self.cbo_order_by, self.cbo_kolom],
            "requery_kelas": [self.cbo_tapel]
        }
        for signal, combos in combobox_mapping.items():
            for combo in combos:
                combo.currentIndexChanged.connect(getattr(self, signal))

        for title, config in TAB_CONFIG.items():
            attr_name = config["show_page"]
            action_name = config["action"]
            page = getattr(self, attr_name)
            action = getattr(self, action_name)
            action.triggered.connect(partial(self.add_tab, page, title))
        # Tab and search signals
        self.line_search.textChanged.connect(self.delayed_search)
        self.main_tab.currentChanged.connect(self.tab_index_changed)
        self.main_tab.tabCloseRequested.connect(self.close_tab)
        # DIALOG
        self.actionInput_By_Excel.triggered.connect(lambda: DialogInputExcel(self).exec())
        self.actionExport_Excel.triggered.connect(lambda: DialogExportExcel(self).exec())
        self.actionStatic_Values.triggered.connect(lambda: Dialog_Static_Values(self).exec())
        self.actionCari.triggered.connect(self.show_detail_siswa)
        # VIEW
        self.actionShow_Filter.toggled.connect(self.show_hide_filter)
        self.list_jenjang.itemSelectionChanged.connect(self.list_jenjang_selected)
        self.list_tingkat.itemSelectionChanged.connect(self.list_tingkat_selected)
        self.list_kelas.itemSelectionChanged.connect(self.list_kelas_selected)
        self.actionDark_Mode.toggled.connect(self.toggle_theme)

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

    def close_tab(self, index):
        self.main_tab.removeTab(index)

    def requery_page(self):
        tab_name = self.main_tab.tabText(self.main_tab.currentIndex())
        config = TAB_CONFIG.get(tab_name)
        if config and hasattr(self, config["show_page"]):
            getattr(self, config["show_page"]).show_page()

    def add_combo_value(self):
        combo_values = {
            self.cbo_tapel: self.model_main.get_list_tapel,}
        for combo, values in combo_values.items():
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(values() if callable(values) else values)
            combo.blockSignals(False)
        self.requery_kelas()

    def list_jenjang_selected(self):
        self.str_jenjang = self.list_jenjang.currentItem().text().strip()
        self.requery_kelas()

    def list_tingkat_selected(self):
        self.quoted_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat, 'quoted')
        self.not_quoted_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat, 'not_quoted')
        self.list_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat)
        self.quoted_tingkat = get_selected_list_widget_item(self.list_tingkat, 'quoted')
        self.not_quoted_tingkat = get_selected_list_widget_item(self.list_tingkat, 'not_quoted')
        self.requery_kelas()

    def requery_kelas(self):
        self.list_kelas.clear()
        data_kelas = self.model_main.get_kelas(
            jenjang=self.str_jenjang,
            tapel=self.cbo_tapel.currentText(),
            tingkat=self.quoted_daftar_tingkat
            )
        
        populate_list_widget(self.list_kelas, data_kelas, False, False, 'kelas', 'id')
        self.list_kelas.setFixedWidth(int((len(data_kelas)+1)*25.5))
        
        self.delayed_requery()

    def list_kelas_selected(self):
        self.quoted_daftar_kelas = get_selected_list_widget_items(self.list_kelas, 'quoted')
        self.str_kelas = self.list_kelas.currentItem().text()
        self.data_kelas = get_selected_list_widget_data(self.list_kelas)
        self.delayed_requery()

    def delayed_action(self, interval=200, update_text=None, is_search=False):
        if is_search and update_text != self.last_search_text:
            self.last_search_text = update_text
            interval = 100 if update_text == "" else 200

        self.requery_timer.setInterval(interval)
        self.requery_timer.stop()
        self.requery_timer.start()

    def delayed_requery(self):
        self.delayed_action(interval=200)

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
        self.EDIT_BIODATA = DialogDetailSiswa(self)
        ThemeManager.apply_theme(self.EDIT_BIODATA, 'dark', './resources/style.qss')
        self.EDIT_BIODATA.show_dialog(
            tabel= tabel, 
            nis_lokal=self.nis_lokal, 
            nis_index=self.nis_index)
        self.EDIT_BIODATA.showMaximized()

    def show_detail_guru(self):
        self.DETAIL_GURU = DialogDetailGuru(self)
        self.DETAIL_GURU.show_dialog(self.id_guru)
        self.DETAIL_GURU.showMaximized()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu:
            self.handle_context_menu(source)
            action = self.cmenu.exec(source.mapToGlobal(event.pos()))
            if action == self.detail_siswa_action:
                self.show_detail_siswa(source)
            elif action == self.detail_guru_action:
                self.show_detail_guru()
            elif action == self.tidak_naik_action:
                self.self.NAIK.tidak_naikkan_siswa()
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                copyCells(source)
                print("COPIED")
                return True
            elif event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
                pasteCells(source)
                print("PASTED")
                return True
        return super().eventFilter(source, event)
    
    def handle_context_menu(self, source):
        self.cmenu.clear()
        if source in self.tabel_siswa:
            self.cmenu.addActions([
                self.detail_siswa_action,
            ])
            nama_tabel = source.objectName()
            if nama_tabel == 'tbl_list_siswa_kenaikan':
               self.cmenu.addAction(self.tidak_naik_action,) 
        elif source in self.tabel_guru:
            self.cmenu.addActions([
                self.detail_guru_action,
            ])
            
    def tabel_tabel(self):
        sub_class_siswa = [
            self.BUKU_INDUK_SISWA, self.CEKLIS_EMIS, self.DK, self.NAIK, self.LULUS, self.MUTASI_KELUAR, self.PINDAH_KELAS, self.MI2MD, self.REKAP_SISWA
        ]
        self.tabel_siswa = []
        for parent_class in sub_class_siswa:
            self.tabel_siswa.extend(parent_class.findChildren(QTableWidget))

        sub_class_guru = [self.BUKUINDUKGURU, self.KEAKTIFANGURU, self.RIWAYAT_MENGAJAR]
        self.tabel_guru = []
        for parent_class in sub_class_guru:
            self.tabel_guru.extend(parent_class.findChildren(QTableWidget))

        sub_class_nilai = [self.INPUT_NILAI]
        self.tabel_nilai = []
        for parent_class in sub_class_nilai:
            self.tabel_nilai.extend(parent_class.findChildren(QTableWidget))
        
    def show_hide_filter(self):
        if self.actionShow_Filter.isChecked():
            self.frame_filter.show()
        else:
            self.frame_filter.hide()

    def apply_style(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        STYLE_PATH = os.path.join(BASE_DIR, '..', 'resources', 'style.qss')
        with open(STYLE_PATH, 'r') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)

    def toggle_theme(self):
        ThemeManager.apply_theme(self, 'dark', './resources/style.qss')
        # if self.actionDark_Mode.isChecked():
        #     ThemeManager.apply_theme(self, 'dark', './resources/style.qss')
        # else:
        #     print('belum dibuat')

class ThemeManager:
    @classmethod
    def load_qss(cls, filename, variables):
        with open(filename, "r") as f:
            qss = f.read()
        # Ganti var(--xxx) dengan warna dari dict
        for key, value in variables.items():
            qss = qss.replace(f"var({key})", value)
        return qss

    @classmethod
    def apply_theme(cls, app_or_widget, theme_name, qss_file):
        if theme_name not in THEMES:
            raise ValueError(f"Theme '{theme_name}' tidak ditemukan")

        colors = THEMES[theme_name]
        qss = cls.load_qss(qss_file, colors)

        # Kalau dikasih QApplication → theme global
        if isinstance(app_or_widget, QApplication):
            app_or_widget.setStyleSheet(qss)
        else:
            app_or_widget.setStyleSheet(qss)
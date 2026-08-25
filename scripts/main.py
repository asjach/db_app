from functools import partial
from ui.ui_main import Ui_MainWindow
# from ui.ui_widgets import Ui_Form
from PySide6.QtCore import QTimer, QEvent, Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QTabBar, QWidget, QMenuBar, QTableWidget
from PySide6.QtGui import QAction
from models.model_main import Model_Main
from scripts.dialogs.detail_siswa import DialogDetailSiswa
from scripts.dialogs.detail_guru import DialogDetailGuru
from scripts.dialogs.input_excel import DialogInputExcel
from scripts.tab_config import TAB_CONFIG
from utils.static_values import *
from utils.fungsi.general_functions import *
from resources.color_var import THEMES
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from utils.whatsapp.whatsapp_sender import WhatsAppSender
from pathlib import Path
import logging


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        register_all_windows_fonts()
        self.setupUi(self)
        self.main_tab.setCornerWidget(self.btn_info, Qt.TopRightCorner)
        self.toggle_theme()
        self.showMaximized()

        # Initialization
        self.initialize_menu()
        self.initialize_variables()
        self.initialize_class()
        self.connect_signals()
        self.initialize_components()


    # ----------------------------------------------------------------------
    # INITIALIZATION
    # ----------------------------------------------------------------------
    def initialize_components(self):
        # Delegate untuk list widget
        self.list_tingkat.setItemDelegate(CenteredDelegate())
        self.list_kelas.setItemDelegate(CenteredDelegate())
        self.list_jenjang.setItemDelegate(CenteredDelegate())

        # ComboBox alignment
        for combo in [self.cbo_tapel, self.cbo_order_by, self.cbo_kolom, self.cbo_search_by]:
            right_combo(combo)

        self.fill_cbo_tapel()

        # Default selection
        self.list_jenjang.setCurrentRow(0)
        self.list_tingkat.setCurrentRow(0)

        # Load tab default
        config = TAB_CONFIG["Daftar Kelas"]
        page = getattr(self, config["show_page"])
        self.add_tab(page, "Daftar Kelas")

    def initialize_variables(self):
        path_json = os.path.join(BASE_DIR, "utils", "static_values.json")
        self.static_values = get_json_data(path_json)
        # self.static_values = get_json_data(os.path.join("E:/APP/DB App", "utils", "static_values.json"))

        # Timer untuk requery
        self.requery_timer = QTimer(self)
        self.requery_timer.setInterval(200)
        self.requery_timer.setSingleShot(True)
        self.requery_timer.timeout.connect(self.requery_page)

        # Model & menu
        self.model_main = Model_Main()
        self.cmenu = QMenu()

        # Actions
        self.detail_siswa_action = QAction("Detail Siswa")
        self.detail_guru_action = QAction("Detail Guru")
        self.tidak_naik_action = QAction("Tidak Naik")
        self.fill_no_urut_siswa_action = QAction("Isi Nomor Absen")

        # Variabel state
        self.str_jenjang = None
        self.str_tapel = None
        self.default_font_size = 10
        self.current_font_size = self.default_font_size
        self._last_search_text = ""
        self.str_search_by = 'Nama'
        self.str_order_by = 'Nama'

        # Tingkat
        self.quoted_daftar_tingkat = None
        self.str_daftar_tingkat = None
        self.list_daftar_tingkat = None
        self.quoted_tingkat = None
        self.str_tingkat = None

        # Kelas
        self.quoted_daftar_kelas = None
        self.data_kelas = None
        self.str_kelas = None
        self.nis_lokal = None
        self.nis_index = None

        #font size
        self.font_size = self.spin_fontsize.value()

    def initialize_class(self):
        for config in TAB_CONFIG.values():
            attr_name = config["show_page"]
            page_class = config["page_class"]
            setattr(self, attr_name, page_class(self))

    def initialize_menu(self):
        self.menu_bar = QMenuBar()


        # --- Santri ---
        self.menu_santri = QMenu("Santri", self)
        self.menu_santri.addActions([
            self.actionDaftar_Kelas,
            self.actionRekap_Santri,
            self.menu_santri.addSeparator(),
            self.actionMutasiMasuk,
            self.actionMutasiKeluar,
            self.menu_santri.addSeparator(),
            self.actionPindah_Kelas,
            self.actionMI_ke_MD,
            self.menu_santri.addSeparator(),
            self.actionKenaikan,
            self.actionKelulusan,
            self.menu_santri.addSeparator(),
            self.actionCari,
            self.actionCeklis_EMIS,
            self.actionBukuInduk,
        ])

        # --- Guru ---
        self.menu_guru = QMenu("Guru", self)
        self.menu_guru.addActions([
            self.actionBukuIndukGuru,
            self.actionRiwayatKeaktifan,
            self.actionRiwayat_Mengajar,
            self.actionAdmGuru,
        ])

        # --- Nilai ---
        self.menu_nilai = QMenu("Nilai", self)
        self.menu_nilai.addActions([
            self.actionRiwayatKegiatan,
            self.actionPesertaKegiatan,
            self.actionMapelKegiatan,
            self.actionEkskulKegiatan,
            self.menu_nilai.addSeparator(),
            self.actionInput_Nilai,
            self.actionPrestasi,
            self.actionInput_Ekstrakurikuler,
            self.menu_nilai.addSeparator(),
            self.actionKartu_Peserta,
            self.actionRekap,
            self.actionRapor,
        ])

        # --- Dokumen ---
        self.menu_dokumen = QMenu("Dokumen", self)
        self.menu_dokumen.addActions([
            self.actionLihat_Dokumen,
            self.actionTambah_Dokumen,
            self.actionCopy_Dokumen,
            self.actionCompare_Dokumen,
            self.actionRename_Dokumen,
            self.actionGanti_Dokumen,
            self.actionHapus_Dokumen,
        ])

        # --- Setting ---
        self.menu_setting = QMenu("Setting", self)
        self.menu_setting.addActions([
            self.actionInput_By_Excel,
            self.actionExport_Excel,
        ])

        # --- Preferensi ---
        self.menu_preferensi = QMenu("Preferensi", self)
        self.menu_preferensi.addActions([
            self.actionRiwayatKelas,
            self.actionAlamat,
            self.actionSekolah,
            self.actionKey_Value,
            self.actionStatic_Values,
        ])

        # --- View ---
        self.menu_view = QMenu("View", self)
        self.menu_view.addActions([self.actionDark_Mode])

        # Add menus to menubar
        self.menu_bar.addMenu(self.menu_santri)
        self.menu_bar.addMenu(self.menu_guru)
        self.menu_bar.addMenu(self.menu_nilai)
        self.menu_bar.addMenu(self.menu_dokumen)
        self.menu_bar.addMenu(self.menu_setting)
        self.menu_bar.addMenu(self.menu_preferensi)
        self.menu_bar.addMenu(self.menu_view)
        self.horizontalLayout_2.addChildWidget(self.menu_bar)

    # ----------------------------------------------------------------------
    # SIGNALS
    # ----------------------------------------------------------------------
    def connect_signals(self):
        self.tabel_tabel()

        # Event filter untuk semua tabel
        for tabel in self.findChildren(QTableWidget):
            tabel.installEventFilter(self)

        # Filter button
        for combo in [self.cbo_tapel, self.cbo_order_by, self.cbo_kolom]:
            fungsi_filter_buttons(combo)

        # ComboBox requery mapping
        combobox_mapping = {
            "delayed_requery": [self.cbo_order_by, self.cbo_kolom],
            "requery_kelas": [self.cbo_tapel]
        }
        for signal, combos in combobox_mapping.items():
            for combo in combos:
                combo.currentIndexChanged.connect(getattr(self, signal))

        # Tab actions
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

        # Dialog actions
        self.actionInput_By_Excel.triggered.connect(lambda: DialogInputExcel(self).exec())
        self.actionExport_Excel.triggered.connect(lambda: DialogExportExcel(self).exec())
        self.actionStatic_Values.triggered.connect(lambda: Dialog_Static_Values(self).exec())
        self.actionCari.triggered.connect(lambda: self.show_detail_siswa(None))

        # List selection
        self.list_jenjang.itemSelectionChanged.connect(self.list_jenjang_selected)
        self.cbo_tapel.currentIndexChanged.connect(self.cbo_tapel_selected)
        self.list_tingkat.itemSelectionChanged.connect(self.list_tingkat_selected)
        self.list_kelas.itemSelectionChanged.connect(self.list_kelas_selected)
        self.cbo_search_by.currentIndexChanged.connect(self.cbo_search_by_selected)
        self.cbo_order_by.currentIndexChanged.connect(self.cbo_order_by_selected)
        self.spin_fontsize.valueChanged.connect(self.requery_kelas)

        # Theme toggle
        self.actionDark_Mode.toggled.connect(self.toggle_theme)

        # Refresh
        self.btn_refresh.clicked.connect(self.requery_page)

    # ----------------------------------------------------------------------
    # TAB MANAGEMENT
    # ----------------------------------------------------------------------
    def add_tab(self, page_class, title):
        existing_tabs = [self.main_tab.tabText(i) for i in range(self.main_tab.count())]
        if title in existing_tabs:
            self.main_tab.setCurrentIndex(existing_tabs.index(title))
            return

        page_instance = page_class(self) if isinstance(page_class, type) else page_class
        index = self.main_tab.addTab(page_instance, title)
        self.main_tab.setCurrentWidget(page_instance)

        if title == "Daftar Kelas":
            self.main_tab.tabBar().setTabButton(index, QTabBar.RightSide, None)

    def close_tab(self, index):
        self.main_tab.removeTab(index)

    def tab_index_changed(self):
        current_index = self.main_tab.currentIndex()
        if current_index == -1:
            return

        tab_name = self.main_tab.tabText(current_index)
        config = TAB_CONFIG.get(tab_name, {})

        # if config.get('right_panel') and hasattr(self, config['right_panel']):
        #     self.main_tab.setCornerWidget()

        # Reset combo box
        for combo in [self.cbo_kolom, self.cbo_order_by, self.cbo_search_by]:
            combo.blockSignals(True)
            combo.clear()

        frames = {
            "jenjang": self.list_jenjang,
            "tapel": self.cbo_tapel,
            "tingkat": self.list_tingkat,
            "kelas": self.list_kelas,
            "order_by": self.cbo_order_by,
            "search_by": self.frame_search,
            "kolom": self.cbo_kolom,
        }

        default_visible_frames = {"jenjang", "tapel", "tingkat", "kelas"}

        # Set visibility
        for key, frame in frames.items():
            is_default_visible = key in default_visible_frames
            is_visible = is_default_visible or config.get(key, False)
            frame.setEnabled(bool(is_visible))

            if is_visible and key not in default_visible_frames:
                combo_box = getattr(self, f"cbo_{key}")
                combo_box.addItems(config.get(key, []))

        # Hide frames
        for frame_name in config.get("hidden_frame", set()):
            frame = frames.get(frame_name.lower())
            if frame:
                frame.setEnabled(False)

        for combo in [self.cbo_kolom, self.cbo_order_by, self.cbo_search_by]:
            combo.blockSignals(False)

        self.delayed_requery()

    # ----------------------------------------------------------------------
    # QUERY & FILTER
    # ----------------------------------------------------------------------
    def requery_page(self):
        tab_name = self.main_tab.tabText(self.main_tab.currentIndex())
        config = TAB_CONFIG.get(tab_name)
        if config and hasattr(self, config["show_page"]):
            getattr(self, config["show_page"]).show_page()

    def fill_cbo_tapel(self):
        list_tapel = self.model_main.get_list_tapel()
        populate_combobox(self.cbo_tapel, list_tapel)

    def list_jenjang_selected(self):
        item = self.list_jenjang.currentItem()
        if item is None:
            return
        self.str_jenjang = item.text().strip()
        self.requery_kelas()

    def cbo_tapel_selected(self):
        self.str_tapel = self.cbo_tapel.currentText()
        self.str_next_tapel = tapel_berikutnya(self.str_tapel)
        self.str_prev_tapel = tapel_sebelumnya(self.str_tapel)
        self.requery_kelas()

    def list_tingkat_selected(self):
        self.quoted_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat, 'quoted')
        self.str_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat, 'not_quoted')
        self.list_daftar_tingkat = get_selected_list_widget_items(self.list_tingkat)
        self.quoted_tingkat = get_selected_list_widget_item(self.list_tingkat, 'quoted')
        self.str_tingkat = get_selected_list_widget_item(self.list_tingkat, 'not_quoted')
        self.requery_kelas()


    def requery_kelas(self):
        self.list_kelas.clear()
        data_kelas = self.model_main.get_kelas(
            jenjang=self.str_jenjang,
            tapel=self.cbo_tapel.currentText(),
            tingkat=self.quoted_daftar_tingkat
        )
        populate_list_widget(self.list_kelas, data_kelas, False, False, 'kelas', 'id')
        self.delayed_requery()

    def list_kelas_selected(self):
        item = self.list_kelas.currentItem()
        if item is None:
            return
        self.quoted_daftar_kelas = get_selected_list_widget_items(self.list_kelas, 'quoted')
        self.str_kelas = item.text()
        self.data_kelas = get_selected_list_widget_data(self.list_kelas)
        self.delayed_requery()

    def cbo_search_by_selected(self):
        self.str_search_by = self.cbo_search_by.currentText()
        self.delayed_requery()

    def cbo_order_by_selected(self):
        self.str_order_by = self.cbo_order_by.currentText()
        self.delayed_requery()


    # ----------------------------------------------------------------------
    # DELAYED ACTIONS
    # ----------------------------------------------------------------------
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

    # ----------------------------------------------------------------------
    # DETAIL DIALOGS
    # ----------------------------------------------------------------------
    def show_detail_siswa(self, tabel):
        self.EDIT_BIODATA = DialogDetailSiswa(self)
        ThemeManager.apply_theme(
            self.EDIT_BIODATA,
            'dark',
            str(Path(__file__).resolve().parent.parent / 'resources' / 'style.qss')
        )
        self.EDIT_BIODATA.show_dialog(
            tabel=tabel,
            nis_lokal=self.nis_lokal,
            nis_index=self.nis_index
        )
        self.EDIT_BIODATA.showMaximized()

    def show_detail_guru(self):
        self.DETAIL_GURU = DialogDetailGuru(self)
        self.DETAIL_GURU.show_dialog(self.id_guru)
        self.DETAIL_GURU.showMaximized()

    # ----------------------------------------------------------------------
    # EVENT FILTER
    # ----------------------------------------------------------------------
    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu:
            self.handle_context_menu(source)
            action = self.cmenu.exec(source.mapToGlobal(event.pos()))
            if action == self.detail_siswa_action:
                self.show_detail_siswa(source)
            elif action == self.detail_guru_action:
                self.show_detail_guru()
            elif action == self.tidak_naik_action:
                self.NAIK.tidak_naikkan_siswa()
            elif action == self.fill_no_urut_siswa_action:
                self.DK.fill_no_urut()

        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                copyCells(source)
                return True
            elif event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
                pasteCells(source)
                return True
        return super().eventFilter(source, event)

    def handle_context_menu(self, source):
        self.cmenu.clear()
        if source in self.tabel_siswa:
            self.cmenu.addAction(self.detail_siswa_action)
            if source.objectName() == 'tbl_list_siswa_kenaikan':
                self.cmenu.addAction(self.tidak_naik_action)
            if source.objectName() == 'tbl_widget':
                self.cmenu.addAction(self.fill_no_urut_siswa_action)
        elif source in self.tabel_guru:
            self.cmenu.addAction(self.detail_guru_action)

    # ----------------------------------------------------------------------
    # TABLE COLLECTION
    # ----------------------------------------------------------------------
    def tabel_tabel(self):
        sub_class_siswa = [
            self.BUKU_INDUK_SISWA, self.CEKLIS_EMIS, self.DK, self.NAIK, self.LULUS,
            self.MUTASI_KELUAR, self.PINDAH_KELAS, self.MI2MD, self.REKAP_SISWA
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

    # ----------------------------------------------------------------------
    # STYLING
    # ----------------------------------------------------------------------
    def apply_style(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        STYLE_PATH = os.path.join(BASE_DIR, '..', 'resources', 'style.qss')
        with open(STYLE_PATH, 'r') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)

    def toggle_theme(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        ThemeManager.apply_theme(
            self,
            'dark',
            str(BASE_DIR / 'resources' / 'style.qss')
        )
        # ThemeManager.apply_theme(self, 'dark', './resources/style.qss')


# ----------------------------------------------------------------------
# THEME MANAGER
# ----------------------------------------------------------------------
class ThemeManager:
    @classmethod
    def load_qss(cls, filename, variables):
        with open(filename, "r") as f:
            qss = f.read()
        for key, value in variables.items():
            qss = qss.replace(f"var({key})", value)
        return qss

    @classmethod
    def apply_theme(cls, app_or_widget, theme_name, qss_file):
        if theme_name not in THEMES:
            raise ValueError(f"Theme '{theme_name}' tidak ditemukan")

        colors = THEMES[theme_name]
        qss = cls.load_qss(qss_file, colors)
        app_or_widget.setStyleSheet(qss)

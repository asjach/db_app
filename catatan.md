python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate.ps1

pip install mysql-connector-python PySide6 openpyxl python-dateutil python-dotenv reportlab pypdf2 pandas PyMuPdf


## convert ui to py

pyside6-uic -o ui/ui_main.py ui/sources/main.ui
pyside6-uic -o ui/ui_page_with_table_widget.py ui/sources/page_with_table_widget.ui


## PAGE
### SISWA
pyside6-uic -o ui/ui_page_daftar_kelas.py ui/sources/page_daftar_kelas.ui
pyside6-uic -o ui/ui_page_rekap_siswa.py ui/sources/page_rekap_siswa.ui
pyside6-uic -o ui/ui_page_pindah_kelas.py ui/sources/page_pindah_kelas.ui
pyside6-uic -o ui/ui_page_mutasi_masuk.py ui/sources/page_mutasi_masuk.ui
pyside6-uic -o ui/ui_page_mutasi_keluar.py ui/sources/page_mutasi_keluar.ui
pyside6-uic -o ui/ui_page_kenaikan.py ui/sources/page_kenaikan.ui
pyside6-uic -o ui/ui_page_kelulusan.py ui/sources/page_kelulusan.ui
pyside6-uic -o ui/ui_page_mi_ke_md.py ui/sources/page_mi_ke_md.ui

### GURU
pyside6-uic -o ui/ui_page_buku_induk_guru.py ui/sources/page_buku_induk_guru.ui
pyside6-uic -o ui/ui_page_riwayat_keaktifan_guru.py ui/sources/page_riwayat_keaktifan_guru.ui
pyside6-uic -o ui/ui_page_riwayat_mengajar.py ui/sources/page_riwayat_mengajar.ui

### DOKUMEN
pyside6-uic -o ui/ui_page_dokumen.py ui/sources/page_dokumen.ui

### NILAI
pyside6-uic -o ui/ui_page_peserta.py ui/sources/page_peserta.ui
pyside6-uic -o ui/ui_page_legger.py ui/sources/page_legger.ui
pyside6-uic -o ui/ui_page_input_nilai.py ui/sources/page_input_nilai.ui
pyside6-uic -o ui/ui_page_rekap_nilai.py ui/sources/page_rekap_nilai.ui

## PREF
pyside6-uic -o ui/ui_page_pref_riwayat_kelas.py ui/sources/page_pref_riwayat_kelas.ui
pyside6-uic -o ui/ui_page_pref_alamat.py ui/sources/page_pref_alamat.ui

## DIALOG
pyside6-uic -o ui/ui_dialog_detail_siswa.py ui/sources/dialog_detail_siswa.ui
pyside6-uic -o ui/ui_dialog_detail_guru.py ui/sources/dialog_detail_guru.ui
pyside6-uic -o ui/ui_dialog_input_excel.py ui/sources/dialog_input_excel.ui
pyside6-uic -o ui/ui_dialog_input_preferensi.py ui/sources/dialog_input_preferensi.ui

## WIDGET
pyside6-uic -o ui/ui_widget_image_viewer.py ui/sources/widget_image_viewer.ui
pyside6-uic -o ui/ui_widget_dokumen_viewer.py ui/sources/widget_dokumen_viewer.ui

# convert resources
pyside6-rcc -o resources_rc.py resources.qrc


        self._dynamic_attributs()
        self._signals_slots()


    def _dynamic_attributs(self):
        self.txt_jenjang = self.parent.cbo_jenjang.currentText()
        self.txt_tapel = self.parent.cbo_tapel.currentText()
        self.txt_tingkat = self.parent.cbo_tingkat.currentText()
        self.txt_kelas = self.parent.cbo_kelas.currentText()
        self.txt_search_by = self.parent.cbo_search_by.currentText()
        self.txt_search = self.parent.line_search.text()
        self.txt_order = self.parent.cbo_order_by.currentText()
        self.txt_kolom = self.parent.cbo_kolom.currentText()

    def _signals_slots(self):
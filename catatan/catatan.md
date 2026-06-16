python -m venv venv
python -m venv lvenv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
yay
windows: `venv\Scripts\activate.ps1`
linux di fish: `source lvenv/bin/activate.fish` atau `. lvenv/bin/activate.fish`

pip install pandas mysql-connector-python PySide6 openpyxl Send2Trash dotenv reportlab PyPDF2 PyMuPDF

pip freeze > requirements.txt
pip install -r requirements.txt

## convert ui to py

pyside6-uic -o ui/ui_main.py ui/sources/main.ui
pyside6-uic -o ui/ui_widgets.py ui/sources/widgets.ui
pyside6-uic -o ui/ui_main_2.py ui/sources/main_2.ui
pyside6-uic -o ui/ui_page_with_table_widget.py ui/sources/page_with_table_widget.ui


## PAGE
### SISWA
pyside6-uic -o ui/ui_page_buku_induk.py ui/sources/page_buku_induk.ui
pyside6-uic -o ui/ui_page_daftar_kelas.py ui/sources/page_daftar_kelas.ui
pyside6-uic -o ui/ui_page_rekap_siswa.py ui/sources/page_rekap_siswa.ui
pyside6-uic -o ui/ui_page_pindah_kelas.py ui/sources/page_pindah_kelas.ui
pyside6-uic -o ui/ui_page_mutasi_masuk.py ui/sources/page_mutasi_masuk.ui
pyside6-uic -o ui/ui_page_mutasi_keluar.py ui/sources/page_mutasi_keluar.uij
pyside6-uic -o ui/ui_page_kenaikan.py ui/sources/page_kenaikan.ui
pyside6-uic -o ui/ui_page_kelulusan.py ui/sources/page_kelulusan.ui
pyside6-uic -o ui/ui_page_mi_ke_md.py ui/sources/page_mi_ke_md.ui
pyside6-uic -o ui/ui_page_ceklis_emis.py ui/sources/page_ceklis_emis.ui

### GURU
pyside6-uic -o ui/ui_page_buku_induk_guru.py ui/sources/page_buku_induk_guru.ui
pyside6-uic -o ui/ui_page_riwayat_keaktifan_guru.py ui/sources/page_riwayat_keaktifan_guru.ui
pyside6-uic -o ui/ui_page_riwayat_mengajar.py ui/sources/page_riwayat_mengajar.ui
pyside6-uic -o ui/ui_page_adm_guru.py ui/sources/page_adm_guru.ui

### DOKUMEN
pyside6-uic -o ui/ui_page_dokumen.py ui/sources/page_dokumen.ui
pyside6-uic -o ui/ui_page_lihat_dokumen.py ui/sources/page_lihat_dokumen.ui
pyside6-uic -o ui/ui_page_tambah_dokumen.py ui/sources/page_tambah_dokumen.ui
pyside6-uic -o ui/ui_page_compare_dokumen.py ui/sources/page_compare_dokumen.ui
pyside6-uic -o ui/ui_page_copy_dokumen.py ui/sources/page_copy_dokumen.ui
pyside6-uic -o ui/ui_page_rename_dokumen.py ui/sources/page_rename_dokumen.ui

### NILAI
pyside6-uic -o ui/ui_page_peserta.py ui/sources/page_peserta.ui
pyside6-uic -o ui/ui_page_mapel_kegiatan.py ui/sources/page_mapel_kegiatan.ui
pyside6-uic -o ui/ui_page_input_nilai.py ui/sources/page_input_nilai.ui
pyside6-uic -o ui/ui_page_kartu_peserta.py ui/sources/page_kartu_peserta.ui
pyside6-uic -o ui/ui_page_rekap_nilai.py ui/sources/page_rekap_nilai.ui
pyside6-uic -o ui/ui_page_cetak_rapor.py ui/sources/page_cetak_rapor.ui
pyside6-uic -o ui/ui_page_ekskul_kegiatan.py ui/sources/page_ekskul_kegiatan.ui
pyside6-uic -o ui/ui_page_prestasi.py ui/sources/page_prestasi.ui

### PEMBAYARAN
pyside6-uic -o ui/ui_page_transaksi_pembayaran.py ui/sources/page_transaksi_pembayaran.ui
pyside6-uic -o ui/ui_page_riwayat_biaya.py ui/sources/page_riwayat_biaya.ui

### PREF
pyside6-uic -o ui/ui_page_pref_riwayat_kelas.py ui/sources/page_pref_riwayat_kelas.ui
pyside6-uic -o ui/ui_page_pref_alamat.py ui/sources/page_pref_alamat.ui
pyside6-uic -o ui/ui_page_biaya.py ui/sources/page_biaya.ui

### DIALOG
pyside6-uic -o ui/ui_dialog_detail_siswa.py ui/sources/dialog_detail_siswa.ui
pyside6-uic -o ui/ui_dialog_detail_guru.py ui/sources/dialog_detail_guru.ui
pyside6-uic -o ui/ui_dialog_input_excel.py ui/sources/dialog_input_excel.ui
pyside6-uic -o ui/ui_dialog_input_preferensi.py ui/sources/dialog_input_preferensi.ui
pyside6-uic -o ui/ui_dialog_export_excel.py ui/sources/dialog_export_excel.ui
pyside6-uic -o ui/ui_dialog_static_values.py ui/sources/dialog_static_values.ui


### WIDGET
pyside6-uic -o ui/ui_widget_image_viewer.py ui/sources/widget_image_viewer.ui
pyside6-uic -o ui/ui_widget_dokumen_viewer.py ui/sources/widget_dokumen_viewer.ui

# convert resources
pyside6-rcc -o resources_rc.py resources.qrc

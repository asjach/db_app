from PySide6.QtWidgets import QWidget, QMainWindow
from utils.fungsi.general_functions import *
from ui.ui_page_pengaturan_kegiatan import Ui_Form
from models.nilai.pengaturan import Pengaturan


class PagePengaturanKegiatan(QWidget, Ui_Form):
    def __init__(self, parent:QMainWindow):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.SQL = Pengaturan()
        self.id = None
        self.jenjang=None
        self.tingkat=None
        self.kegiatan=None
        self.tapel=None
        self.kegiatan_tbl.itemSelectionChanged.connect(self.tbl_kegiatan_selected)
        self.kegiatan_tbl.itemChanged.connect(self.update_kegiatan)
        self.kelas_tbl.itemSelectionChanged.connect(self.kelas_tbl_selected)
        self.kelas_tbl.itemChanged.connect(self.update_kelas)
        self.peserta_tbl.itemSelectionChanged.connect(self.tbl_peserta_selected)
        self.peserta_tbl.itemChanged.connect(self.update_peserta)
        self.mapel_tbl.itemSelectionChanged.connect(self.tabel_mapel_selected)
        self.mapel_tbl.itemChanged.connect(self.update_mapel)
        self.ekskul_tbl.itemSelectionChanged.connect(self.tabel_ekskul_selected)
        self.ekskul_tbl.itemChanged.connect(self.update_ekskul)

        self.guru_cbo.currentIndexChanged.connect(self.guru_cbo_selected)
        self.wali_kelas_cbo.currentIndexChanged.connect(self.wali_kelas_cbo_selected)
        self.pembimbing_cbo.currentIndexChanged.connect(self.pembimbing_cbo_selected)
        self.generate_peserta_btn.clicked.connect(self.generate_peserta)
        self.clear_peserta_btn.clicked.connect(self.clear_peserta_btn_clicked)
        self.clear_mapel_btn.clicked.connect(self.clear_mapel_btn_clicked)
        self.clear_ekskul_btn.clicked.connect(self.clear_ekskul_btn_clicked)
        self.tujuan_cbo.currentIndexChanged.connect(self.fill_preview_tbl)
        self.kegiatan_cbo.currentIndexChanged.connect(self.fill_preview_tbl)
        self.execute_insert_btn.clicked.connect(self.execute_insert_btn_clicked)
        self.kegiatan_cbo.setCurrentIndex(-1)

    def show_page(self):
        print("PENGATURAN KEGIATAN")
        self.fill_riwayat_kegiatan()

    # TABEL RIWAYAT KEGIATAN
    def fill_riwayat_kegiatan(self):
        data = self.SQL.get_kegiatan_riwayat(self.parent.cbo_tapel.currentText())
        fill_table_with_input(
            data=data,
            table=self.kegiatan_tbl,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_kegiatan_riwayat,
            hidden_column=[]
        )

    def tbl_kegiatan_selected(self):
        self.id_kelas_line.clear()
        table_selected(self.kegiatan_tbl, self, self.parent)
        self.id_kegiatan_line.setText(self.id)
        self.fill_kelas_riwayat()
        self.fill_peserta_tbl()
        self.fill_preview_tbl()
        
    def update_kegiatan(self):
        sukses=handle_item_changed(
            tabel_ui=self.kegiatan_tbl,
            tabel_sql='kegiatan_riwayat',
            primary_key="id",
            must_insert=['jenjang', 'tapel', 'semester', 'kegiatan'],
            not_updatable_column=['id'])
        if sukses:self.fill_riwayat_kegiatan()
    
    def delete_kegiatan_riwayat(self):
        sukses = delete_by_id('kegiatan_riwayat', 'id', self.id)
        if sukses:self.show_page()

    # TABEL KELAS
    def fill_kelas_riwayat(self):
        data = self.SQL.get_kelas_riwayat_with_peserta(self.jenjang, self.tapel, self.id_kegiatan_line.text())
        fill_table_with_input(data, self.kelas_tbl, zero=0)

    def kelas_tbl_selected(self):
        table_selected(self.kelas_tbl,self, self.parent, ['id'])
        self.id_kelas_line.setText(self.id)
        self.fill_peserta_tbl()
        self.fill_tabel_mapel()  
        self.fill_tabel_ekskul()
        self.fill_guru_walikelas_pembimbing_cbo()
    
    def update_kelas(self):
        sukses = handle_item_changed(
            tabel_ui=self.kelas_tbl,
            tabel_sql='kelas_riwayat',
            primary_key='id',
            must_insert=['jenjang', 'tapel', 'semester', 'tingkat', 'kelas'],
            not_updatable_column=['id']
        )
        if sukses:
            self.fill_kelas_riwayat()
    
    def fill_guru_walikelas_pembimbing_cbo(self):
        self.guru_cbo.blockSignals(True)
        self.wali_kelas_cbo.blockSignals(True)
        self.pembimbing_cbo.blockSignals(True)
        self.guru_cbo.clear()
        self.wali_kelas_cbo.clear()
        print(self.id_kelas_line.text())
        data_guru = self.SQL.get_guru_aktif(self.jenjang, self.tapel, self.id_kelas_line.text())
        for guru in data_guru:
            nama_guru = guru['nama_lengkap']
            id_guru = guru['id_guru']
            self.guru_cbo.addItem(nama_guru, userData=id_guru)
            self.wali_kelas_cbo.addItem(nama_guru, userData=id_guru)
            self.pembimbing_cbo.addItem(nama_guru, userData=id_guru)
        self.guru_cbo.blockSignals(False)
        self.wali_kelas_cbo.blockSignals(False)
        self.pembimbing_cbo.blockSignals(False)

    def wali_kelas_cbo_selected(self):
        id_kelas = self.id_kelas_line.text()
        id_walas = self.wali_kelas_cbo.currentData()
        if id_kelas != '':
            sukses = update_from_controls(
                tabel_sql='kelas_riwayat', 
                key_column='id', 
                key_value=id_kelas, 
                **{"id_walas": id_walas}
                )
            if sukses:
                self.fill_kelas_riwayat()
                self.id_kelas_line.clear()
                self.wali_kelas_cbo.setCurrentIndex(-1)

    #TABEL PESERTA
    def fill_peserta_tbl(self): 
        data = self.SQL.get_peserta_kegiatan(
            id_kegiatan=self.id_kegiatan_line.text(),
            id_kelas = self.id_kelas_line.text(),
        )
        fill_table_with_input(
            data=data,
            table=self.peserta_tbl,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_peserta,
            hidden_column=[]
        )

    def tbl_peserta_selected(self):
        table_selected(self.peserta_tbl, self, self.parent, ['id'])

    def generate_peserta(self):
        sukses = False
        list_kelas = self.SQL.get_kelas_riwayat(self.jenjang, self.tapel)
        for kelas in list_kelas:
            jenjang = kelas['jenjang']
            tapel = kelas['tapel']
            tingkat = kelas['tingkat']
            id_kelas = kelas['id']
            kls = kelas['kelas']
            id_kegiatan = self.id_kegiatan_line.text()
            kegiatan = self.kegiatan
            if kegiatan in ['PAS', 'AS Ganjil']:
                sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            elif kegiatan in ['PAT', 'AS Genap']:
                if tingkat not in ['6', '9', '12']:
                    sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            elif kegiatan in ['UAP', 'RTR', 'NA', 'US', 'AM']:
                if tingkat in ['6', '9', '12']:
                    sukses = self.SQL.generate_peserta(jenjang, tapel, id_kelas, kls, id_kegiatan)
            else: return
        if sukses:
            pesan_sukses("Berhasil", "Peserta Kegiatan berhasil digenerate!")
            self.fill_peserta_tbl()
            self.fill_kelas_riwayat()

    def update_peserta(self): 
        sukses = handle_item_changed(
            tabel_ui=self.peserta_tbl,
            tabel_sql='kegiatan_peserta',
            primary_key='id',
            must_insert=['id_kelas', 'id_kegiatan', 'nis_lokal'],
            not_updatable_column=['id'])
        if sukses:self.fill_peserta_tbl()      

    def delete_peserta(self):
        sukses = delete_by_id('kegiatan_peserta', 'id', self.id_mapel_line.text())
        if sukses: self.fill_peserta_tbl()

    def clear_peserta_btn_clicked(self):
        konfirimasi = pesan_konfirmasi("Hapus Seluruh Peserta", "Anda akan menghapus seluruh Peserta kegiatan")
        if konfirimasi:
            sukses  = self.SQL.clear_peserta(self.id_kegiatan_line.text())
            if sukses:
                self.fill_kelas_riwayat()
                self.fill_peserta_tbl()

    #MAPEL
    def fill_tabel_mapel(self):
        data = self.SQL.get_mapel(
            id_kelas=self.id_kelas_line.text(),
            id_kegiatan=self.id_kegiatan_line.text())
        fill_table_with_input(
            data=data,
            table=self.mapel_tbl,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_mapel,
            hidden_column=[0])

    def tabel_mapel_selected(self):
        table_selected(self.mapel_tbl, self, self.parent,['id'])
        self.id_mapel_line.setText(self.id)
    
    def update_mapel(self):
        sukses = handle_item_changed(
            tabel_ui=self.mapel_tbl,
            tabel_sql='mapel_riwayat',
            primary_key='id',
            must_insert=['id_kelas', 'id_kegiatan', 'mapel'],
            not_updatable_column=['id'])
        if sukses: self.fill_tabel_mapel()

    def delete_mapel(self):
        sukses = delete_by_id('mapel_riwayat', 'id', self.id)
        if sukses: self.fill_tabel_mapel()
    
    def guru_cbo_selected(self):
        id_mapel = self.id_mapel_line.text()
        id_guru = self.guru_cbo.currentData()
        updated = {"id_guru": id_guru}
        if id_mapel != '':
            sukses = update_from_controls(
                tabel_sql='mapel_riwayat', 
                key_column='id', 
                key_value=id_mapel, 
                **updated
                )
            if sukses:
                self.fill_tabel_mapel()
                self.id_mapel_line.clear()
                self.guru_cbo.setCurrentIndex(-1)

    def clear_mapel_btn_clicked(self):
        konfirimasi = pesan_konfirmasi("Hapus Seluruh Mapel", "Anda akan menghapus seluruh mapel kegiatan")
        if konfirimasi:
            sukses  = self.SQL.clear_mapel(self.id_kegiatan_line.text())
            if sukses:
                self.fill_tabel_mapel()

    # EKSKUL
    def fill_tabel_ekskul(self):
        data = self.SQL.get_ekskul(
            id_kelas=self.id_kelas_line.text(),
            id_kegiatan=self.id_kegiatan_line.text())
        fill_table_with_input(
            data=data,
            table=self.ekskul_tbl,
            icon_akhir=":/icon/resources/icon/multiply.svg",
            fungsi_akhir=self.delete_ekskul,
            hidden_column=[0])
            
    def tabel_ekskul_selected(self):
        table_selected(self.ekskul_tbl, self, self.parent,['id'])
        self.id_ekskul_line.setText(self.id)
    
    def update_ekskul(self):
        sukses = handle_item_changed(
            tabel_ui=self.ekskul_tbl,
            tabel_sql='ekskul_riwayat',
            primary_key='id',
            must_insert=['id_kelas', 'id_kegiatan', 'ekskul'],
            not_updatable_column=['id'])
        if sukses: self.fill_tabel_ekskul()
            
    def delete_ekskul(self):
        sukses = delete_by_id('ekskul_riwayat', 'id', self.id)
        if sukses: self.fill_tabel_ekskul()

    def pembimbing_cbo_selected(self):
        id_ekskul = self.id_ekskul_line.text()
        id_pembimbing = self.pembimbing_cbo.currentData()
        updated = {"id_pembimbing": id_pembimbing}
        if id_ekskul != '':
            sukses = update_from_controls(
                tabel_sql='ekskul_riwayat', 
                key_column='id', 
                key_value=id_ekskul, 
                **updated)
            if sukses:
                self.fill_tabel_ekskul()
                self.id_ekskul_line.clear()
                self.pembimbing_cbo.setCurrentIndex(-1)

    def clear_ekskul_btn_clicked(self):
        konfirimasi = pesan_konfirmasi("Hapus Seluruh Ekstrakurikuler", "Anda akan menghapus seluruh ekskul kegiatan")
        if konfirimasi:
            sukses  = self.SQL.clear_ekskul(self.id_kegiatan_line.text())
            if sukses:
                self.fill_tabel_ekskul()

    # GABUNGAN MAPEL DAN EKSKUL
    def fill_preview_tbl(self):
        tujuan = self.tujuan_cbo.currentText().lower()
        if tujuan == 'mapel':
            data = self.SQL.get_mapel_list(self.jenjang, self.tapel, self.kegiatan_cbo.currentText())
        elif tujuan == 'ekskul':
            data = []
        generate_table(data, self.preview_tbl)

    def execute_insert_btn_clicked(self):
        opsi_tujuan = self.tujuan_cbo.currentText().lower()
        opsi_insert = self.opsi_insert_cbo.currentText().lower()
        list_input = [input.strip() for input in self.input_line.text().split(",") if input.strip()]
        id_kelas = self.id_kelas_line.text()
        id_kegiatan = self.id_kegiatan_line.text()
        if opsi_insert == 'list':
            if not id_kelas or not id_kegiatan or not list_input: 
                print("Input tidak lengkap!")
            else:
                for input in list_input:
                    if opsi_tujuan == 'mapel':
                        result = self.SQL.insert_by_list_mapel(id_kelas, id_kegiatan, input)
                        if result == "EXISTS": 
                            print(f"{input} sudah ada, dilewati.")
                        elif not result: 
                            print(f"Gagal memasukkan {input}")
                        self.fill_tabel_mapel()
                    elif opsi_tujuan == 'ekskul':
                        result = self.SQL.insert_by_list_ekskul(id_kelas, id_kegiatan, input)
                        if result == "EXISTS": 
                            print(f"{input} sudah ada, dilewati.")
                        elif not result: 
                            print(f"Gagal memasukkan {input}")
                        self.fill_tabel_ekskul()
        elif opsi_insert == 'kegiatan':
            if opsi_tujuan == 'mapel':
                id_kegiatan = self.id_kegiatan_line.text()
                jenjang = self.jenjang
                tapel = self.tapel
                if not id_kegiatan or not jenjang or not tapel: 
                    print("Input tidak lengkap!")
                else:
                    if opsi_tujuan == 'mapel':
                        result = self.SQL.insert_by_kegiatan_mapel(jenjang, tapel, id_kegiatan)
                        if not result: 
                            print(f"Gagal memasukkan data dari kegiatan dengan ID {id_kegiatan}")
                        self.fill_tabel_mapel()  # Hanya untuk mapel
                    elif opsi_tujuan == 'ekskul':
                        result = self.SQL.insert_by_kegiatan_ekskul(jenjang, tapel, id_kegiatan)
                        if not result: 
                            print(f"Gagal memasukkan data dari kegiatan dengan ID {id_kegiatan}")
                        self.fill_tabel_ekskul()
        self.input_line.clear()

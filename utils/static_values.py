AGAMA = ('', 'Islam', 'Katolik', 'Protestan', 'Hindu', 'Budha', 'Konghuchu')
ALASAN_MUTASI = ('', 'Pindah Sekolah', 'Menikah', 'Mengundurkan Diri', 'Drop Out', 'Meninggal', 'Tanpa Keterangan')
BENTUK_BUKU = ('', 'Cetak', 'Ebook', 'Audio Book')
BENTUK_PERATURAN = ('', 'UUD', 'UU', 'PP Pengganti UU', 'Perpres', 'Permen', 'Pergub', 'Perda', 'Perbup')
BIAYA = ('', 'Orangtua', 'Wali/Orang Tua Asuh', 'Tanggungan Sendiri', 'Lainnya')
CITA_CITA = ('', 'Lainnya', 'PNS', 'TNI/Polri', 'Dokter', 'Politikus', 'Wiraswasta', 
             'Seniman/Artis', 'Ilmuwan', 'Agamawan', 'Arsitek', 'Guru')
FUNGSI_GURU = ('', 'Guru', 'Tenaga Kependidikan', 'Calon Guru')
GOLONGAN_DARAH = ('', 'A', 'B', 'AB', 'O')
HOBI = ('', 'Lainnya', 'Olahraga', 'Kesenian', 'Membaca', 'Menulis', 
        'Jalan-jalan', 'Bernyanyi', 'Menggambar', 'Berenang', 'Koleksi', 'Memasak')
JARAK = ('', '<5 km', '5-10 km', '11-20 km', '21-30 km', '> 30 km')
JENIS_BUKU = ('', 'Pelajaran', 'Bacaan Umum', 'Referensi', 'Lain-lain')
JENIS_DOKUMEN = ('', 
                 'Formulir', 
                 'Formulir Pendaftaran',
                 'Kartu Keluarga', 
                 'Akta', 
                 'KTP', 
                 'Ijazah', 
                 'Nilai Ijazah', 
                 'Foto', 
                 'Surat', 
                 'Buku Rekening',
                 'NPWP', 
                 'Kartu KIP',
                 'Tanda Tangan',
                 'Tanda Tangan Rapor',
                )

TEMPLATE_KETERANGAN = {
                    "Formulir": ('', 'Pendaftaran'),
                    "Kartu Keluarga": ('',),
                    "Akta": ('', 'Kelahiran', 'Pendirian', 'Notaris'),
                    "KTP":('', 'Pribadi', 'Orang Tua', 'Ayah', 'Ibu'),
                    "Ijazah": ('', 'RA', 'TK', 'SD', 'MI', 'MTs', 'SMP', 'MLN', 'MA', 'SMA', 'D1', 'D2', 'D3', 'D4', 'S1', 'S2', 'S3'),
                    "Nilai Ijazah": ('', 'JENJANG', 'Rapor'),
                    "Foto": ('', 'Pas', 'Bersama', 'KEGIATAN'),
                    "Surat": ('', 'SK', 'SKet', 'Instruksi', 'Pemberitahuan', 'Perjanjian')
                    }
JENIS_KELAMIN = ('', 'Laki-laki', 'Perempuan')
JENIS_SEKOLAH = ('', 'RA', 'TK', 'PAUD', 'Orangtua', 'MI', 'SD', 'SLB')
JENIS_SK_GURU = ('', 'SK CPNS', 'SK Kenaikan Pangkat PNS (Reguler)', 'SK Kenaikan Pangkat PNS (Pilihan)', 'SK Non-PNS', 'SK Yayasan', 'SK PPPK', 'SK Pensiun', 'SK PTK')
JENIS_TUGAS_GURU = ('Guru Kelas', 'Guru Mapel', 'Guru BK', 'Guru Inklusi')
JENIS_TUGAS_KEPENDIDIKAN = ('', 'Kepala Perpustakaan', 'Wali Kelas', 'Tata Usaha', 'Pustakawan', 'Laboran', 'Pembimbing Ekstrakurikuler', 'Petugas Kebersihan', 'Penjaga Sekolah', 'Tenaga Keamanan', 'Pengemudi', 'Teknisi', 'Bendahara', 'Kepala Tata Usaha', 'Operator', 'Operator Aplikasi Data', 'Operator Aplikasi Keuangan', 'Operator Aplikasi Lainnya')
JENJANG = ("MI", "MD", '')
JENJANG_SERTIFIKASI = ('', 'SD', 'SMP', 'SMA')
JENJANG_SEKOLAH = ('', 'SD/Sederajat', 'SMP/Sederajat', 'SMA/Sederajat', 'D1', 'D2', 'D3', 'D4/S1', 'S2', 'S3')
JK = ('', 'L', 'P')
KEB_KHUSUS = ('', 'Tidak Ada', 'Lamban Belajar', 'Kesulitan Belajar Spesifik', 'Gangguan Komunikasi', 'Berbakat/Cerdas Luar Biasa', 'Lainnya')
KEG_EVALUATIF_MD = ('', 'PAS', 'PAT', 'UAP')
KEG_EVALUATIF_MI = ('', 'PAS', 'PAT', 'US', 'RTR', 'NA')
MELANJUTKAN_KE = ('', 'MTs', 'SLTP', 'Tidak Melanjutkan')
PEKERJAAN = ('', 'Tidak Bekerja', 'IRT', 'Pensiunan', 'PNS', 'TNI/Polisi', 'Guru/Dosen', 'Pegawai Swasta', 'Wiraswasta', 'Pengacara', 'Seniman', 'Dokter', 'Perawat', 'Pilot', 'Pedagang', 'Petani/Peternak', 'Nelayan', 'Buruh', 'Sopir', 'Politikus', 'Lainnya')
PENDIDIKAN = ('', 'Belum Sekolah', 'Tidak Bersekolah', 'SD', 'SMP', 'SMA', 'D1', 'D2', 'D3', 'S1', 'S2', 'S3')
PENGHASILAN = ('', '< 500.000', '500.001 - 1.000.000', '1.000.001 - 2.000.000', '2.000.001-3.000.000', '3.000.001-5.000.000', '> 5.000.000', 'Tidak Ada')
PILIHAN_JENJANG = ('', 'MI dan MD', 'MI Saja', 'MD Saja')
SEMESTER = ('', 'Ganjil', 'Genap')
STATUS_AKHIR = ('', 'Aktif', 'Naik Kelas', 'Tidak Naik', 'Lulus', 'Keluar')
STATUS_AKTIF = ('', 'Ya', 'Tidak')
STATUS_ANAK = ('', 'Kandung', 'Tiri', 'Angkat')
STATUS_AWAL = ('', 'Siswa Baru', 'Kenaikan', 'Mengulang', 'Pindahan')
STATUS_DITERIMA = ('', 'Diterima', 'Ditolak')
STATUS_KEPEGAWAIAN = ('', 'PNS', 'Non-PNS', 'PPPK')
STATUS_MENIKAH = ('', 'Menikah', 'Belum Menikah', 'Duda', 'Janda')
STATUS_ORTU = ('', 'Masih Hidup', 'Sudah Meninggal', 'Tidak Diketahui')
STATUS_PENUGASAN = ('', 'Guru/Pegawai Tetap', 'Guru/Pegawai Tidak Tetap', 'Guru/Pegawai Diperbantukan', 'Guru/Pegawai Dipekerjakan')
STATUS_SEKOLAH = ('', 'Negeri', 'Swasta')
STATUS_SERTIFIKASI = ('', 'Sudah Mengikuti', 'Belum Mengikuti')
STATUS_TEMPAT_TINGGAL = ('', 'Milik Sendiri', 'Rumah Orang Tua', 'Rumah Saudara', 'Rumah Dinas', 'Kontrak', 'Sewa', 'Lainnya')
STATUS_WALI = ('', 'Sama Dengan Ayah', 'Sama Dengan Ibu', 'Lainnya')
SURAT_JENIS = ('', 'Masuk', 'Keluar')
SURAT_KATEGORI = ('', 'Surat Keputusan', 'Surat Keterangan', 'Surat Pernyataan', 
                  'Surat Permohonan', 'Surat Kuasa', 'Surat Pengantar', 
                  'Surat Perintah', 'Surat Undangan', 'Surat Edaran', 'Surat Instruksi', 'Pemberitahuan')
TINGKAT = ('1', '2', '3', '4', '5', '6', "")
TRANSPORTASI = ('', 'Jalan Kaki', 'Sepeda', 'Antar Jemput Sekolah', 'Sepeda Motor', 'Mobil', "Lainnya")
TUGAS_POKOK = ('', 'Guru', 'Tenaga Kependidikan', 'Calon Guru')
WAKTU_TEMPUH = ('', '1-10 menit', '10-19 menit', '20-30 menit', '30-39 menit', '1-2 jam', '> 2 jam')

LEFT_COLUMN = [
    "nama_lengkap", "nama_singkat", "tgl_lahir", "ayah_nama", "nama_ayah", "ayah",
    "ibu_nama", "nama_ibu", "ibu", "alamat_sekolah_asal", "kepala_keluarga", "jalan",
    "kampung", "alamat", "alamat_full", "nama_sekolah_asal", "value", "key", "orangtua",
    "namafile", "jenis_dok", "alamat_sekolah_tujuan", "alamat_sekolah", "nama_dokumen",
    "wali_kelas", "catatan_walas", "pelajaran", "mata_pelajaran", "nama_sekolah", "nilai", "kunci", 
    "nama_biaya", "deskripsi", "kategori_pembayaran", "sql_insert"
]
DK_ORDER = ('Nama', 'JK', 'Urutan', 'Ayah', 'Ibu', 'Alamat')
DK_SEARCH = ('nama_lengkap', 'ayah_nama', 'ibu_nama', 'alamat', 'status_awal', 'status_akhir')
DK_KOLOM = ('Default', 'Nama', 'Lengkap', 'Ringkasan', 'Biodata', 'Orangtua', 'Detail Ayah', 
            'Detail Ibu', 'Alamat', 'Sekolah Asal', 'Umur', 'Umur (YM)', 'Riwayat', 'Custom')
TABEL_INSERT = ('siswa_psb', 'siswa', 'guru', 'nilai_mi', 'nilai_md', )
KOLOM_ANGKA = ("id", "pai", "qds", "aq", "fkh", "ski", "pkn", "bina", "bar", "mtk", "ipa", "ips", 
               "ipas", "sbk", "pjok", "bsun", "bing", "tik", "plh", "ranking", "tjw", "hfz", "taf", 
               "thd", "akh", "fqh", "ufq", "trh", "qrh", "ktb", "imla", "lgh", "ins", "in_im", "nhw", 
               "srf", "irb", "adb", "hky", "hsb", "doa", "tlw", "qur", "hds", "syr", "bar1", 
               "bar2", "p_qur", "p_ibd", "p_bar")
KOLOM_FLOAT = ('kehadiran', 'harian', 'uts', 'tulis', 'praktek', 'nilai_akhir')
KOLOM_TANGGAL = ('tgl_lahir', 'tgl_daftar', 'tgl_mulai', 'tgl_masuk', 'tgl_ijazah', 
                 'ayah_tgl_lahir', 'ibu_tgl_lahir', 'wali_tgl_lahir', 
                 'tgl_kk', 'tmt_pegawai', 'tmt_guru', 'tgl_lulus_sertifikasi', 'tgl_keluar', 'tgl_lulus', 'tgl_bayar', 'tgl_selesai', 'tgl_transaksi')
KOLOM_CURRENCY = ('nominal', 'nominal_tagihan', 'nominal_bayar')
# KOLOM_KUNCI = {'siswa_psb': 'id', 'siswa': 'nis_lokal', 
 
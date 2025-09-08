DAFTAR_KELAS= {
    "default": """r.nis_lokal, nama_lengkap, nama_singkat, r.no_urut as no, s.nisn, s.nik, 
                    s.jk, r.kelas, s.tmp_lahir, s.tgl_lahir, s.ayah_nama, s.ibu_nama, s.kampung, 
                    r.status_awal, r.status_akhir, r.is_active""",

    "nama": 'r.nis_lokal, nama_lengkap, nama_singkat, kelas',

    "lengkap": 's.*, r.kelas, r.status_awal',

    "ringkasan": '''r.nis_lokal, nama_lengkap, jk, tmp_lahir, tgl_lahir, ayah_nama as ayah, 
                    ibu_nama as ibu, alamat, kel_desa, kecamatan, kabkota, kelas''',

    "biodata": '''  r.nis_lokal, nama_lengkap, nama_singkat, nik, jk, tmp_lahir, tgl_lahir, 
                    j_saudara, anak_ke, cita_cita, hobi, agama, r.is_active''',

    "orang tua": '''r.nis_lokal, nama_lengkap, ayah_nama, ayah_status, ayah_nik, ayah_tmp_lahir, 
                    ayah_tgl_lahir, ayah_pendidikan, ayah_pekerjaan, ayah_penghasilan, ayah_telp, 
                    ibu_nama, ibu_status, ibu_nik, ibu_tmp_lahir, ibu_tgl_lahir, ibu_pendidikan, 
                    ibu_pekerjaan, ibu_penghasilan, ibu_telp, status_wali, wali_nama, wali_nik, 
                    wali_tmp_lahir, wali_tgl_lahir, wali_pendidikan, wali_pekerjaan, wali_telp, 
                    no_kk, kepala_keluarga, tgl_kk''',

    "detail ayah": '''r.nis_lokal, nama_lengkap, ayah_nama, ayah_status, ayah_nik, ayah_tmp_lahir, 
                    ayah_tgl_lahir, ayah_pendidikan, ayah_pekerjaan, ayah_penghasilan, ayah_telp''',

    "detail ibu": '''r.nis_lokal, nama_lengkap, ibu_nama, ibu_status, ibu_nik, ibu_tmp_lahir, 
                    ibu_tgl_lahir, ibu_pendidikan, ibu_pekerjaan, ibu_penghasilan, ibu_telp''',

    "alamat": 'r.nis_lokal, nama_lengkap, nisn, nik, nama_lengkap, jalan, kampung, rt, rw, kel_desa, kecamatan, kabkota, provinsi, kodepos, alamat, alamat_full, transportasi, jarak, waktu_tempuh',
    "pendaftaran": 'r.nis_lokal, nama_lengkap, pilihan_jenjang, s.tgl_masuk, tapel_masuk, kls_masuk, s.no_urut',

    "sekolah asal": 'r.nis_lokal, nama_lengkap, nik, nss_sekolah_asal, npsn_sekolah_asal, nama_sekolah_asal, alamat_sekolah_asal, pilihan_jenjang'
    }

PINDAH_KELAS = {
    'default': 'r.id, r.nis_lokal, nama_lengkap, kelas, jk', 
    'lengkap': 'r.id, r.nis_lokal, nama_lengkap, kelas, jk, kampung, pilihan_jenjang', 
    'ringkas': 'r.id, r.nis_lokal, nama_lengkap', 
    'pilihan jenjang': 'r.id, r.nis_lokal, s.nama_lengkap, kelas, pilihan_jenjang', 
    'alamat': 'r.id, r.nis_lokal, nama_lengkap, kelas, kampung',
}

GURU = {
    'default': 'id, r.id_guru, jenjang, tapel, nama_lengkap, kelas, jk, tmp_lahir, tgl_lahir, nuptk, nik, niat_npa, nuptk, no_telp, r.is_active as status_keaktifan, g.is_active',
    'lengkap': 'id, r.id, g.*',
    'nama saja': 'id, r.id_guru, nama_lengkap, gelar_belakang',
    'kontak': 'id, r.id_guru, nama_lengkap, no_telp, email',
    'masa kerja': '''
        id, r.id_guru, nama_lengkap, g.tmt_pegawai,
        CONCAT(
        FLOOR(DATEDIFF(CURDATE(), g.tmt_pegawai) / 365), ' tahun ',
        FLOOR((DATEDIFF(CURDATE(), g.tmt_pegawai) % 365) / 30), ' bulan') AS masa_kerja
    ''',

}
BUKU_INDUK= {
    "default": """nis_lokal, nama_lengkap, nama_singkat, no_urut as no, nisn, nik, 
                    jk, tmp_lahir, tgl_lahir, ayah_nama, ibu_nama, kampung, 
                    kelas_akhir, pilihan_jenjang, status_keaktifan """,

    "nama": 'nis_lokal, nama_lengkap, nama_singkat, kelas_akhir',

    "lengkap": 's.*, kelas_akhir, status_awal',

    "ringkasan": '''nis_lokal, nama_lengkap, jk, tmp_lahir, tgl_lahir, ayah_nama as ayah, 
                    ibu_nama as ibu, alamat, kel_desa, kecamatan, kabkota, kelas_akhir''',

    "biodata": '''  nis_lokal, nama_lengkap, nama_singkat, nik, jk, tmp_lahir, tgl_lahir, 
                    j_saudara, anak_ke, cita_cita, hobi, agama, status_keaktifan''',

    "orang tua": '''nis_lokal, nama_lengkap, ayah_nama, ayah_status, ayah_nik, ayah_tmp_lahir, 
                    ayah_tgl_lahir, ayah_pendidikan, ayah_pekerjaan, ayah_penghasilan, ayah_telp, 
                    ibu_nama, ibu_status, ibu_nik, ibu_tmp_lahir, ibu_tgl_lahir, ibu_pendidikan, 
                    ibu_pekerjaan, ibu_penghasilan, ibu_telp, status_wali, wali_nama, wali_nik, 
                    wali_tmp_lahir, wali_tgl_lahir, wali_pendidikan, wali_pekerjaan, wali_telp, 
                    no_kk, kepala_keluarga, tgl_kk''',

    "detail ayah": '''nis_lokal, nama_lengkap, ayah_nama, ayah_status, ayah_nik, ayah_tmp_lahir, 
                    ayah_tgl_lahir, ayah_pendidikan, ayah_pekerjaan, ayah_penghasilan, ayah_telp''',

    "detail ibu": '''nis_lokal, nama_lengkap, ibu_nama, ibu_status, ibu_nik, ibu_tmp_lahir, 
                    ibu_tgl_lahir, ibu_pendidikan, ibu_pekerjaan, ibu_penghasilan, ibu_telp''',

    "alamat": 'nis_lokal, nama_lengkap, nisn, nik, nama_lengkap, jalan, kampung, rt, rw, kel_desa, kecamatan, kabkota, provinsi, kodepos, alamat, alamat_full, transportasi, jarak, waktu_tempuh',
    "pendaftaran": 'nis_lokal, nama_lengkap, pilihan_jenjang, s.tgl_masuk, tapel_masuk, kls_masuk, s.no_urut',

    "sekolah asal": 'nis_lokal, nama_lengkap, nik, nss_sekolah_asal, npsn_sekolah_asal, nama_sekolah_asal, alamat_sekolah_asal, pilihan_jenjang'
    }
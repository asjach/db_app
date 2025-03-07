from utils.static_values import *
from utils.key_value.kolom_sql import *

TAB_CONFIG = {
    "Daftar Kelas": {
        "order_by"      : ('Nama', 'JK','Ayah', 'Ibu', 'Urutan', 'Alamat'),
        "search_by"     : ('Nama', 'Ayah', 'Ibu', 
                           'Alamat', 'Status Awal', 'Keaktifan'),
        "kolom"         : {key.title(): value for key, value in DAFTAR_KELAS.items()},
        "show_page"     : "DK",
    },

    "Rekap Siswa": {
        "hidden_frame"  : ['tingkat', 'kelas'],
        "show_page"     : "REKAP_SISWA",
    },

    "Mutasi Masuk": {
        "order_by"      : ['Nama', 'JK', 'Aktif', 'No Urut'],
        "search_by"     : ['Nama', 'Ayah', 'Ibu'],
        "kolom"         : [],  
        "hidden_frame"  : ['tingkat', 'kelas'],
        "show_page"     : "MUTASI_MASUK",
    },

    "Mutasi Keluar": {
        "order_by"      : ['Nama', 'JK', 'Tanggal Keluar', 'Tanggal Keluar DESC'],
        "search_by"     : ['Nama', 'Ayah', 'Ibu', 'NIS'],
        "kolom"         : [], 
        "show_page"     : "MUTASI_KELUAR",
    },

    "Pindah Kelas" : {
        "order_by"      : ['Nama', 'Pilihan Jenjang', 'Alamat', 'JK'],
        "search_by"     : ['Nama', 'Alamat', 'Ayah', 'Ibu'],
        "kolom"         : {key.title(): value for key, value in PINDAH_KELAS.items()},
        "hidden_frame"  : ['kelas'],
        "show_page"     : "PINDAH_KELAS",
    },
    
    "MI ke MD": {
        "order_by"      : ['Nama', 'JK',],
        "search_by"     : ['Nama', 'Ayah', 'Ibu', 'NIS'],
        "kolom"         : [], 
        "hidden_frame"  : ["jenjang"], 
        "show_page"     : "MI2MD",
    },
    "Kenaikan": {
        "order_by"      : ['Nama', 'JK', ],
        "search_by"     : ['Nama', 'Ayah', 'Ibu', 'NIS'],
        "kolom"         : [],  
        "show_page"     : "NAIK",
    },

    "Kelulusan": {
        "order_by"      : ['Nama', 'JK', ],
        "search_by"     : ['Nama', 'Ayah', 'Ibu', 'NIS'],
        "kolom"         : [],  
        "hidden_frame"  : ["tingkat", "kelas"], 
        "show_page"     : "LULUS",
    },

    "Buku Induk Guru": {
        "order_by"      : ['Nama', 'JK', 'ID Guru'],
        "search_by"     : ['Nama', ],
        "kolom"         : [],  
        "hidden_frame"  : ['jenjang', 'tapel', 'tingkat', 'kelas'], 
        "show_page"     : "BUKUINDUKGURU",
    },

    "Keaktifan Guru": {
        "order_by"      : ['Nama', 'JK',],
        "search_by"     : ['Nama', ],
        "kolom"         : {key.title(): value for key, value in GURU.items()},  
        "hidden_frame"  : ['tingkat', 'kelas'], 
        "show_page"     : "KEAKTIFANGURU",
    },
    "Riwayat Mengajar": {
        "order_by"      : ['Nama', 'JK',],
        "search_by"     : ['Nama', ],
        "hidden_frame"  : ['tingkat', 'kelas'], 
        "show_page"     : "RIWAYAT_MENGAJAR",
    },

    "Dokumen": {
        "order_by"      : ['Nama', 'JK',],
        "search_by"     : ['Nama', ],
        "show_page"     : "DOKUMEN",
    },

    "Pengaturan Kegiatan": {
        "hidden_frame"  : [ 'jenjang', 'tingkat', 'kelas'], 
        "show_page"     : "PENGATURAN_KEGIATAN",
    },

    "Input Nilai": {
        "show_page"     : "INPUT_NILAI",
    },

    "Rekap Nilai": {
        "show_page"     : "REKAP_NILAI",
    },

    "Riwayat Kelas": {
        "hidden_frame"  : ['tingkat', 'kelas'], 
        "show_page"     : "RIWAYAT_KELAS",

    },
    "Alamat": {
        "search_by"     : ['Kampung', ],
        "hidden_frame"  : ['jenjang', 'tapel', 'tingkat', 'kelas'], 
        "show_page"     : "ALAMAT",

    },
}


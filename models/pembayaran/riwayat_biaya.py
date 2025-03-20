from utils.database import ConnectDB

class RiwayatBiaya(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_riwayat_biaya(self, tapel):
        sql = """
            SELECT      r.id, r.id_biaya, b.nama_biaya, r.tapel, periode, nominal, 
                        tgl_mulai, tgl_selesai, catatan, count(t.id) as jumlah
            FROM        riwayat_biaya r
            JOIN        biaya b ON b.id = r.id_biaya
            LEFT JOIN        tagihan t on t.id_riwayat_biaya = r.id
            WHERE       r.tapel = %s
            GROUP BY    r.id, r.id_biaya, b.nama_biaya, r.tapel, periode, nominal, 
                        tgl_mulai, tgl_selesai, catatan
            ORDER BY    b.no_urut;
        """
        params = (tapel,)
        return self.get_data(sql, params, True)

    def get_biaya(self):
        sql = """
            SELECT      id, nama_biaya
            FROM        biaya
            ORDER BY    ISNULL(no_urut), CAST(no_urut AS UNSIGNED);
        """
        return self.get_data(sql)
    
    def insert_riwayat_biaya(self, id_biaya, tapel, periode, nominal):
        sql = """
            INSERT INTO     riwayat_biaya
                            (id_biaya, tapel, periode, nominal)
            VALUES          (%s, %s, %s, %s)
        """
        params = (id_biaya, tapel, periode, nominal)
        return self.update_data(sql, params)
    
    def generate_biaya_siswa(self, id_biaya, id_riwayat_biaya, tapel):
        sql = """
            INSERT INTO tagihan (nis_lokal, id_riwayat_biaya, nominal_tagihan, status_tagihan)
            SELECT DISTINCT sr.nis_lokal, %(id_riwayat_biaya)s,
                ROUND(rb.nominal * COALESCE(sd.persentase_dispensasi / 100, 1), 0) AS nominal_tagihan,
                CASE 
                    WHEN rb.tgl_mulai IS NULL OR rb.tgl_selesai IS NULL THEN 'tunggakan'
                    WHEN rb.tgl_selesai < CURRENT_DATE THEN 'tunggakan'
                    WHEN rb.tgl_mulai <= CURRENT_DATE AND rb.tgl_selesai >= CURRENT_DATE THEN 'belum lunas'
                    WHEN rb.tgl_mulai > CURRENT_DATE THEN 'belum aktif'
                    ELSE 'tunggakan'
                END AS status_tagihan
            FROM siswa_riwayat sr
            JOIN riwayat_biaya rb 
                ON rb.tapel = %(tapel)s 
                AND rb.id = %(id_riwayat_biaya)s
            LEFT JOIN dispensasi_siswa sd 
                ON sr.nis_lokal = sd.nis_lokal
            WHERE sr.is_active = 'Ya'
                AND sr.tapel = rb.tapel
        """
        params = {
            'id_riwayat_biaya': id_riwayat_biaya,
            'tapel': tapel
        }

        # Ambil kondisi dari tabel biaya
        kondisi_data = self.get_kondisi_from_tbl_biaya(id_biaya)
        if not kondisi_data:  # Jika None karena error atau tidak ada data
            print("Failed to fetch conditions from biaya table")
            return None

        kondisi_jenjang = kondisi_data.get('kondisi_jenjang', '')
        kondisi_tingkat = kondisi_data.get('kondisi_tingkat', '')
        kondisi_status_awal = kondisi_data.get('kondisi_status_awal', '')

        # Tambahkan kondisi jenjang
        sql += self.kondisi_jenjang(kondisi_jenjang)

        # Tambahkan kondisi tingkat
        if kondisi_tingkat:
            tingkat_list = kondisi_tingkat.split(',') if isinstance(kondisi_tingkat, str) else kondisi_tingkat
            tingkat_sql, tingkat_params = self.kondisi_tingkat(tingkat_list)
            sql += tingkat_sql
            params.update(tingkat_params)

        # Tambahkan kondisi status awal
        if kondisi_status_awal:
            status_list = kondisi_status_awal.split(',') if isinstance(kondisi_status_awal, str) else kondisi_status_awal
            if status_list:  # Pastikan status_list tidak kosong
                status_sql, status_params = self.kondisi_status_awal(status_list)
                sql += status_sql
                params.update(status_params)
            else:
                print("Warning: kondisi_status_awal is empty after processing")
        # Tambahkan NOT EXISTS
        sql += """
            AND NOT EXISTS (
                SELECT 1 FROM tagihan t 
                WHERE t.nis_lokal = sr.nis_lokal 
                    AND t.id_riwayat_biaya = %(id_riwayat_biaya)s
            );
        """
        # Eksekusi kueri
        row_count = self.update_data(sql, params)
        if row_count is False:
            print("Failed to update tagihan")
            return None
        print(f"Inserted/Updated {row_count} rows")
        return sql  # Opsional untuk debugging

    def kondisi_jenjang(self, jenjang: str):
        if jenjang == "All":
            # Union Penuh: Semua siswa di MI atau MD (dan jenjang lain seperti MTs, MA jika ada)
            # Untuk saat ini, hanya MI dan MD, tapi bisa diubah jadi "" jika jenjang lain ditambahkan
            return "    AND sr.jenjang IN ('MI', 'MD')\n"
        elif jenjang == "MI-MD":
            # Intersection: Siswa yang punya MI dan MD
            return """
            AND sr.jenjang IN ('MI', 'MD')
            AND EXISTS (
                SELECT 1 FROM siswa_riwayat sr2 
                WHERE sr2.nis_lokal = sr.nis_lokal 
                    AND sr2.tapel = sr.tapel 
                    AND sr2.jenjang = CASE 
                        WHEN sr.jenjang = 'MI' THEN 'MD' 
                        WHEN sr.jenjang = 'MD' THEN 'MI' 
                        END
                    AND sr2.is_active = 'Ya'
            )
            """
        elif jenjang == "MI Saja":
            # Hanya MI: Siswa di MI tapi tidak di MD
            return """
            AND sr.jenjang = 'MI'
            AND NOT EXISTS (
                SELECT 1 FROM siswa_riwayat sr2 
                WHERE sr2.nis_lokal = sr.nis_lokal 
                    AND sr2.tapel = sr.tapel 
                    AND sr2.jenjang = 'MD' 
                    AND sr2.is_active = 'Ya'
            )
            """
        elif jenjang == "MD Saja":
            # Hanya MD: Siswa di MD tapi tidak di MI
            return """
            AND sr.jenjang = 'MD'
            AND NOT EXISTS (
                SELECT 1 FROM siswa_riwayat sr2 
                WHERE sr2.nis_lokal = sr.nis_lokal 
                    AND sr2.tapel = sr.tapel 
                    AND sr2.jenjang = 'MI' 
                    AND sr2.is_active = 'Ya'
            )
            """
        elif jenjang == "MI":
            # Semua MI: Siswa yang punya jenjang MI (termasuk MI-MD)
            return "    AND sr.jenjang = 'MI'\n"
        elif jenjang == "MD":
            # Semua MD: Siswa yang punya jenjang MD (termasuk MI-MD)
            return "    AND sr.jenjang = 'MD'\n"
        elif jenjang == "MTs":
            # Semua MTs: Siswa yang punya jenjang MTs (tanpa interseksi dengan MI/MD)
            return "    AND sr.jenjang = 'MTs'\n"
        elif jenjang == "MA":
            # Semua MA: Siswa yang punya jenjang MA (tanpa interseksi dengan MI/MD)
            return "    AND sr.jenjang = 'MA'\n"
        return ""  # Default jika jenjang tidak valid

    def kondisi_tingkat(self, tingkat):
        if tingkat and len(tingkat) > 0:
            placeholders = ', '.join([f'%(tingkat_{i})s' for i in range(len(tingkat))])
            sql = f"    AND sr.tingkat IN ({placeholders})"
            params = {f'tingkat_{i}': val.strip() for i, val in enumerate(tingkat)}
            return sql, params
        return "", {}

    def kondisi_status_awal(self, status_awal):
        if status_awal and len(status_awal) > 0:
            placeholders = ', '.join([f'%(status_{i})s' for i in range(len(status_awal))])
            sql = f"    AND sr.status_awal IN ({placeholders})"
            params = {f'status_{i}': val.strip() for i, val in enumerate(status_awal)}
            return sql, params
        return "", {}

    def get_kondisi_from_tbl_biaya(self, id_biaya):
        sql = """
            SELECT kondisi_jenjang, kondisi_tingkat, kondisi_status_awal
            FROM biaya
            WHERE id = %s
        """
        params = (id_biaya,)
        return self.get_one_data(sql, params)  # Mengembalikan dict atau None
    

    def get_tagihan_siswa_by_biaya(self, id_riwayat_biaya):
        sql = """
            SELECT DISTINCT t.id, t.nis_lokal, nama_lengkap, sr.kelas, nominal_tagihan, status_tagihan
            FROM            tagihan t
            JOIN            siswa s on t.nis_lokal=s.nis_lokal
            JOIN            riwayat_biaya rb on rb.id = t.id_riwayat_biaya
            JOIN            siswa_riwayat sr on sr.nis_lokal = t.nis_lokal
                    AND     sr.tapel = rb.tapel
            WHERE           id_riwayat_biaya = %s

        """
        params = (id_riwayat_biaya,)
        return self.get_data(sql, params)
    
    def delete_tagihan_by_biaya(self, id_riwayat_biaya):
        sql = """
            DELETE      FROM tagihan
            WHERE       id_riwayat_biaya = %s
        """
        return self.update_data(sql, (id_riwayat_biaya,))
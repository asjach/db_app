from utils.database import ConnectDB
from utils.fungsi.functions import build_in_clause, validate_sql_identifier, validate_sql_order_by

# from utils.fungsi.functions import tapel_sebelumnya


class Model_Nilai(ConnectDB):
    def __init__(self, database_name=None):
        super().__init__(database_name)

    def get_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      id, kegiatan
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s AND tapel = %s
            ORDER BY    is_active DESC
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    ##  RIWAYAT KEGIATAN
    def get_kegiatan_riwayat(self, tapel):
        sql = """
            SELECT      id, jenjang, tapel, semester, kegiatan, tgl_pembagian, tgl_titimangsa, is_active
            FROM        kegiatan_riwayat
            WHERE       tapel = %s
            ORDER BY    jenjang DESC, tapel, semester
        """
        params = (tapel,)
        return self.get_data(sql, params, True)

    # def get_kegiatan_riwayat(self, tapel):
    #     sql = """
    #         SELECT      id, jenjang, tapel, semester, kegiatan, tgl_titimangsa
    #         FROM kegiatan_riwayat
    #         WHERE       tapel = %s
    #         ORDER BY    jenjang DESC, tapel, semester
    #     """
    #     params = (tapel,)
    #     return self.get_data(sql, params)

    ##  MAPEL

    def get_guru_aktif(self, jenjang, params):
        sql = """
            SELECT     gk.id_guru, nama_lengkap
            FROM        guru_keaktifan gk
            JOIN        guru g ON g.id_guru = gk.id_guru
            WHERE       jenjang = %s AND tapel = %s AND fungsi_jabatan = 'Guru'
            ORDER BY    nama_lengkap
        """
        params = (jenjang, params)
        return self.get_data(sql, params)

    def get_guru_by_kelas(self, jenjang, tapel, kelas):
        sql = """
            SELECT      km.id_guru, nama_lengkap
            FROM        guru_kelas_mengajar km
            JOIN        kelas_riwayat kr    ON kr.id = km.id_kelas
            JOIN        guru g              ON g.id_guru = km.id_guru
            WHERE       jenjang = %s AND tapel = %s AND kelas = %s
            ORDER BY    nama_lengkap
        """
        params = (jenjang, tapel, kelas)
        return self.get_data(sql, params)

    def get_mapel(
        self,
        jenjang,
        tapel,
        kegiatan,
        tingkat="",
        kelas="",
    ):
        sql = """
            SELECT      mr.id, mr.id_kelas, mr.id_kegiatan, kr.jenjang, kr.tapel, kr.tingkat, kr.kelas, mapel, no, mr.id_guru, nama_lengkap
            FROM        mapel_riwayat mr
            LEFT JOIN   guru g ON g.id_guru = mr.id_guru
            JOIN        kelas_riwayat kr ON kr.id = mr.id_kelas
            JOIN        kegiatan_riwayat kg ON kg.id = mr.id_kegiatan
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kr.tingkat LIKE %s
                AND     kr.kelas LIKE %s AND kegiatan = %s
            ORDER BY    no
        """
        params = (jenjang, tapel, f"%{tingkat}%", f"%{kelas}%", kegiatan)
        return self.get_data(sql, params, True)

    def get_mapel_list(self, jenjang, tapel, kegiatan):
        sql = """
                SELECT k.id, k.kelas, COALESCE(GROUP_CONCAT(m.mapel), '') AS list_mapel, COUNT(m.mapel) as jml_mapel
                FROM kelas_riwayat k
                JOIN (
                    SELECT m.id_kelas, m.mapel
                    FROM mapel_riwayat m
                    INNER JOIN kegiatan_riwayat kr ON m.id_kegiatan = kr.id
                    WHERE kr.kegiatan = %s
                ) m ON k.id = m.id_kelas
                WHERE k.jenjang = %s
                    AND k.tapel = %s
                GROUP BY k.id, k.kelas;
            """
        params = (kegiatan, jenjang, tapel)
        return self.get_data(sql, params)

    def insert_by_list_mapel(self, id_kelas, id_kegiatan, mapel):
        sql = """
            INSERT INTO mapel_riwayat (id_kelas, id_kegiatan, mapel)
            SELECT %s, %s, %s
            WHERE NOT EXISTS (
                SELECT 1
                FROM mapel_riwayat
                WHERE id_kelas = %s
                    AND id_kegiatan = %s
                    AND mapel = %s
            )
        """
        params = (id_kelas, id_kegiatan, mapel, id_kelas, id_kegiatan, mapel)
        try:
            result = self.update_data(sql, params)
            if result is False:
                return False
            elif result == 0:
                print(
                    f"Kombinasi {id_kelas}, {id_kegiatan}, {mapel} sudah ada, dilewati."
                )
                return "EXISTS"
            return True
        except Exception as e:
            print(f"Error inserting {id_kelas}, {id_kegiatan}, {mapel}: {e}")
            return False

    def insert_by_kegiatan_mapel(self, jenjang, tapel, id_kegiatan):
        sql = """
            INSERT INTO mapel_riwayat (id_kelas, id_kegiatan, id_guru, mapel, no)
            SELECT m.id_kelas, %s, m.id_guru, m.mapel, m.no
            FROM mapel_riwayat m
            JOIN kegiatan_riwayat k ON k.id = m.id_kegiatan
            LEFT JOIN mapel_riwayat m2 ON m2.mapel = m.mapel AND m2.id_kegiatan = %s
            JOIN kelas_riwayat kr ON kr.id = m.id_kelas
            WHERE k.kegiatan IN ('PAS', 'ASAS', 'PSAS')
                AND k.jenjang = %s
                AND k.tapel = %s
                AND m2.mapel IS NULL
        """
        params = (id_kegiatan, id_kegiatan, jenjang, tapel)
        return self.update_data(sql, params)

    def clear_mapel(self, id_kegiatan):
        sql = "DELETE FROM mapel_riwayat WHERE id_kegiatan = %s"
        params = (id_kegiatan,)
        return self.update_data(sql, params)

    ##  EKSKUL
    def get_pembimbing(self):
        sql = "SELECT id_pembimbing, nama_lengkap FROM pembimbing_ekskul;"
        return self.get_data(sql)

    def get_ekskul(self):
        sql = "SELECT * FROM ekskul"
        return self.get_data(sql)

    def get_riwayat_ekskul(self, jenjang, tapel, kegiatan):
        sql = """
            SELECT      er.id, er.id_kegiatan, kr.jenjang, kr.tapel, ekskul, er.id_pembimbing, nama_lengkap
            FROM        ekskul_riwayat er
            LEFT JOIN   pembimbing_ekskul p ON p.id_pembimbing = er.id_pembimbing
            JOIN        kegiatan_riwayat kr ON kr.id = er.id_kegiatan
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kegiatan = %s
            ORDER BY    er.ekskul
        """
        params = (jenjang, tapel, kegiatan)
        return self.get_data(sql, params, True)

    def insert_by_list_ekskul(self, id_kegiatan, ekskul):
        sql = """
            INSERT INTO ekskul_riwayat (id_kegiatan, ekskul)
            SELECT %s, %s
            WHERE NOT EXISTS (
                SELECT 1
                FROM ekskul_riwayat
                WHERE id_kegiatan = %s
                    AND ekskul = %s
            )
        """
        params = (id_kegiatan, ekskul, id_kegiatan, ekskul)
        try:
            result = self.update_data(sql, params)
            if result is False:
                return False
            elif result == 0:
                print(f"Kombinasi {id_kegiatan} dan {ekskul} sudah ada, dilewati.")
                return "EXISTS"
            return True
        except Exception as e:
            print(f"Error inserting {id_kegiatan}, {ekskul}: {e}")
            return False

    ##  PRESTASI
    def get_peserta_all(self, id_kegiatan, kelas, search_text):
        sql = """
            SELECT kp.id, kp.nis_lokal, s.nama_lengkap, kelas
            FROM    kegiatan_peserta kp
            JOIN    siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN    kelas_riwayat kr on kr.id = kp.id_kelas
            WHERE   id_kegiatan = %s
            AND     nama_lengkap LIKE %s
        """

        params = [id_kegiatan, f"%{search_text}%"]
        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kelas IN ({placeholders})"
                params.extend(items)
        sql += " ORDER BY kelas, nama_lengkap "
        return self.get_data(sql, tuple(params))

    def get_prestasi_kegiatan(self, id_kegiatan):
        sql = """
            SELECT  np.id, np.id_peserta, nama_lengkap, kelas, jenis_prestasi, keterangan
            FROM    nilai_prestasi np
            LEFT JOIN    kegiatan_peserta kp ON kp.id = np.id_peserta
            LEFT JOIN    siswa s ON s.nis_lokal = kp.nis_lokal
            LEFT JOIN    kelas_riwayat kr on kr.id = kp.id_kelas
            WHERE   id_kegiatan = %s

        """
        params = (id_kegiatan,)
        return self.get_data(sql, params)

    def tambah_prestasi_siswa(self, id_peserta):
        sql = """
        INSERT INTO nilai_prestasi (id_peserta)
        VALUES  (%s);
        """
        params = (id_peserta,)
        return self.update_data(sql, params)


    ##  PESERTA

    def get_peserta_kegiatan(
            self,
            id_kegiatan,
            tingkat=None,
            kelas=None):

        sql = """
            SELECT      kp.id,
                        kp.id_kelas,
                        kp.id_kegiatan,
                        kp.no_urut,
                        kp.nis_lokal,
                        kp.no_peserta,
                        s.nama_lengkap,
                        kr.kelas
            FROM        kegiatan_peserta kp
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
            WHERE       kp.id_kegiatan = %s
        """

        params = [id_kegiatan]

        if kelas:
            placeholders, items = build_in_clause(kelas)
            if placeholders:
                sql += f" AND kr.kelas IN ({placeholders})"
                params.extend(items)

        if tingkat:
            placeholders, items = build_in_clause(tingkat)
            if placeholders:
                sql += f" AND kr.tingkat IN ({placeholders})"
                params.extend(items)

        sql += """
            ORDER BY
                kr.kelas,
                CAST(NULLIF(kp.no_urut, '') AS UNSIGNED),
                s.nama_lengkap
        """

        return self.get_data(sql, tuple(params), True)


    # def get_peserta_kegiatan(self, id_kegiatan, id_kelas):
    #     sql = """   SELECT      kp.id, id_kelas, id_kegiatan, kp.no_urut, kp.nis_lokal, kp.no_peserta, nama_lengkap, kelas
    #                 FROM        kegiatan_peserta kp
    #                 JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
    #                 JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
    #                 WHERE       id_kegiatan = %s"""
    #     params = [id_kegiatan]
    #     if id_kelas not in [None, ""]:
    #         sql += " AND kp.id_kelas = %s "
    #         params.append(id_kelas)
    #     sql += """ ORDER BY    kelas, CAST(NULLIF(kp.no_urut, '') AS UNSIGNED), nama_lengkap"""
    #     return self.get_data(sql, tuple(params), True)

    def update_data_peserta(self, key, column_name, value):
        sql = """UPDATE kegiatan_riwayat SET {} = %s WHERE id = %s""".format(
            column_name
        )
        return self.update_data(sql, (value, key))

    def get_kelas_riwayat(self, jenjang, tapel):
        sql = """SELECT * FROM kelas_riwayat WHERE jenjang = %s AND tapel = %s"""
        return self.get_data(sql, (jenjang, tapel))

    def generate_peserta(self, jenjang, tapel, id_kelas, kelas, id_kegiatan):
        sql = """INSERT INTO    kegiatan_peserta (id_kelas, id_kegiatan, nis_lokal, no_urut)
                SELECT          {}, {}, r.nis_lokal, r.no_urut FROM siswa_riwayat r
                WHERE           jenjang = %s AND tapel = %s AND kelas = %s AND is_active = 'Ya'
                                AND nis_lokal NOT IN(SELECT  nis_lokal FROM kegiatan_peserta
                                WHERE id_kegiatan = %s)""".format(id_kelas, id_kegiatan)
        return self.update_data(sql, (jenjang, tapel, kelas, id_kegiatan))

    def clear_peserta(self, id_kegiatan):
        return self.update_data(
            "DELETE FROM kegiatan_peserta WHERE id_kegiatan = %s", (id_kegiatan,)
        )

    def generate_no_peserta(self, tapel, kegiatan):
        sql = """
            UPDATE kegiatan_peserta kp
            JOIN kelas_riwayat kr ON kr.id = kp.id_kelas
            JOIN kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
            JOIN siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN (
                SELECT tapel, tingkat, kegiatan, nis_lokal,
                CONCAT(kegiatan, '-', tapel, '-', tingkat, '-', LPAD(urut, 3, '0')) AS nomor_peserta
                FROM (
                    SELECT  kr.tapel, kr.tingkat, krw.kegiatan, kp.nis_lokal,
                    ROW_NUMBER() OVER (
                    PARTITION BY kr.tapel, krw.kegiatan
                    ORDER BY kr.kelas, s.nama_lengkap) AS urut
                FROM kegiatan_peserta kp
                JOIN kelas_riwayat kr ON kr.id = kp.id_kelas
                JOIN kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
                JOIN siswa s ON s.nis_lokal = kp.nis_lokal
                GROUP BY kr.tapel, kr.tingkat, kr.kelas, krw.kegiatan, kp.nis_lokal, s.nama_lengkap
                ) AS peserta_unik
            ) n ON n.tapel = kr.tapel AND n.kegiatan = krw.kegiatan AND n.nis_lokal = kp.nis_lokal
            SET kp.no_peserta = n.nomor_peserta
            WHERE kr.tapel = %s AND krw.kegiatan = %s;
        """
        return self.update_data(sql, (tapel, kegiatan))

    def peserta_belum_masuk(self, jenjang, tapel, id_kegiatan):
        sql = """
            SELECT r.nis_lokal, nama_lengkap, r.kelas
            FROM    siswa_riwayat r
            JOIN    siswa s ON s.nis_lokal = r.nis_lokal
            WHERE   r.jenjang = %s AND r.tapel = %s AND r.is_active = 'Ya'
                AND r.nis_lokal NOT IN (SELECT kp.nis_lokal
                    FROM kegiatan_peserta kp
                    WHERE   kp.id_kegiatan = %s)
            ORDER BY kelas, nama_lengkap
        """
        return self.get_data(sql, (jenjang, tapel, id_kegiatan))

    def peserta_tidak_aktif(self, jenjang, tapel, id_kegiatan):
        sql = """   SELECT kp.nis_lokal, nama_lengkap, kr.kelas
                    FROM        kegiatan_peserta kp
                    JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
                    JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
                    WHERE       kp.id_kegiatan = %s
                        AND     kp.nis_lokal NOT IN (
                            SELECT  r.nis_lokal FROM siswa_riwayat r
                            WHERE   r.jenjang = %s AND r.tapel = %s AND r.is_active = 'Ya')"""
        return self.get_data(sql, (id_kegiatan, jenjang, tapel))

    ##  CETAK RAPORT
    def get_kelas(self, jenjang, tapel):
        sql = """
        SELECT      id, kelas
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s
        ORDER BY    kelas;
        """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def get_siswa_aktif(self, jenjang, tapel, kelas, kegiatan):
        sql = """
            SELECT      kp.id, id_kelas, id_kegiatan, kp.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta kp
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kt ON kt.id = kp.id_kegiatan
            JOIN        kelas_riwayat kr ON kr.id = kp.id_kelas
            WHERE       kr.jenjang = %s AND kr.tapel = %s AND kr.kelas = %s AND kegiatan  = %s
            ORDER BY    kelas, nama_lengkap
        """
        params = (jenjang, tapel, kelas, kegiatan)
        return self.get_data(sql, params)

    def get_list_mapel(self, jenjang, tapel, kegiatan, tingkat, kelas):
        sql = """
                SELECT      mapel
                from        mapel_riwayat m
                LEFT JOIN   kegiatan_riwayat r on r.id = m.id_kegiatan
                LEFT JOIN   kelas_riwayat k on k.id = m.id_kelas
                where 	    r.jenjang = %s
                AND		    r.tapel = %s
                AND 	    r.kegiatan = %s
                AND 	    k.tingkat = %s
                AND 	    k.kelas = %s
                ORDER BY    m.no
            """
        params = (jenjang, tapel, kegiatan, tingkat, kelas)
        return self.get_data(sql, params)

    def data_rapor(self, id_kelas, id_kegiatan, nis_lokal, limit=None):
        sql = """
            SELECT 		k.id_kelas, k.id_kegiatan, krw.jenjang, krw.tapel,
                        krw.kelas, kr.semester, kr.kegiatan, kr.tgl_titimangsa,
                        sum(n.nilai) as jml,
                        round(avg(n.nilai), 2) as rt,
                        k.ranking, k.sakit, k.ijin, k.alpa,
                        k.catatan_walas, k.status_naik,
                        CONCAT_WS(', ', PROPER_CASE(gw.nama_lengkap), gw.gelar_belakang) AS walas,
                        d.namafile as ttd_walas,
                        CONCAT_WS(', ', PROPER_CASE(gm.nama_lengkap), gm.gelar_belakang) AS mudir,
                        dm.namafile as ttd_mudir,
                        s.*
            FROM		kegiatan_peserta k
            JOIN		nilai_angka n on n.id_peserta = k.id
            JOIN		siswa s on s.nis_lokal = k.nis_lokal
            JOIN		kelas_riwayat krw on krw.id = k.id_kelas
            JOIN        jenjang j on j.jenjang = krw.jenjang
            LEFT JOIN	guru gw on gw.id_guru = krw.id_walas
            LEFT JOIN   guru gm on gm.id_guru = j.id_mudir
            JOIN		kegiatan_riwayat kr on kr.id = k.id_kegiatan
            LEFT JOIN	dokumen d on d.nomor_induk = gw.id_guru and d.jenis_dokumen IN('TTD Rapor', 'Tanda Tangan Rapor')
            LEFT JOIN   dokumen dm on dm.nomor_induk = j.id_mudir and dm.jenis_dokumen = 'Tanda Tangan Rapor'
            WHERE		k.id_kelas = %s
                and 	k.id_kegiatan = %s
                and k.nis_lokal LIKE %s
            GROUP BY	k.nis_lokal, k.id, d.id, mudir, ttd_mudir
            ORDER BY    krw.kelas, s.nama_lengkap
        """
        if limit:
            sql += " LIMIT %s"
            params = (id_kelas, id_kegiatan, f"%{nis_lokal}%", limit)
        else:
            params = (id_kelas, id_kegiatan, f"%{nis_lokal}%")
        return self.get_data(sql, params)

    def data_nilai(self, id_kelas, id_kegiatan, nis_lokal):
        sql = """
            SELECT 		k.id_kelas, k.id_kegiatan, nis_lokal, mata_pelajaran, n.mapel,
                        nilai,
                        CONCAT(
                            CASE
                                WHEN g.jk = 'L' THEN 'Ust. '
                                WHEN g.jk = 'P' THEN 'Ibu '
                                ELSE ''
                            END,
                            PROPER_CASE(g.nama_lengkap),
                            IF(g.gelar_belakang IS NOT NULL AND g.gelar_belakang <> '',
                            CONCAT(', ', g.gelar_belakang),
                            ''
                            )
                        ) AS nama_guru
            FROM  		kegiatan_peserta k
            JOIN		nilai_angka n on n.id_peserta = k.id
            JOIN        mapel m on m.mapel = n.mapel
            JOIN        mapel_riwayat mr
                ON      mr.id_kelas =k.id_kelas
                    AND mr.id_kegiatan=k.id_kegiatan
                    AND mr.mapel = n.mapel
            LEFT JOIN   guru g ON g.id_guru = mr.id_guru
            WHERE 		k.id_kelas = %s
                AND 	k.id_kegiatan = %s
                AND     k.nis_lokal = %s
            ORDER BY    mr.no
        """
        params = (id_kelas, id_kegiatan, nis_lokal)
        return self.get_data(sql, params)

    def data_ekskul(self, nis_lokal, id_kegiatan=None):
        sql = """
            SELECT kp.nis_lokal, e.nama_ekskul,
            CONCAT(
                CASE
                    WHEN p.jk = 'L' THEN 'Ust. '
                    WHEN p.jk = 'P' THEN 'Ibu '
                    WHEN p.jk = 'PAK' Then 'Pak '
                    WHEN p.jk = 'Kang' Then 'Kang '
                    WHEN p.jk = 'Teh' Then 'Teh '
                    ELSE ''
                END,
                PROPER_CASE(p.nama_lengkap)
            ) AS pembimbing,
            ne.predikat
            from nilai_ekskul ne
            left join kegiatan_peserta kp on kp.id = ne.id_peserta
            left join ekskul e on e.ekskul = ne.ekskul
            left join ekskul_riwayat er on er.ekskul = ne.ekskul
            left join pembimbing_ekskul p on p.id_pembimbing = er.id_pembimbing
            where kp.nis_lokal = %s
            and kp.id_kegiatan = %s
        """
        params = (nis_lokal, id_kegiatan)
        return self.get_data(sql, params)

    def data_prestasi(self, nis_lokal, id_kegiatan=None):
        sql = """
            SELECT np.jenis_prestasi, np.keterangan
            FROM nilai_prestasi np
            JOIN kegiatan_peserta kp ON kp.id = np.id_peserta
            WHERE   kp.nis_lokal = %s
            and kp.id_kegiatan = %s
        """
        params = (nis_lokal, id_kegiatan)
        return self.get_data(sql, params)

    def get_setting_rapor(self, id_kelas):
        sql = """
            SELECT setting_rapor
            FROM    kelas_riwayat
            where   id = %s
            """
        params = (id_kelas,)
        return self.get_one_data(sql, params)

    def update_setting_rapor(self, id_kelas, nilai_setting):
        sql = """
            UPDATE kelas_riwayat
            SET setting_rapor = %s
            WHERE id = %s
            """
        params = (nilai_setting, id_kelas)
        return self.update_data(sql, params)

    ##  REKAP NILAI
    def get_kelas_riwayat_with_peserta(self, jenjang, tapel, id_kegiatan):
        sql = """
            SELECT      r.id, jenjang, tapel, tingkat, kelas, id_walas,
                        nama_lengkap, COUNT(kp.id_kelas) AS jml
            FROM        kelas_riwayat r
            LEFT JOIN   guru g ON g.id_guru = r.id_walas
            JOIN   kegiatan_peserta kp ON kp.id_kelas = r.id AND kp.id_kegiatan = %s
            WHERE       jenjang = %s AND tapel = %s
            GROUP BY    r.id, jenjang, tapel, tingkat, kelas,
                        id_walas, nama_lengkap
        """
        params = (
            id_kegiatan,
            jenjang,
            tapel,
        )
        return self.get_data(sql, params)

    def get_nilai_by_kegiatan(
        self,
        kolom_mapel,
        jenjang,
        tapel,
        tingkat,
        kelas,
        kegiatan,
        order,
        opsi_nama="lengkap",
    ):
        kolom_mapel = f"{kolom_mapel}, " if kolom_mapel else ""
        if opsi_nama == "lengkap":
            nama = "s.nama_lengkap"
        else:
            nama = "s.nama_singkat"
        if order == "JK":
            order_by = f"s.jk, {nama}"
        elif order.lower() == "peringkat":
            order_by = "cast(ranking as unsigned)"
        else:
            order_by = f"{nama}"
        sql = """
            SELECT      kp.no_urut as `#`, """
        sql += f" {nama}, "
        sql += """ kelas as kls,
                        {}
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            JOIN        guru g ON g.id_guru = k.id_walas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat = %s
                AND     k.kelas = %s
                AND     kr.kegiatan = %s
            GROUP BY    kp.no_urut, {}, kp.ranking, s.jk
            ORDER BY    {}
            """.format(kolom_mapel, nama, order_by)
        params = (jenjang, tapel, tingkat, kelas, kegiatan)
        return self.get_data(sql, params)

    def get_daftar_peringkat(
        self, id_kegiatan, ayah=True, ibu=True, alamat=True, opsi=3
    ):
        if ayah:
            ayah = "ayah_nama, "
        if ibu:
            ibu = "ibu_nama, "
        if alamat:
            alamat = "kampung, "
        kampung = "kampung "

        if opsi == 1:
            opsi_peringkat = "AND kp.ranking IN (1)"
        elif opsi == 3:
            opsi_peringkat = "AND kp.ranking IN (1, 2, 3)"
        elif opsi == 10:
            opsi_peringkat = "AND kp.ranking IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
        else:
            opsi_peringkat = ""
        sql = """
            SELECT      k.kelas as KLS,
                        ranking as `RANK`,
                        nama_lengkap,
                        {}{}{}
                        SUM(n.nilai) as JML,
                        AVG(n.nilai) as RT
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       kp.id_kegiatan = %s
            {}
            GROUP BY    kelas, ranking, nama_lengkap, {}{}{}
            ORDER BY    kelas, CAST(ranking as unsigned)
        """.format(ayah, ibu, alamat, opsi_peringkat, ayah, ibu, kampung)
        params = (id_kegiatan,)
        return self.get_data(sql, params)

    def get_setting_rekap(self, id_kelas):
        sql = """
            SELECT setting_rekap_nilai
            FROM kelas_riwayat
            WHERE id = %s
            """
        params = (id_kelas,)
        return self.get_one_data(sql, params)

    def update_setting_rekap(self, id_kelas, value):
        sql = """
            UPDATE kelas_riwayat
            SET setting_rekap_nilai = %s
            WHERE id = %s
        """
        params = (value, id_kelas)
        return self.update_data(sql, params)

    ##  INPUT NILAI
    def get_id_kegiatan(self, jenjang, tapel):
        sql = """
            SELECT      kegiatan, id
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s
                AND     tapel = %s
            ORDER BY    is_active DESC
            """
        params = (jenjang, tapel)
        return self.get_data(sql, params)

    def data_siswa(self, jenjang, tapel, kegiatan):
        sql = """
            SELECT      id_kelas, id_kegiatan, p.no_urut, p.id as id_peserta, p.nis_lokal, nama_lengkap, kelas
            FROM        kegiatan_peserta p
            JOIN   		siswa s on s.nis_lokal = p.nis_lokal
            JOIN        kegiatan_riwayat r on r.id = p.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = p.id_kelas
            WHERE       r.jenjang = %s
                AND		r.tapel = %s
                AND     r.kegiatan = %s
            ORDER BY    k.kelas, cast(p.no_urut as unsigned), nama_lengkap
            """
        params = (jenjang, tapel, kegiatan)
        return self.get_data(sql, params)

    def get_path(self, jenjang, tapel, kegiatan, kolom):
        sql = """
            SELECT      {}
            FROM        kegiatan_riwayat
            WHERE       jenjang = %s
                AND     tapel = %s
                AND     kegiatan = %s
            """.format(kolom)
        params = (jenjang, tapel, kegiatan)
        return self.get_data(sql, params)

    def update_path(self, jenjang, tapel, kegiatan, kolom, nilai):
        sql = """
            UPDATE      kegiatan_riwayat
            SET         {} = %s
            WHERE       jenjang = %s
                AND     tapel = %s
                AND     kegiatan = %s
        """.format(kolom)
        params = (nilai, jenjang, tapel, kegiatan)
        return self.update_data(sql, params)

    def all_mapel(self):
        sql = """
            SELECT      mapel
            FROM        mapel
        """
        mapel = self.get_data(sql)
        to_list = [d["mapel"] for d in mapel]
        return to_list

    def all_ekskul(self):
        sql = """
            SELECT ekskul from ekskul
        """
        ekskul = self.get_data(sql)
        to_list = [d["ekskul"] for d in ekskul]
        return to_list

    def cek_nilai_bulk(self, keys):
        if not keys:
            return {}
        placeholders = ",".join(["(%s, %s)" for _ in keys])
        sql = f"""
            SELECT id, id_peserta, mapel, nilai
            FROM nilai_angka
            WHERE (id_peserta, mapel) IN ({placeholders})
        """
        params = [item for key in keys for item in key]  # Flatten keys
        results = self.get_data(sql, params)
        existing_dict = {
            (r["id_peserta"], r["mapel"]): (r["id"], r["nilai"]) for r in results
        }
        return existing_dict

    def cek_ekskul_bulk(self, keys):
        if not keys:
            return {}
        placeholders = ",".join(["(%s, %s)" for _ in keys])
        sql = f"""
            SELECT id, id_peserta, ekskul, predikat
            FROM nilai_ekskul
            WHERE (id_peserta, ekskul) IN ({placeholders})
        """
        params = [item for key in keys for item in key]  # Flatten keys
        results = self.get_data(sql, params)
        existing_dict = {
            (r["id_peserta"], r["ekskul"]): (r["id"], r["predikat"]) for r in results
        }
        return existing_dict

    def insert_nilai_bulk(self, data):
        if not data:
            return

        sql = """
            INSERT INTO nilai_angka (id_peserta, mapel, nilai)
            VALUES (%s, %s, %s)
        """
        row_count = self.update_data(sql, data)
        return row_count

    def update_nilai_bulk(self, data):
        if not data:
            return

        sql = """
            UPDATE nilai_angka
            SET nilai = %s
            WHERE id = %s
        """
        row_count = self.update_data(sql, data)
        return row_count

    def insert_ekskul_bulk(self, data):
        if not data:
            return

        sql = """
            INSERT INTO nilai_ekskul (id_peserta, ekskul, predikat)
            VALUES (%s, %s, %s)
        """
        row_count = self.update_data(sql, data)
        return row_count

    def update_ekskul_bulk(self, data):
        if not data:
            return

        sql = """
            UPDATE nilai_ekskul
            SET predikat = %s
            WHERE id = %s
        """
        row_count = self.update_data(sql, data)
        return row_count

    def cek_peserta_bulk(self, keys):
        if not keys:
            return {}

        placeholders = ",".join(["(%s)" for _ in keys])
        sql = f"""
            SELECT id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas, ranking, status_naik
            FROM kegiatan_peserta
            WHERE id IN ({placeholders})
        """
        params = keys
        results = self.get_data(sql, params)

        existing_dict = {
            r["id"]: {
                "no_urut": r["no_urut"],
                "sakit": r["sakit"],
                "ijin": r["ijin"],
                "alpa": r["alpa"],
                "catatan_walas": r["catatan_walas"],
                "ranking": r["ranking"],
                "status_naik": r["status_naik"],
            }
            for r in results
        }
        return existing_dict

    def insert_peserta_bulk(self, data):
        if not data:
            return

        sql = """
            INSERT INTO kegiatan_peserta (id, id_kelas, id_kegiatan, no_urut, sakit, ijin, alpa, catatan_walas, ranking, status_naik)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        row_count = self.update_data(sql, data)
        return row_count

    def update_peserta_bulk(self, data):
        if not data:
            return

        sql = """
            UPDATE kegiatan_peserta
            SET no_urut = %s, sakit = %s, ijin = %s, alpa = %s, catatan_walas = %s, ranking = %s, status_naik = %s
            WHERE id = %s
        """
        row_count = self.update_data(sql, data)
        return row_count

    def get_list_mapel(self, jenjang, tapel, kegiatan, tingkat, kelas):
        sql = """
                SELECT      mapel
                from        mapel_riwayat m
                LEFT JOIN   kegiatan_riwayat r on r.id = m.id_kegiatan
                LEFT JOIN   kelas_riwayat k on k.id = m.id_kelas
                where 	    r.jenjang = %s
                AND		    r.tapel = %s
                AND 	    r.kegiatan = %s
                AND 	    k.tingkat LIKE %s
                AND 	    k.kelas LIKE %s
                ORDER BY    m.no
            """
        params = (jenjang, tapel, kegiatan, f"%{tingkat}%", f"%{kelas}%")
        return self.get_data(sql, params)

    def get_catatan_by_kegiatan(self, jenjang, tapel, tingkat, kelas, kegiatan):
        if kegiatan in ["PAT", 'UKK', 'PSAT', 'ASAT']:
            kenaikan = ", kp.status_naik "
        else:
            kenaikan = ""
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`,
                        kp.catatan_walas
                        {}
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat LIKE %s
                AND     k.kelas LIKE %s
                AND     kr.kegiatan = %s
            GROUP BY    kelas, kp.no_urut, s.nama_lengkap, kp.ranking, kp.catatan_walas {}
            ORDER BY    kelas, s.nama_lengkap
            """.format(kenaikan, kenaikan)

        params = (jenjang, tapel, f"%{tingkat}%", f"%{kelas}%", kegiatan)
        return self.get_data(sql, params)

    def get_nilai_catatan_by_kegiatan(
        self, kolom_mapel, jenjang, tapel, tingkat, kelas, kegiatan
    ):
        if kegiatan in ["PAT", 'UKK', 'PSAT', 'ASAT']:
            kenaikan = ", kp.status_naik "
        else:
            kenaikan = ""
        sql = """
            SELECT      kp.no_urut as `#`, s.nama_lengkap, kelas as kls,
                        {},
                        SUM(n.nilai) as jml,
                        AVG(n.nilai) as rt,
                        kp.ranking as `rank`,
                        kp.catatan_walas
                        {}
            FROM        nilai_angka n
            JOIN        kegiatan_peserta kp ON kp.id = n.id_peserta
            JOIN        siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN        kegiatan_riwayat kr ON kr.id = kp.id_kegiatan
            JOIN        kelas_riwayat k ON k.id = kp.id_kelas
            WHERE       k.jenjang = %s
                AND     k.tapel = %s
                AND     k.tingkat LIKE %s
                AND     k.kelas LIKE %s
                AND     kr.kegiatan = %s
            GROUP BY    kelas, kp.no_urut, s.nama_lengkap, kp.ranking, kp.catatan_walas {}
            ORDER BY    kelas, s.nama_lengkap
            """.format(kolom_mapel, kenaikan, kenaikan)
        params = (jenjang, tapel, f"%{tingkat}%", f"%{kelas}%", kegiatan)
        return self.get_data(sql, params)

    def get_kelas(self, jenjang, tapel):
        sql = """
        SELECT      id, kelas
        FROM        kelas_riwayat
        WHERE       jenjang = %s AND tapel = %s
        ORDER BY    kelas;
        """
        params = (
            jenjang,
            tapel,
        )
        return self.get_data(sql, params)

    ##  KARTU PESERTA
    def get_data_peserta(
        self, tapel, kegiatan, distintc=False, limit=True, limit_value=4
    ):
        sql = " SELECT "
        if distintc:
            sql += " DISTINCT "
        sql += """
                no_peserta,
                s.nis_lokal,
                s.nisn,
                s.nama_lengkap,
                kr.kelas,
                concat(s.tmp_lahir, ", ", DATE_FORMAT(s.tgl_lahir, "%d-%m-%Y")) as ttl,
                d.namafile as foto
            FROM    kegiatan_peserta kp
            JOIN    siswa s ON s.nis_lokal = kp.nis_lokal
            JOIN    kelas_riwayat kr ON kr.id = kp.id_kelas
            JOIN    kegiatan_riwayat krw ON krw.id = kp.id_kegiatan
            LEFT JOIN dokumen d ON d.nomor_induk = kp.nis_lokal AND jenis_dokumen = 'Foto' AND keterangan = 'Pas'
            WHERE   kr.tapel = %s
                AND krw.kegiatan = %s
            ORDER BY kr.kelas, s.nama_lengkap
        """
        if limit:
            sql += f" LIMIT {limit_value}"
        params = (tapel, kegiatan)
        return self.get_data(sql, params)

    def get_setting(self, id_kegiatan, jenis_setting="setting_kartu"):
        sql = """
            SELECT {}
            FROM kegiatan_riwayat
            WHERE id = %s
            """.format(jenis_setting)

        params = (id_kegiatan,)
        return self.get_one_data(sql, params)

    def update_setting(self, id_kegiatan, value, jenis_setting="setting_kartu"):
        sql = """
            UPDATE kegiatan_riwayat
            SET {} = %s
            WHERE id = %s
        """.format(jenis_setting)
        params = (value, id_kegiatan)
        return self.update_data(sql, params)

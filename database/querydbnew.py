import psycopg2

db_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'berthdb1',
    'user': 'admin',
    'password': 'admin'
}

try:
    connection = psycopg2.connect(**db_config)
    print("Koneksi berhasil!")
    cur = connection.cursor()

#     cur.execute("""
#   CREATE TABLE IF NOT EXISTS pelanggan (
#     id_pelanggan VARCHAR(10) PRIMARY KEY,
#     phone_number VARCHAR(15) NOT NULL,
#     nik CHAR(16) NOT NULL UNIQUE,
#     username VARCHAR(50) NOT NULL UNIQUE,
#     password TEXT NOT NULL,
#     status SMALLINT CHECK (status IN (0, 1)) DEFAULT 0
# );
#     """)

#     cur.execute("""
#     CREATE SEQUENCE IF NOT EXISTS pelanggan_seq START 1;
#     """)
#
#     cur.execute("""
# CREATE OR REPLACE FUNCTION generate_id_pelanggan()
# RETURNS TRIGGER AS $$
# DECLARE
#     new_id VARCHAR(10);
# BEGIN
#     new_id := 'CUS-' || LPAD(NEXTVAL('pelanggan_seq')::TEXT, 3, '0');
#     NEW.id_pelanggan := new_id;
#     RETURN NEW;
# END;
# $$ LANGUAGE plpgsql;
#     """)
#
#     cur.execute("""
#     CREATE TRIGGER pelanggan_id_trigger
# BEFORE INSERT ON pelanggan
# FOR EACH ROW
# WHEN (NEW.id_pelanggan IS NULL)
# EXECUTE FUNCTION generate_id_pelanggan();
#     """)

    # cur.execute("""
    # ALTER TABLE pelanggan
    # ALTER COLUMN status SET DEFAULT 0;
    # """)

    # cur.execute("""
    # ALTER TABLE pelanggan
    # ADD COLUMN fullname VARCHAR(30) NOT NULL;
    # """)
    # cur.execute("""
    # ALTER TABLE pelanggan
    # ADD COLUMN birthdate DATE NOT NULL;
    # """)


#     cur.execute("""
#     INSERT INTO pelanggan (phone_number, username, password, status, fullname,birthdate, email)
# VALUES ('081234567890', 'diddyjomok', 'password123', 1, 'p.diddy', '2000-08-24','pdiddy@example.com');
#     """)

    # cur.execute("""
    # ALTER TABLE pelanggan
    # ADD COLUMN email VARCHAR(100) ;
    # """)



#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS admin(
#     id_admin VARCHAR(20) PRIMARY KEY,
#     nama_admin VARCHAR(50) NOT NULL,
#     username VARCHAR(100) NOT NULL UNIQUE,
#     password VARCHAR(100)
#     );
#     """)
#     cur.execute("""
#     create sequence if not exists admin_seq start 1;
#     """)
#
#     cur.execute("""
#     CREATE OR REPLACE FUNCTION generate_id_admin()
# RETURNS TRIGGER AS $$
# DECLARE
#     new_id VARCHAR(10);
# BEGIN
#     new_id := 'admin-' || LPAD(NEXTVAL('admin_seq')::TEXT, 3, '0');
#     NEW.id_admin := new_id;
#     RETURN NEW;
# END;
# $$ LANGUAGE plpgsql;
#     """)
#
#     cur.execute("""
#     CREATE TRIGGER admin_id_trigger
#     BEFORE INSERT ON admin
#     FOR EACH ROW
#     WHEN (NEW.id_admin IS NULL)
#     EXECUTE FUNCTION generate_id_admin();
#     """)

    # cur.execute("""
    # alter table admin add column phone_number INT NOT NULL;
    # """)

    # cur.execute("""
    # alter table admin alter column phone_number type VARCHAR(20);
    # """)


    # cur.execute("""
    # insert into admin(nama_admin, username, password, phone_number) values('baskoro', 'baskoro123', 'admin1','08123456789');
    # """)
    # cur.execute("""
    # SELECT * FROM kapal;
    #
    # """)
    # data = cur.fetchall()
    # for i in data :
    #     print(i)

    # cur.execute("""
    # CREATE TABLE kelas(id_kelas SERIAL PRIMARY KEY, jenis_kelas VARCHAR(20) NOT NULL);
    # """)

    # cur.execute('''
    # create table kapal(id_kapal varchar(20) primary key, nama_kapal varchar(30) not null, tujuan varchar(20) not null,kapasitas varchar(10) not null);
    # ''')

    # cur.execute("""
    # create sequence kapal_seq start 1;
    # """)

    # cur.execute("""
    # create or replace function generate_id_kapal()
    # returns trigger as $$
    # declare
    #     new_id varchar(10);
    # begin
    #     new_id := 'kpl-' || lpad(nextval('kapal_seq')::text, 3,'0');
    #     new.id_kapal := new_id;
    #     return new;
    # end;
    # $$ language plpgsql;
    # """)

    # cur.execute("""
    # create or replace trigger kapal_id_trigger
    # before insert on kapal
    # for each row
    # when (new.id_kapal is null)
    # execute function generate_id_kapal();
    # """)

    # cur.execute("""
    # insert into kapal(nama_kapal, tujuan , kapasitas) values('nusantara','madura','1000');
    # """)

    # cur.execute('''create sequence kelas_seq start 1;''')

    # cur.execute("""insert into kelas (jenis_kelas) values ('ekonomi');""")
    # cur.execute("""insert into kelas (jenis_kelas) values ('bisnis');""")
    # cur.execute("""insert into kelas (jenis_kelas) values ('vip');""")

    # cur.execute("""create table if not exists schedule(
    # id_schedule serial primary key,
    # day varchar(10) not null,
    # dep_time time not null,
    # arr_time time not null,
    # id_kapal varchar(10) not null,
    # id_kelas int not null,
    # constraint fk_kapal foreign key (id_kapal) references kapal(id_kapal),
    # constraint fk_kelas foreign key (id_kelas) references kelas(id_kelas)
    # );""")



    # cur.execute('''insert into schedule (day,dep_time,arr_time,id_kapal,id_kelas) values ('Senin','08:00:00','10:00:00','kpl-001',1)''')

    # cur.execute('select * from kapal')
    #
    # c = cur.fetchall()
    # for i in c:
    #     print(i)

#     cur.execute("""INSERT INTO kapal (nama_kapal, tujuan, kapasitas)
# VALUES ('Kamikaze','Surabaya','800'),
# ('Utopia','Madura','1100'),
# ('Andromeda', 'Bandung', 1200),
# ('Laut Bahari', 'Semarang', 1000),
# ('Nusantara', 'Paciran', 1800),
# ('Timur Sejahtera', 'Tegal', 800),
# ('North Quay', 'Cirebon', 900),
# ('Lautan Indah', 'Jakarta', 2200),
# ('Budiono Siregar', 'Gresik', 1400),
# ('Ferrydom', 'Semarang', 1100),
# ('Laut Cakrawala', 'Yogyakarta', 950),
# ('Wisata Bahari', 'Banten', 1300);
# """)

#     cur.execute("""ALTER TABLE schedule DROP CONSTRAINT fk_kapal;""")
#     cur.execute("""ALTER TABLE schedule
# ADD CONSTRAINT fk_kapal
# FOREIGN KEY (id_kapal) REFERENCES kapal (id_kapal) ON UPDATE CASCADE;""")

    # cur.execute("""TRUNCATE TABLE schedule RESTART IDENTITY CASCADE;""")
    # queries = [
    #     # Senin
    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Senin', '08:00:00', '12:00:00', 'kpl-001', '1'),
    #     ('Senin', '13:00:00', '17:00:00', 'kpl-002', '2'),
    #     ('Senin', '17:00:00', '21:00:00', 'kpl-003', '1'),
    #     ('Senin', '21:00:00', '01:00:00', 'kpl-004', '2');""",
    #
    #     # Selasa
    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Selasa', '08:00:00', '12:00:00', 'kpl-005', '1'),
    #     ('Selasa', '13:00:00', '17:00:00', 'kpl-006', '2'),
    #     ('Selasa', '17:00:00', '21:00:00', 'kpl-007', '1'),
    #     ('Selasa', '21:00:00', '01:00:00', 'kpl-008', '2');""",
    #
    #     # Rabu
    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Rabu', '08:00:00', '12:00:00', 'kpl-009', '1'),
    #     ('Rabu', '13:00:00', '17:00:00', 'kpl-010', '2'),
    #     ('Rabu', '17:00:00', '21:00:00', 'kpl-011', '1'),
    #     ('Rabu', '21:00:00', '01:00:00', 'kpl-012', '2');""",
    #
    #     # Thursday

    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Thursday', '08:00:00', '12:00:00', 'kpl-001', '1'),
    #     ('Thursday', '13:00:00', '17:00:00', 'kpl-002', '2'),
    #     ('Thursday', '17:00:00', '21:00:00', 'kpl-003', '1'),
    #     ('Thursday', '21:00:00', '01:00:00', 'kpl-004', '2');""",
    #
    #     # Friday

    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Friday', '08:00:00', '12:00:00', 'kpl-005', '1'),
    #     ('Friday', '13:00:00', '17:00:00', 'kpl-006', '2'),
    #     ('Friday', '17:00:00', '21:00:00', 'kpl-007', '1'),
    #     ('Friday', '21:00:00', '01:00:00', 'kpl-008', '2');""",
    #
    #     # Saturday

    #     """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Saturday', '08:00:00', '12:00:00', 'kpl-009', '1'),
    #     ('Saturday', '13:00:00', '17:00:00', 'kpl-010', '2'),
    #     ('Saturday', '17:00:00', '21:00:00', 'kpl-011', '1'),
    #     ('Saturday', '21:00:00', '01:00:00', 'kpl-012', '2');"""
    # ]

#     cur.execute("""ALTER TABLE pelanggan ALTER COLUMN status SET DEFAULT 0;
# """)

    # cur.execute("""
    # alter table pelanggan alter column nik type VARCHAR(50);
    # """)
    # query = """
    # INSERT INTO pelanggan (username, password, fullname, email, phone_number, birthdate, nik)
    # VALUES
    # ('andiwijaya95', 'pass1234', 'Andi Wijaya', 'andi.wijaya@example.com', '081234567890', '1995-01-15', '1234567890123456'),
    # ('budi_santoso', 'pass1234', 'Budi Santoso', 'budi.santoso@example.com', '081234567891', '1992-02-20', '2234567890123456'),
    # ('citra.d', 'pass1234', 'Citra Dewi', 'citra.dewi@example.com', '081234567892', '1990-03-10', '3234567890123456'),
    # ('dewianggra98', 'pass1234', 'Dewi Anggraini', 'dewi.anggraini@example.com', '081234567893', '1998-04-25', '4234567890123456'),
    # ('ekapratama94', 'pass1234', 'Eka Pratama', 'eka.pratama@example.com', '081234567894', '1994-05-30', '5234567890123456'),
    # ('fikri_hsn', 'pass1234', 'Fikri Hasan', 'fikri.hasan@example.com', '081234567895', '1996-06-18', '6234567890123456'),
    # ('gitapus91', 'pass1234', 'Gita Puspita', 'gita.puspita@example.com', '081234567896', '1991-07-22', '7234567890123456'),
    # ('hadikur_93', 'pass1234', 'Hadi Kurnia', 'hadi.kurnia@example.com', '081234567897', '1993-08-14', '8234567890123456'),
    # ('indahlestari', 'pass1234', 'Indah Lestari', 'indah.lestari@example.com', '081234567898', '1989-09-05', '9234567890123456'),
    # ('jokoryadi88', 'pass1234', 'Joko Riyadi', 'joko.riyadi@example.com', '081234567899', '1988-10-11', '1034567890123456'),
    # ('putra_kwn95', 'pass1234', 'Kurniawan Putra', 'kurniawan.putra@example.com', '081234567900', '1995-11-19', '1134567890123456'),
    # ('lestari_dew97', 'pass1234', 'Lestari Dewi', 'lestari.dewi@example.com', '081234567901', '1997-12-24', '1234567891123456'),
    # ('maya_sari92', 'pass1234', 'Maya Sari', 'maya.sari@example.com', '081234567902', '1992-01-06', '1334567890123456'),
    # ('nurul_huda90', 'pass1234', 'Nurul Huda', 'nurul.huda@example.com', '081234567903', '1990-02-14', '1434567890123456'),
    # ('oki_prasetya87', 'pass1234', 'Oki Prasetya', 'oki.prasetya@example.com', '081234567904', '1987-03-22', '1534567890123456'),
    # ('pandu_s89', 'pass1234', 'Pandu Setiawan', 'pandu.setiawan@example.com', '081234567905', '1989-04-13', '1634567890123456'),
    # ('rina_sftr96', 'pass1234', 'Rina Safitri', 'rina.safitri@example.com', '081234567906', '1996-05-25', '1734567890123456'),
    # ('siti.aminah94', 'pass1234', 'Siti Aminah', 'siti.aminah@example.com', '081234567907', '1994-06-17', '1834567890123456'),
    # ('taufik_hdy93', 'pass1234', 'Taufik Hidayat', 'taufik.hidayat@example.com', '081234567908', '1993-07-30', '1934567890123456'),
    # ('usman_halim91', 'pass1234', 'Usman Halim', 'usman.halim@example.com', '081234567909', '1991-08-15', '2034567890123456');
    # """
    # cur.execute("select tujuan from kapal")
    # tujuan = [row[0] for row in cur.fetchall()]
    # print(tujuan)
    # cur.execute("truncate table kelas restart identity cascade")
    # cur.execute("alter table kelas add column cabin varchar(50) not null")
    # cur.execute("""insert into kelas (jenis_kelas,cabin) values ('ekonomi','A1');""")
    # cur.execute("""insert into kelas (jenis_kelas,cabin) values ('bisnis','A2');""")
    # cur.execute("""insert into kelas (jenis_kelas,cabin) values ('First Class','A3');""")

    # queries = [
    #     # Senin
    # cur.execute("""INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Monday', '08:00:00', '15:00:00', 'kpl-001', '3'),
    #     ('Monday', '13:00:00', '17:00:00', 'kpl-002', '2'),
    #     ('Monday', '17:00:00', '21:00:00', 'kpl-003', '1'),
    #     ('Monday', '21:00:00', '01:00:00', 'kpl-004', '1');""")
    #
    #     # Selasa
    # cur.execute("""INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Tuesday', '08:00:00', '12:00:00', 'kpl-005', '2'),
    #     ('Tuesday', '13:00:00', '17:00:00', 'kpl-006', '1'),
    #     ('Tuesday', '17:00:00', '21:00:00', 'kpl-007', '2'),
    #     ('Tuesday', '21:00:00', '01:00:00', 'kpl-008', '3');""")
    #
    #     # Rabu
    # cur.execute("""INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
    #     VALUES
    #     ('Wednesday', '08:00:00', '12:00:00', 'kpl-009', '3'),
    #     ('Wednesday', '13:00:00', '17:00:00', 'kpl-010', '2'),
    #     ('Wednesday', '17:00:00', '02:00:00', 'kpl-011', '3'),
    #     ('Wednesday', '21:00:00', '01:00:00', 'kpl-012', '1');""")
    #
    queries = [

        """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
        VALUES
        ('Thursday
', '08:00:00', '12:00:00', 'kpl-001', '3'),
        ('Thursday
', '13:00:00', '17:00:00', 'kpl-002', '2'),
        ('Thursday
', '17:00:00', '21:00:00', 'kpl-003', '1'),
        ('Thursday
', '21:00:00', '01:00:00', 'kpl-004', '1');""",

        # Friday

        """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
        VALUES
        ('Friday
', '08:00:00', '12:00:00', 'kpl-005', '3'),
        ('Friday
', '13:00:00', '17:00:00', 'kpl-006', '2'),
        ('Friday
', '17:00:00', '21:00:00', 'kpl-007', '1'),
        ('Friday
', '21:00:00', '01:00:00', 'kpl-008', '3');""",

        # Saturday

        """INSERT INTO schedule (day, dep_time, arr_time, id_kapal, id_kelas)
        VALUES
        ('Saturday
', '08:00:00', '12:00:00', 'kpl-009', '3'),
        ('Saturday
', '13:00:00', '17:00:00', 'kpl-010', '2'),
        ('Saturday
', '17:00:00', '21:00:00', 'kpl-011', '3'),
        ('Saturday
', '21:00:00', '01:00:00', 'kpl-012', '1');"""
    ]
    def get_rute():

        from datetime import datetime
        # Mengambil tujuan dan tanggal dari input pengguna
        tujuan = "Semarang"
        date = "2024-12-16"
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        day_name = date_obj.strftime("%A")
        print(day_name)

        find_rute = "SELECT id_kapal FROM kapal WHERE tujuan = %s"
        cur.execute(find_rute, (tujuan,))
        kapal_ids = cur.fetchall()
        print(kapal_ids)

        if not kapal_ids:
            print("Tidak ada kapal yang ditemukan untuk tujuan ini.")
            return

        sch = []
        find_schedule = "SELECT * FROM schedule WHERE id_kapal = %s and day= %s"
        for kapal_id in kapal_ids:
            cur.execute(find_schedule, (kapal_id[0],day_name))
            sch.extend(cur.fetchall())
        if not sch:
            print("Tidak ada jadwal ditemukan.")
        else:
            for schedule in sch:
                print(schedule)

    get_rute()
    # for i in queries:
    #     cur.execute(i)
    connection.commit()
    print("done.")
    cur.close()
    connection.close()


except psycopg2.Error as e:
    print(f"Error: {e}")
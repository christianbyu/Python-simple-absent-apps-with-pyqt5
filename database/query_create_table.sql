-- sqlite3 db_absen.db;

CREATE TABLE db_user (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Nama TEXT NOT NULL,
Email TEXT NOT NULL,
Username TEXT NOT NULL,
Passwd TEXT NOT NULL
);

--- Create Admin user Manually
INSERT INTO db_user (ID, Nama, Email, Username, Passwd) VALUES (1, 'Admin', 'Admin@google.com', 'Admin', 'Admin');

--- Query for
CREATE TABLE db_absen_masuk (
Nama TEXT NOT NULL,
Tanggal TEXT NOT NULL,
Waktu TEXT NOT NULL
);

CREATE TABLE db_absen_keluar (
Nama TEXT NOT NULL,
Tanggal TEXT NOT NULL,
Waktu TEXT NOT NULL
);

--- INSERT INTO db_absen_masuk (Nama, Tanggal, Waktu) VALUES ('Bayu', '{datetime(now)}', '{datetime(now)}');
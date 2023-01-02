--- Create Database db_absen.db
--- sqlite3 db_absen.db; 

CREATE TABLE db_user (
Nama TEXT NOT NULL,
Email TEXT NOT NULL,
Passwd TEXT NOT NULL
);

--- Create Admin user Manually
INSERT INTO db_user (Nama, Email, Passwd) VALUES ('Admin', 'Admin@google.com', 'Admin');

--- Query for Create table db_absen_masuk
CREATE TABLE db_absen_masuk (
Nama TEXT NOT NULL,
Tanggal TEXT NOT NULL,
Waktu TEXT NOT NULL
);

--- Query for Create table db_absen_keluar
CREATE TABLE db_absen_keluar (
Nama TEXT NOT NULL,
Tanggal TEXT NOT NULL,
Waktu TEXT NOT NULL
);
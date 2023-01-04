import sys
import tkinter
import sqlite3
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

# Fungsi Pada Form login.ui
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("./assets/login_baru.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        # Apabila email dan password kosong atau NULL
        if email=='' or password=='':
            print("Email dan Password tidak boleh Kosong!!!")
        else:
        # Open database
            conn = sqlite3.connect('./database/db_absen.db')
            print("Berhasil terkoneksi ke DB")
        # Select query
            cursor = conn.execute('SELECT * from db_user where Email="%s" and Passwd="%s"'%(email,password))
        # Fetch data 
            if cursor.fetchone():
                print("Login Berhasil!!")
                pilih=Pilihan() 
                widget.addWidget(pilih)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print("Email dan Password Salah!!!")

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada pilihan.ui
class Pilihan(QDialog):
    def __init__(self):
        super(Pilihan,self).__init__()
        loadUi("./assets/pilihan.ui",self)
        self.AbsenMasuk.clicked.connect(self.Masuk)
        self.AbsenKeluar.clicked.connect(self.Keluar)
        self.ListAbsenMasuk.clicked.connect(self.ListMasuk)
        self.ListAbsenKeluar.clicked.connect(self.Keluar)

    def Masuk(self):
        masuk=Masuk() 
        widget.addWidget(masuk)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ListMasuk(self):
        listmasuk=Masuk() 
        widget.addWidget(listmasuk)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        isidata=self.isidata.text()
        # Open database
        conn = sqlite3.connect('./database/db_absen.db')
        print("Berhasil terkoneksi ke DB")
        # Select query
        cursor = conn.execute('SELECT * from db_absen_masuk',(isidata))
        # Fetch data 

    def Keluar(self):
        keluar=Keluar() 
        widget.addWidget(keluar)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada masuk.ui
class Masuk(QDialog):
    def __init__(self):
        super(Masuk,self).__init__()
        loadUi("./assets/masuk.ui",self)
        self.MKembali.clicked.connect(self.Back)
        self.MSubmit.clicked.connect(self.Submit)
    
    def Back(self):
        back=Pilihan() 
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Submit(self):
        nama=self.nama.text()
        tanggal=self.tanggal.text()
        waktu=self.waktu.text()
        # Apabila email dan password kosong atau NULL
        if nama=='' or tanggal=='' or waktu=='':
            print("Data tidak boleh Kosong!!!")
        else:
        # Open database
            conn = sqlite3.connect('./database/db_absen.db')
            print("Berhasil terkoneksi ke DB")
        # Insert query
        query = "INSERT INTO db_absen_masuk (Nama, Tanggal, Waktu) VALUES ('"+nama+"', '"+tanggal+"', '"+waktu+"')"
        cursor = conn.execute(query)
        conn.commit()
        # Fetch data 
        if cursor.fetchone():
            print("Absensi Gagal!!!")
        else:
            print("Absensi Berhasil!!!")
            submit=Result() 
            widget.addWidget(submit)
            widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada keluar.ui
class Keluar(QDialog):
    def __init__(self):
        super(Keluar,self).__init__()
        loadUi("./assets/keluar.ui",self)
        self.KKembali.clicked.connect(self.Back)
        self.KSubmit.clicked.connect(self.Submit)

    def Back(self):
        back=Pilihan() 
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Submit(self):
        nama=self.nama.text()
        tanggal=self.tanggal.text()
        waktu=self.waktu.text()
        # Apabila email dan password kosong atau NULL
        if nama=='' or tanggal=='' or waktu=='':
            print("Data tidak boleh Kosong!!!")
        else:
        # Open database
            conn = sqlite3.connect('./database/db_absen.db')
            print("Berhasil terkoneksi ke DB")
        # Insert query
        query = "INSERT INTO db_absen_keluar (Nama, Tanggal, Waktu) VALUES ('"+nama+"', '"+tanggal+"', '"+waktu+"')"
        cursor = conn.execute(query)
        conn.commit()
        # Fetch data 
        if cursor.fetchone():
            print("Absensi Gagal!!!")
        else:
            print("Absensi Berhasil!!!")
            submit=Result() 
            widget.addWidget(submit)
            widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada result.ui
class Result(QDialog):
    def __init__(self):
        super(Result,self).__init__()
        loadUi("./assets/result.ui",self)
        self.KembaliLogin.clicked.connect(self.BackLogin)
    
    def BackLogin(self):
        backlogin=Login() 
        widget.addWidget(backlogin)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada createacc.ui
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("./assets/createacc_baru.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.KKembali.clicked.connect(self.BackLogin)
        self.passwrd.setEchoMode(QtWidgets.QLineEdit.Password)

    def BackLogin(self):
        backlogin=Login() 
        widget.addWidget(backlogin)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def createaccfunction(self):
        nama=self.nama.text()
        email=self.email.text()
        passwrd=self.passwrd.text()
        # Apabila email dan password kosong atau NULL
        if nama=='' or email=='' or passwrd=='':
            print("Data tidak boleh Kosong!!!")
        else:
        # Open database
            conn = sqlite3.connect('./database/db_absen.db')
            print("Berhasil terkoneksi ke DB")
        # Insert query
        query = "INSERT INTO db_user(Nama, Email, Passwd) VALUES ('"+nama+"', '"+email+"', '"+passwrd+"')"
        cursor = conn.execute(query)
        conn.commit()
        # Fetch data 
        if cursor.fetchone():
            print("Sign Up Gagal!!!")
        else:
            print("Sign Up Berhasil!!!")
            login=Login() 
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
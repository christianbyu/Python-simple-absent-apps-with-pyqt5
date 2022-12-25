import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

# Fungsi Pada Form login.ui
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login_baru.ui",self)
        self.loginbutton.clicked.connect(self.pilihan)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)
    
    def pilihan(self):
        pilih=Pilihan() 
        widget.addWidget(pilih)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada pilihan.ui
class Pilihan(QDialog):
    def __init__(self):
        super(Pilihan,self).__init__()
        loadUi("pilihan.ui",self)
        self.AbsenMasuk.clicked.connect(self.Masuk)
        self.AbsenKeluar.clicked.connect(self.Keluar)

    def Masuk(self):
        masuk=Masuk() 
        widget.addWidget(masuk)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Keluar(self):
        keluar=Keluar() 
        widget.addWidget(keluar)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada masuk.ui
class Masuk(QDialog):
    def __init__(self):
        super(Masuk,self).__init__()
        loadUi("masuk.ui",self)
        self.MKembali.clicked.connect(self.Back)
        self.MSubmit.clicked.connect(self.Submit)
    
    def Back(self):
        back=Pilihan() 
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Submit(self):
        submit=Result() 
        widget.addWidget(submit)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada keluar.ui
class Keluar(QDialog):
    def __init__(self):
        super(Keluar,self).__init__()
        loadUi("keluar.ui",self)
        self.KKembali.clicked.connect(self.Back)
        self.KSubmit.clicked.connect(self.Submit)

    def Back(self):
        back=Pilihan() 
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Submit(self):
        submit=Result() 
        widget.addWidget(submit)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada result.ui
class Result(QDialog):
    def __init__(self):
        super(Result,self).__init__()
        loadUi("result.ui",self)
        self.KembaliLogin.clicked.connect(self.BackLogin)
    
    def BackLogin(self):
        backlogin=Login() 
        widget.addWidget(backlogin)
        widget.setCurrentIndex(widget.currentIndex()+1)

# Fungsi pada createacc.ui
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc_baru.ui",self)
        self.signupbutton.clicked.connect(self.crseateaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
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
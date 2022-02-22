import sys, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from db_control import *
from design_autorization import *

base = sqlite3.connect('users.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS {}(name, password)'.format('users'))
base.commit()
cur.execute('INSERT INTO users VALUES(?, ?)', ('viktor', '123456'))
base.commit()


class Sign_app(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        self.ui.btn_registration.clicked.connect(self.reg)
        self.ui.btn_sign.clicked.connect(self.sign)
        self.base_line_edit = [self.ui.lineEdit_login, self.ui.lineEdit_password]
        
        self.db_control = CheckThread()
        self.db_control.mysignal.connect(self.signal_handler)
        
    def signal_handler(self, value):
            QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper
        
    @check_input
    def sign(self):
        name = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        self.db_control.thr_login(name, password)


    @check_input
    def reg(self):
        name = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        self.db_control.thr_register(name, password)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Sign_app()
    mywin.show()
    sys.exit(app.exec_())


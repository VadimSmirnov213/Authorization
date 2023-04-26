import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
import sqlite3
f = open("addres.txt", 'w')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 499)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 280, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #7d7a7a;\n"
                                      "    border: 2px solid #fc8383;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"                    
                                      "QPushButton::hover{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #fc8383;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #ff4545;\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: white;\n"
                                    "color: black;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: white;\n"
                                      "color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 370, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #7d7a7a;\n"
                                        "    border: 2px solid #fc8383;\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #fc8383;\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "    border-radius: 6px;\n"
                                        "    background-color: #ff4545;\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "pushButton"))
        self.label.setText(_translate("MainWindow", "label"))
        self.label_2.setText(_translate("MainWindow", "label_2"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "lineEdit"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "lineEdit_2"))
        self.pushButton_2.setText(_translate("MainWindow", "pushButton_2"))
        
        
db = sqlite3.connect('base.sqlite')
cursor = db.cursor()
db.commit()


class Registration(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Регистрация')
        self.lineEdit.setPlaceholderText('Введите Логин')
        self.lineEdit_2.setPlaceholderText('Введите Пароль')
        self.pushButton.setText('Регистрация')
        self.pushButton_2.setText('Вход')
        self.setWindowTitle('Регистрация')
        self.pushButton.pressed.connect(self.reg)
        self.pushButton_2.pressed.connect(self.login)
        
    def login(self):
        self.login = Login()
        self.login.show()
        self.hide()

    def reg(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        if len(user_password) < 8 or '123' in user_password or 'qwe' in user_password or '...' in user_password:
            self.label.setText(f'Пароль сишком простой')
        else:
            user_password = hashlib.sha3_512(user_password.encode()).hexdigest()
            if len(user_login) == 0:
                return
            if len(user_password) == 0:
                return
            cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO users(login, password) VALUES ("{user_login}", "{user_password}")')
                self.label.setText(f'Аккаунт {user_login} успешно зарегистрирован!')
                db.commit()
            else:
                self.label.setText('Такая записать уже имеется!')


class Login(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Логин')
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton.setText('Вход')
        self.pushButton_2.setText('Регистрация')
        self.setWindowTitle('Вход')
        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)

    def reg(self):
        self.reg = Registration()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()
        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()
        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            self.label.setText('Успешная авторизация!')
            f.write(user_login)
            f.close()
        else:
            self.label.setText('Ошибка авторизации!')


App = QtWidgets.QApplication([])
window = Login()
window.show()
App.exec()







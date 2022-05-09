from PyQt5 import QtCore,QtWidgets

class RegisterWindow():
    def setup(self,registerWindow):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(624,511)
        self.centralwidget = QtWidgets.QWidget(registerWindow)
        self.UserPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.UserPhone.setGeometry(QtCore.QRect(240, 100, 200, 50))
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(240, 160, 200, 50))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 110, 200, 30))
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, 170, 200, 30))
        self.buttonRegister = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRegister.setGeometry(QtCore.QRect(200, 250, 100, 60))
        self.buttonlogin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlogin.setGeometry(QtCore.QRect(330, 250, 100, 60))

        registerWindow.setCentralWidget(self.centralwidget)
        self.Register_retranslate(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)
    def Register_retranslate(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "登录界面"))
        self.label1.setText(_translate("registerWindow", "手机号码："))
        self.label2.setText(_translate("registerWindow", "密码："))
        self.buttonRegister.setText(_translate("registerWindow","注册"))
        self.buttonlogin.setText(_translate("registerWindow","登录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerWindow = QtWidgets.QMainWindow()
    ui = RegisterWindow()
    ui.setup(registerWindow)
    registerWindow.show()
    sys.exit(app.exec_())

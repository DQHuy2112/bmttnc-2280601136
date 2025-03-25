# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 737)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(380, 60, 161, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 350, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(500, 140, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(510, 350, 81, 31))
        self.label_5.setObjectName("label_5")
        self.btn_gen_keys = QtWidgets.QPushButton(MainWindow)
        self.btn_gen_keys.setGeometry(QtCore.QRect(600, 70, 93, 28))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.btn_encrypt = QtWidgets.QPushButton(MainWindow)
        self.btn_encrypt.setGeometry(QtCore.QRect(150, 520, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(MainWindow)
        self.btn_decrypt.setGeometry(QtCore.QRect(400, 520, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(MainWindow)
        self.btn_sign.setGeometry(QtCore.QRect(600, 520, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(MainWindow)
        self.btn_verify.setGeometry(QtCore.QRect(850, 520, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        self.txt_plain_text = QtWidgets.QPlainTextEdit(MainWindow)
        self.txt_plain_text.setGeometry(QtCore.QRect(150, 140, 341, 131))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_info = QtWidgets.QPlainTextEdit(MainWindow)
        self.txt_info.setGeometry(QtCore.QRect(600, 140, 341, 131))
        self.txt_info.setObjectName("txt_info")
        self.txt_sign = QtWidgets.QPlainTextEdit(MainWindow)
        self.txt_sign.setGeometry(QtCore.QRect(600, 350, 341, 131))
        self.txt_sign.setObjectName("txt_sign")
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(MainWindow)
        self.txt_cipher_text.setGeometry(QtCore.QRect(150, 350, 341, 131))
        self.txt_cipher_text.setObjectName("txt_cipher_text")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">RSA CIPHER</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Plain Text</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Cipher Text</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Information</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Signature</span></p></body></html>"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creating_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 577)
        MainWindow.setMinimumSize(QtCore.QSize(388, 542))
        MainWindow.setMaximumSize(QtCore.QSize(450, 600))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #FFFAFA;\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 140, 291, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D3D3D3;;\n"
"    border-radius: 10px; /* Задайте радиус, чтобы сделать форму овальной */\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    qproperty-alignment: \'AlignCenter\'; /* выравнивание по центру */\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 220, 291, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D3D3D3;;\n"
"    border-radius: 10px; /* Задайте радиус, чтобы сделать форму овальной */\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    qproperty-alignment: \'AlignCenter\'; /* выравнивание по центру */\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 300, 271, 171))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 2px solid #D3D3D3;;\n"
"    border-radius: 10px; /* Задайте радиус, чтобы сделать форму овальной */\n"
"\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;    \n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    text-align: center; /* выравнивание по центру */\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 500, 200, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 20px;\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #00CED1;\n"
"    border-radius: 12px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #FFFAFA; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #48D1CC;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 70, 291, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #D3D3D3;;\n"
"    border-radius: 10px; /* Задайте радиус, чтобы сделать форму овальной */\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    qproperty-alignment: \'AlignCenter\'; /* выравнивание по центру */\n"
"}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 201, 16))
        self.label.setStyleSheet("QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    border: None;\n"
"    \n"
"}")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 201, 16))
        self.label_2.setStyleSheet("QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    border: None;\n"
"    \n"
"}")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 201, 16))
        self.label_3.setStyleSheet("QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    border: None;\n"
"    \n"
"}")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 20, 22, 21))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */    \n"
"    border-radius: 10px; /* задайте радиус, чтобы сделать кнопку круглой */\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    font-family: Arial;\n"
"    font-size: 10px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    font-family: Arial;\n"
"    font-size: 10px;\n"
"    background-color: #F0F8FF; /* цвет кнопки */\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #DCDCDC;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 260, 231, 23))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"       background-color: transparent;\n"
"       border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    font-family: Arial;\n"
"    font-size: 13px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"    text-decoration: underline;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(209, 190, 131, 16))
        self.pushButton_2.setToolTipDuration(1000000000)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"       background-color: transparent;\n"
"       border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"    text-decoration: underline;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Сервис:</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Логин:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Пароль:</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_7.setText(_translate("MainWindow", "Использовать генератор паролей"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Пароль должен содержать:</span></p><p><span style=\" font-size:9pt;\">1. Минимум 8 символов;</span></p><p><span style=\" font-size:9pt;\">2. Минимум 1 заглавную букву (A- Z);</span></p><p><span style=\" font-size:9pt;\">3. Минимум 1 строчную букву (a- z);</span></p><p><span style=\" font-size:9pt;\">4. Минимум 1 специальный символ (!@#$%^&amp;*()_+{}\\[]:;&lt;&gt;,.?~)</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Требования к паролю"))

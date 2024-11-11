# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(388, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(388, 500))
        MainWindow.setMaximumSize(QtCore.QSize(388, 500))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #FFFAFA;\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 400, 211, 41))
        self.pushButton_2.setMinimumSize(QtCore.QSize(84, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 190, 311, 131))
        self.label.setStyleSheet("QLabel {\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080;\n"
"    border: None;\n"
"    qproperty-text: \"<html><head/><body><p>Для подтверждения вашей учетной записи, введите ваш действующий адрес электронной почты. Мы отправим вам уведомление и инструкции по завершению регистрации. Ваши личные данные будут храниться в безопасности и использоваться только в соответствии с политикой конфиден- циальности.</p></body></html>\";\n"
"}")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 20, 22, 21))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 20, 22, 21))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */    \n"
"    border-radius: 10px; /* задайте радиус, чтобы сделать кнопку круглой */\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    font-family: Arial;\n"
"    font-size: 10px;\n"
"\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 131, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Managerio"))
        self.pushButton_2.setText(_translate("MainWindow", "Log in"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Для подтверждения вашей учетной записи, введите ваш действующий адрес электронной почты. Мы отправим вам уведомление и инструкции по завершению регистрации. Ваши личные данные будут храниться в безопасности и использоваться только в соответствии с политикой конфиден- циальности.</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "—"))
        self.pushButton.setText(_translate("MainWindow", "< Вернуться назад"))

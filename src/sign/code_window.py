# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 303)
        MainWindow.setMinimumSize(QtCore.QSize(354, 303))
        MainWindow.setMaximumSize(QtCore.QSize(354, 303))
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
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 131, 41))
        self.pushButton_2.setMinimumSize(QtCore.QSize(84, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 20px;\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #00CED1;\n"
"    border-radius: 12px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"\n"
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
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 181, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 240, 131, 41))
        self.pushButton_3.setMinimumSize(QtCore.QSize(84, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 20px;\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #00CED1;\n"
"    border-radius: 12px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #FFFAFA; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #48D1CC;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 200, 121, 21))
        self.label.setStyleSheet("QLabel{\n"
"    border: None\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 291, 101))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    border: none;\n"
"    font-family: Arial;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"    color: #808080;\n"
"    text-align: Center;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.pushButton_3.setText(_translate("MainWindow", "Отмена"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))

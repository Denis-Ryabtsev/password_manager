# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rule_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 500)
        MainWindow.setMinimumSize(QtCore.QSize(388, 500))
        MainWindow.setMaximumSize(QtCore.QSize(388, 500))
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #FFFAFA;\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 420, 200, 40))
        self.pushButton_2.setMinimumSize(QtCore.QSize(84, 40))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #D3D3D3; /* цвет обводки */\n"
"    border-radius: 20px;\n"
"    background-color: #FFFAFA; /* цвет кнопки */\n"
"    min-width: 80px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"    color: #E0FFFF;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #808080; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #00CED1;\n"
"    border-radius: 12px;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"    color: #E0FFFF;\n"
"    font-weight: normal; /* жирный или обычный */\n"
"    color: #FFFAFA; /* цветтекста кнопки */\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #48D1CC;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 50, 331, 321))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(331, 321))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(331, 321))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Понятно"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Пожалуйста, перед тем как продолжить, убедитесь в следующем:\n"
" \n"
"   1.  У   вас    должны    быть   установлены   драйвера на   используемые     видеокамеры.   Это    необходимо      для корректной  работы функции биометрического сравнения лица.\n"
"   \n"
"   2.  Не отключайте веб-камеру во время использования программы. В  случае  отключения   камеры  приложение может выйти из строя. Убедитесь, что  ваша веб-камера активна и работает исправно.\n"
"   \n"
"   3.  Если   вы   еще   не  подключили   нужные   камеры, сделайте это сейчас. Убедитесь, что  все  необходимые видеокамеры подключены к вашему устройству.\n"
"   \n"
"   4.  Для корректного выполнения съемки  изображения лица, следует соблюдать определенные параметры: \n"
"          а) Расположите лицо в пределах от 30 до 100 см от видеокамеры. \n"
"          б) Голова должна быть направлена в  сторону камеры для лучшего качества изображения. \n"
"          в) Подождите   появления   красного   квадрата   вокруг  лица  в  окне  приложения, затем  нажмите  на кнопку \"фото\", чтобы сделать снимок. "))

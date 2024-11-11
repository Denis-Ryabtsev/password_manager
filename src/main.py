import asyncio
import sys

from PyQt5 import QtWidgets

from sign.base_general import MainApp


# After tests need to return default state
         
#pyuic5 Main_window.ui -o Main_window.py


        # # email
        # self.pushButton_5.setEnabled(False)
        # self.pushButton_5.setVisible(False)
        # self.pushButton_6.setEnabled(False)
        # self.pushButton_6.setVisible(False)
        # self.lineEdit.setEnabled(False)
        # self.lineEdit.setVisible(False)
        # self.label_3.setEnabled(False)
        # self.label_3.setVisible(False)
        # # logpass
        # self.pushButton_7.setEnabled(False)
        # self.pushButton_7.setVisible(False)
        # self.pushButton_8.setEnabled(False)
        # self.pushButton_8.setVisible(False)
        # self.pushButton_9.setEnabled(False)
        # self.pushButton_9.setVisible(False)
        # self.label_4.setEnabled(False)
        # self.label_4.setVisible(False)
        # self.label_5.setEnabled(False)
        # self.label_5.setVisible(False)
        # self.label_6.setEnabled(False)
        # self.label_6.setVisible(False)
        # self.lineEdit_2.setEnabled(False)
        # self.lineEdit_2.setVisible(False)
        # self.lineEdit_3.setEnabled(False)
        # self.lineEdit_3.setVisible(False)
        # self.lineEdit_2.setEnabled(False)
        # self.lineEdit_2.setVisible(False)
        # self.checkBox.setVisible(False)
        # self.checkBox.setEnabled(False)
        # # recovery
        # self.pushButton_10.setEnabled(False)
        # self.pushButton_10.setVisible(False)
        # self.label_7.setEnabled(False)
        # self.label_7.setVisible(False)
        # self.label_8.setEnabled(False)
        # self.label_8.setVisible(False)
        # self.label_9.setEnabled(False)
        # self.label_9.setVisible(False)
        # self.lineEdit_5.setEnabled(False)
        # self.lineEdit_5.setVisible(False)
        # self.pushButton_11.setEnabled(False)
        # self.pushButton_11.setVisible(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    # запуск приложения
    app.exec_()

if __name__ == '__main__': 
    asyncio.run(main())
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from application import manager_window, generate_window, creating_window
from utils.generate_passwd import gen_passwd
from utils.operation import count_note, get_decrypt_serlog, make_note, \
                            remove_note, select_data, update_note
from utils.protect import password_complexity


class ManagerApp(QtWidgets.QMainWindow, manager_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.login = ""
        self.passwd = ""
        self.key = ''
        self.list_iv = []
        self.list_decrypt = []
        self.list_serlogpas = []
        self.connect = ""
        self.tableWidget.cellClicked.connect(self.expand_info)
        self.tableWidget.itemSelectionChanged.connect(self.display_info)
        self.pushButton.clicked.connect(self.create_note)
        self.pushButton_2.clicked.connect(self.update_note)
        self.pushButton_3.clicked.connect(self.delete_note)
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(self.close_window)
        self.pushButton_6.clicked.connect(self.export_csv)
        self.pushButton_7.clicked.connect(self.export_txt)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 160)
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setMouseTracking(True)

    def close_window(self: object) -> None:
        self.exit = []
        self.exit.links.append(self)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.exit.move(center_x - self.exit.width() // 2, 
                       center_y - self.exit.height() // 2)
        self.exit.show()

    def expand_info(self: object, row: int) -> None:
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                item.setSelected(True)

    async def display_info(self: object) -> None:
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            selected_row_data = [self.tableWidget.item(row, col).text() \
                                for col in range(self.tableWidget.columnCount())]
            resource = selected_row_data[1]
            log = selected_row_data[2]
            number = int(selected_row_data[0]) - 1
            temp = await select_data(self.login, self.passwd, resource, log, self.key,
                               self.list_iv[number][0], self.list_iv[number][1])
            self.textBrowser.setText\
            (f"<html><head/><body><p><span style='font-size: 13px;'><u>Сервис:"\
             f"</u></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{resource}"\
             f"<p><span style='font-size: 13px;'><u>Логин:</u></span> "\
             f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{log}</p>"\
             f"<p><span style='font-size: 13px;'><u>Пароль:</u>"\
             f"</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{temp[0]}</p>"\
             f"<center><span style='font-size: 13px;'><u>Описание</u>"\
             f"</center><p>{temp[1]}</h2></p></body></html>")
            
    async def delete_note(self: object) -> None:
        selected_items = self.tableWidget.selectedItems()
        if len(selected_items) > 0:
            number = int(selected_items[0].text()) - 1
            resource = selected_items[1].text()
            log = selected_items[2].text()
            await remove_note(self.login, self.passwd, resource,
                        log, self.key, self.list_iv[number][0])
            self.reload_table()
            self.textBrowser.clear()
        else:
            self.error = []
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Выделите строку, которую "\
                                           f"собираетесь удалить"\
                                           f"</center></h2></p></body></html>")
            self.error.show()

    async def update_note(self: object) -> None:
        selected_items = self.tableWidget.selectedItems()
        if len(selected_items) > 0:
            number = int(selected_items[0].text()) - 1
            resource = selected_items[1].text()
            log = selected_items[2].text()
            temp = await select_data(self.login, self.passwd, resource, log, self.key, 
                               self.list_iv[number][0], self.list_iv[number][1])
            self.creating = CreatingApp()
            self.creating.login = self.login
            self.creating.lineEdit_3.setReadOnly(True)
            self.creating.lineEdit.setReadOnly(True)
            self.creating.passwd = self.passwd
            self.creating.temp_res = resource
            self.creating.temp_log = log
            self.creating.key = self.key
            self.creating.check_list = self.list_decrypt
            self.creating.check_serlogpas = self.list_serlogpas
            self.creating.connect = self.connect
            self.creating.link.append(self)
            self.creating.iv_log = self.list_iv[number][0]
            self.creating.lineEdit_3.setText(resource)
            self.creating.lineEdit.setText(log)
            self.creating.pushButton.setText("Изменить")
            self.creating.lineEdit_2.setText(temp[0])
            self.creating.textEdit.setPlainText(temp[1])
            self.creating.show()
        else:
            self.error = []
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Выделите строку, которую "\
                                           f"собираетесь изменить"\
                                           f"</center></h2></p></body></html>")
            self.error.show()

    def create_note(self: object) -> None:
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.creating = CreatingApp()
        self.creating.login = self.login
        self.creating.passwd = self.passwd
        self.creating.key = self.key
        self.creating.check_list = self.list_decrypt
        self.creating.check_serlogpas = self.list_serlogpas
        self.creating.connect = self.connect
        self.creating.link.append(self)
        self.creating.move(center_x - self.creating.width() // 2, 
                           center_y - self.creating.height() // 2)
        self.creating.show()
        self.reload_table()

    async def reload_table(self: object) -> None:
        notes, self.list_iv = await count_note(self.login, self.passwd, self.key)
        self.list_decrypt, self.list_serlogpas = await get_decrypt_serlog(self.login, 
                                                                    self.passwd, 
                                                                    self.key)
        if notes != False:
            self.tableWidget.setRowCount(len(notes))
            for i in range(0, len(notes)):
                temp = notes[i]
                number = QTableWidgetItem(str(i + 1))
                service = QTableWidgetItem(temp[0])
                log = QTableWidgetItem(temp[1])
                self.tableWidget.setItem(i, 0, number)
                self.tableWidget.setItem(i, 1, service)
                self.tableWidget.setItem(i, 2, log)
                number.setTextAlignment(Qt.AlignCenter)
                service.setTextAlignment(Qt.AlignCenter)
                log.setTextAlignment(Qt.AlignCenter)
                if i % 2 == 0:
                    for col in range(self.tableWidget.columnCount()):
                        self.tableWidget.item(i, col).setBackground(QColor("#F0F0F0"))
        else:
            self.tableWidget.clear()

    def mousePressEvent(self: object, event) -> None:
        # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class CreatingApp(QtWidgets.QMainWindow, creating_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.login = ""
        self.passwd = ""
        self.key = ""
        self.check_list = []
        self.check_serlogpas = []
        self.link = []
        self.gen_passwd = ""
        self.iv_log = ""
        self.old_passwd = ""
        self.connect = ""
        self.temp_res = self.lineEdit_3.text()
        self.temp_log = self.lineEdit.text()
        self.lineEdit.textChanged.connect(self.check_limit)
        self.lineEdit_2.textChanged.connect(self.check_limit)
        self.lineEdit_3.textChanged.connect(self.check_limit)
        self.textEdit.textChanged.connect(self.check_limit)
        self.pushButton.clicked.connect(self.add_note)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.generate_passwd)
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setMouseTracking(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setTabOrder(self.lineEdit_3, self.lineEdit)
        self.setTabOrder(self.lineEdit, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.textEdit)

    def check_limit(self: object) -> None:
        if len(self.lineEdit.text()) >= 50:
            self.lineEdit.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)
        if len(self.lineEdit_2.text()) >= 50:
            self.lineEdit_2.setEnabled(False)
        else:
            self.lineEdit_2.setEnabled(True)
        if len(self.lineEdit_3.text()) >= 50:
            self.lineEdit_3.setEnabled(False)
        else:
            self.lineEdit_3.setEnabled(True)
        if len(self.textEdit.toPlainText()) >= 200:
            self.textEdit.setEnabled(False)
        else:
            self.textEdit.setEnabled(True)

    async def add_note(self: object) -> None:
        service = self.lineEdit_3.text()
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        description = self.textEdit.toPlainText()
        if not service or not login or not password:
            self.error = []
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Поля 'сервис', 'логин' и 'пароль' "\
                                           f"должны быть обязательно заполнены"\
                                           f"</center></h2> </p></body></html>")
            self.error.show()
        if password_complexity(password):
            if ([service, login] in self.check_list):
                if self.iv_log != "":
                    await update_note(self.login, self.passwd, service, login,
                                self.link[0].key, self.iv_log, password,
                                description)
                    self.close()
                    self.link[0].textBrowser.clear()
                    self.link[0].reload_table()
                else:
                    self.error = []
                    current_geometry = self.geometry()
                    center_x = current_geometry.x() + current_geometry.width() // 2
                    center_y = current_geometry.y() + current_geometry.height() // 2
                    self.error.move(center_x - self.error.width() // 2, 
                                center_y - self.error.height() // 2)
                    self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                                   f"Данная запись уже существует. "\
                                                   f"Для смены пароля выберите "\
                                                   f"требуемую строку и нажмите "\
                                                   f"кнопку 'Редактировать'"\
                                                   f"</center></h2></p></body></html>")
                    self.error.show()
            else:
                await make_note(self.key, self.login, self.passwd, 
                          service, login, password, description)
                self.close()
                self.link[0].textBrowser.clear()
                self.link[0].reload_table()
        else:
            self.error = []
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Введенный пароль должен "\
                                           f"соответствовать требованиям. "\
                                           f"Они указаны в окне создания записи"\
                                           f"</center></h2> </p></body></html>")
            self.error.show()

    def generate_passwd(self: object):
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.generate = GenerateApp()
        self.generate.link.append(self)
        self.generate.move(center_x - self.generate.width() // 2, 
                            center_y - self.generate.height() // 2)
        self.generate.show()
        

    def mousePressEvent(self: object, event) -> None:
        # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class GenerateApp(QtWidgets.QMainWindow, generate_window.Ui_MainWindow):
    
    def __init__(self: object):
        super().__init__()
        self.setupUi(self)
        self.link = []
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.create_passwd)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal) 
    
    def create_passwd(self: object):
        value = self.spinBox.value()
        if value <=7:
            self.error = []
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Длина пароля должна быть минимум "\
                                           f"8 символов.</center></h2>"\
                                           f"</p></body></html>")
            self.error.show()
        else:
            self.link[0].lineEdit_2.setText(gen_passwd(value))
            self.close()
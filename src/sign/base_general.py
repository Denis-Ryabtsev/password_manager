import os
import random
import smtplib
import string
from typing import Union

import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QLineEdit

from application.base_application import ManagerApp
from sign import face_window, progress_bar, rule_window, secret_window, \
                    captcha_window, code_window, error_window, exit_window, \
                    main_window, password_window, recover_window
from utils.control_photo import check_face_photo, check_photo, comparison_photo
from utils.operation import get_key, save_account, ban_record, change_passwd, \
                            check_ban, check_user, contains_sql_injection, \
                            create_session, email_data, email_deliver, \
                            export_photo, get_reckey, get_time, get_timeban, update_count
from utils.protect import generate_captcha, generate_key, check_internet, \
                            generate_captcha, generate_code, password_complexity


class MainApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        # вызов конструктора класса QT для инициализации элементов
        super().__init__()
        # инициализация дизайна
        self.setupUi(self)
        self.email = ""
        self.login = ""
        self.password = ""
        self.pushButton.clicked.connect(self.open_entry)
        self.pushButton_2.clicked.connect(self.open_email)
        self.pushButton_3.clicked.connect(self.close_window)
        self.pushButton_4.clicked.connect(self.showMinimized)
        # email
        self.pushButton_5.clicked.connect(self.open_main)
        self.pushButton_6.clicked.connect(self.message)
        # logpass
        self.pushButton_7.clicked.connect(self.main_log)
        self.pushButton_8.setEnabled(True)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.pushButton_8.clicked.connect(self.check_values)
        self.pushButton_9.clicked.connect(self.recovery_passwd)
        self.lineEdit_2.textChanged.connect(self.clear_input)
        self.lineEdit_3.textChanged.connect(self.clear_input)
        self.lineEdit_5.textChanged.connect(self.clear_recovery)
        self.pushButton_11.clicked.connect(self.rec_logpass)
        self.pushButton_10.clicked.connect(self.check_login)
        self.checkBox.stateChanged.connect(self.show_passwd)
        self.label_6.setStyleSheet("QLabel{\n"
                                   "font-family: Arial;\n"
                                   "font-size: 12px;\n"
                                   "font-weight: normal;\n"
                                   "color: #808080;\n"
                                   "border: None;\n}")
        self.email_object = [self.pushButton_5, self.pushButton_6, 
                             self.lineEdit, self.label_3]
        self.main_object = [self.pushButton, self.pushButton_2, 
                            self.label, self.label_2]
        self.logpass_object = [self.pushButton_7, self.pushButton_8,
                               self.label_4, self.label_5, self.label_6,
                               self.lineEdit_2, self.lineEdit_3, self.checkBox,
                               self.pushButton_9, self.lineEdit_2]
        self.recovery_object = [self.pushButton_10, self.label_7, self.label_8,
                                self.label_9, self.lineEdit_5, self.pushButton_11]
        self.domain = ("@bk.ru", "@mail.ru", "@gmail", "@outlook.com", 
                       "@yandex.ru", "@list.ru", "@inbox.ru")
        # удаление шапки
        self.setWindowFlags(Qt.FramelessWindowHint)
        # перемещение окна
        self.setMouseTracking(True)
    
    def recovery_passwd(self: object):
        for object in self.logpass_object:
            object.setEnabled(False)
            object.setVisible(False)
        self.label_4.setVisible(True)
        for element in self.recovery_object:
            element.setEnabled(True)
            element.setVisible(True)
    
    def show_passwd(self, state):
        if state == 2:
            self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_3.setEchoMode(QLineEdit.Password)

    async def check_login(self: object):
        email = self.lineEdit_5.text()
        if await check_user(email) and email[email.find("@"):] in self.domain and \
        not(contains_sql_injection(email)):
            self.recover = RecoverApp()
            self.recover.login = email
            self.recover.code_db = await get_reckey(self.recover.login)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.recover.move(center_x - self.recover.width() // 2, 
                            center_y - self.recover.height() // 2)
            self.recover.show()
        else:
            self.label_9.setText("Аккаунта с данным логином не существует")
            self.label_9.setStyleSheet("QLabel {\n"
                                     "font-family: Arial;\n"
                                     "font-size: 12px;\n"
                                     "font-weight: normal;\n"
                                     "color: #DC143C;\n"
                                     "border: None;\n}")
            self.lineEdit_5.setStyleSheet("QLineEdit {\n"
                                        "border: 2px solid #D3D3D3;\n"
                                        "border-radius: 10px;\n"
                                        "font-family: Arial;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: normal;\n"
                                        "color: #DC143C;\n"
                                        "border-color: #DC143C;\n"
                                        "qproperty-alignment: \'AlignCenter\';}")

    async def message(self: object) -> None: 
        self.email = self.lineEdit.text()
        if (contains_sql_injection(self.email)) or \
        not(self.email[self.email.find("@"):] in self.domain):
            self.error = ErrorApp()
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Введен некорректный адрес "\
                                           f"электронной почты</center>"\
                                           f"</h2> </p></body></html>")
            self.error.show()
        elif self.email[self.email.find("@"):] in self.domain \
            and not(await check_user(self.email)): 
            self.code = CodeApp()
            self.code.links.append(self)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.code.move(center_x - self.code.width() // 2, 
                           center_y - self.code.height() // 2) 
            self.code.email = self.email
            self.code.textBrowser.setText(f"<html><head/><body><p><center>"\
                    f"На почту {self.code.email} было вышлено письмо с" \
                    f"кодом подтверждения. Введите его в поле приложения для "\
                    f"продолжения этапа регистрации. В случае, если был указан "\
                    f"неверный адрес электронной почты, нажмите кнопку 'Отмена' "\
                    f"и повторите ввод.</center></h2> </p></body></html>") 
            self.code.code_gen = self.send_message()
            if self.code.code_gen:
                self.code.show()
            else:
                self.error = ErrorApp()
                self.error.links_log.append(self)
                current_geometry = self.geometry()
                center_x = current_geometry.x() + current_geometry.width() // 2
                center_y = current_geometry.y() + current_geometry.height() // 2
                self.error.move(center_x - self.error.width() // 2, 
                                center_y - self.error.height() // 2)
                self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                               f"Отсутствует интернет соединение"\
                                               f"</center></h2> </p></body></html>")
                self.error.show()
        else:
            self.error = ErrorApp()
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Пользователь с таким логином уже "\
                                           f"существует</center></h2> </p>"\
                                           f"</body></html>")
            self.error.show()
 
    def send_message(self: object) -> Union[str, bool]:
        if check_internet():
            email, password = email_data()
            destination_email = self.email
            message = MIMEMultipart()
            # Заголовок письма
            message['From'] = email
            message['To'] = destination_email
            message['Subject'] = 'Подтверждение электронной почты'
            code = generate_code()
            body = f"""
                <body style='background-color: #f0f0f0; text-align: center;'>
                <div style='padding: 20px; display: inline-block; \
                background-color: #ffffff; border-radius: 10px; text-align: left;'>
                <p style='color: #555555; font-size: 14px; margin-bottom: 20px;'>
                Здравствуйте, вас приветствует команда Managerio.\
                <br>Чтобы завершить регистрацию, необходимо подтвердить\
                адрес вашей электронной почты, введя следующий код в поле\
                приложения:
                </p>
                <h2 style='color: #333333; font-size: 35px;margin-bottom: 10px;'>\
                <center>{code}</center>
                </h2>
                <p style='color: #777777; font-size: 12px;'>
                <br><br><br>* Никому не сообщайте данный код</p></p>
                </p>
                </div>
                </body>"""
            try:
                message.attach(MIMEText(body, 'html'))
                with smtplib.SMTP('smtp.bk.ru', 587) as server:
                # Устанавливаем соединение с сервером
                    server.starttls()
                # Входим в аккаунт
                    server.login(email, password)
                # Отправляем письмо
                    server.send_message(message)
                return code
            except:
                return True
        else:  
            return False
    
    def open_main(self: object) -> None:
        for element in self.email_object:
            element.setEnabled(False)
            element.setVisible(False)
        for object in self.main_object:
            object.setEnabled(True)
            object.setVisible(True)
        self.lineEdit.setText("")
    
    def main_log(self: object) -> None:
        for element in self.main_object:
            element.setEnabled(True)
            element.setVisible(True)
        for object in self.logpass_object:
            object.setEnabled(False)
            object.setVisible(False)
        self.pushButton_9.setVisible(False)
        self.pushButton_9.setEnabled(False)
        self.lineEdit_3.setText("")
        self.lineEdit_2.setText("")
        self.label_6.setStyleSheet("QLabel{\n"
                                 "font-family: Arial;\n"
                                 "font-size: 12px;\n"
                                 "font-weight: normal;\n"
                                 "color: #808080;\n"
                                 "border: None;\n}")

    def clear_input(self: object) -> None:
        self.label_6.setText("")
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid #D3D3D3;\n"
                                    "border-radius: 10px;\n"
                                    "font-family: Arial;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: normal;\n"
                                    "color: #808080;\n"
                                    "qproperty-alignment: \'AlignCenter\';}")
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "border: 2px solid #D3D3D3;\n"
                                      "border-radius: 10px;\n"
                                      "font-family: Arial;\n"
                                      "font-size: 16px;\n"
                                      "font-weight: normal;\n"
                                      "color: #808080;\n"
                                      "qproperty-alignment: \'AlignCenter\';}\n")
        if not(self.lineEdit_3.text()) or not(self.lineEdit_2.text()):
            self.pushButton_8.setEnabled(False)
        else:
            self.pushButton_8.setEnabled(True)

    def clear_recovery(self: object) -> None:
        self.label_9.setText("")
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid #D3D3D3;\n"
                                    "border-radius: 10px;\n"
                                    "font-family: Arial;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: normal;\n"
                                    "color: #808080;\n"
                                    "qproperty-alignment: \'AlignCenter\';}")

    async def check_values(self: object) -> None:
        self.login = self.lineEdit_2.text()
        self.password = self.lineEdit_3.text()
        if await check_ban(self.login) <= 6 or (await check_ban(self.login) >= 7 and 
                                          str(get_time()) >= 
                                          await get_timeban(self.login)[0]):
            if await check_ban(self.login) >= 7:
                await update_count(self.login)
            if contains_sql_injection(self.login) or \
            contains_sql_injection(self.password):
                self.label_6.setText("Неверный логин или пароль")
                self.label_6.setStyleSheet("QLabel {\n"
                                        "font-family: Arial;\n"
                                        "font-size: 12px;\n"
                                        "font-weight: normal;\n"
                                        "color: #DC143C;\n"
                                        "border: None;\n}")
                self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                            "border: 2px solid #D3D3D3;\n"
                                            "border-radius: 10px;\n"
                                            "font-family: Arial;\n"
                                            "font-size: 16px;\n"
                                            "font-weight: normal;\n"
                                            "color: #DC143C;\n"
                                            "border-color: #DC143C;\n"
                                            "qproperty-alignment: \'AlignCenter\';}")
                self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                            "border: 2px solid #D3D3D3;\n"
                                            "border-radius: 10px;\n"
                                            "font-family: Arial;\n"
                                            "font-size: 16px;\n"
                                            "font-weight: normal;\n"
                                            "color: #DC143C;\n"
                                            "border-color: #DC143C;\n"
                                            "qproperty-alignment: \'AlignCenter\';}\n")
            elif await create_session(self.login, self.password):
                self.progress = Progress()
                current_geometry = self.geometry()
                center_x = current_geometry.x() + current_geometry.width() // 2
                center_y = current_geometry.y() + current_geometry.height() // 2
                self.progress.move(center_x - self.progress.width() // 2, 
                                center_y - self.progress.height() // 2)
                self.progress.finished.connect(self.close_all)
                self.progress.show()
                self.close()

            elif not await create_session(self.login, self.password):
                if await check_user(self.login):
                    if await check_ban(self.login) == 2 or await check_ban(self.login) == 5:
                        self.captcha = CaptchaApp()
                        self.captcha.showed()
                        self.captcha.link.append(self)
                        current_geometry = self.geometry()
                        center_x = current_geometry.x() + current_geometry.width() // 2
                        center_y = current_geometry.y() + current_geometry.height() // 2
                        self.captcha.move(center_x - self.captcha.width() // 2, 
                                center_y - self.captcha.height() // 2)
                        self.captcha.show()
                    else:
                        await ban_record(self.login)
                self.label_6.setText("Неверный логин или пароль")
                self.label_6.setStyleSheet("QLabel {\n"
                                        "font-family: Arial;\n"
                                        "font-size: 12px;\n"
                                        "font-weight: normal;\n"
                                        "color: #DC143C;\n"
                                        "border: None;\n}")
                self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                            "border: 2px solid #D3D3D3;\n"
                                            "border-radius: 10px;\n"
                                            "font-family: Arial;\n"
                                            "font-size: 16px;\n"
                                            "font-weight: normal;\n"
                                            "color: #DC143C;\n"
                                            "border-color: #DC143C;\n"
                                            "qproperty-alignment: \'AlignCenter\';}")
                self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                            "border: 2px solid #D3D3D3;\n"
                                            "border-radius: 10px;\n"
                                            "font-family: Arial;\n"
                                            "font-size: 16px;\n"
                                            "font-weight: normal;\n"
                                            "color: #DC143C;\n"
                                            "border-color: #DC143C;\n"
                                            "qproperty-alignment: \'AlignCenter\';}\n")
        else:
            ban = await get_timeban(self.login)
            self.label_6.setText(f"Аккаунт заблокирован до {ban[0][11:16]}")
            self.label_6.setStyleSheet("QLabel {\n"
                                        "font-family: Arial;\n"
                                        "font-size: 12px;\n"
                                        "font-weight: normal;\n"
                                        "color: #DC143C;\n"
                                        "border: None;\n}")
            if ban[1] == 0:
                email, password = email_data()
                destination_email = self.lineEdit_2.text()
                message = MIMEMultipart()
                # Заголовок письма
                message['From'] = email
                message['To'] = destination_email
                message['Subject'] = 'Аккаунт заблокирован'
                body = f"""
                <body style='background-color: #f0f0f0; text-align: center;'>
                <div style='padding: 20px; display: inline-block; \
                background-color: #ffffff; border-radius: 10px; text-align: left;'>
                <p style='color: #555555; font-size: 14px; margin-bottom: 20px;'>
                Здравствуйте, вас приветствует команда Managerio.\
                <br>Из-за большого количество неудачных попыток входа нам пришлось 
                заблокировать ваш аккаунт на 1 час. Блокировка снимется в:
                </p><h2 style='color: #333333; font-size: 35px;margin-bottom: 10px;'>\
                <center>{ban[0][11:16]}</center></h2><p style='color: #777777;
                font-size: 12px;'></p></p>
                </p>
                </div>
                </body>"""
                message.attach(MIMEText(body, 'html'))
                with smtplib.SMTP('smtp.bk.ru', 587) as server:
                    server.starttls()
                    server.login(email, password)
                    server.send_message(message)
                await email_deliver(self.login)

    async def close_all(self: object) -> None:
        self.progress.close()
        self.face = FaceSign()
        self.face.login = self.login
        self.face.passwd = self.password
        await export_photo(self.login, self.password)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.face.move(center_x - self.face.width() // 2, 
                    center_y - self.face.height() // 2)
        self.face.show()

    def open_email(self: object) -> None:
        for element in self.email_object:
            element.setEnabled(True)
            element.setVisible(True)
        for object in self.main_object:
            object.setEnabled(False)
            object.setVisible(False)
    
    def rec_logpass(self: object):
        for element in self.recovery_object:
            element.setEnabled(False)
            element.setVisible(False)
        for object in self.logpass_object:
            object.setEnabled(True)
            object.setVisible(True)

    def open_entry(self: object) -> None:
        for element in self.main_object:
            element.setEnabled(False)
            element.setVisible(False)
        for object in self.logpass_object:
            object.setEnabled(True)
            object.setVisible(True)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setVisible(True)
        self.pushButton_9.setEnabled(True)
        
    def close_window(self: object) -> None:
        self.exit = ExitApp()
        self.exit.links.append(self)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.exit.move(center_x - self.exit.width() // 2, 
                       center_y - self.exit.height() // 2)
        self.exit.show()
    
    def mousePressEvent(self: object, event) -> None:
        # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
                                    self.frameGeometry().topLeft()
        
    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class ErrorApp(QtWidgets.QMainWindow, error_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close_all)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.links_log = []
        self.links_sign = []
    
    def close_all(self: object):
        if self.links_sign:
            self.links_sign[0].open_logpass()
        elif self.links_log:
            self.links_log[0].open_email()
        self.close()
    

class ExitApp(QtWidgets.QMainWindow, exit_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.links = []
        self.pushButton_2.clicked.connect(self.close_all)
        self.pushButton_3.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
    
    def close_all(self: object) -> None:
        self.close()
        self.links[0].close()


class PasswordApp(QtWidgets.QMainWindow, password_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self) 
        self.login = ""
        self.status = 0
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.open_secret)
        self.pushButton_3.clicked.connect(self.close_window)
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.textChanged.connect(self.control_lineEdit)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.textChanged.connect(self.check_password)
        self.checkBox.stateChanged.connect(self.show_passwd)
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setMouseTracking(True)

    async def recover(self: object):
       password = self.lineEdit.text()
       await change_passwd(self.login, password)
       self.close()

    def close_window(self: object) -> None:
        self.exit = ExitApp()
        self.exit.links.append(self)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.exit.move(center_x - self.exit.width() // 2, 
                       center_y - self.exit.height() // 2)
        self.exit.show()

    def show_passwd(self: object, state) -> None:
        if state == 2:
            self.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.lineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.Password)
            self.lineEdit.setEchoMode(QLineEdit.Password)

    def control_lineEdit(self: object) -> None:
        if len(self.lineEdit.text()) >= 50:
            self.lineEdit.setEnabled(False)
        elif len(self.lineEdit_2.text()) >= 50:
            self.lineEdit_2.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)

    def check_password(self: object) -> None:
        if (self.lineEdit.text() == self.lineEdit_2.text()) and \
            (len(self.lineEdit.text()) >= 8) and \
                not(contains_sql_injection(self.lineEdit.text())) and \
                password_complexity(self.lineEdit.text()):
            self.label_3.setText("")
            self.pushButton_2.setEnabled(True)
            self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                          "border: 2px solid #D3D3D3;\n"
                                          "border-radius: 10px;\n"
                                          "font-family: Arial;\n"
                                          "font-size: 16px;\n"
                                          "font-weight: normal;\n"
                                          "color: #808080;\n"
                                          "qproperty-alignment: \'AlignCenter\';}")
        elif len(self.lineEdit.text()) <= 7:
            self.pushButton_2.setEnabled(False)
            self.label_3.setText("Короткий пароль")
            self.label_3.setStyleSheet("QLabel{\n"
                                       "border: None;\n"
                                       "color: #DC143C;\n"
                                       "font-size: 12px;}")
        elif contains_sql_injection(self.lineEdit.text()) or \
                not password_complexity(self.lineEdit.text()):
            self.pushButton_2.setEnabled(False)
            self.label_3.setText("Недопустимый пароль")
            self.label_3.setStyleSheet("QLabel{\n"
                                       "border: None;\n"
                                       "color: #DC143C;\n"
                                       "font-size: 12px;}")
        else: 
            self.pushButton_2.setEnabled(False)
            self.label_3.setText("Пароли не совпадают")
            self.label_3.setStyleSheet("QLabel{\n"
                                       "border: None;\n"
                                       "color: #DC143C;\n"
                                       "font-size: 12px;}")
            self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                          "border: 2px solid #D3D3D3;\n"
                                          "border-radius: 10px;\n"
                                          "font-family: Arial;\n"
                                          "font-size: 16px;\n"
                                          "font-weight: normal;\n"
                                          "color: #DC143C;\n"
                                          "border-color: #DC143C;\n"
                                          "qproperty-alignment: \'AlignCenter\';}")

    async def open_secret(self: object) -> None:
        if self.status == 0:
            self.secret = SecretApp()
            self.secret.login = self.login
            self.secret.passwd = self.lineEdit.text()
            self.secret.links.append(self)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.secret.move(center_x - self.secret.width() // 2, 
                         center_y - self.secret.height() // 2)
            self.secret.show()
        else:
            password = self.lineEdit.text()
            await change_passwd(self.login, password)
            self.close()

    def mousePressEvent(self: object, event) -> None:
        # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class RecoverApp(QtWidgets.QMainWindow, recover_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.input_code = ""
        self.code_db = ""
        self.login = ""
        self.pushButton_2.clicked.connect(self.validate_code)
        self.pushButton_3.clicked.connect(self.close)
        self.lineEdit.textChanged.connect(self.clear_error)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    def clear_error(self: object) -> None:
        self.label.setText("")
        self.label.setStyleSheet("QLabel{\n"
                                 "border: None;}")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid #D3D3D3;\n"
                                    "border-radius: 10px;\n"
                                    "font-family: Arial;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: normal;\n"
                                    "color: #808080;\n"
                                    "qproperty-alignment: \'AlignCenter\';}")

    def validate_code(self: object) -> None:
        self.input_code = self.lineEdit.text()
        if self.code_db == self.input_code:
            self.close()
            self.passwd = PasswordApp()
            self.passwd.login = self.login
            self.passwd.status = 1
            self.passwd.pushButton_2.clicked.connect(self.passwd.recover)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.passwd.move(center_x - self.passwd.width() // 2, 
                       center_y - self.passwd.height() // 2)
            self.passwd.show()
        else:
            self.label.setStyleSheet("QLabel{\n"
                                     "border: None;\n"
                                     "color: #DC143C;}")
            self.label.setText("Код введен неверно")
            self.lineEdit.setStyleSheet("QLineEdit{\n"
                                        "border: 2px solid #D3D3D3;\n"
                                        "border-radius: 10px;\n"
                                        "font-family: Arial;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: normal;\n"
                                        "border-color: #DC143C;\n"
                                        "color: #DC143C;\n"
                                        "qproperty-alignment: \'AlignCenter\';}")


class CodeApp(QtWidgets.QMainWindow, code_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.input_code = ""
        self.email = ""
        self.code_gen = ""
        self.links = []
        self.pushButton_2.clicked.connect(self.validate_code)
        self.pushButton_3.clicked.connect(self.close)
        self.lineEdit.textChanged.connect(self.clear_error)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    def clear_error(self: object) -> None:
        self.label.setText("")
        self.label.setStyleSheet("QLabel{\n"
                                 "border: None;}")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid #D3D3D3;\n"
                                    "border-radius: 10px;\n"
                                    "font-family: Arial;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: normal;\n"
                                    "color: #808080;\n"
                                    "qproperty-alignment: \'AlignCenter\';}")

    def validate_code(self: object) -> None:
        self.input_code = self.lineEdit.text()
        if self.code_gen == self.input_code:
            self.rule = RuleApp()
            self.rule.email = self.email
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.rule.move(center_x - self.rule.width() // 2, 
                           center_y - self.rule.height() // 2)
            self.links[0].close()
            self.close()
            self.rule.show()
        else:
            self.label.setStyleSheet("QLabel{\n"
                                     "border: None;\n"
                                     "color: #DC143C;}")
            self.label.setText("Пароли не совпадают")
            self.lineEdit.setStyleSheet("QLineEdit{\n"
                                        "border: 2px solid #D3D3D3;\n"
                                        "border-radius: 10px;\n"
                                        "font-family: Arial;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: normal;\n"
                                        "border-color: #DC143C;\n"
                                        "color: #DC143C;\n"
                                        "qproperty-alignment: \'AlignCenter\';}")


class CaptchaApp(QtWidgets.QMainWindow, captcha_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.code = ""
        self.image = ""
        self.link = []
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.check_code)
        self.lineEdit.textChanged.connect(self.clear_object)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def showed(self: object):
        self.code = generate_captcha()
        self.label.setPixmap(QPixmap("captcha.png"))

    def closeEvent(self: object, event):
        os.remove("captcha.png")
        event.accept()

    def clear_object(self: object):
        self.label_2.setText("")
        self.label_2.setStyleSheet("QLabel{\n"
                                 "border: None;}")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border: 2px solid #D3D3D3;\n"
                                    "border-radius: 10px;\n"
                                    "font-family: Arial;\n"
                                    "font-size: 16px;\n"
                                    "font-weight: normal;\n"
                                    "color: #808080;\n"
                                    "qproperty-alignment: \'AlignCenter\';}")

    async def check_code(self: object):
        if self.lineEdit.text() != self.code:
            self.label_2.setStyleSheet("QLabel{\n"
                                     "border: None;\n"
                                     "color: #DC143C;}")
            self.label_2.setText("Введен неверный код")
            self.lineEdit.setStyleSheet("QLineEdit{\n"
                                        "border: 2px solid #D3D3D3;\n"
                                        "border-radius: 10px;\n"
                                        "font-family: Arial;\n"
                                        "font-size: 16px;\n"
                                        "font-weight: normal;\n"
                                        "border-color: #DC143C;\n"
                                        "color: #DC143C;\n"
                                        "qproperty-alignment: \'AlignCenter\';}")
        else:
            await ban_record(self.link[0].login)
            self.close()


class FaceSign(QtWidgets.QMainWindow, face_window.Ui_MainWindow):
    
    def __init__(self: object):
        super().__init__()
        self.setupUi(self)
        self.login = ''
        self.passwd = ''
        self.index_camera = 0
        self.pushButton.clicked.connect(self.back_cam)
        self.pushButton_2.clicked.connect(self.next_cam)
        self.pushButton_3.clicked.connect(self.take_photo)        
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(self.close_window)
        self.pushButton_6.clicked.connect(self.open_logpass) 
        self.count_camera = self.available_cameras()
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True) 

    def close_window(self: object) -> None:
        self.exit = ExitApp()
        self.exit.links.append(self)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.exit.move(center_x - self.exit.width() // 2, 
                       center_y - self.exit.height() // 2)
        self.exit.show()

    def open_logpass(self: object) -> None:
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.close()
        self.camera.release()
        cv2.destroyAllWindows()
        self.main = MainApp()
        self.main.open_entry()
        self.main.move(center_x - self.main.width() // 2, 
                       center_y - self.main.height() // 2)
        self.main.show()
        
    def update_frame(self: object) -> None:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                            'haarcascade_frontalface_default.xml')
        if self.camera.isOpened():
            status, frame = self.camera.read()
            if status:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Детектирование лиц
                gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)
                faces = face_cascade.detectMultiScale(gray_frame, 
                                                      scaleFactor=1.1, 
                                                      minNeighbors=5, 
                                                      minSize=(30, 30))
            # Отображение квадратов вокруг лиц
                for (x, y, width, height) in faces:
                    cv2.rectangle(rgb_frame, (x, y), (x + width, y + height),
                                (255, 0, 0), 2)
            # Код для отображения изображения в QLabel
                height, width, channel = rgb_frame.shape
                bytes_line = channel * width
                convert_to_Qt = QImage(rgb_frame.data, width, height, 
                                       bytes_line, QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(convert_to_Qt))
        else:
            self.timer.stop()
            self.error = ErrorApp()
            self.error.links_sign.append(self)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Нет рабочих камер. Убедитесь, "\
                                           f"что хотя бы одна камера подключена "\
                                           f"к компьютеру</center></h2> </p>"\
                                           f"</body></html>")
            self.error.show()

    async def take_photo(self: object) -> None:
        status, frame = self.camera.read()
        if status:
            cv2.imwrite('input_photo.jpg', frame)
        if check_face_photo('input_photo.jpg') == True:
            if check_photo('input_photo.jpg') >= 16 and comparison_photo() < 700000:
                self.close()
                current_geometry = self.geometry()
                center_x = current_geometry.x() + current_geometry.width() // 2
                center_y = current_geometry.y() + current_geometry.height() // 2
                self.manager = ManagerApp()
                self.manager.login = self.login
                self.manager.passwd = self.passwd
                self.manager.connect = await create_session(self.login, self.passwd)
                self.manager.key = await get_key(self.login, self.passwd)  
                self.manager.reload_table()
                self.manager.move(center_x - self.manager.width() // 2, 
                                  center_y - self.manager.height() // 2)
                self.manager.show()

    def closeEvent(self, event):
        if os.path.isfile(os.path.join(os.getcwd(), "input_photo.jpg")):
            os.remove("input_photo.jpg")
            os.remove("database_input_photo.jpg")
            event.accept()
        else:
            os.remove("database_input_photo.jpg")

    def available_cameras(self: object) -> int:
        index = 0
        camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        while camera.isOpened():
            camera.release()
            cv2.destroyAllWindows()
            index += 1
            camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        return index
    
    def next_cam(self: object) -> None:
        self.index_camera = (self.index_camera + 1) % self.count_camera
        self.camera.release()
        cv2.destroyAllWindows()
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)

    def back_cam(self: object) -> None:
        if self.index_camera == 0:
            self.index_camera = self.count_camera - 1
        else:
            self.index_camera -= 1
        self.camera.release()
        cv2.destroyAllWindows()
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)
    
    def mousePressEvent(self: object, event) -> None:
       # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class FaceLog(QtWidgets.QMainWindow, face_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.drag_start_position = 0
        self.login = ""
        self.pushButton.clicked.connect(self.back_cam)
        self.pushButton_2.clicked.connect(self.next_cam)
        self.pushButton_3.clicked.connect(self.take_photo)        
        self.pushButton_4.clicked.connect(self.showMinimized)
        self.pushButton_5.clicked.connect(self.close_window)
        self.pushButton_6.clicked.connect(self.open_email)
        self.count_camera = self.available_cameras()
        self.index_camera = 0
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True) 

    def close_window(self: object) -> None:
        self.exit = ExitApp()
        self.exit.links.append(self)
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.exit.move(center_x - self.exit.width() // 2, 
                       center_y - self.exit.height() // 2)
        self.exit.show()

    def open_email(self: object) -> None:
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.close()
        self.camera.release()
        cv2.destroyAllWindows()
        self.main = MainApp()
        self.main.move(center_x - self.main.width() // 2, 
                        center_y - self.main.height() // 2)
        self.main.open_email()
        self.main.show()
        
    def update_frame(self: object) -> None:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                            'haarcascade_frontalface_default.xml')
        if self.camera.isOpened():        
            status, frame = self.camera.read()
            if status:
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Детектирование лиц
                gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)
                faces = face_cascade.detectMultiScale(
                    gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            # Отображение квадратов вокруг лиц
                for (x, y, width, height) in faces:
                    cv2.rectangle(rgb_frame, (x, y), (x + width, y + height),
                                (255, 0, 0), 2)
            # Код для отображения изображения в QLabel
                height, width, channel = rgb_frame.shape
                bytes_line = channel * width
                convert_to_Qt = QImage(rgb_frame.data, width, height, bytes_line,
                                    QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(convert_to_Qt))
        else:
            self.timer.stop()
            self.error = ErrorApp()
            self.error.links_log.append(self)
            current_geometry = self.geometry()
            center_x = current_geometry.x() + current_geometry.width() // 2
            center_y = current_geometry.y() + current_geometry.height() // 2
            self.error.move(center_x - self.error.width() // 2, 
                            center_y - self.error.height() // 2)
            self.error.textBrowser.setText(f"<html><head/><body><p><center>"\
                                           f"Нет рабочих камер. Убедитесь, "\
                                           f"что хотя бы одна камера подключена"\
                                           f" к компьютеру</center></h2> </p>"\
                                           f"</body></html>")
            self.error.show()    

    def take_photo(self: object) -> None:
        status, frame = self.camera.read()
        if status:
            cv2.imwrite('input_photo.jpg', frame)
        if check_face_photo('input_photo.jpg') == True:
            if check_photo('input_photo.jpg') >= 16:
                # self.camera.release()
                # cv2.destroyAllWindows()
                self.close()
                self.password = PasswordApp()
                self.password.login = self.login
                current_geometry = self.geometry()
                center_x = current_geometry.x() + current_geometry.width() // 2
                center_y = current_geometry.y() + current_geometry.height() // 2
                self.password.move(center_x - self.password.width() // 2, 
                                   center_y - self.password.height() // 2)
                
                self.password.show()

    def available_cameras(self: object) -> int:
        index = 0
        camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        while camera.isOpened():
            camera.release()
            cv2.destroyAllWindows()
            index += 1
            camera = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        return index
    
    def next_cam(self: object) -> None:
        self.index_camera = (self.index_camera + 1) % self.count_camera
        self.camera.release()
        cv2.destroyAllWindows()
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)

    def back_cam(self: object) -> None:
        if self.index_camera == 0:
            self.index_camera = self.count_camera - 1
        else:
            self.index_camera -= 1
        self.camera.release()
        cv2.destroyAllWindows()
        self.camera = cv2.VideoCapture(self.index_camera, cv2.CAP_DSHOW)
    
    def mousePressEvent(self: object, event) -> None:
       # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class SecretApp(QtWidgets.QMainWindow, secret_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.login = ""
        self.passwd = ""
        self.links = []
        self.secret = self.secret_code()
        self.pushButton_2.clicked.connect(self.close_all)
        self.label.setText(f"<html><head/><body><p>Поздравляем! Регистрация\
                           завершена успешно. <br/>Ниже будет представлен \
                           ваш секретный код, необходимый  для \
                           восстановления доступа к вашей учетной записи\
                           в случае потери или забытого пароля. \
                           Благодарим за выбор нашего приложения! \
                           Секретный код:<h2 style='color: #333333; \
                           font-size: 60px;margin-bottom: 10px;'><center>\
                           {self.secret}</center></h2> </p></body></html>")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
    
    def closeEvent(self, event):
        os.remove("input_photo.jpg")
        event.accept()

    async def close_all(self: object) -> None:
        key = generate_key()
        await save_account("input_photo.jpg", self.login, 
                     self.passwd, self.secret, key)
        self.close()
        self.links[0].close()
        self.manager = ManagerApp()
        self.manager.login = self.login
        self.manager.passwd = self.passwd
        self.manager.connect = await create_session(self.login, self.passwd)
        self.manager.key = await get_key(self.login, self.passwd)
        self.manager.reload_table()
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.manager.move(center_x - self.manager.width() // 2, 
                          center_y - self.manager.height() // 2)
        self.manager.show()
        
    def secret_code(self: object) -> str:
        digits = ''.join(random.choice(string.digits) for _ in range(2))
        letters = ''.join(random.choice(string.ascii_letters) \
                          for _ in range(2))
        special_chars = ''.join(random.choice('!@#$%^&*()_+?') \
                                for _ in range(2))
        code = ''.join(random.sample(digits + letters + special_chars, k = 6))
        return code
 

class RuleApp(QtWidgets.QMainWindow, rule_window.Ui_MainWindow):
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.email = ""
        self.pushButton_2.clicked.connect(self.open_progress)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True) 
    
    def open_progress(self: object) -> None:
        self.progress = Progress()
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.progress.move(center_x - self.progress.width() // 2, 
                           center_y - self.progress.height() // 2)
        self.progress.finished.connect(self.close_all)
        self.progress.show()
        self.close()

    def close_all(self: object) -> None:
        self.progress.close()
        self.face = FaceLog()
        self.face.login = self.email
        current_geometry = self.geometry()
        center_x = current_geometry.x() + current_geometry.width() // 2
        center_y = current_geometry.y() + current_geometry.height() // 2
        self.face.move(center_x - self.face.width() // 2, 
                        center_y - self.face.height() // 2)
        self.face.show()

    def mousePressEvent(self: object, event) -> None:
        # Запоминаем начальные координаты при нажатии мыши
        self.drag_start_position = event.globalPos() - \
        self.frameGeometry().topLeft()

    def mouseMoveEvent(self: object, event) -> None:
        # Перемещаем окно при перемещении мыши
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)


class Progress(QtWidgets.QMainWindow, progress_bar.Ui_MainWindow):
    
    finished = pyqtSignal()
    
    def __init__(self: object) -> None:
        super().__init__()
        self.setupUi(self)
        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(70)
        self.setWindowFlags(Qt.FramelessWindowHint) 
       
    def update_progress(self: object) -> None:
        value = self.progressBar.value() + 1
        if value < 40:
            self.label.setText("Поиск доступных камер")
            self.progressBar.setValue(value)
        elif value < 80:
            self.label.setText("Проверка установленных драйверов")
            self.progressBar.setValue(value)
        elif value < 100:
            self.label.setText("Подготовка оборудования")
            self.progressBar.setValue(value)
        elif value == 100:
            self.progress_timer.stop()
            self.finished.emit()
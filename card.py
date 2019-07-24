#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess, sys, time, requests, binascii

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget, QMessageBox


class AuthWindow(QWidget):
    BUTTON_SIZES = [380, 70, 90, 30]

    def __init__(self):
        super().__init__()
        self.screen = app.primaryScreen()
        self.size = self.screen.size()

        self.card_edit = self.build_edit(90, 30, 215, 30)
        self.card_label = self.build_label("Enter card name:", 135, 10)
        self.card_label = self.setFont(QtGui.QFont('SansSerif', 11))

        self.apply_btn = self.build_button("Apply", 155, 90, self.write_card)

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setFixedHeight(150)
        self.setFixedWidth(400)
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(window_geometry.topLeft())
        self.show()

    def build_label(self, label_text, label_pos_x, label_pos_y):
        qlabel = QLabel(self)
        qlabel.setText(label_text)
        qlabel.move(label_pos_x, label_pos_y)
        return qlabel

    def build_edit(self, edit_x, edit_y, edit_pos_x, edit_pos_y):
        qline_edit = QLineEdit(self)
        qline_edit.move(edit_x, edit_y)
        qline_edit.resize(edit_pos_x, edit_pos_y)
        return qline_edit

    def build_button(self, btn_text, btn_pos_x, btn_pos_y, connect_method):
        qbutton = QPushButton(btn_text, self)
        qbutton.setGeometry(self.BUTTON_SIZES[0], self.BUTTON_SIZES[1], self.BUTTON_SIZES[2], self.BUTTON_SIZES[3])
        qbutton.clicked.connect(connect_method)
        qbutton.move(btn_pos_x, btn_pos_y)
        return qbutton

    def write_card(self):
        if self.card_edit.text():
            self.file = open('/home/user/{}'.format(self.card_edit.text()), "w+")
            self.card1 = subprocess.check_output(['curl', 'https://www.halls.my-support.club/api/getfilecard.php?FileCardId=131843_31'])
            self.card2 = str(self.card1, 'utf-8')

            get_int_from_hex = bytearray.fromhex(self.card2)
            list_int = list(get_int_from_hex)
            for i in list_int:
                dex_var = chr(i)
                a = str(print(dex_var, end=''))
                break

            self.file.write(a)
            self.file.close()

            QWidget.close(self)
            #hile True:
                   #subprocess.call("wine explorer /desktop=name,1280x1024 launcher.exe", shell=True)
                    #ime.sleep(1)
        else:
            QMessageBox.information(None, "Error", "Enter file card",defaultButton=QMessageBox.Ok)

        #subprocess.call(
        #    "rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --delete-excluded  --force rsync://my@update.bug.com:1111/globalslots/plugins_dir/plugins/ ./plugins/ &",
        #    shell=True)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = AuthWindow()
    sys.exit(app.exec_())
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser, subprocess, sys, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QDesktopWidget, QMessageBox, QProgressBar


class SelectWindow(QWidget):
    BUTTON_SIZES = [380, 90, 300, 45]

    def __init__(self):
        super().__init__()
  #      self.screen = app.primaryScreen()
  #      self.size = self.screen.size()
  #      self.fixed_width = 1280
  #      self.fixed_height = 1024

        #       self.config = configparser.ConfigParser()
        #       self.config.optionxform = str
        #       self.config.read('launcher.ini')

  #      self.pass_edit = self.build_edit(90, 70, 215, 30)
  #      self.pass_label = self.build_label("Password:", 25, 75)

  #      self.serial_edit = self.build_edit(90, 120, 215, 30)
  #      self.serial_edit.setText(self.config.get('Options', 'Serial'))
  #      self.serial_label = self.build_label("Serial:", 48, 125)

        self.app1 = self.build_button("App №1", 200, 90, self.btn_click1)
#        self.app2 = self.build_button("App №2", 200, 140, self.btn_click2)
#        self.app3 = self.build_button("App №3", 200, 190, self.btn_click3)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 140, 300, 20)
        self.progress.setMaximum(100)
#        self.button = QPushButton('Start', self)
#        self.button.move(200, 140)
#        self.show()

        self.setWindowTitle('- Select applications - ')
        self.setFixedHeight(450)
        self.setFixedWidth(700)
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(window_geometry.topLeft())
        self.show()

    def build_button(self, btn_text, btn_pos_x, btn_pos_y, connect_method):
        qbutton = QPushButton(btn_text, self)
        qbutton.setGeometry(self.BUTTON_SIZES[0], self.BUTTON_SIZES[1], self.BUTTON_SIZES[2], self.BUTTON_SIZES[3])
        qbutton.clicked.connect(connect_method)
        qbutton.move(btn_pos_x, btn_pos_y)
        return qbutton

    def btn_click1(self):
        subprocess.call(
#            "rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --delete-excluded  --force rsync://gup@update.gslots.win:49873/globalslots/plugins_dir/plugins/ ./plugins/ &",
#            shell=True)
            "echo app1", shell=True)

#    def btn_click2(self):
#        subprocess.call(
#            "rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --delete-excluded  --force rsync://gup@update.gslots.win:49873/globalslots/plugins_dir/plugins/ ./plugins/ &",
#            shell=True)
#            "echo app2", shell=True)

#    def btn_click3(self):
#        subprocess.call(
#            "rsync $args --password-file=/run/initramfs/memory/data/Progs/GlobalSlots/rsyncp -Lrv --progress --times --ignore-errors --delete-excluded  --force rsync://gup@update.gslots.win:49873/globalslots/plugins_dir/plugins/ ./plugins/ &",
#            shell=True)
#            "echo app3", shell=True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SelectWindow()
    sys.exit(app.exec_())

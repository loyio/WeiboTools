# -*- coding: utf-8 -*-
"""
Created on 2018/10/8 

@author: loyio
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QTextEdit, QTableWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
import sys
import sqlite3
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+"."))
import login_account_cookies


conn = sqlite3.connect("cookies.db")


class WeiboInputCookis(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博Cookies管理系统')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon("resource/favicon.ico"))
        self.inputCookis = QLineEdit("")
        # self.Cookies_table()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        lblTitle = QLabel("Cookies:")
        btnInsure = QPushButton("确定录入", self)
        btnLookcookies = QPushButton("查看cookies", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        btnLookcookies.clicked.connect(self.click_showcookies)
        mainLayout = QGridLayout()
        mainLayout.addWidget(lblTitle)
        mainLayout.addWidget(self.inputCookis)
        mainLayout.addWidget(btnLookcookies)
        mainLayout.addWidget(btnInsure)
        # mainLayout.addWidget(self.table)
        self.setLayout(mainLayout)

    def Cookies_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(100)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 50)


    @pyqtSlot()
    def click_btnInsure(self):
        pass

    @pyqtSlot()
    def click_showcookies(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeiboInputCookis()
    ex.show()
    sys.exit(app.exec_())

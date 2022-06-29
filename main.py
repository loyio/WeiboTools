# -*- coding: utf-8 -*-
"""
Created on 2018/10/8 

@author: loyio
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import sqlite3
import os
import json
from auto_comment.main import auto_comment_func
from weibo_data.get_user_info import getUesrInfo
from auto_post.main import auto_post_weibo
from auto_repost.main import auto_repost_func, auto_repost_test_func
from auto_follow.main import auto_follow
from energy_hitting.main import post_weibo, repost_weibo, cheer_card
from fake_login.main import fake_login
from auto_like.main import auto_like
import requests


conn = sqlite3.connect("weibo_account.sqlite")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博自动转赞评系统(By loyio)')
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setMaximumSize(400, 300)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.MainInitUi()
        self.show()

    def MainInitUi(self):
        self.setGeometry(400, 200, 400, 300)
        btnInputCookies = QPushButton("管理微博账号✔️", self)
        btnInputCookies.clicked.connect(self.click_btnInputCookies)
        btnInputWeiboAccount = QPushButton("录入微博账号数据✔️", self)
        btnInputWeiboAccount.clicked.connect(self.click_btnInputWeiboAccount)
        btnWeiboData = QPushButton("查看微博数据✔️", self)
        btnWeiboData.clicked.connect(self.click_btnGetUserInfo)
        btnUpgradeWeibo = QPushButton("微博自动养号✔️", self)
        btnUpgradeWeibo.clicked.connect(self.click_btnWeiboUpgrade)
        btnAutoComment = QPushButton("微博自动刷评✔️", self)
        btnAutoComment.clicked.connect(self.click_btnAutoComment)
        btnAutoCommentLike = QPushButton("微博评论点赞✔️", self)
        btnAutoCommentLike.clicked.connect(self.click_btnAutoCommentLike)
        btnAutoLike = QPushButton("微博自动点赞✔️", self)
        btnAutoLike.clicked.connect(self.click_btnAutoLike)
        btnPostWeibo = QPushButton("自动发布微博✔️️", self)
        btnPostWeibo.clicked.connect(self.click_btnAutoPost)
        btnRepostWeibo = QPushButton("自动转发微博✔️", self)
        btnRepostWeibo.clicked.connect(self.click_btnRepostWeibo)
        btnSuperstar = QPushButton("超新星全运会✔️", self)
        btnSuperstar.clicked.connect(self.click_btnSuperstar)
        mainFuncLayout = QGridLayout()
        mainFuncLayout.addWidget(btnInputCookies, 0, 0)
        mainFuncLayout.addWidget(btnInputWeiboAccount, 0, 1)
        mainFuncLayout.addWidget(btnWeiboData, 1, 0)
        mainFuncLayout.addWidget(btnUpgradeWeibo, 1, 1, )
        mainFuncLayout.addWidget(btnAutoComment, 2, 0)
        mainFuncLayout.addWidget(btnAutoCommentLike, 2, 1)
        mainFuncLayout.addWidget(btnAutoLike, 3, 0)
        mainFuncLayout.addWidget(btnPostWeibo, 3, 1)
        mainFuncLayout.addWidget(btnRepostWeibo, 4, 0)
        mainFuncLayout.addWidget(btnSuperstar, 4, 1)
        self.setLayout(mainFuncLayout)

    # 微博输入cookies
    def click_btnInputCookies(self):
        self.inputCookiesWindow = WeiboInputCookies()
        self.hide()
        self.inputCookiesWindow.show()
        self.show()

    # 微博输入账号
    def click_btnInputWeiboAccount(self):
        self.inputWeiboAccountWindow = WeiboInputAccount()
        self.hide()
        self.inputWeiboAccountWindow.show()
        self.show()

    # 微博自动评论
    def click_btnAutoComment(self):
        self.AutoCommentWindow = WeiboAutoComment()
        self.hide()
        self.AutoCommentWindow.show()
        self.show()

    # 自动发布微博
    def click_btnAutoPost(self):
        self.AutoPostWindow = WeiboAutoPost()
        self.hide()
        self.AutoPostWindow.show()
        self.show()

    # 自动转发微博
    def click_btnRepostWeibo(self):
        self.AutoRepostWindow = WeiboAutoRepost()
        self.hide()
        self.AutoRepostWindow.show()
        self.show()

    # 评论点赞
    def click_btnAutoCommentLike(self):
        msg_box = QMessageBox(QMessageBox.Warning, "警告", "功能暂时不开放")
        msg_box.show()
        msg_box.exec_()

    # 微博点赞
    def click_btnAutoLike(self):
        self.AutoLikeWindow = WeiboAutoLike()
        self.hide()
        self.AutoLikeWindow.show()
        self.show()

    # 获取微博数据
    def click_btnGetUserInfo(self):
        self.GetUserInfoWindow = WeiboGetUserInfo()
        self.hide()
        self.GetUserInfoWindow.show()
        self.show()

    def click_btnWeiboUpgrade(self):
        self.WeiboUpgradeAccountWindow = WeiboUpgradeAccount()
        self.hide()
        self.WeiboUpgradeAccountWindow.show()
        self.show()

    # 超新星全运会打榜
    def click_btnSuperstar(self):
        self.SuperstarWindow = WeiboSuperStar()
        self.hide()
        self.SuperstarWindow.show()
        self.show()


# 输入cookies
class WeiboInputCookies(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博Cookies管理系统')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.FilePathInput = QLineEdit()
        self.AccountFileOpen = QFileDialog()

        self.AccountInput = QLineEdit()
        self.AccountInput.setPlaceholderText("请输入微博账号")
        self.PasswordInput = QLineEdit()
        self.PasswordInput.setPlaceholderText("请输入微博密码")

        #账号组名
        self.AccountGroupNameInput = QLineEdit()
        self.AccountGroupNameInput.setPlaceholderText("号组名")
        self.AccountIndexInput = QLineEdit()
        self.AccountIndexInput.setPlaceholderText("账号ID")

        self.account_combo = QComboBox()
        self.accountgroup_combo = QComboBox()
        self.CookiesInput = QLineEdit()
        self.DeleteIndex = QLineEdit()
        self.DeleteIndex.setPlaceholderText("索引")
        self.generate_combo()
        self.generate_accountgroup_combo()
        self.fill_lineEdit()
        self.cookies_table()
        self.click_showcookies()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        btnFileDialog = QPushButton("选择文件",self)
        btnFileDialog.clicked.connect(self.click_btnFileDialog)
        btnInsureBatchInsert = QPushButton("批量插入", self)
        btnInsureBatchInsert.clicked.connect(self.click_btnInsureBatchInsert)
        btnInsureInsert = QPushButton("确定插入", self)
        btnInsureInsert.clicked.connect(self.click_btnInsureInsert)
        btnInsureChange = QPushButton("确定修改", self)
        btnInsureChange.clicked.connect(self.click_btnInsureChange)
        btnDeleteData = QPushButton("删除此行", self)
        btnDeleteData.clicked.connect(self.click_btnDeleteData)
        btnInsertAccountGroup = QPushButton("添加号组")
        btnInsertAccountGroup.clicked.connect(self.click_btnInsertAccountGroup)
        btnChangeAccountGroup = QPushButton("改变号组")
        btnChangeAccountGroup.clicked.connect(self.click_btnChangeAccountGroup)
        btnLookcookies = QPushButton("刷新数据库", self)
        btnLookcookies.clicked.connect(self.click_showcookies)
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.FilePathInput, 0, 0, 1, 5)
        mainLayout.addWidget(btnFileDialog, 0, 5, 1, 1)
        mainLayout.addWidget(btnInsureBatchInsert, 0, 6, 1, 2)
        mainLayout.addWidget(self.AccountInput, 1, 0, 1, 3)
        mainLayout.addWidget(self.PasswordInput, 1, 3, 1, 3)
        mainLayout.addWidget(btnInsureInsert, 1, 6, 1, 2)
        mainLayout.addWidget(self.account_combo, 2, 0, 1, 1)
        mainLayout.addWidget(self.CookiesInput, 2, 1, 1, 4)
        mainLayout.addWidget(btnInsureChange, 2, 5, 1, 1)
        mainLayout.addWidget(self.DeleteIndex, 2, 6, 1, 1)
        mainLayout.addWidget(btnDeleteData, 2, 7, 1, 1)
        mainLayout.addWidget(self.AccountGroupNameInput, 3, 0, 1, 2)
        mainLayout.addWidget(btnInsertAccountGroup, 3, 2, 1, 2)
        mainLayout.addWidget(self.AccountIndexInput, 3, 4, 1, 1)
        mainLayout.addWidget(self.accountgroup_combo, 3, 5, 1, 1)
        mainLayout.addWidget(btnChangeAccountGroup, 3, 6, 1, 2)
        mainLayout.addWidget(btnLookcookies, 4, 0, 1, 8)
        mainLayout.addWidget(self.table, 5, 0, 1, 8)
        self.setLayout(mainLayout)

    def cookies_table(self):
        self.table = QTableWidget()
        horizontalHeader = ["ID", "账号", "密码", "提示", "Cookies", "状态", "号组"]
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(horizontalHeader)


    def generate_accountgroup_combo(self):
        for i in range(0, self.accountgroup_combo.count()):
            self.accountgroup_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accountgroup_combo.addItem(accountgroup_list[i][1])

    def generate_combo(self):
        for i in range(0, self.account_combo.count()):
            self.account_combo.removeItem(0)
        self.account_combo.currentIndexChanged.connect(self.fill_lineEdit)
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        for i in range(0, len(cookies_list)):
            self.account_combo.addItem(str(i+1))

    def fill_lineEdit(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        if self.account_combo.currentText() != "" and int(self.account_combo.currentText()) - 1 != len(cookies_list):
            current_index = int(self.account_combo.currentText()) - 1
            self.CookiesInput.setText(cookies_list[current_index][4])
        else:
            pass

    @pyqtSlot()
    def click_btnFileDialog(self):
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file','.', "txt files (*.txt)")
        print(absolute_path)
        self.FilePathInput.setText(absolute_path[0])

    @pyqtSlot()
    def click_btnInsureBatchInsert(self):
        c = conn.cursor()
        with open(self.FilePathInput.text(), 'r') as f:
            while True:
                account = f.readline().strip()
                if account == "":
                    break
                account_list = account.split("----")
                cmd = "INSERT INTO WeiboCookies VALUES(NULL, \'" + account_list[0] + "\', \'" + account_list[1] + "\', \'\', \'\', \'\', \'\');"
                c.execute(cmd)
                conn.commit()
        self.click_showcookies()

    @pyqtSlot()
    def click_btnInsureInsert(self):
        username = self.AccountInput.text()
        password = self.PasswordInput.text()
        c = conn.cursor()
        cmd = "INSERT INTO WeiboCookies VALUES(NULL, \'" + username + "\', \'" + password + "\', \"\", \"\", \"\", \"\");"
        c.execute(cmd)
        conn.commit()
        fake_login(username, password, conn)
        self.AccountInput.setText("")
        self.PasswordInput.setText("")
        self.click_showcookies()

    @pyqtSlot()
    def click_btnInsureChange(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        cmd = "UPDATE WeiboCookies SET COOKIES = \"" + self.CookiesInput.text() + "\" WHERE USERNAME = \"" + cookies_list[int(self.account_combo.currentText())-1][1] + "\""
        c.execute(cmd)
        conn.commit()
        self.click_showcookies()


    @pyqtSlot()
    def click_btnDeleteData(self):
        if self.DeleteIndex.text() != "":
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            if int(self.DeleteIndex.text()) - 1 < len(cookies_list):
                print("之前")
                cmd = "DELETE FROM WeiboCookies  WHERE USERNAME = \"" + cookies_list[int(self.DeleteIndex.text()) - 1][1] + "\""
                c.execute(cmd)
                conn.commit()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "你的操作有误")
                msg_box.show()
                msg_box.exec_()
            self.account_combo.setCurrentIndex(0)
            self.click_showcookies()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "没有输入要删除的账号索引")
            msg_box.show()
            msg_box.exec_()


    # 插入号组
    @pyqtSlot()
    def click_btnInsertAccountGroup(self):
        if self.AccountGroupNameInput.text() != "":
            c = conn.cursor()
            cmd = "INSERT INTO WeiboAccountGroup VALUES(NULL, \'" + self.AccountGroupNameInput.text() + "\', \"\");"
            try:
                c.execute(cmd)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "你输入的号组名已存在")
                msg_box.show()
                msg_box.exec_()
            conn.commit()
            self.generate_accountgroup_combo()
            self.AccountGroupNameInput.setText("")

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请输入你要添加的号组名")
            msg_box.show()
            msg_box.exec_()

    # 改变号组
    @pyqtSlot()
    def click_btnChangeAccountGroup(self):
        if self.AccountIndexInput.text() != "":
            c = conn.cursor()
            cmd = "UPDATE WeiboCookies SET GROUPID= \"" + self.accountgroup_combo.currentText() + "\" WHERE ID = "+ self.AccountIndexInput.text()
            try:
                c.execute(cmd)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
                msg_box.show()
                msg_box.exec_()
            conn.commit()
            self.click_showcookies()
            self.AccountIndexInput.setText("")

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "没有输入账号ID")
            msg_box.show()
            msg_box.exec_()


    @pyqtSlot()
    def click_showcookies(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        conn.commit()
        self.table.setRowCount(len(cookies_list))
        for i in range(0, len(cookies_list)):
            self.table.setItem(i, 0, QTableWidgetItem(str(cookies_list[i][0])))
            self.table.setItem(i, 1, QTableWidgetItem(cookies_list[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(cookies_list[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(cookies_list[i][3]))
            self.table.setItem(i, 4, QTableWidgetItem(cookies_list[i][4]))
            self.table.setItem(i, 5, QTableWidgetItem(cookies_list[i][5]))
            self.table.setItem(i, 6, QTableWidgetItem(cookies_list[i][6]))
        self.generate_combo()


# 创建自己的浏览器控件，继承自QWebEngineView
class MyWebEngineView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(MyWebEngineView, self).__init__(*args, **kwargs)
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self.cookies = {}  # 存放cookie字典

    def onCookieAdd(self, cookie):  # 处理cookie添加的事件
        name = cookie.name().data().decode('utf-8')  # 先获取cookie的名字，再把编码处理一下
        value = cookie.value().data().decode('utf-8')  # 先获取cookie值，再把编码处理一下
        self.cookies[name] = value  # 将cookie保存到字典里

    # 获取cookie
    def get_cookie(self):
        cookie_str = ''
        for key, value in self.cookies.items():  # 遍历字典
            cookie_str += (key + '=' + value + ';')  # 将键值对拿出来拼接一下
        return cookie_str  # 返回拼接好的字符串

# 输入微博账号
class WeiboInputAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("微博账号输入系统")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        # 设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.AccountInput = QLineEdit()
        self.AccountInput.setReadOnly(True)
        self.PasswordInput = QLineEdit()
        self.PasswordInput.setReadOnly(True)
        self.lblState = QLabel()
        self.generate_combo()
        self.setup()
        self.fill_lineEdit()
        self.judge_cookies_useful()
        self.show()

    def setup(self):
        mainLayout = QGridLayout(self)  # 创建一个垂直布局来放控件
        self.btn_refresh = QPushButton("刷新")
        self.btn_refresh.clicked.connect(self.click_refresh)
        self.btn_logout = QPushButton("登出")
        self.btn_logout.clicked.connect(self.click_logout)
        self.btn_get = QPushButton('获取cookies')  # 创建一个按钮涌来了点击获取cookie
        self.btn_get.clicked.connect(self.get_cookie)  # 绑定按钮点击事件
        self.web = MyWebEngineView()  # 创建浏览器组件对象
        self.web.resize(800, 600)  # 设置大小
        self.web.load(QUrl("https://m.weibo.cn"))  # 微博页面
        mainLayout.addWidget(self.accout_combo, 0, 0, 1, 1)
        mainLayout.addWidget(self.AccountInput, 0, 1, 1, 4)
        mainLayout.addWidget(self.PasswordInput, 0, 5, 1, 4)
        mainLayout.addWidget(self.btn_refresh, 1, 0, 1, 2)
        mainLayout.addWidget(self.btn_logout, 1, 3, 1, 2)
        mainLayout.addWidget(self.lblState, 1, 5, 1, 3)
        mainLayout.addWidget(self.btn_get, 1, 7, 1, 2)  # 将组件放到布局内，先在顶部放一个按钮
        mainLayout.addWidget(self.web, 2, 0, 1, 9)  # 再放浏览器
        self.setLayout(mainLayout)

    @pyqtSlot()
    def get_cookie(self):
        cookie = self.web.get_cookie()
        c = conn.cursor()
        cmd = "UPDATE WeiboCookies SET COOKIES = \""+ cookie +"\" WHERE USERNAME = \""+ self.AccountInput.text() + "\""
        c.execute(cmd)
        conn.commit()
        self.judge_cookies_useful()


    def generate_combo(self):
        try:
            self.accout_combo = QComboBox()
            self.accout_combo.currentIndexChanged.connect(self.fill_lineEdit)
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            for i in range(0, len(cookies_list)):
                self.accout_combo.addItem(str(i+1))
        except Exception as e:
            print(e)

    def fill_lineEdit(self):
        self.accout_combo.currentText()
        c = conn.cursor()
        try:
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            current_index = int(self.accout_combo.currentText()) - 1
            print(current_index)
            self.AccountInput.setText(cookies_list[current_index][1])
            self.PasswordInput.setText(cookies_list[current_index][2])
            self.judge_cookies_useful()
        except Exception as e:
            print(e)

    @pyqtSlot()
    def click_refresh(self):
        self.web.reload()

    @pyqtSlot()
    def click_logout(self):
        self.web.load(QUrl("https://m.weibo.cn/logout"))

    @pyqtSlot()
    def judge_cookies_useful(self):
        try:
            c = conn.cursor()
            cmd = "SELECT * FROM WeiboCookies WHERE USERNAME = \""+ self.AccountInput.text() + "\""
            print(cmd)
            cookies = c.execute(cmd).fetchall()
            print(cookies)
            headers = {
                "Referer": "https://m.weibo.cn/",
                "Cookie": cookies[0][4]
            }
            session = requests.session()
            judge_login_res = session.get("https://m.weibo.cn/api/config", headers=headers).text
            judge_login_res_json = json.loads(judge_login_res)
            if judge_login_res_json["data"]["login"] == True:
                self.lblState.setText("Cookies有效")
                print(1, "自动登录成功")
            else:
                self.lblState.setText("Cookies无效")
                print("不能直接登录,需要进行手势验证码验证")
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
            msg_box.show()
            msg_box.exec_()
            exit()



# 获取用户信息
class WeiboGetUserInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博用户数据获取系统')
        # 设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboId = QLineEdit("")
        self.inputWeiboId.setPlaceholderText("请输入用户的唯一标识")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        self.outputResult.setFontPointSize(19)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        self.NameRadioButton = QRadioButton("以用户名查找")
        self.NameRadioButton.setChecked(True)
        self.UidRadioButton = QRadioButton("以uid查找")
        btnInsure = QPushButton("确定开始", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.NameRadioButton, 0, 0, 1, 1)
        mainLayout.addWidget(self.UidRadioButton, 0, 1, 1, 1)
        mainLayout.addWidget(self.inputWeiboId, 0, 2, 1, 5)
        mainLayout.addWidget(btnInsure, 0, 7, 1, 1)
        mainLayout.addWidget(self.outputResult, 1, 0, 1, 8)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    @pyqtSlot()
    def click_btnInsure(self):
        if (self.inputWeiboId.text() != ""):
            self.outputResult.clear()
            if self.NameRadioButton.isChecked():
                getUesrInfo(0, self.inputWeiboId.text(), self.printToGui)
            if self.UidRadioButton.isChecked():
                getUesrInfo(1, self.inputWeiboId.text(), self.printToGui)
        else:
            if self.NameRadioButton.isChecked():
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "用户名为空")
                msg_box.show()
                msg_box.exec_()
            if self.UidRadioButton.isChecked():
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "uid为空")
                msg_box.show()
                msg_box.exec_()


#微博批量自动养号
class WeiboUpgradeAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博批量自动养号操作')
        # 设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboId = QLineEdit("")
        self.inputWeiboId.setPlaceholderText("请输入用户的uid")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        self.outputResult.setFontPointSize(19)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        btnAutoFollow = QPushButton("自动关注", self)
        btnAutoFollow.clicked.connect(self.click_btnAutoFollow)
        btnAutoChangeName = QPushButton("自动改名", self)
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.inputWeiboId, 0, 0, 1, 5)
        mainLayout.addWidget(btnAutoFollow, 0, 5, 1, 1)
        mainLayout.addWidget(btnAutoChangeName, 1, 0, 1, 6)
        mainLayout.addWidget(self.outputResult, 2, 0, 1, 6)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    # 自动批量关注
    @pyqtSlot()
    def click_btnAutoFollow(self):
        if (self.inputWeiboId.text() != ""):
            self.outputResult.clear()
            auto_follow(self.inputWeiboId.text(), self.printToGui, conn)

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "uid为空")
            msg_box.show()
            msg_box.exec_()

    # 自动批量改名
    @pyqtSlot()
    def click_btnAutoChangeName(self):
        pass



# 微博自动评论
class WeiboAutoComment(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博自动刷评系统')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboLink = QLineEdit("")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        # 生成账号组下拉菜单
        self.generate_combo()
        # 生成评论数下拉菜单
        self.generate_comment_count_combo()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        lblTitle = QLabel("微博链接:")
        btnInsure = QPushButton("确定开始", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        mainLayout = QGridLayout()
        mainLayout.addWidget(lblTitle, 0, 0, 1, 1)
        mainLayout.addWidget(self.inputWeiboLink, 0, 1, 1, 5)
        mainLayout.addWidget(self.accout_group_combo, 0, 6, 1, 2)
        mainLayout.addWidget(self.comment_count_combo, 0, 8, 1, 1)
        mainLayout.addWidget(btnInsure, 0, 9, 1, 1)
        mainLayout.addWidget(self.outputResult, 1, 0, 1, 10)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    def generate_combo(self):
        self.accout_group_combo = QComboBox()
        for i in range(0, self.accout_group_combo.count()):
            self.accout_group_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accout_group_combo.addItem(accountgroup_list[i][1])

    def generate_comment_count_combo(self):
        self.comment_count_combo = QComboBox()
        for i in range(1, 26):
            self.comment_count_combo.addItem(str(i))

    @pyqtSlot()
    def click_btnInsure(self):
        if (self.inputWeiboLink.text() != ""):
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            use_cookies = []
            for i in range(0, len(cookies_list)):
                if(cookies_list[i][6] == self.accout_group_combo.currentText()):
                    use_cookies.append(cookies_list[i][4])
                else:
                    pass
            try:
                auto_comment_func(self.inputWeiboLink.text(), use_cookies, self.comment_count_combo.currentIndex()+1, self.printToGui, conn)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
                msg_box.show()
                msg_box.exec_()

            self.generate_combo()
            self.inputWeiboLink.setText("")
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "微博链接为空")
            msg_box.show()
            msg_box.exec_()

# 微博自动点赞
class WeiboAutoLike(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博自动点赞系统')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboLink = QLineEdit("")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        # 生成账号组下拉菜单
        self.generate_combo()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        lblTitle = QLabel("微博链接:")
        btnInsure = QPushButton("开始点赞", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        mainLayout = QGridLayout()
        mainLayout.addWidget(lblTitle, 0, 0, 1, 1)
        mainLayout.addWidget(self.inputWeiboLink, 0, 1, 1, 5)
        mainLayout.addWidget(self.accout_group_combo, 0, 6, 1, 3)
        mainLayout.addWidget(btnInsure, 0, 9, 1, 1)
        mainLayout.addWidget(self.outputResult, 1, 0, 1, 10)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    def generate_combo(self):
        self.accout_group_combo = QComboBox()
        for i in range(0, self.accout_group_combo.count()):
            self.accout_group_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accout_group_combo.addItem(accountgroup_list[i][1])

    @pyqtSlot()
    def click_btnInsure(self):
        if (self.inputWeiboLink.text() != ""):
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            use_cookies = []
            for i in range(0, len(cookies_list)):
                if(cookies_list[i][6] == self.accout_group_combo.currentText()):
                    use_cookies.append(cookies_list[i][4])
                else:
                    pass
            try:
                auto_like(self.inputWeiboLink.text(), use_cookies, self.printToGui, conn)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
                msg_box.show()
                msg_box.exec_()
            self.generate_combo()
            self.inputWeiboLink.setText("")
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "微博链接为空")
            msg_box.show()
            msg_box.exec_()

# 自动发布微博
class WeiboAutoPost(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('自动发微博系统')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboContent = QTextEdit("")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        # 生成账号组下拉菜单
        self.generate_combo()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        lblTitle = QLabel("微博内容:")
        btnInsure = QPushButton("确定发布", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        mainLayout = QGridLayout()
        mainLayout.addWidget(lblTitle, 0, 0, 1, 1)
        mainLayout.addWidget(self.inputWeiboContent, 0, 1, 1, 5)
        mainLayout.addWidget(self.accout_group_combo, 0, 6, 1, 2)
        mainLayout.addWidget(btnInsure, 0, 8, 1, 1)
        mainLayout.addWidget(self.outputResult, 1, 0, 1, 9)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    def generate_combo(self):
        self.accout_group_combo = QComboBox()
        for i in range(0, self.accout_group_combo.count()):
            self.accout_group_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accout_group_combo.addItem(accountgroup_list[i][1])

    @pyqtSlot()
    def click_btnInsure(self):
        if (self.inputWeiboContent.toPlainText() != ""):
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            use_cookies = []
            for i in range(0, len(cookies_list)):
                if(cookies_list[i][6] == self.accout_group_combo.currentText()):
                    use_cookies.append(cookies_list[i][4])
                else:
                    pass
            try:
                auto_post_weibo(use_cookies, self.inputWeiboContent.toPlainText(), self.printToGui, conn)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
                msg_box.show()
                msg_box.exec_()
            self.generate_combo()
            self.inputWeiboContent.setText("")
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "微博内容为空")
            msg_box.show()
            msg_box.exec_()


# 自动转发微博
class WeiboAutoRepost(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博自动转发系统')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.inputWeiboLink = QLineEdit("")
        self.inputTopic = QLineEdit("")
        self.inputTopic.setPlaceholderText("转发内容")
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        # 生成账号组下拉菜单
        self.generate_combo()
        # 生成转发数下拉菜单
        self.generate_repost_count_combo()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        lblTitle = QLabel("微博链接:")
        btnInsure = QPushButton("确定开始", self)
        btnInsure.clicked.connect(self.click_btnInsure)
        mainLayout = QGridLayout()
        mainLayout.addWidget(lblTitle, 0, 0, 1, 1)
        mainLayout.addWidget(self.inputWeiboLink, 0, 1, 1, 5)
        mainLayout.addWidget(self.accout_group_combo, 0, 6, 1, 2)
        mainLayout.addWidget(self.repost_count_combo, 0, 8, 1, 1)
        mainLayout.addWidget(self.inputTopic, 1, 0, 1, 6)
        mainLayout.addWidget(btnInsure, 1, 6, 1, 3)
        mainLayout.addWidget(self.outputResult, 2, 0, 1, 9)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    def generate_combo(self):
        self.accout_group_combo = QComboBox()
        for i in range(0, self.accout_group_combo.count()):
            self.accout_group_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accout_group_combo.addItem(accountgroup_list[i][1])

    def generate_repost_count_combo(self):
        self.repost_count_combo = QComboBox()
        for i in range(1, 11):
            self.repost_count_combo.addItem(str(i))

    @pyqtSlot()
    def click_btnInsure(self):
        if (self.inputWeiboLink.text() != ""):
            c = conn.cursor()
            cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
            use_cookies = []
            for i in range(0, len(cookies_list)):
                if(cookies_list[i][6] == self.accout_group_combo.currentText()):
                    use_cookies.append(cookies_list[i][4])
                else:
                    pass
            try:
                auto_repost_func(self.inputWeiboLink.text(), self.inputTopic.text(), use_cookies, self.repost_count_combo.currentIndex()+1, self.printToGui, conn)
            except Exception as e:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
                msg_box.show()
                msg_box.exec_()
            self.generate_combo()
            self.inputWeiboLink.setText("")
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "微博链接为空")
            msg_box.show()
            msg_box.exec_()

# 超新星全运会打榜
class WeiboSuperStar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('超新星全运会打榜操作')
        self.setMaximumSize(600, 400)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)
        self.setFixedSize(600, 400)
        #设置图标
        icon = QIcon()
        icon.addPixmap(QPixmap("favicon.ico"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.outputResult = QTextEdit("")
        self.outputResult.setReadOnly(True)
        # 生成账号组下拉菜单
        self.generate_combo()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 600, 400)
        btnPostWeibo = QPushButton("发微博", self)
        btnPostWeibo.clicked.connect(self.click_btnPostWeibo)
        btnRepostWeibo = QPushButton("去转发", self)
        btnRepostWeibo.clicked.connect(self.click_btnRepostWeibo)
        btnCheerCard = QPushButton("加油卡", self)
        btnCheerCard.clicked.connect(self.click_btnCheerCard)
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.accout_group_combo, 0, 0, 1, 2)
        mainLayout.addWidget(btnPostWeibo, 0, 2, 1, 1)
        mainLayout.addWidget(btnRepostWeibo, 0, 3, 1, 1)
        mainLayout.addWidget(btnCheerCard, 0, 4, 1, 1)
        mainLayout.addWidget(self.outputResult, 1, 0, 1, 5)
        self.setLayout(mainLayout)

    def printToGui(self, text):
        self.outputResult.append(text)

    def generate_combo(self):
        self.accout_group_combo = QComboBox()
        for i in range(0, self.accout_group_combo.count()):
            self.accout_group_combo.removeItem(0)
        c = conn.cursor()
        accountgroup_list = c.execute("SELECT * FROM WeiboAccountGroup").fetchall()
        for i in range(0, len(accountgroup_list)):
            self.accout_group_combo.addItem(accountgroup_list[i][1])

    # 发微博
    @pyqtSlot()
    def click_btnPostWeibo(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        use_cookies = []
        for i in range(0, len(cookies_list)):
            if (cookies_list[i][6] == self.accout_group_combo.currentText()):
                use_cookies.append(cookies_list[i][4])
            else:
                pass
        try:
            post_weibo(use_cookies, self.printToGui)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
            msg_box.show()
            msg_box.exec_()

    # 转发微博
    @pyqtSlot()
    def click_btnRepostWeibo(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        up_down = self.accout_group_combo.currentText().split("-")
        use_cookies = []
        for i in range(0, len(cookies_list)):
            if (cookies_list[i][6] == self.accout_group_combo.currentText()):
                use_cookies.append(cookies_list[i][4])
            else:
                pass
        try:
            repost_weibo(use_cookies, self.printToGui)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
            msg_box.show()
            msg_box.exec_()

    # 加油卡
    @pyqtSlot()
    def click_btnCheerCard(self):
        c = conn.cursor()
        cookies_list = c.execute("SELECT * FROM WeiboCookies").fetchall()
        up_down = self.accout_group_combo.currentText().split("-")
        use_cookies = []
        for i in range(0, len(cookies_list)):
            if (cookies_list[i][6] == self.accout_group_combo.currentText()):
                use_cookies.append(cookies_list[i][4])
            else:
                pass
        try:
            cheer_card(use_cookies, self.printToGui)
        except Exception as e:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", str(e))
            msg_box.show()
            msg_box.exec_()
            exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = MainWindow()
    sys.exit(app.exec_())

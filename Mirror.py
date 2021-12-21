# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirror.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Juzhong import *
from Fuwocheng import *
from Shendun import *
from Jingzi import *
import requests
import json
from PyQt5.QtCore import *
import time
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

class Mirror(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Mirror, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def fuwocheng(self):
        self.fwc = Fuwocheng()
        self.fwc.show()


    def shendun(self):
        self.sd = Shendun()
        self.sd.show()

    def juzhong(self):
        self.ftd = Juzhong()
        self.ftd.show()

    def jingzi(self):
        self.jz = Jingzi()
        self.jz.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 917)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-image: url(./fuwocheng.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 300, 150, 80))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 300, 150, 80))
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 300, 150, 80))
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 440, 200, 100))
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_4.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_4.setObjectName("pushButton_4")

        self.Timer = QTimer()
        self.Timer.start(500) #0.5s
        self.Timer.timeout.connect(self.updateTime)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 251, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 131, 61))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:transparent;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 70, 211, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(26)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:transparent;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 140, 131, 61))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:transparent;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 580, 201, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(32)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 670, 191, 51))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 740, 191, 51))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(20)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 810, 191, 51))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(20)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #链接关系
        self.pushButton.clicked.connect(self.fuwocheng) 
        self.pushButton_2.clicked.connect(self.shendun) 
        self.pushButton_3.clicked.connect(self.juzhong) 
        self.pushButton_4.clicked.connect(self.jingzi) 
        
    def updateTime(self):
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt; color:#ffffff;\">" + QDateTime.currentDateTime().toString('hh:mm:ss') + "</span></p></body></html>"))

    def retranslateUi(self, MainWindow):
        
        #天气
        weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=北京"  # 将链接定义为一个字符串
        response = requests.get(weatherJsonUrl)  # 获取并下载页面，其内容会保存在respons.text成员变量里面
        response.raise_for_status()  # 这句代码的意思如果请求失败的话就会抛出异常，请求正常就上面也不会做
        # 将json文件格式导入成python的格式
        weatherData = json.loads(response.text)
        gaowen = str(weatherData['data']['forecast'][0]['high'])+"   "
        diwen = str(weatherData['data']['forecast'][0]['low'])+"   "
        tianqi = str(weatherData['data']['forecast'][0]['type'])+"   "

        #时间
        now_date = time.strftime("%Y-%m-%d")
        now_week = time.strftime("%A")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "魔镜"))
        self.pushButton.setText(_translate("MainWindow", "俯卧撑"))
        self.pushButton_2.setText(_translate("MainWindow", "深蹲"))
        self.pushButton_3.setText(_translate("MainWindow", "举重"))
        self.pushButton_4.setText(_translate("MainWindow", "镜子模式"))
        # self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">"+timee+"</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt; color:#ffffff;\">" + now_date + "</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">" + now_week + "</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">" + "最" + gaowen + "</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">" + "最" + diwen + "</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">" + tianqi + "</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">今日事项</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "俯卧撑50个"))
        self.checkBox_2.setText(_translate("MainWindow", "深蹲20个"))
        self.checkBox_3.setText(_translate("MainWindow", "举重20个"))




if __name__ == '__main__':   
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)  # 定义Qt应用
    MainWindow = QtWidgets.QMainWindow()  # 窗口实例
    ui = Mirror()  # 界面UI实例
    ui.setupUi(MainWindow)  # 绘制界面
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # 应用关闭
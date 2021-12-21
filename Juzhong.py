import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time

class Juzhong(QtWidgets.QMainWindow):
    def __init__(self):
        super(Juzhong, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    
    #####提示函数#####
    def f1(self):
        self.s = "sssssss"

    def setupUi(self, MainWindow):
        
        ###执行提示函数###
        self.f1()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 909)

        ###设置背景###
        MainWindow.setStyleSheet("QWidget{background-color:#000000;}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ###标准动作播放###
        self.labelx = QtWidgets.QLabel(MainWindow)
        self.labelx.setGeometry(QtCore.QRect(70, 213, 500, 300))
        self.labelx.setObjectName("label")

        self.gif = QMovie('juzhong.gif')
        self.labelx.setMovie(self.gif)
        self.gif.start()
        
        ###时间###
        self.Timer = QTimer()
        self.Timer.start(500) #0.5s
        self.Timer.timeout.connect(self.updateTime)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 0, 221, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        ###日期###
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 70, 251, 71))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        ###星期###
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 140, 131, 61))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")

        ###模式###
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(5, 25, 300, 150))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        
        ###提示###
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 560, 491, 311))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n""background-color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
    def updateTime(self):
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt; color:#ffffff;\">" + QDateTime.currentDateTime().toString('hh:mm:ss') + "</span></p></body></html>"))

    def retranslateUi(self, MainWindow):
        #时间
        now_date = time.strftime("%Y-%m-%d")
        now_week = time.strftime("%A")
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "举重"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">" + now_date + "</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">" + now_week + "</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">现在是‘举重’模式！</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">" + self.s + "</span></p></body></html>"))

      
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)  # 定义Qt应用
    MainWindow = QtWidgets.QMainWindow()  # 窗口实例
    ui = Juzhong()  # 界面UI实例
    ui.setupUi(MainWindow)  # 绘制界面
    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # 应用关闭 
 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__main__\Python\photo puzzle\design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 420)
        MainWindow.setMinimumSize(QtCore.QSize(810, 420))
        MainWindow.setMaximumSize(QtCore.QSize(810, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_Button = QtWidgets.QPushButton(self.centralwidget)
        self.file_Button.setGeometry(QtCore.QRect(40, 40, 130, 30))
        self.file_Button.setObjectName("file_Button")
        self.folder_Button = QtWidgets.QPushButton(self.centralwidget)
        self.folder_Button.setGeometry(QtCore.QRect(40, 110, 130, 30))
        self.folder_Button.setObjectName("folder_Button")
        self.ren_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ren_Button.setGeometry(QtCore.QRect(60, 300, 260, 30))
        self.ren_Button.setObjectName("ren_Button")
        self.file_Label = QtWidgets.QLabel(self.centralwidget)
        self.file_Label.setGeometry(QtCore.QRect(190, 40, 150, 30))
        self.file_Label.setObjectName("file_Label")
        self.folde_Label = QtWidgets.QLabel(self.centralwidget)
        self.folde_Label.setGeometry(QtCore.QRect(190, 110, 150, 30))
        self.folde_Label.setObjectName("folde_Label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 360, 360))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_Button.setText(_translate("MainWindow", "Открыть картинку"))
        self.folder_Button.setText(_translate("MainWindow", "Указать папку"))
        self.ren_Button.setText(_translate("MainWindow", "Преобразовать"))
        self.file_Label.setText(_translate("MainWindow", "Имя файла"))
        self.folde_Label.setText(_translate("MainWindow", "Путь к папке"))


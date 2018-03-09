#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:


    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig,
                _encoding)


except AttributeError:


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_browse(object):

    def setupUi(self, browse):
        browse.setObjectName(_fromUtf8('browse'))
        browse.resize(800, 600)
        self.centralwidget = QtGui.QWidget(browse)
        self.centralwidget.setObjectName(_fromUtf8('centralwidget'))
        self.pushButton = QtGui.QPushButton(self.centralwidget)#Browse Button
        self.pushButton.setGeometry(QtCore.QRect(270, 380, 88, 27))
        self.pushButton.setObjectName(_fromUtf8('pushButton'))
        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 380, 211, 27))
        self.lineEdit.setText(_fromUtf8(''))
        self.lineEdit.setObjectName(_fromUtf8('lineEdit'))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)#Begin Button
        self.pushButton_2.setGeometry(QtCore.QRect(270, 460, 88, 27))
        self.pushButton_2.setObjectName(_fromUtf8('pushButton_2'))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)#View Summary Button
        self.pushButton_3.setGeometry(QtCore.QRect(480, 460, 88, 27))
        self.pushButton_3.setObjectName(_fromUtf8('pushButton_3'))
        
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)#Output Box
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 601, 300))
        self.lineEdit_2.setText(_fromUtf8(''))
        self.lineEdit_2.setObjectName(_fromUtf8('lineEdit_2'))
        
        browse.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(browse)
        self.statusbar.setObjectName(_fromUtf8('statusbar'))
        browse.setStatusBar(self.statusbar)

        self.retranslateUi(browse)
        QtCore.QMetaObject.connectSlotsByName(browse)

    def retranslateUi(self, browse):
        browse.setWindowTitle(_translate('browse', 'Audio File To Speech', None))
        self.pushButton.setText(_translate('browse', 'Browse', None))
        self.pushButton_2.setText(_translate('browse', 'Begin', None))
        self.pushButton_3.setText(_translate('browse', 'Summary', None))
        self.pushButton.clicked.connect(lambda:self.open())

    def open(self):
    	filename = QtGui.QFileDialog.getOpenFileName(None, 'Open File', ' ', "Audio files (*.mp3 *.wav *.flac)")
        self.lineEdit.setText(filename)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    browse = QtGui.QMainWindow()
    ui = Ui_browse()
    ui.setupUi(browse)
    browse.show()
    sys.exit(app.exec_())

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import audio_file_streaming
from subprocess import call
from PyQt4 import QtCore, QtGui
import sys
import os
import json
import requests
def getSummary(text):
    f = open('summary.txt', 'w')
    #print (text)
    text = str(text)
    r = requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': text,
        },
        headers={'api-key': '418a9720-2b4c-4331-90c0-7b6d48236b59'}
    )
    if r.status_code == 200:
        f.write(r.json()['output'])
    else:
        f.write('Summary Could not be generated. Data invalid')
    f.close()
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

    def browseShow(self):
        getSummary(self.lineEdit_2.toPlainText())
        call(["python2", "summary.py"])

    def transcript(self):
        path_to_file = self.lineEdit.toPlainText()
        output = audio_file_streaming.transcribe_streaming(str(path_to_file))
        self.lineEdit_2.setText(output)
        f = open('tone_output.txt' , 'r')
        strs = f.read()
        print strs
        self.lineEdit_3.setText(strs)
        f.close()


    def setupUi(self, browse):
        browse.setObjectName(_fromUtf8('browse'))
        browse.resize(800, 600)
        self.centralwidget = QtGui.QWidget(browse)
        self.centralwidget.setObjectName(_fromUtf8('centralwidget'))
        self.pushButton = QtGui.QPushButton(self.centralwidget)#Browse Button
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 88, 27))
        self.pushButton.setObjectName(_fromUtf8('pushButton'))
        self.pushButton.clicked.connect(lambda:self.open())
        
        self.lineEdit = QtGui.QTextEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 240, 200, 27))
        self.lineEdit.setText(_fromUtf8(''))
        self.lineEdit.setObjectName(_fromUtf8('lineEdit'))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)#Begin Button
        self.pushButton_2.setGeometry(QtCore.QRect(270, 300, 88, 27))
        self.pushButton_2.setObjectName(_fromUtf8('pushButton_2'))
        self.pushButton_2.clicked.connect(lambda:self.transcript())

        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)#View Summary Button
        self.pushButton_3.setGeometry(QtCore.QRect(480, 300, 88, 27))
        self.pushButton_3.setObjectName(_fromUtf8('pushButton_3'))
        self.pushButton_3.clicked.connect(lambda:self.browseShow())
        
        
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)#save transcript Button
        self.pushButton_4.setGeometry(QtCore.QRect(350, 340, 88, 27))
        self.pushButton_4.setObjectName(_fromUtf8('pushButton_4'))
        self.pushButton_4.clicked.connect(lambda:self.saver())
        

        self.lineEdit_2 = QtGui.QTextEdit(self.centralwidget)#Output Box
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 601, 200))
        self.lineEdit_2.setText(_fromUtf8(''))
        self.lineEdit_2.setObjectName(_fromUtf8('lineEdit_2'))

        self.lineEdit_3 = QtGui.QTextEdit(self.centralwidget)#Tone Box
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 400 , 601, 200))
        self.lineEdit_3.setText('Tone output will be displayed here')
        self.lineEdit_3.setObjectName(_fromUtf8('lineEdit_3'))
        
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
        self.pushButton_4.setText(_translate('browse', 'Save', None))


    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Open File', ' ', "Audio files (*.mp3 *.wav *.flac)")
        self.lineEdit.setText(filename)

    def saver(self):
        filename = QtGui.QFileDialog.getSaveFileName(None, 'Open File', ' ', "Text files (*.txt)")
        f = open(filename,'w')

        f.write(str(self.lineEdit_2.toPlainText()))
        ##print str(self.realtime_output.toPlainText())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    browse = QtGui.QMainWindow()
    ui = Ui_browse()
    ui.setupUi(browse)
    browse.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stream.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
import requests
import json

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
    print (r)
    f.write(r.json()['output'])
    f.close()

from subprocess import call

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_stream(QtGui.QMainWindow):
    def browseShow(self):
        getSummary(self.realtime_output.toPlainText())

        call(["python2", "summary.py"])

    def dataReady(self):
        self.realtime_output.clear()
        cursor = self.realtime_output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.realtime_output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start('python2',['speech_tone/speech_main.py'])
        #self.process.start('ping',['localhost'])

    def setupUi(self, stream):
        stream.setObjectName(_fromUtf8("stream"))
        stream.resize(800, 600)
        self.centralwidget = QtGui.QWidget(stream)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.convert_button = QtGui.QPushButton(self.centralwidget)#start button
        self.convert_button.setGeometry(QtCore.QRect(260, 180, 88, 27))
        self.convert_button.setObjectName(_fromUtf8("convert_button"))
        
        self.realtime_output = QtGui.QTextEdit(self.centralwidget)#realtime output
        self.realtime_output.setGeometry(QtCore.QRect(80, 70, 641, 100))
        self.realtime_output.setObjectName(_fromUtf8("realtime_output"))
        
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)#View Summary Button
        self.pushButton_3.setGeometry(QtCore.QRect(420, 180, 88, 27))
        self.pushButton_3.setObjectName(_fromUtf8('pushButton_3'))
        

        self.tone_output = QtGui.QTextEdit(self.centralwidget)#realtime output
        self.tone_output.setGeometry(QtCore.QRect(80, 380 , 641, 100))
        self.tone_output.setObjectName(_fromUtf8("tone_output"))
        self.tone_output.setText('Tone output will be shown here')
        
        stream.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(stream)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        stream.setStatusBar(self.statusbar)

        self.retranslateUi(stream)
        QtCore.QMetaObject.connectSlotsByName(stream)
        # PARALLEL OUTPUT PART
        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.convert_button.clicked.connect(self.callProgram)
        self.process.started.connect(lambda: self.convert_button.setEnabled(False))
        self.process.finished.connect(lambda: self.finished_transcript())

        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(290, 230, 200, 27))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.saveButton.setText(_translate('saveButton' , 'Save Transcription' , None))


    def retranslateUi(self, stream):
        stream.setWindowTitle(_translate("stream", "MainWindow", None))
        self.convert_button.setText(_translate("stream", "Start", None))
        self.pushButton_3.setText(_translate('View Summary', 'Summary', None))

    def finished_transcript(self):
        self.pushButton_3.clicked.connect(lambda:self.browseShow())
        f = open('tone_output.txt' , 'r')
        self.tone_output.setText(f.read())
        f.close()
        self.convert_button.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    stream = QtGui.QMainWindow()
    ui = Ui_stream()
    ui.setupUi(stream)
    stream.show()
    sys.exit(app.exec_())


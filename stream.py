# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stream.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_stream(object):
    def setupUi(self, stream):
        stream.setObjectName(_fromUtf8("stream"))
        stream.resize(800, 600)
        self.centralwidget = QtGui.QWidget(stream)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.convert_button = QtGui.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(360, 330, 88, 27))
        self.convert_button.setObjectName(_fromUtf8("convert_button"))
        self.realtime_output = QtGui.QTextEdit(self.centralwidget)
        self.realtime_output.setGeometry(QtCore.QRect(80, 70, 641, 241))
        self.realtime_output.setObjectName(_fromUtf8("realtime_output"))
        stream.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(stream)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        stream.setStatusBar(self.statusbar)

        self.retranslateUi(stream)
        QtCore.QMetaObject.connectSlotsByName(stream)

    def retranslateUi(self, stream):
        stream.setWindowTitle(_translate("stream", "MainWindow", None))
        self.convert_button.setText(_translate("stream", "Start", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    stream = QtGui.QMainWindow()
    ui = Ui_stream()
    ui.setupUi(stream)
    stream.show()
    sys.exit(app.exec_())


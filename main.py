# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from subprocess import call
from PyQt4 import QtCore, QtGui
from stream import Ui_stream
from browse import Ui_browse
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

class Ui_Dialog(object):
	def streamShow(self):
		call(["python2", "stream.py"])
	
	def browseShow(self):
		call(["python2", "browse.py"])
	
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(554, 474)
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(240, 340, 88, 27))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.radioButton = QtGui.QRadioButton(Dialog)
		self.radioButton.setGeometry(QtCore.QRect(230, 160, 106, 23))
		self.radioButton.setObjectName(_fromUtf8("radioButton"))
		self.radioButton_2 = QtGui.QRadioButton(Dialog)
		self.radioButton_2.setGeometry(QtCore.QRect(230, 200, 106, 23))
		self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def update(self):
		self.pushButton.setEnabled(True)
	
	def process_choice(self):
		if self.radioButton.isChecked() == 1:
			self.browseShow()
		else:
			self.streamShow()

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.pushButton.setText(_translate("Dialog", "Start", None))
		self.radioButton.setText(_translate("Dialog", "Browse File", None))
		self.radioButton_2.setText(_translate("Dialog", "Live Stream", None))
		self.radioButton.clicked.connect(lambda:self.update())
		self.radioButton_2.clicked.connect(lambda:self.update())
		self.pushButton.setEnabled(False)
		self.pushButton.clicked.connect(lambda:self.process_choice())

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Dialog = QtGui.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())


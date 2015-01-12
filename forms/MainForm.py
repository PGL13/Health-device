# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, Qt
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
class mainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(495, 344)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 290, 118, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(280, -20, 194, 22))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 451, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 20, 101, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 451, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 451, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 190, 451, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.groupBox_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(280, 10, 101, 51))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Температура", None))
        self.groupBox.setTitle(_translate("MainWindow", "Идентификация", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Алкоголь", None))
 
def init(token,temperature,alcohol):
	app = QtGui.QApplication(sys.argv)
	MainWindow=QtGui.QMainWindow()
	form=mainWindow()
	form.setupUi(MainWindow)
	#step
	form.progressBar.setProperty("value", token)
	#temperature
	form.lcdNumber.setProperty("value",temperature)
	#alcohol
	form.lcdNumber_2.setProperty("value",alcohol)
	#MainWindow.show()
	#sys.exit(app.exec_())
	return app, form, MainWindow
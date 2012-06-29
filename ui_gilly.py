# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gilly.ui'
#
# Created: Sat May 26 23:18:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GillyCricket(object):
    def setupUi(self, GillyCricket):
        GillyCricket.setObjectName(_fromUtf8("GillyCricket"))
        GillyCricket.resize(800, 600)
        self.centralwidget = QtGui.QWidget(GillyCricket)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.GillyText = QtGui.QTextEdit(self.centralwidget)
        self.GillyText.setEnabled(True)
        self.GillyText.setReadOnly(True)
        self.GillyText.setObjectName(_fromUtf8("GillyText"))
        self.gridLayout.addWidget(self.GillyText, 0, 0, 1, 1)
        GillyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GillyCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGilly_Cricket = QtGui.QMenu(self.menubar)
        self.menuGilly_Cricket.setObjectName(_fromUtf8("menuGilly_Cricket"))
        GillyCricket.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(GillyCricket)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        GillyCricket.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout = QtGui.QAction(GillyCricket)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(GillyCricket)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/img/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtGui.QAction(GillyCricket)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/img/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon1)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.menuGilly_Cricket.addAction(self.actionRefresh)
        self.menuGilly_Cricket.addAction(self.actionAbout)
        self.menuGilly_Cricket.addSeparator()
        self.menuGilly_Cricket.addAction(self.actionExit)
        self.menubar.addAction(self.menuGilly_Cricket.menuAction())
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(GillyCricket)
        QtCore.QMetaObject.connectSlotsByName(GillyCricket)

    def retranslateUi(self, GillyCricket):
        GillyCricket.setWindowTitle(QtGui.QApplication.translate("GillyCricket", "Gilly Cricket", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGilly_Cricket.setTitle(QtGui.QApplication.translate("GillyCricket", "Gilly Cricket", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("GillyCricket", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("GillyCricket", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("GillyCricket", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("GillyCricket", "Fetch Latest", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setShortcut(QtGui.QApplication.translate("GillyCricket", "R", None, QtGui.QApplication.UnicodeUTF8))

import gilly_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GillyCricket = QtGui.QMainWindow()
    ui = Ui_GillyCricket()
    ui.setupUi(GillyCricket)
    GillyCricket.show()
    sys.exit(app.exec_())


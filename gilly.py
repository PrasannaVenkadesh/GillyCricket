#!/usr/bin/python

from PyQt4 import QtCore,QtGui
from ui_gilly import Ui_GillyCricket
from cricbuzz import *
import sys

class GillyApp(QtGui.QMainWindow,Ui_GillyCricket):
    def __init__(self,parent = None):
        super(GillyApp,self).__init__(parent)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.exitapp)
        self.actionRefresh.triggered.connect(self.refresh)
        self.refresh()

    def refresh(self):
        cric = CricbuzzParser()
        match = cric.getXml()
        details = cric.handleMatches(match) #Returns Match details as a Dictionary. Parse it according to requirements.
        self.GillyText.setText("")
        for detail in details:
            if type(detail) is dict:
                for keys in detail:
                    if detail[keys]!=None and detail[keys]!='':
                        self.GillyText.append(keys+":"+ str(detail[keys]))
                self.GillyText.append("\n")

    def exitapp(self):
        sys.exit(0)
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gc = GillyApp()
    gc.show()
    app.exec_()

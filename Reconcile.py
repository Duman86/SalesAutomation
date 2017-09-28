# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'SalesForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Input2DB import PA
import datetime

class SalesForm(QtWidgets.QWidget):
    
    def __init__(self):
        super(SalesForm,self).__init__()
        self.Checkup=[] 
        self.CheckupKeys=[]
        
        self.I2DB=PA()
        self.setGeometry(300,300,843,500)

        self.lineEdit=QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(700, 30, 113, 20))
        
        self.pushButton = QtWidgets.QPushButton(self) 
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 141, 61))
        self.pushButton.clicked.connect(self.RecordSales)
        self.pushButton.setText("OK")

        self.pushButton_2 = QtWidgets.QPushButton(self)        
        self.pushButton_2.setGeometry(QtCore.QRect(210, 350, 141, 61))
        self.pushButton_2.setText("Cancel")
       
                
        self.show()
        
    def keyPressEvent(self, e):
        
        if e.key()==16777220:                     
            self.Checkup.append(self.lineEdit.text())
            self.lineEdit.setText('')
           
        
        
    def RecordSales(self):
        num=[]
        keys=[]
        
        self.Checkup=['8710732217127', '8710732217127', '8710732217127', '8710732217127',
                      '8710732217127', '8710732217127', '9556412600006', '9556412600006',
                      '9556412600006', '9556412600006', '9556412600006']

        for i in self.Checkup:
            if not i in keys:
                num.append(self.Checkup.count(i))
                keys.append(i)
                
        print(list(zip(keys,num)))
            

       
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = SalesForm()
    sys.exit(app.exec_())



  


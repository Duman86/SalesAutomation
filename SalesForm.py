# -*- coding: utf-8 -*-
'''   
    def keyPressEvent(self,event):
        if e.key() == QtCore.Qt.Key_Escape:
            
            self.close()

        if e.key()==QtCore.Qt.Key_Return:
            print(self.BarcodeValue)
            self.BarcodeValue=''
        else:
            self.BarcodeValue+=chr(e.key())'''


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

        self.Reader=''
        
        self.I2DB=PA()
        self.setGeometry(300,300,843,500)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.resizeColumnsToContents()
        
        self.tableWidget.setGeometry(QtCore.QRect(40, 10, 620, 281))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
       
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        
        
        self.tableWidget.setHorizontalHeaderLabels(['Штрихкод', 'Примечание', 'Цена', 'Количество', 'Итого'])
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setRowCount(1)
        
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(0,i,QtWidgets.QTableWidgetItem(''))
            
        self.tableWidget.cellChanged.connect(self.cellchanged)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.lineEdit=QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(700, 30, 113, 20))
        

        
        self.pushButton = QtWidgets.QPushButton(self) 
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 141, 61))
        self.pushButton.clicked.connect(self.RecordSales)
        self.pushButton.setText("OK")

        self.pushButton_2 = QtWidgets.QPushButton(self)        
        self.pushButton_2.setGeometry(QtCore.QRect(210, 350, 141, 61))
        self.pushButton_2.setText("Cancel")
        self.pushButton_2.clicked.connect(self.ClearSales)
        
        
        self.show()
        
    def cellchanged(self):
        pass


    def keyPressEvent(self, e):

        if e.key()==16777220:
            print("ENter pressed")
            self.GetDataFromDB()
            self.Reader=''
            self.lineEdit.setText('')
           
        else:
            self.Reader+=chr(e.key())
        

    def AddRow(self):
        self.RCount=self.tableWidget.rowCount()+1
        self.tableWidget.setRowCount(self.RCount)
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(self.RCount-1,i,QtWidgets.QTableWidgetItem(''))
        
    def GetDataFromDB(self):
        try :
                        
            #DataStock=self.I2DB.ExtData(str(self.tableWidget.item(self.tableWidget.rowCount()-1, 0).text()))
            DataStock=self.I2DB.ExtData(self.lineEdit.text())
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,0,QtWidgets.QTableWidgetItem(DataStock[1]))            
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,1,QtWidgets.QTableWidgetItem(DataStock[4]))
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,2,QtWidgets.QTableWidgetItem(str(DataStock[6])))
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,3,QtWidgets.QTableWidgetItem('1'))
            amount=int(self.tableWidget.item(self.tableWidget.rowCount()-1, 2).text())*int(self.tableWidget.item(self.tableWidget.rowCount()-1, 3).text())
            self.tableWidget.setItem(self.tableWidget.rowCount()-1,4,QtWidgets.QTableWidgetItem(str(amount)))
           
            self.AddRow()
            print(DataStock)
        except:
            print("Не правильно вели шрихкод или нет такой вещи в база данных")

    def ClearSales(self):

        for i in reversed(range(self.tableWidget.rowCount())):
            self.tableWidget.removeRow(i)

        self.tableWidget.setRowCount(1)

    def RecordSales(self):

              

        self.s=PA()

        for i in range(self.tableWidget.rowCount()-1):
            date=str(datetime.datetime.now()).split('.')
            sales=[]            
            sales=[date[0],
                   self.tableWidget.item(i, 0).text(),
                   int(self.tableWidget.item(i, 3).text()),
                   int(self.tableWidget.item(i, 2).text())]
            
            self.s.SalesRec(sales)
        self.ClearSales()
       

        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = SalesForm()
    sys.exit(app.exec_())



  


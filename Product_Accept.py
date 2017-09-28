# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Product_Accept.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Input2DB import PA
import datetime

class Ui_ProductAccept(object):
    def setupUi(self, ProductAccept):
        ProductAccept.setObjectName("ProductAccept")
        ProductAccept.resize(745, 665)
        ProductAccept.setMinimumSize(QtCore.QSize(745, 665))
        ProductAccept.setMaximumSize(QtCore.QSize(745, 665))
        self.lineEdit = QtWidgets.QLineEdit(ProductAccept)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(ProductAccept)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(ProductAccept)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(ProductAccept)
        self.label.setGeometry(QtCore.QRect(20, 34, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ProductAccept)
        self.label_2.setGeometry(QtCore.QRect(20, 61, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ProductAccept)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 47, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ProductAccept)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 47, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(ProductAccept)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(ProductAccept)
        self.label_5.setGeometry(QtCore.QRect(250, 10, 480, 640))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../PyQT5/Python.jpg"))
        self.label_5.setObjectName("label_5")
        self.Pict_Update = QtWidgets.QPushButton(ProductAccept)
        self.Pict_Update.setGeometry(QtCore.QRect(10, 260, 141, 41))
        self.Pict_Update.setObjectName("Pict_Update")
        self.Pict_Update.clicked.connect(self.PictureInsert)


        
        self.lineEdit_5 = QtWidgets.QLineEdit(ProductAccept)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(ProductAccept)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(ProductAccept)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.put_2_DB = QtWidgets.QPushButton(ProductAccept)
        self.put_2_DB.setGeometry(QtCore.QRect(10, 310, 141, 41))
        self.put_2_DB.setObjectName("put_2_DB")
        self.put_2_DB.clicked.connect(self.InputDB)
        
        self.label_8 = QtWidgets.QLabel(ProductAccept)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(ProductAccept)
        self.textEdit.setGeometry(QtCore.QRect(120, 180, 111, 71))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ProductAccept)
        QtCore.QMetaObject.connectSlotsByName(ProductAccept)
        
        # setting validator
        
        self.lineEdit_3.setValidator(QtGui.QIntValidator(0,1000))
        self.lineEdit_4.setValidator(QtGui.QIntValidator(0,100000))
        self.lineEdit_4.setValidator(QtGui.QIntValidator(0,100000))
        self.lineEdit_4.setValidator(QtGui.QIntValidator(0,100000))
        


        

    def retranslateUi(self, ProductAccept):
        _translate = QtCore.QCoreApplication.translate
        ProductAccept.setWindowTitle(_translate("ProductAccept", "Dialog"))
        self.label.setText(_translate("ProductAccept", "Группа"))
        self.label_2.setText(_translate("ProductAccept", "Тип"))
        self.label_3.setText(_translate("ProductAccept", "Количество"))
        self.label_4.setText(_translate("ProductAccept", "Цена"))
        self.Pict_Update.setText(_translate("ProductAccept", "Обновить снимок"))
        self.label_6.setText(_translate("ProductAccept", "Штрихкод"))
        self.label_7.setText(_translate("ProductAccept", "Введите данные"))
        self.put_2_DB.setText(_translate("ProductAccept", "Добавить в базу данных"))
        self.label_8.setText(_translate("ProductAccept", "Примечание"))

    def PictureInsert(self):
        print("Картина обновлена")
        pass

    def InputDB(self):
        # Переводим textEdit в LineEdit
        self.mynote=''        
        self.mytext=self.textEdit.toPlainText()
        for line in self.mytext.split('\n'):
            self.mynote=self.mynote+line+','
        # Проверка на пустые строки
        self.incoming=[(self.lineEdit_5.text(),self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text()), self.mynote]


        if '' in self.incoming[0]:
            self.label_7.setText("Fill all lines!!!")
        else: 
            self.c=PA()

            date=str(datetime.datetime.now()).split('.')

            self.c.Input2DB(date[0],self.lineEdit_5.text(),self.lineEdit.text(),self.lineEdit_2.text(),self.mynote,int(self.lineEdit_3.text()),int(self.lineEdit_4.text()))

            self.label_7.setText("Данные внесены")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.textEdit.setText('')
            
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductAccept = QtWidgets.QDialog()
    ui = Ui_ProductAccept()
    ui.setupUi(ProductAccept)
    ProductAccept.show()
    sys.exit(app.exec_())


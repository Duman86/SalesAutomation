# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'India_shop_Mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Product_Accept import Ui_ProductAccept
from SalesForm import SalesForm

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(675, 350)
        aboutDialog.setMinimumSize(QtCore.QSize(675, 350))
        aboutDialog.setMaximumSize(QtCore.QSize(675, 450))
        self.pushButton = QtWidgets.QPushButton(aboutDialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 201, 191))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.StoreWindow)
        
        self.pushButton_2 = QtWidgets.QPushButton(aboutDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 80, 201, 191))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.SaleWindow)

       
        self.pushButton_3 = QtWidgets.QPushButton(aboutDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 80, 201, 191))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(aboutDialog)
        self.label.setGeometry(QtCore.QRect(20, 270, 211, 71))
        self.label.setObjectName("label")
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.pushButton.raise_()

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "Индийский магазин"))
        self.pushButton.setText(_translate("aboutDialog", "Прием товара"))
        self.pushButton_2.setText(_translate("aboutDialog", "Продажи"))
        self.pushButton_3.setText(_translate("aboutDialog", "Ревизия"))
        self.label.setText(_translate("aboutDialog", "<html><head/><body><p>Разработчик Жумадилов Д.С.</p><p>Duman.Zhumadilov@gmail.com</p></body></html>"))

    def StoreWindow(self):
        self.SWin=QtWidgets.QDialog()
        self.ui=Ui_ProductAccept()
        self.ui.setupUi(self.SWin)
        self.SWin.show()
        
    def SaleWindow(self):
        self.SF=SalesForm()
        self.SF.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutDialog = QtWidgets.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())


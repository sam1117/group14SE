# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhhod\Desktop\group14SE\storeFront.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from driver  import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(935, 375)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(100, 100, 70, 17))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 120, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 140, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(100, 200, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(100, 180, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")

        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(100, 160, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(720, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(730, 50, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.onClickedRadioBtn)

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(730, 80, 111, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.onClickedRadioBtn)


        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(730, 110, 121, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(self.onClickedRadioBtn)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(checkOptions)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "shirt"))
        self.checkBox_2.setText(_translate("Dialog", "pants"))
        self.checkBox_3.setText(_translate("Dialog", "shoes"))
        self.checkBox_4.setText(_translate("Dialog", "jacket"))
        self.checkBox_5.setText(_translate("Dialog", "socks"))
        self.checkBox_6.setText(_translate("Dialog", "hat"))
        self.pushButton.setText(_translate("Dialog", "Purchase"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.radioButton.setText(_translate("Dialog", "Starkville Location"))
        self.radioButton_2.setText(_translate("Dialog", "Jackson Location"))
        self.radioButton_3.setText(_translate("Dialog", "Memphis Location"))

    def checkOptions(self):

    def onClickedRadioBtn(self):
        radioButton = self.radioButton
        radioButton_2 = self.radioButton_2
        radioButton_3 = self.radioButton_3


        if radioButton.isChecked():
            setLocation("Starkville_Location")

        if radioButton_2.isChecked():
            setLocation("Jackson_Location")

        if radioButton_3.isChecked():
            setLocation("Memphis_Location")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

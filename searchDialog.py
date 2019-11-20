# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mhhod\Desktop\group14SE\searchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_search(object):
    def setupUi(self, Dialog_search):
        Dialog_search.setObjectName("Dialog_search")
        Dialog_search.resize(592, 302)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_search)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 481, 111))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(Dialog_search)
        self.widget.setGeometry(QtCore.QRect(270, 250, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.cancel_search = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cancel_search.setFont(font)
        self.cancel_search.setCheckable(False)
        self.cancel_search.setObjectName("cancel_search")
        self.horizontalLayout.addWidget(self.cancel_search)
        self.widget1 = QtWidgets.QWidget(Dialog_search)
        self.widget1.setGeometry(QtCore.QRect(50, 40, 301, 72))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.searchID_radioButton = QtWidgets.QRadioButton(self.widget1)
        self.searchID_radioButton.setObjectName("searchID_radioButton")
        self.verticalLayout_2.addWidget(self.searchID_radioButton)
        self.searchDate_radioButton = QtWidgets.QRadioButton(self.widget1)
        self.searchDate_radioButton.setObjectName("searchDate_radioButton")
        self.verticalLayout_2.addWidget(self.searchDate_radioButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.widget1)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_search)
        QtCore.QMetaObject.connectSlotsByName(Dialog_search)

    def retranslateUi(self, Dialog_search):
        _translate = QtCore.QCoreApplication.translate
        Dialog_search.setWindowTitle(_translate("Dialog_search", "Search Transactions"))
        self.search.setText(_translate("Dialog_search", "Search"))
        self.cancel_search.setText(_translate("Dialog_search", "Cancel"))
        self.label.setText(_translate("Dialog_search", "Search Type"))
        self.searchID_radioButton.setText(_translate("Dialog_search", "Search by TransactionID"))
        self.searchDate_radioButton.setText(_translate("Dialog_search", "Search by Transaction Date"))
        self.label_2.setText(_translate("Dialog_search", "Search Criteria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_search = QtWidgets.QDialog()
    ui = Ui_Dialog_search()
    ui.setupUi(Dialog_search)
    Dialog_search.show()
    sys.exit(app.exec_())

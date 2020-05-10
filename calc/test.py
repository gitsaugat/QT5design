# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(352, 386)
        Calculator.setMinimumSize(QtCore.QSize(352, 386))
        Calculator.setMaximumSize(QtCore.QSize(352, 386))
        Calculator.setStyleSheet("QWidget{\n"
"   background-color :rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"QTextEdit{\n"
"   background-color :rgb(255, 255, 255);\n"
"  color : black;\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"   background-color :rgb(255, 179, 47);\n"
"  border-radius : 1px solid rgb(227, 227, 227) ;\n"
"  padding:5px;\n"
"  color:black;\n"
"\n"
" \n"
"}\n"
"QPushButton:pressed{\n"
"   background-color :rgb(255, 237, 162);\n"
"  color:black;\n"
" \n"
"}")
        self.pushButton = QtWidgets.QPushButton(Calculator)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Calculator)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Calculator)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 240, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Calculator)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 310, 61, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Calculator)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 110, 61, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Calculator)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 170, 61, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Calculator)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 240, 61, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Calculator)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 310, 61, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Calculator)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 110, 61, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Calculator)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 170, 61, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textEdit = QtWidgets.QTextEdit(Calculator)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 351, 75))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_11 = QtWidgets.QPushButton(Calculator)
        self.pushButton_11.setGeometry(QtCore.QRect(160, 310, 61, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Calculator)
        self.pushButton_12.setGeometry(QtCore.QRect(160, 240, 61, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Calculator)
        self.pushButton_13.setGeometry(QtCore.QRect(270, 110, 61, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Calculator)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 170, 61, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Calculator)
        self.pushButton_15.setGeometry(QtCore.QRect(270, 240, 61, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Calculator)
        self.pushButton_16.setGeometry(QtCore.QRect(270, 310, 61, 41))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Calculator)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 80, 311, 28))
        self.pushButton_17.setObjectName("pushButton_17")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.pushButton.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_10.setText(_translate("Calculator", "0"))
        self.pushButton_11.setText(_translate("Calculator", "."))
        self.pushButton_12.setText(_translate("Calculator", "Del"))
        self.pushButton_13.setText(_translate("Calculator", "+"))
        self.pushButton_14.setText(_translate("Calculator", "-"))
        self.pushButton_15.setText(_translate("Calculator", "x"))
        self.pushButton_16.setText(_translate("Calculator", "/"))
        self.pushButton_17.setText(_translate("Calculator", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simple_Test_02.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox_Input = QtWidgets.QComboBox(Dialog)
        self.comboBox_Input.setGeometry(QtCore.QRect(10, 70, 231, 71))
        self.comboBox_Input.setObjectName("comboBox_Input")
        self.textBrowser_out = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_out.setGeometry(QtCore.QRect(40, 150, 231, 71))
        self.textBrowser_out.setObjectName("textBrowser_out")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(130, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QT Designer 01"))
        self.label1.setText(_translate("Dialog", "PyQt TEST"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/product images/digital-marketing-plan-circle-shape-operations-financial-planning-46039103.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.input_textEdit.setGeometry(QtCore.QRect(220, 60, 301, 87))
        self.input_textEdit.setObjectName("input_textEdit")
        self.correct_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.correct_pushButton.setGeometry(QtCore.QRect(140, 250, 161, 51))
        self.correct_pushButton.setObjectName("correct_pushButton")
        self.output_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.output_textEdit.setGeometry(QtCore.QRect(230, 390, 301, 87))
        self.output_textEdit.setObjectName("output_textEdit")
        self.reset_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.reset_pushButton.setGeometry(QtCore.QRect(460, 250, 151, 51))
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 241, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 340, 241, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grammarectify"))
        self.correct_pushButton.setText(_translate("MainWindow", "Correct"))
        self.reset_pushButton.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", " Enter text to check grammatical errors"))
        self.label_2.setText(_translate("MainWindow", "Reultant text after check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


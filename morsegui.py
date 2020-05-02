# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morse.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time
import PiLeds as led
import alphabetPi as alpha

led.setup()

name = "BOB"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.redButton = QtWidgets.QRadioButton(self.centralwidget)
        self.redButton.setGeometry(QtCore.QRect(120, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.redButton.setFont(font)
        self.redButton.setObjectName("redButton")
        self.yellowButton = QtWidgets.QRadioButton(self.centralwidget)
        self.yellowButton.setGeometry(QtCore.QRect(120, 60, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.yellowButton.setFont(font)
        self.yellowButton.setObjectName("yellowButton")
        self.greenButton = QtWidgets.QRadioButton(self.centralwidget)
        self.greenButton.setGeometry(QtCore.QRect(120, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.greenButton.setFont(font)
        self.greenButton.setObjectName("greenButton")
        self.allOffButton = QtWidgets.QRadioButton(self.centralwidget)
        self.allOffButton.setGeometry(QtCore.QRect(280, 40, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.allOffButton.setFont(font)
        self.allOffButton.setObjectName("allOffButton")
        self.allOnButton = QtWidgets.QRadioButton(self.centralwidget)
        self.allOnButton.setGeometry(QtCore.QRect(280, 80, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.allOnButton.setFont(font)
        self.allOnButton.setObjectName("allOnButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(190, 290, 91, 31))
        self.exitButton.setObjectName("exitButton")
        self.inputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(60, 140, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.inputBox.setFont(font)
        self.inputBox.setText("")
        self.inputBox.setObjectName("inputBox")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(150, 200, 171, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.redButton.clicked.connect(led.redLed)
        self.yellowButton.clicked.connect(led.yellowLed)
        self.greenButton.clicked.connect(led.greenLed)
        self.allOnButton.clicked.connect(led.allOn)
        self.allOffButton.clicked.connect(led.allOff)
        self.exitButton.clicked.connect(self.exit)
        self.actionExit.triggered.connect(self.exit)
        self.convertButton.clicked.connect(self.convert)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traffic Lights"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.yellowButton.setText(_translate("MainWindow", "Yellow"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.allOffButton.setText(_translate("MainWindow", "All Off"))
        self.allOnButton.setText(_translate("MainWindow", "All On"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.convertButton.setText(_translate("MainWindow", "Convert to Morse"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))

    def exit(self):
        GPIO.output(17,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        QtCore.QCoreApplication.instance().quit()

    def convert(self):
        name = self.inputBox.text().upper()
        for i in name:
            alphabet[i](self)
            alpha.newLetter(self)

alphabet = {
    "A": alpha.A,
    "B": alpha.B,
    "C": alpha.C,
    "D": alpha.D,
    "E": alpha.E,
    "F": alpha.F,
    "G": alpha.G,
    "H": alpha.H,
    "I": alpha.I,
    "J": alpha.J,
    "K": alpha.K,
    "L": alpha.L,
    "M": alpha.M,
    "N": alpha.N,
    "O": alpha.O,
    "P": alpha.P,
    "Q": alpha.Q,
    "R": alpha.R,
    "S": alpha.S,
    "T": alpha.T,
    "U": alpha.U,
    "V": alpha.V,
    "W": alpha.W,
    "X": alpha.X,
    "Y": alpha.Y,
    "Z": alpha.Z,
    " ": alpha.space
}


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    
    
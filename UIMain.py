
from PyQt5 import QtCore, QtGui, QtWidgets
from APIRequest import APIRequest
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #beaver container
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 70, 271, 261))
        self.label.setObjectName("label")

        #another label
        self.responseLabel = QtWidgets.QLabel("I am a response")
        self.responseLabel.setWordWrap(True)
        self.text = QTextEdit(self)
        self.text.setMinimumSize(480, 800)
        self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.responseLabel, 0, 0)
        self.layout.addWidget(self.text, 1, 0)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        self.setLayout(self.layout)
        self.setMinimumSize(self.sizeHint())

        # Layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.text, 1, 0)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        self.setLayout(self.layout)

        self.setMinimumSize(self.sizeHint())

        #textField
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(302, 360, 341, 22))
        self.lineEdit.setObjectName("lineEdit")

        #beaverPower button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 390, 120, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.raise_()

        # Connects button's clicked signal to function openClick
        self.pushButton.clicked.connect(self.beaverPowerPressed)

        self.label.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/BeaverImage/beaver.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Beaver Power!"))
        self.updateTextField("Hello, I am Beaver Bot. How can I help? ")


    def updateTextField(self, text):
        self.lineEdit.setText(text)

    def beaverPowerPressed(self):
        input = self.lineEdit.text()
        print(input)

        #sample audio, but still need to fix what will go to audio
        os.system("say thank you for your question " + input)

        # When button is clicked, calls getResponse function from APIRequest
        api = APIRequest()
        response = api.getResponse(input)
        print(response)

        #update textField with current response, also when done it should be cleared
        self.updateTextField(response)
        stringResponse = str(response)
        print("I am a string: " + stringResponse)

        #need the type of the response so can convert to string to use in speech
        os.system("say the" + stringResponse)

import BeaverSource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
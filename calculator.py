# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 433)
        MainWindow.setWindowOpacity(0.96)
        MainWindow.setStyleSheet("background-color: rgb(66,66,66);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setIndent(1)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 320, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_4.addWidget(self.pushButton_17)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 320, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_18.setFlat(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_5.addWidget(self.pushButton_18)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 290, 320, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_19.setFlat(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_6.addWidget(self.pushButton_19)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 340, 320, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_7.addWidget(self.pushButton_11)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: rgb(15, 15, 15);\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_7.addWidget(self.pushButton_12)
        self.pushButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_20.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_20.setFlat(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_7.addWidget(self.pushButton_20)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 140, 320, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_14.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_8.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_8.addWidget(self.pushButton_13)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_8.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #383838;\n"
"  border-radius: 0px; \n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: rgba(112, 112, 112);\n"
"}")
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_8.addWidget(self.pushButton_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_11.clicked.connect(lambda: onbuttonclicked('.'))
        self.pushButton.clicked.connect(lambda: onbuttonclicked('0'))
        self.pushButton_2.clicked.connect(lambda: onbuttonclicked('1'))
        self.pushButton_3.clicked.connect(lambda: onbuttonclicked('2'))
        self.pushButton_4.clicked.connect(lambda: onbuttonclicked('3'))
        self.pushButton_5.clicked.connect(lambda: onbuttonclicked('4'))
        self.pushButton_6.clicked.connect(lambda: onbuttonclicked('5'))
        self.pushButton_7.clicked.connect(lambda: onbuttonclicked('6'))
        self.pushButton_9.clicked.connect(lambda: onbuttonclicked('7'))
        self.pushButton_8.clicked.connect(lambda: onbuttonclicked('8'))
        self.pushButton_10.clicked.connect(lambda: onbuttonclicked('9'))
        self.pushButton_13.clicked.connect(lambda: onbuttonclicked('sqre'))
        self.pushButton_15.clicked.connect(lambda: onbuttonclicked('c'))
        self.pushButton_14.clicked.connect(lambda: onbuttonclicked('ce'))
        self.pushButton_16.clicked.connect(lambda: onbuttonclicked('%'))
        self.pushButton_12.clicked.connect(lambda: onbuttonclicked('='))
        self.pushButton_20.clicked.connect(lambda: onbuttonclicked('+'))
        self.pushButton_19.clicked.connect(lambda: onbuttonclicked('-'))
        self.pushButton_18.clicked.connect(lambda: onbuttonclicked('*'))
        self.pushButton_17.clicked.connect(lambda: onbuttonclicked('/'))


        self.evalution = ''
        number = ['.','0','1','2','3','4','5','6','7','8','9']
        operator = ['+','-','*','/']
        single_op = ['%','=','sqre','c','ce']

        def onbuttonclicked(key):
                result = 0
                if key in number or key in operator:
                        self.evalution = self.evalution + key
                        self.label.setText(self.evalution)
                elif key in single_op:
                        try:
                                if key == '=':
                                        result = eval(self.evalution)
                                elif key == '%':
                                        result = eval(self.evalution + '*' + '100')
                                elif key == 'sqre':
                                        result = eval(self.evalution + '**' + '2')
                                elif key == 'ce':
                                        result = ''
                                        self.evalution = ''
                                else:
                                        result = self.evalution[:-1]    
                        except Exception as e:
                                self.label.setText('syntax Error')
                                return None
                        self.label.setText(str(result))
                        self.evalution = str(result)
                        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "9"))
        self.pushButton_17.setText(_translate("MainWindow", "÷"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_18.setText(_translate("MainWindow", "x"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_19.setText(_translate("MainWindow", "-"))
        self.pushButton_11.setText(_translate("MainWindow", "."))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "="))
        self.pushButton_20.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "CE"))
        self.pushButton_13.setText(_translate("MainWindow", "x²"))
        self.pushButton_15.setText(_translate("MainWindow", "C"))
        self.pushButton_16.setText(_translate("MainWindow", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

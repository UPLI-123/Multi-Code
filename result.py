# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_RH(object):
    def setupUi(self, Frame_RH):
        Frame_RH.setObjectName("Frame_RH")
        Frame_RH.resize(359, 285)
        Frame_RH.setStyleSheet("background-image: url(:/images/bg01_cs02.png);")
        self.frame2 = QtWidgets.QFrame(Frame_RH)
        self.frame2.setGeometry(QtCore.QRect(10, 20, 321, 261))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.horizontalWidget = QtWidgets.QWidget(self.frame2)
        self.horizontalWidget.setGeometry(QtCore.QRect(30, 190, 301, 80))
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalWidget = QtWidgets.QWidget(self.frame2)
        self.verticalWidget.setGeometry(QtCore.QRect(44, 0, 271, 181))
        self.verticalWidget.setStyleSheet("")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.r1 = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.r1.setFont(font)
        self.r1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r1.setStyleSheet("background: transparent;  ")
        self.r1.setObjectName("r1")
        self.verticalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.r2.setFont(font)
        self.r2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r2.setStyleSheet("background: transparent;  ")
        self.r2.setObjectName("r2")
        self.verticalLayout.addWidget(self.r2)
        self.r3 = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.r3.setFont(font)
        self.r3.setStyleSheet("background: transparent;  ")
        self.r3.setObjectName("r3")
        self.verticalLayout.addWidget(self.r3)
        self.r4 = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.r4.setFont(font)
        self.r4.setStyleSheet("background: transparent;  ")
        self.r4.setObjectName("r4")
        self.verticalLayout.addWidget(self.r4)

        self.retranslateUi(Frame_RH)
        self.pushButton.clicked.connect(Frame_RH.ok) # type: ignore
        self.pushButton_2.clicked.connect(Frame_RH.cancel) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Frame_RH)

    def retranslateUi(self, Frame_RH):
        _translate = QtCore.QCoreApplication.translate
        Frame_RH.setWindowTitle(_translate("Frame_RH", "下游任务选择"))
        self.pushButton.setText(_translate("Frame_RH", "确定"))
        self.pushButton_2.setText(_translate("Frame_RH", "取消"))
        self.r1.setText(_translate("Frame_RH", "决策树分类器"))
        self.r2.setText(_translate("Frame_RH", "K最近邻分类器"))
        self.r3.setText(_translate("Frame_RH", "自适应增强分类器"))
        self.r4.setText(_translate("Frame_RH", "支持向量机分类器"))
import image_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCRV.ui'
#
# Created: Mon Jul 21 16:11:25 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SCRV(object):
    def setupUi(self, SCRV):
        SCRV.setObjectName("SCRV")
        SCRV.resize(QtCore.QSize(QtCore.QRect(0,0,528,642).size()).expandedTo(SCRV.minimumSizeHint()))

        self.SCRVName = QtGui.QLabel(SCRV)
        self.SCRVName.setGeometry(QtCore.QRect(160,10,361,71))

        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setItalic(True)
        font.setUnderline(False)
        font.setBold(True)
        self.SCRVName.setFont(font)
        self.SCRVName.setObjectName("SCRVName")

        self.AlbaLogo = QtGui.QLabel(SCRV)
        self.AlbaLogo.setGeometry(QtCore.QRect(10,10,126,71))
        self.AlbaLogo.setPixmap(QtGui.QPixmap(":/ALBA_Logo.png"))
        self.AlbaLogo.setObjectName("AlbaLogo")

        self.upperJawLabel = QtGui.QLabel(SCRV)
        self.upperJawLabel.setGeometry(QtCore.QRect(10,90,154,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.upperJawLabel.setFont(font)
        self.upperJawLabel.setObjectName("upperJawLabel")

        self.lowerJawLabel = QtGui.QLabel(SCRV)
        self.lowerJawLabel.setGeometry(QtCore.QRect(10,600,152,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.lowerJawLabel.setFont(font)
        self.lowerJawLabel.setObjectName("lowerJawLabel")

        self.abort = QtGui.QPushButton(SCRV)
        self.abort.setGeometry(QtCore.QRect(330,80,141,41))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abort.sizePolicy().hasHeightForWidth())
        self.abort.setSizePolicy(sizePolicy)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,127,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,63,63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(170,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,127,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,127,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,63,63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(170,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,127,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.AlternateBase,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.WindowText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Button,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,127,127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Light,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,63,63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Midlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Dark,brush)

        brush = QtGui.QBrush(QtGui.QColor(170,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Mid,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.BrightText,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.ButtonText,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Shadow,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.AlternateBase,brush)
        self.abort.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(19)
        self.abort.setFont(font)
        self.abort.setObjectName("abort")

        self.upperJaw = QtGui.QGroupBox(SCRV)
        self.upperJaw.setGeometry(QtCore.QRect(10,140,190,144))
        self.upperJaw.setObjectName("upperJaw")

        self.vboxlayout = QtGui.QVBoxLayout(self.upperJaw)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.upperStepper = TauGroupBox(self.upperJaw)
        self.upperStepper.setFlat(True)
        self.upperStepper.setShowText(False)
        self.upperStepper.setObjectName("upperStepper")

        self.gridlayout = QtGui.QGridLayout(self.upperStepper)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.upperLabelState = TauValueLabel(self.upperStepper)
        self.upperLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.upperLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.upperLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.upperLabelState.setShowQuality(False)
        self.upperLabelState.setUseParentModel(True)
        self.upperLabelState.setObjectName("upperLabelState")
        self.hboxlayout.addWidget(self.upperLabelState)

        self.upperLedState = TauStateLed(self.upperStepper)
        self.upperLedState.setUseParentModel(True)
        self.upperLedState.setObjectName("upperLedState")
        self.hboxlayout.addWidget(self.upperLedState)

        spacerItem = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.upperLimitN = TauLimitSwitch(self.upperStepper)
        self.upperLimitN.setUseParentModel(True)
        self.upperLimitN.setBoolIndex(2)
        self.upperLimitN.setObjectName("upperLimitN")
        self.hboxlayout.addWidget(self.upperLimitN)

        self.upperLimitLabel = QtGui.QLabel(self.upperStepper)
        self.upperLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.upperLimitLabel.setObjectName("upperLimitLabel")
        self.hboxlayout.addWidget(self.upperLimitLabel)

        self.upperLimitP = TauLimitSwitch(self.upperStepper)
        self.upperLimitP.setUseParentModel(True)
        self.upperLimitP.setBoolIndex(1)
        self.upperLimitP.setObjectName("upperLimitP")
        self.hboxlayout.addWidget(self.upperLimitP)
        self.gridlayout.addLayout(self.hboxlayout,0,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.upperMoveIn = QtGui.QPushButton(self.upperStepper)
        self.upperMoveIn.setObjectName("upperMoveIn")
        self.hboxlayout1.addWidget(self.upperMoveIn)

        self.upperInValue = QtGui.QDoubleSpinBox(self.upperStepper)
        self.upperInValue.setDecimals(3)
        self.upperInValue.setMinimum(0.005)
        self.upperInValue.setMaximum(20.0)
        self.upperInValue.setSingleStep(0.001)
        self.upperInValue.setProperty("value",QtCore.QVariant(1.0))
        self.upperInValue.setObjectName("upperInValue")
        self.hboxlayout1.addWidget(self.upperInValue)

        self.upperInStepperUnits = TauConfigLabel(self.upperStepper)
        self.upperInStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperInStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperInStepperUnits.setUseParentModel(True)
        self.upperInStepperUnits.setObjectName("upperInStepperUnits")
        self.hboxlayout1.addWidget(self.upperInStepperUnits)
        self.gridlayout.addLayout(self.hboxlayout1,1,0,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setSpacing(2)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.upperMoveOut = QtGui.QPushButton(self.upperStepper)
        self.upperMoveOut.setObjectName("upperMoveOut")
        self.hboxlayout2.addWidget(self.upperMoveOut)

        self.upperOutValue = QtGui.QDoubleSpinBox(self.upperStepper)
        self.upperOutValue.setDecimals(3)
        self.upperOutValue.setMinimum(0.005)
        self.upperOutValue.setMaximum(20.0)
        self.upperOutValue.setSingleStep(0.001)
        self.upperOutValue.setProperty("value",QtCore.QVariant(1.0))
        self.upperOutValue.setObjectName("upperOutValue")
        self.hboxlayout2.addWidget(self.upperOutValue)

        self.upperOutStepperUnits = TauConfigLabel(self.upperStepper)
        self.upperOutStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperOutStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperOutStepperUnits.setUseParentModel(True)
        self.upperOutStepperUnits.setObjectName("upperOutStepperUnits")
        self.hboxlayout2.addWidget(self.upperOutStepperUnits)
        self.gridlayout.addLayout(self.hboxlayout2,2,0,1,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setSpacing(2)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.upperMoveAbs = QtGui.QPushButton(self.upperStepper)
        self.upperMoveAbs.setObjectName("upperMoveAbs")
        self.hboxlayout3.addWidget(self.upperMoveAbs)

        self.upperAbsValue = QtGui.QDoubleSpinBox(self.upperStepper)
        self.upperAbsValue.setDecimals(3)
        self.upperAbsValue.setMaximum(20.0)
        self.upperAbsValue.setSingleStep(0.001)
        self.upperAbsValue.setProperty("value",QtCore.QVariant(1.0))
        self.upperAbsValue.setObjectName("upperAbsValue")
        self.hboxlayout3.addWidget(self.upperAbsValue)

        self.upperAbsStepperUnits = TauConfigLabel(self.upperStepper)
        self.upperAbsStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperAbsStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperAbsStepperUnits.setUseParentModel(True)
        self.upperAbsStepperUnits.setObjectName("upperAbsStepperUnits")
        self.hboxlayout3.addWidget(self.upperAbsStepperUnits)
        self.gridlayout.addLayout(self.hboxlayout3,3,0,1,1)
        self.vboxlayout.addWidget(self.upperStepper)

        self.upperEnc = TauGroupBox(self.upperJaw)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperEnc.sizePolicy().hasHeightForWidth())
        self.upperEnc.setSizePolicy(sizePolicy)
        self.upperEnc.setFlat(True)
        self.upperEnc.setShowText(False)
        self.upperEnc.setObjectName("upperEnc")

        self.gridlayout1 = QtGui.QGridLayout(self.upperEnc)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setVerticalSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.upperEncLabel = QtGui.QLabel(self.upperEnc)
        self.upperEncLabel.setObjectName("upperEncLabel")
        self.hboxlayout4.addWidget(self.upperEncLabel)

        self.upperEncRead = TauValueLabel(self.upperEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperEncRead.sizePolicy().hasHeightForWidth())
        self.upperEncRead.setSizePolicy(sizePolicy)
        self.upperEncRead.setUseParentModel(True)
        self.upperEncRead.setObjectName("upperEncRead")
        self.hboxlayout4.addWidget(self.upperEncRead)

        self.upperEncUnits = TauConfigLabel(self.upperEnc)
        self.upperEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperEncUnits.setUseParentModel(True)
        self.upperEncUnits.setObjectName("upperEncUnits")
        self.hboxlayout4.addWidget(self.upperEncUnits)
        self.gridlayout1.addLayout(self.hboxlayout4,0,0,1,1)
        self.vboxlayout.addWidget(self.upperEnc)

        self.lowerJaw = QtGui.QGroupBox(SCRV)
        self.lowerJaw.setGeometry(QtCore.QRect(10,450,190,144))
        self.lowerJaw.setObjectName("lowerJaw")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.lowerJaw)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.lowerStepper = TauGroupBox(self.lowerJaw)
        self.lowerStepper.setFlat(True)
        self.lowerStepper.setShowText(False)
        self.lowerStepper.setObjectName("lowerStepper")

        self.gridlayout2 = QtGui.QGridLayout(self.lowerStepper)
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(0)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.lowerLabelState = TauValueLabel(self.lowerStepper)
        self.lowerLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.lowerLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.lowerLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.lowerLabelState.setShowQuality(False)
        self.lowerLabelState.setUseParentModel(True)
        self.lowerLabelState.setObjectName("lowerLabelState")
        self.hboxlayout5.addWidget(self.lowerLabelState)

        self.lowerLedState = TauStateLed(self.lowerStepper)
        self.lowerLedState.setUseParentModel(True)
        self.lowerLedState.setObjectName("lowerLedState")
        self.hboxlayout5.addWidget(self.lowerLedState)

        spacerItem1 = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem1)

        self.lowerLimitN = TauLimitSwitch(self.lowerStepper)
        self.lowerLimitN.setUseParentModel(True)
        self.lowerLimitN.setBoolIndex(2)
        self.lowerLimitN.setObjectName("lowerLimitN")
        self.hboxlayout5.addWidget(self.lowerLimitN)

        self.lowerLimitLabel = QtGui.QLabel(self.lowerStepper)
        self.lowerLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lowerLimitLabel.setObjectName("lowerLimitLabel")
        self.hboxlayout5.addWidget(self.lowerLimitLabel)

        self.lowerLimitP = TauLimitSwitch(self.lowerStepper)
        self.lowerLimitP.setUseParentModel(True)
        self.lowerLimitP.setBoolIndex(1)
        self.lowerLimitP.setObjectName("lowerLimitP")
        self.hboxlayout5.addWidget(self.lowerLimitP)
        self.gridlayout2.addLayout(self.hboxlayout5,0,0,1,1)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setSpacing(1)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.lowerMoveIn = QtGui.QPushButton(self.lowerStepper)
        self.lowerMoveIn.setObjectName("lowerMoveIn")
        self.hboxlayout6.addWidget(self.lowerMoveIn)

        self.lowerInValue = QtGui.QDoubleSpinBox(self.lowerStepper)
        self.lowerInValue.setDecimals(3)
        self.lowerInValue.setMinimum(0.005)
        self.lowerInValue.setMaximum(20.0)
        self.lowerInValue.setSingleStep(0.001)
        self.lowerInValue.setProperty("value",QtCore.QVariant(1.0))
        self.lowerInValue.setObjectName("lowerInValue")
        self.hboxlayout6.addWidget(self.lowerInValue)

        self.lowerInStepperUnits = TauConfigLabel(self.lowerStepper)
        self.lowerInStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerInStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerInStepperUnits.setUseParentModel(True)
        self.lowerInStepperUnits.setObjectName("lowerInStepperUnits")
        self.hboxlayout6.addWidget(self.lowerInStepperUnits)
        self.gridlayout2.addLayout(self.hboxlayout6,1,0,1,1)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setSpacing(1)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.lowerMoveOut = QtGui.QPushButton(self.lowerStepper)
        self.lowerMoveOut.setObjectName("lowerMoveOut")
        self.hboxlayout7.addWidget(self.lowerMoveOut)

        self.lowerOutValue = QtGui.QDoubleSpinBox(self.lowerStepper)
        self.lowerOutValue.setDecimals(3)
        self.lowerOutValue.setMinimum(0.005)
        self.lowerOutValue.setMaximum(20.0)
        self.lowerOutValue.setSingleStep(0.001)
        self.lowerOutValue.setProperty("value",QtCore.QVariant(1.0))
        self.lowerOutValue.setObjectName("lowerOutValue")
        self.hboxlayout7.addWidget(self.lowerOutValue)

        self.lowerOutStepperUnits = TauConfigLabel(self.lowerStepper)
        self.lowerOutStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerOutStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerOutStepperUnits.setUseParentModel(True)
        self.lowerOutStepperUnits.setObjectName("lowerOutStepperUnits")
        self.hboxlayout7.addWidget(self.lowerOutStepperUnits)
        self.gridlayout2.addLayout(self.hboxlayout7,2,0,1,1)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setSpacing(1)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.lowerMoveAbs = QtGui.QPushButton(self.lowerStepper)
        self.lowerMoveAbs.setObjectName("lowerMoveAbs")
        self.hboxlayout8.addWidget(self.lowerMoveAbs)

        self.lowerAbsValue = QtGui.QDoubleSpinBox(self.lowerStepper)
        self.lowerAbsValue.setDecimals(3)
        self.lowerAbsValue.setMaximum(20.0)
        self.lowerAbsValue.setSingleStep(0.001)
        self.lowerAbsValue.setProperty("value",QtCore.QVariant(1.0))
        self.lowerAbsValue.setObjectName("lowerAbsValue")
        self.hboxlayout8.addWidget(self.lowerAbsValue)

        self.lowerAbsStepperUnits = TauConfigLabel(self.lowerStepper)
        self.lowerAbsStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerAbsStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerAbsStepperUnits.setUseParentModel(True)
        self.lowerAbsStepperUnits.setObjectName("lowerAbsStepperUnits")
        self.hboxlayout8.addWidget(self.lowerAbsStepperUnits)
        self.gridlayout2.addLayout(self.hboxlayout8,3,0,1,1)
        self.vboxlayout1.addWidget(self.lowerStepper)

        self.lowerEnc = TauGroupBox(self.lowerJaw)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerEnc.sizePolicy().hasHeightForWidth())
        self.lowerEnc.setSizePolicy(sizePolicy)
        self.lowerEnc.setFlat(True)
        self.lowerEnc.setShowText(False)
        self.lowerEnc.setObjectName("lowerEnc")

        self.gridlayout3 = QtGui.QGridLayout(self.lowerEnc)
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setVerticalSpacing(0)
        self.gridlayout3.setObjectName("gridlayout3")

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.lowerEncLabel = QtGui.QLabel(self.lowerEnc)
        self.lowerEncLabel.setObjectName("lowerEncLabel")
        self.hboxlayout9.addWidget(self.lowerEncLabel)

        self.lowerEncRead = TauValueLabel(self.lowerEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerEncRead.sizePolicy().hasHeightForWidth())
        self.lowerEncRead.setSizePolicy(sizePolicy)
        self.lowerEncRead.setUseParentModel(True)
        self.lowerEncRead.setObjectName("lowerEncRead")
        self.hboxlayout9.addWidget(self.lowerEncRead)

        self.lowerEncUnits = TauConfigLabel(self.lowerEnc)
        self.lowerEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerEncUnits.setUseParentModel(True)
        self.lowerEncUnits.setObjectName("lowerEncUnits")
        self.hboxlayout9.addWidget(self.lowerEncUnits)
        self.gridlayout3.addLayout(self.hboxlayout9,0,0,1,1)
        self.vboxlayout1.addWidget(self.lowerEnc)

        self.offsetLabel = QtGui.QLabel(SCRV)
        self.offsetLabel.setGeometry(QtCore.QRect(20,370,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.offsetLabel.setFont(font)
        self.offsetLabel.setObjectName("offsetLabel")

        self.gapLabel = QtGui.QLabel(SCRV)
        self.gapLabel.setGeometry(QtCore.QRect(20,310,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.gapLabel.setFont(font)
        self.gapLabel.setObjectName("gapLabel")

        self.gapAndOffset = QtGui.QGroupBox(SCRV)
        self.gapAndOffset.setGeometry(QtCore.QRect(120,300,131,128))
        self.gapAndOffset.setFlat(True)
        self.gapAndOffset.setObjectName("gapAndOffset")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.gapAndOffset)
        self.vboxlayout2.setSpacing(0)
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.gap = TauGroupBox(self.gapAndOffset)
        self.gap.setShowText(False)
        self.gap.setObjectName("gap")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.gap)
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout10 = QtGui.QHBoxLayout()
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.gapRead = TauValueLabel(self.gap)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gapRead.sizePolicy().hasHeightForWidth())
        self.gapRead.setSizePolicy(sizePolicy)
        self.gapRead.setUseParentModel(True)
        self.gapRead.setObjectName("gapRead")
        self.hboxlayout10.addWidget(self.gapRead)

        self.gapReadUnits = TauConfigLabel(self.gap)
        self.gapReadUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapReadUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapReadUnits.setUseParentModel(True)
        self.gapReadUnits.setObjectName("gapReadUnits")
        self.hboxlayout10.addWidget(self.gapReadUnits)
        self.vboxlayout3.addLayout(self.hboxlayout10)

        self.hboxlayout11 = QtGui.QHBoxLayout()
        self.hboxlayout11.setSpacing(-1)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.gapWrite = TauValueLineEdit(self.gap)
        self.gapWrite.setUseParentModel(True)
        self.gapWrite.setObjectName("gapWrite")
        self.hboxlayout11.addWidget(self.gapWrite)

        self.gapWriteUnits = TauConfigLabel(self.gap)
        self.gapWriteUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapWriteUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapWriteUnits.setUseParentModel(True)
        self.gapWriteUnits.setObjectName("gapWriteUnits")
        self.hboxlayout11.addWidget(self.gapWriteUnits)
        self.vboxlayout3.addLayout(self.hboxlayout11)
        self.vboxlayout2.addWidget(self.gap)

        self.offset = TauGroupBox(self.gapAndOffset)
        self.offset.setShowText(False)
        self.offset.setObjectName("offset")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.offset)
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout12 = QtGui.QHBoxLayout()
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.offsetRead = TauValueLabel(self.offset)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetRead.sizePolicy().hasHeightForWidth())
        self.offsetRead.setSizePolicy(sizePolicy)
        self.offsetRead.setUseParentModel(True)
        self.offsetRead.setObjectName("offsetRead")
        self.hboxlayout12.addWidget(self.offsetRead)

        self.offsetReadUnits = TauConfigLabel(self.offset)
        self.offsetReadUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetReadUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetReadUnits.setUseParentModel(True)
        self.offsetReadUnits.setObjectName("offsetReadUnits")
        self.hboxlayout12.addWidget(self.offsetReadUnits)
        self.vboxlayout4.addLayout(self.hboxlayout12)

        self.hboxlayout13 = QtGui.QHBoxLayout()
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.OffsetWrite = TauValueLineEdit(self.offset)
        self.OffsetWrite.setUseParentModel(True)
        self.OffsetWrite.setObjectName("OffsetWrite")
        self.hboxlayout13.addWidget(self.OffsetWrite)

        self.offsetWriteUnits = TauConfigLabel(self.offset)
        self.offsetWriteUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetWriteUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetWriteUnits.setUseParentModel(True)
        self.offsetWriteUnits.setObjectName("offsetWriteUnits")
        self.hboxlayout13.addWidget(self.offsetWriteUnits)
        self.vboxlayout4.addLayout(self.hboxlayout13)
        self.vboxlayout2.addWidget(self.offset)

        self.retranslateUi(SCRV)
        QtCore.QMetaObject.connectSlotsByName(SCRV)

    def retranslateUi(self, SCRV):
        SCRV.setWindowTitle(QtGui.QApplication.translate("SCRV", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SCRVName.setText(QtGui.QApplication.translate("SCRV", "SCRVName", None, QtGui.QApplication.UnicodeUTF8))
        self.upperJawLabel.setText(QtGui.QApplication.translate("SCRV", "Upper Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerJawLabel.setText(QtGui.QApplication.translate("SCRV", "Lower Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("SCRV", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLabelState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLedState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitN.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitLabel.setText(QtGui.QApplication.translate("SCRV", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitP.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.upperMoveIn.setText(QtGui.QApplication.translate("SCRV", "Move IN", None, QtGui.QApplication.UnicodeUTF8))
        self.upperInStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.upperMoveOut.setText(QtGui.QApplication.translate("SCRV", "Move OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.upperOutStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.upperMoveAbs.setText(QtGui.QApplication.translate("SCRV", "Move TO", None, QtGui.QApplication.UnicodeUTF8))
        self.upperAbsStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncLabel.setText(QtGui.QApplication.translate("SCRV", "Encoder read:", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLabelState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLedState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitN.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitLabel.setText(QtGui.QApplication.translate("SCRV", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitP.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerMoveIn.setText(QtGui.QApplication.translate("SCRV", "Move IN", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerInStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerMoveOut.setText(QtGui.QApplication.translate("SCRV", "Move OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerOutStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerMoveAbs.setText(QtGui.QApplication.translate("SCRV", "Move TO", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerAbsStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncLabel.setText(QtGui.QApplication.translate("SCRV", "Encoder read:", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("SCRV", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.gapLabel.setText(QtGui.QApplication.translate("SCRV", "Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.gapRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapReadUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapWrite.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapWriteUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetReadUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.OffsetWrite.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetWriteUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))

from tau.widget import TauConfigLabel, TauGroupBox, TauValueLineEdit, TauLimitSwitch, TauValueLabel, TauStateLed
import scrapers_rc

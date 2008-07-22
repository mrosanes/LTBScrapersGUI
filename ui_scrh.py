# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCRH.ui'
#
# Created: Mon Jul 21 16:11:24 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SCRH(object):
    def setupUi(self, SCRH):
        SCRH.setObjectName("SCRH")
        SCRH.resize(QtCore.QSize(QtCore.QRect(0,0,707,278).size()).expandedTo(SCRH.minimumSizeHint()))

        self.SCRHName = QtGui.QLabel(SCRH)
        self.SCRHName.setGeometry(QtCore.QRect(160,10,531,71))

        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setItalic(True)
        font.setUnderline(False)
        font.setBold(True)
        self.SCRHName.setFont(font)
        self.SCRHName.setObjectName("SCRHName")

        self.AlbaLogo = QtGui.QLabel(SCRH)
        self.AlbaLogo.setGeometry(QtCore.QRect(10,10,126,71))
        self.AlbaLogo.setPixmap(QtGui.QPixmap(":/ALBA_Logo.png"))
        self.AlbaLogo.setObjectName("AlbaLogo")

        self.leftJawLabel = QtGui.QLabel(SCRH)
        self.leftJawLabel.setGeometry(QtCore.QRect(10,80,120,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.leftJawLabel.setFont(font)
        self.leftJawLabel.setObjectName("leftJawLabel")

        self.rightJawLabel = QtGui.QLabel(SCRH)
        self.rightJawLabel.setGeometry(QtCore.QRect(540,80,142,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.rightJawLabel.setFont(font)
        self.rightJawLabel.setObjectName("rightJawLabel")

        self.gapAndOffset = QtGui.QGroupBox(SCRH)
        self.gapAndOffset.setGeometry(QtCore.QRect(220,180,271,84))
        self.gapAndOffset.setFlat(True)
        self.gapAndOffset.setObjectName("gapAndOffset")

        self.gridlayout = QtGui.QGridLayout(self.gapAndOffset)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.gap = TauGroupBox(self.gapAndOffset)
        self.gap.setShowText(False)
        self.gap.setObjectName("gap")

        self.vboxlayout = QtGui.QVBoxLayout(self.gap)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.gapRead = TauValueLabel(self.gap)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gapRead.sizePolicy().hasHeightForWidth())
        self.gapRead.setSizePolicy(sizePolicy)
        self.gapRead.setUseParentModel(True)
        self.gapRead.setObjectName("gapRead")
        self.hboxlayout.addWidget(self.gapRead)

        self.gapReadUnits = TauConfigLabel(self.gap)
        self.gapReadUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapReadUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapReadUnits.setUseParentModel(True)
        self.gapReadUnits.setObjectName("gapReadUnits")
        self.hboxlayout.addWidget(self.gapReadUnits)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(-1)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.gapWrite = TauValueLineEdit(self.gap)
        self.gapWrite.setUseParentModel(True)
        self.gapWrite.setObjectName("gapWrite")
        self.hboxlayout1.addWidget(self.gapWrite)

        self.gapWriteUnits = TauConfigLabel(self.gap)
        self.gapWriteUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapWriteUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapWriteUnits.setUseParentModel(True)
        self.gapWriteUnits.setObjectName("gapWriteUnits")
        self.hboxlayout1.addWidget(self.gapWriteUnits)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addWidget(self.gap,0,0,1,1)

        self.offset = TauGroupBox(self.gapAndOffset)
        self.offset.setShowText(False)
        self.offset.setObjectName("offset")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.offset)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.offsetRead = TauValueLabel(self.offset)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetRead.sizePolicy().hasHeightForWidth())
        self.offsetRead.setSizePolicy(sizePolicy)
        self.offsetRead.setUseParentModel(True)
        self.offsetRead.setObjectName("offsetRead")
        self.hboxlayout2.addWidget(self.offsetRead)

        self.offsetReadUnits = TauConfigLabel(self.offset)
        self.offsetReadUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetReadUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetReadUnits.setUseParentModel(True)
        self.offsetReadUnits.setObjectName("offsetReadUnits")
        self.hboxlayout2.addWidget(self.offsetReadUnits)
        self.vboxlayout1.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.OffsetWrite = TauValueLineEdit(self.offset)
        self.OffsetWrite.setUseParentModel(True)
        self.OffsetWrite.setObjectName("OffsetWrite")
        self.hboxlayout3.addWidget(self.OffsetWrite)

        self.offsetWriteUnits = TauConfigLabel(self.offset)
        self.offsetWriteUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetWriteUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetWriteUnits.setUseParentModel(True)
        self.offsetWriteUnits.setObjectName("offsetWriteUnits")
        self.hboxlayout3.addWidget(self.offsetWriteUnits)
        self.vboxlayout1.addLayout(self.hboxlayout3)
        self.gridlayout.addWidget(self.offset,0,1,1,1)

        self.gapLabel = QtGui.QLabel(SCRH)
        self.gapLabel.setGeometry(QtCore.QRect(250,140,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.gapLabel.setFont(font)
        self.gapLabel.setObjectName("gapLabel")

        self.offsetLabel = QtGui.QLabel(SCRH)
        self.offsetLabel.setGeometry(QtCore.QRect(380,140,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.offsetLabel.setFont(font)
        self.offsetLabel.setObjectName("offsetLabel")

        self.abort = QtGui.QPushButton(SCRH)
        self.abort.setGeometry(QtCore.QRect(280,90,141,41))

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

        self.leftJaw = QtGui.QGroupBox(SCRH)
        self.leftJaw.setGeometry(QtCore.QRect(10,120,190,144))
        self.leftJaw.setObjectName("leftJaw")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.leftJaw)
        self.vboxlayout2.setSpacing(0)
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.leftStepper = TauGroupBox(self.leftJaw)
        self.leftStepper.setFlat(True)
        self.leftStepper.setShowText(False)
        self.leftStepper.setObjectName("leftStepper")

        self.gridlayout1 = QtGui.QGridLayout(self.leftStepper)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.leftLabelState = TauValueLabel(self.leftStepper)
        self.leftLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.leftLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.leftLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.leftLabelState.setShowQuality(False)
        self.leftLabelState.setUseParentModel(True)
        self.leftLabelState.setObjectName("leftLabelState")
        self.hboxlayout4.addWidget(self.leftLabelState)

        self.leftLedState = TauStateLed(self.leftStepper)
        self.leftLedState.setUseParentModel(True)
        self.leftLedState.setObjectName("leftLedState")
        self.hboxlayout4.addWidget(self.leftLedState)

        spacerItem = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem)

        self.leftLimitN = TauLimitSwitch(self.leftStepper)
        self.leftLimitN.setUseParentModel(True)
        self.leftLimitN.setBoolIndex(2)
        self.leftLimitN.setObjectName("leftLimitN")
        self.hboxlayout4.addWidget(self.leftLimitN)

        self.leftLimitLabel = QtGui.QLabel(self.leftStepper)
        self.leftLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.leftLimitLabel.setObjectName("leftLimitLabel")
        self.hboxlayout4.addWidget(self.leftLimitLabel)

        self.leftLimitP = TauLimitSwitch(self.leftStepper)
        self.leftLimitP.setUseParentModel(True)
        self.leftLimitP.setBoolIndex(1)
        self.leftLimitP.setObjectName("leftLimitP")
        self.hboxlayout4.addWidget(self.leftLimitP)
        self.gridlayout1.addLayout(self.hboxlayout4,0,0,1,1)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setSpacing(2)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.leftMoveIn = QtGui.QPushButton(self.leftStepper)
        self.leftMoveIn.setObjectName("leftMoveIn")
        self.hboxlayout5.addWidget(self.leftMoveIn)

        self.leftInValue = QtGui.QDoubleSpinBox(self.leftStepper)
        self.leftInValue.setDecimals(3)
        self.leftInValue.setMinimum(0.005)
        self.leftInValue.setMaximum(20.0)
        self.leftInValue.setSingleStep(0.001)
        self.leftInValue.setProperty("value",QtCore.QVariant(1.0))
        self.leftInValue.setObjectName("leftInValue")
        self.hboxlayout5.addWidget(self.leftInValue)

        self.leftInStepperUnits = TauConfigLabel(self.leftStepper)
        self.leftInStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftInStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftInStepperUnits.setUseParentModel(True)
        self.leftInStepperUnits.setObjectName("leftInStepperUnits")
        self.hboxlayout5.addWidget(self.leftInStepperUnits)
        self.gridlayout1.addLayout(self.hboxlayout5,1,0,1,1)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setSpacing(2)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.leftMoveOut = QtGui.QPushButton(self.leftStepper)
        self.leftMoveOut.setObjectName("leftMoveOut")
        self.hboxlayout6.addWidget(self.leftMoveOut)

        self.leftOutValue = QtGui.QDoubleSpinBox(self.leftStepper)
        self.leftOutValue.setDecimals(3)
        self.leftOutValue.setMinimum(0.005)
        self.leftOutValue.setMaximum(20.0)
        self.leftOutValue.setSingleStep(0.001)
        self.leftOutValue.setProperty("value",QtCore.QVariant(1.0))
        self.leftOutValue.setObjectName("leftOutValue")
        self.hboxlayout6.addWidget(self.leftOutValue)

        self.leftOutStepperUnits = TauConfigLabel(self.leftStepper)
        self.leftOutStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftOutStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftOutStepperUnits.setUseParentModel(True)
        self.leftOutStepperUnits.setObjectName("leftOutStepperUnits")
        self.hboxlayout6.addWidget(self.leftOutStepperUnits)
        self.gridlayout1.addLayout(self.hboxlayout6,2,0,1,1)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setSpacing(2)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.leftMoveAbs = QtGui.QPushButton(self.leftStepper)
        self.leftMoveAbs.setObjectName("leftMoveAbs")
        self.hboxlayout7.addWidget(self.leftMoveAbs)

        self.leftAbsValue = QtGui.QDoubleSpinBox(self.leftStepper)
        self.leftAbsValue.setDecimals(3)
        self.leftAbsValue.setMaximum(20.0)
        self.leftAbsValue.setSingleStep(0.001)
        self.leftAbsValue.setProperty("value",QtCore.QVariant(1.0))
        self.leftAbsValue.setObjectName("leftAbsValue")
        self.hboxlayout7.addWidget(self.leftAbsValue)

        self.leftAbsStepperUnits = TauConfigLabel(self.leftStepper)
        self.leftAbsStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftAbsStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftAbsStepperUnits.setUseParentModel(True)
        self.leftAbsStepperUnits.setObjectName("leftAbsStepperUnits")
        self.hboxlayout7.addWidget(self.leftAbsStepperUnits)
        self.gridlayout1.addLayout(self.hboxlayout7,3,0,1,1)
        self.vboxlayout2.addWidget(self.leftStepper)

        self.leftEnc = TauGroupBox(self.leftJaw)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftEnc.sizePolicy().hasHeightForWidth())
        self.leftEnc.setSizePolicy(sizePolicy)
        self.leftEnc.setFlat(True)
        self.leftEnc.setShowText(False)
        self.leftEnc.setObjectName("leftEnc")

        self.gridlayout2 = QtGui.QGridLayout(self.leftEnc)
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setVerticalSpacing(0)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.leftEncLabel = QtGui.QLabel(self.leftEnc)
        self.leftEncLabel.setObjectName("leftEncLabel")
        self.hboxlayout8.addWidget(self.leftEncLabel)

        self.leftEncRead = TauValueLabel(self.leftEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftEncRead.sizePolicy().hasHeightForWidth())
        self.leftEncRead.setSizePolicy(sizePolicy)
        self.leftEncRead.setUseParentModel(True)
        self.leftEncRead.setObjectName("leftEncRead")
        self.hboxlayout8.addWidget(self.leftEncRead)

        self.leftEncUnits = TauConfigLabel(self.leftEnc)
        self.leftEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftEncUnits.setUseParentModel(True)
        self.leftEncUnits.setObjectName("leftEncUnits")
        self.hboxlayout8.addWidget(self.leftEncUnits)
        self.gridlayout2.addLayout(self.hboxlayout8,0,0,1,1)
        self.vboxlayout2.addWidget(self.leftEnc)

        self.rightJaw = QtGui.QGroupBox(SCRH)
        self.rightJaw.setGeometry(QtCore.QRect(500,120,190,144))
        self.rightJaw.setObjectName("rightJaw")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.rightJaw)
        self.vboxlayout3.setSpacing(0)
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.rightStepper = TauGroupBox(self.rightJaw)
        self.rightStepper.setFlat(True)
        self.rightStepper.setShowText(False)
        self.rightStepper.setObjectName("rightStepper")

        self.gridlayout3 = QtGui.QGridLayout(self.rightStepper)
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setSpacing(0)
        self.gridlayout3.setObjectName("gridlayout3")

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.rightLabelState = TauValueLabel(self.rightStepper)
        self.rightLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.rightLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.rightLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.rightLabelState.setShowQuality(False)
        self.rightLabelState.setUseParentModel(True)
        self.rightLabelState.setObjectName("rightLabelState")
        self.hboxlayout9.addWidget(self.rightLabelState)

        self.rightLedState = TauStateLed(self.rightStepper)
        self.rightLedState.setUseParentModel(True)
        self.rightLedState.setObjectName("rightLedState")
        self.hboxlayout9.addWidget(self.rightLedState)

        spacerItem1 = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem1)

        self.rightLimitN = TauLimitSwitch(self.rightStepper)
        self.rightLimitN.setUseParentModel(True)
        self.rightLimitN.setBoolIndex(2)
        self.rightLimitN.setObjectName("rightLimitN")
        self.hboxlayout9.addWidget(self.rightLimitN)

        self.rightLimitLabel = QtGui.QLabel(self.rightStepper)
        self.rightLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightLimitLabel.setObjectName("rightLimitLabel")
        self.hboxlayout9.addWidget(self.rightLimitLabel)

        self.rightLimitP = TauLimitSwitch(self.rightStepper)
        self.rightLimitP.setUseParentModel(True)
        self.rightLimitP.setBoolIndex(1)
        self.rightLimitP.setObjectName("rightLimitP")
        self.hboxlayout9.addWidget(self.rightLimitP)
        self.gridlayout3.addLayout(self.hboxlayout9,0,0,1,1)

        self.hboxlayout10 = QtGui.QHBoxLayout()
        self.hboxlayout10.setSpacing(1)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.rightMoveIn = QtGui.QPushButton(self.rightStepper)
        self.rightMoveIn.setObjectName("rightMoveIn")
        self.hboxlayout10.addWidget(self.rightMoveIn)

        self.rightInValue = QtGui.QDoubleSpinBox(self.rightStepper)
        self.rightInValue.setDecimals(3)
        self.rightInValue.setMinimum(0.005)
        self.rightInValue.setMaximum(20.0)
        self.rightInValue.setSingleStep(0.001)
        self.rightInValue.setProperty("value",QtCore.QVariant(1.0))
        self.rightInValue.setObjectName("rightInValue")
        self.hboxlayout10.addWidget(self.rightInValue)

        self.rightInStepperUnits = TauConfigLabel(self.rightStepper)
        self.rightInStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightInStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightInStepperUnits.setUseParentModel(True)
        self.rightInStepperUnits.setObjectName("rightInStepperUnits")
        self.hboxlayout10.addWidget(self.rightInStepperUnits)
        self.gridlayout3.addLayout(self.hboxlayout10,1,0,1,1)

        self.hboxlayout11 = QtGui.QHBoxLayout()
        self.hboxlayout11.setSpacing(1)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.rightMoveOut = QtGui.QPushButton(self.rightStepper)
        self.rightMoveOut.setObjectName("rightMoveOut")
        self.hboxlayout11.addWidget(self.rightMoveOut)

        self.rightOutValue = QtGui.QDoubleSpinBox(self.rightStepper)
        self.rightOutValue.setDecimals(3)
        self.rightOutValue.setMinimum(0.005)
        self.rightOutValue.setMaximum(20.0)
        self.rightOutValue.setSingleStep(0.001)
        self.rightOutValue.setProperty("value",QtCore.QVariant(1.0))
        self.rightOutValue.setObjectName("rightOutValue")
        self.hboxlayout11.addWidget(self.rightOutValue)

        self.rightOutStepperUnits = TauConfigLabel(self.rightStepper)
        self.rightOutStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightOutStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightOutStepperUnits.setUseParentModel(True)
        self.rightOutStepperUnits.setObjectName("rightOutStepperUnits")
        self.hboxlayout11.addWidget(self.rightOutStepperUnits)
        self.gridlayout3.addLayout(self.hboxlayout11,2,0,1,1)

        self.hboxlayout12 = QtGui.QHBoxLayout()
        self.hboxlayout12.setSpacing(1)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.rightMoveAbs = QtGui.QPushButton(self.rightStepper)
        self.rightMoveAbs.setObjectName("rightMoveAbs")
        self.hboxlayout12.addWidget(self.rightMoveAbs)

        self.rightAbsValue = QtGui.QDoubleSpinBox(self.rightStepper)
        self.rightAbsValue.setDecimals(3)
        self.rightAbsValue.setMaximum(20.0)
        self.rightAbsValue.setSingleStep(0.001)
        self.rightAbsValue.setProperty("value",QtCore.QVariant(1.0))
        self.rightAbsValue.setObjectName("rightAbsValue")
        self.hboxlayout12.addWidget(self.rightAbsValue)

        self.rightAbsStepperUnits = TauConfigLabel(self.rightStepper)
        self.rightAbsStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightAbsStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightAbsStepperUnits.setUseParentModel(True)
        self.rightAbsStepperUnits.setObjectName("rightAbsStepperUnits")
        self.hboxlayout12.addWidget(self.rightAbsStepperUnits)
        self.gridlayout3.addLayout(self.hboxlayout12,3,0,1,1)
        self.vboxlayout3.addWidget(self.rightStepper)

        self.rightEnc = TauGroupBox(self.rightJaw)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightEnc.sizePolicy().hasHeightForWidth())
        self.rightEnc.setSizePolicy(sizePolicy)
        self.rightEnc.setFlat(True)
        self.rightEnc.setShowText(False)
        self.rightEnc.setObjectName("rightEnc")

        self.gridlayout4 = QtGui.QGridLayout(self.rightEnc)
        self.gridlayout4.setMargin(0)
        self.gridlayout4.setVerticalSpacing(0)
        self.gridlayout4.setObjectName("gridlayout4")

        self.hboxlayout13 = QtGui.QHBoxLayout()
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.rightEncLabel = QtGui.QLabel(self.rightEnc)
        self.rightEncLabel.setObjectName("rightEncLabel")
        self.hboxlayout13.addWidget(self.rightEncLabel)

        self.rightEncRead = TauValueLabel(self.rightEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightEncRead.sizePolicy().hasHeightForWidth())
        self.rightEncRead.setSizePolicy(sizePolicy)
        self.rightEncRead.setUseParentModel(True)
        self.rightEncRead.setObjectName("rightEncRead")
        self.hboxlayout13.addWidget(self.rightEncRead)

        self.rightEncUnits = TauConfigLabel(self.rightEnc)
        self.rightEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightEncUnits.setUseParentModel(True)
        self.rightEncUnits.setObjectName("rightEncUnits")
        self.hboxlayout13.addWidget(self.rightEncUnits)
        self.gridlayout4.addLayout(self.hboxlayout13,0,0,1,1)
        self.vboxlayout3.addWidget(self.rightEnc)

        self.retranslateUi(SCRH)
        QtCore.QMetaObject.connectSlotsByName(SCRH)

    def retranslateUi(self, SCRH):
        SCRH.setWindowTitle(QtGui.QApplication.translate("SCRH", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SCRHName.setText(QtGui.QApplication.translate("SCRH", "SCRHName", None, QtGui.QApplication.UnicodeUTF8))
        self.leftJawLabel.setText(QtGui.QApplication.translate("SCRH", "Left Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.rightJawLabel.setText(QtGui.QApplication.translate("SCRH", "Right Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.gapRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapReadUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapWrite.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapWriteUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetReadUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.OffsetWrite.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetWriteUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapLabel.setText(QtGui.QApplication.translate("SCRH", "Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("SCRH", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("SCRH", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLabelState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLedState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitN.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitLabel.setText(QtGui.QApplication.translate("SCRH", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitP.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.leftMoveIn.setText(QtGui.QApplication.translate("SCRH", "Move IN", None, QtGui.QApplication.UnicodeUTF8))
        self.leftInStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.leftMoveOut.setText(QtGui.QApplication.translate("SCRH", "Move OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.leftOutStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.leftMoveAbs.setText(QtGui.QApplication.translate("SCRH", "Move TO", None, QtGui.QApplication.UnicodeUTF8))
        self.leftAbsStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncLabel.setText(QtGui.QApplication.translate("SCRH", "Encoder read:", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLabelState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLedState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitN.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitLabel.setText(QtGui.QApplication.translate("SCRH", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitP.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.rightMoveIn.setText(QtGui.QApplication.translate("SCRH", "Move IN", None, QtGui.QApplication.UnicodeUTF8))
        self.rightInStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.rightMoveOut.setText(QtGui.QApplication.translate("SCRH", "Move OUT", None, QtGui.QApplication.UnicodeUTF8))
        self.rightOutStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.rightMoveAbs.setText(QtGui.QApplication.translate("SCRH", "Move TO", None, QtGui.QApplication.UnicodeUTF8))
        self.rightAbsStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncLabel.setText(QtGui.QApplication.translate("SCRH", "Encoder read:", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))

from tau.widget import TauConfigLabel, TauGroupBox, TauValueLineEdit, TauLimitSwitch, TauValueLabel, TauStateLed
import scrapers_rc

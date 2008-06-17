# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCRV.ui'
#
# Created: Tue Jun 17 14:40:26 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SCRV(object):
    def setupUi(self, SCRV):
        SCRV.setObjectName("SCRV")
        SCRV.resize(QtCore.QSize(QtCore.QRect(0,0,528,485).size()).expandedTo(SCRV.minimumSizeHint()))

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

        self.rightJawLabel = QtGui.QLabel(SCRV)
        self.rightJawLabel.setGeometry(QtCore.QRect(10,440,152,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.rightJawLabel.setFont(font)
        self.rightJawLabel.setObjectName("rightJawLabel")

        self.upperJaw = QtGui.QGroupBox(SCRV)
        self.upperJaw.setGeometry(QtCore.QRect(10,130,231,98))
        self.upperJaw.setObjectName("upperJaw")

        self.gridlayout = QtGui.QGridLayout(self.upperJaw)
        self.gridlayout.setMargin(0)
        self.gridlayout.setVerticalSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        self.upperStepper = TauGroupBox(self.upperJaw)
        self.upperStepper.setFlat(True)
        self.upperStepper.setShowText(False)
        self.upperStepper.setObjectName("upperStepper")

        self.gridlayout1 = QtGui.QGridLayout(self.upperStepper)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

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
        self.gridlayout1.addLayout(self.hboxlayout,0,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.upperStepperLabel = QtGui.QLabel(self.upperStepper)
        self.upperStepperLabel.setObjectName("upperStepperLabel")
        self.hboxlayout1.addWidget(self.upperStepperLabel)

        self.upperStepperWrite = TauValueLineEdit(self.upperStepper)
        self.upperStepperWrite.setUseParentModel(True)
        self.upperStepperWrite.setObjectName("upperStepperWrite")
        self.hboxlayout1.addWidget(self.upperStepperWrite)

        self.upperStepperRead = TauValueLabel(self.upperStepper)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperStepperRead.sizePolicy().hasHeightForWidth())
        self.upperStepperRead.setSizePolicy(sizePolicy)
        self.upperStepperRead.setUseParentModel(True)
        self.upperStepperRead.setObjectName("upperStepperRead")
        self.hboxlayout1.addWidget(self.upperStepperRead)

        self.upperStepperUnits = TauConfigLabel(self.upperStepper)
        self.upperStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperStepperUnits.setUseParentModel(True)
        self.upperStepperUnits.setObjectName("upperStepperUnits")
        self.hboxlayout1.addWidget(self.upperStepperUnits)
        self.gridlayout1.addLayout(self.hboxlayout1,1,0,1,1)
        self.gridlayout.addWidget(self.upperStepper,0,0,1,1)

        self.upperEnc = TauGroupBox(self.upperJaw)
        self.upperEnc.setFlat(True)
        self.upperEnc.setShowText(False)
        self.upperEnc.setObjectName("upperEnc")

        self.gridlayout2 = QtGui.QGridLayout(self.upperEnc)
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.upperAbort = QtGui.QPushButton(self.upperEnc)
        self.upperAbort.setMaximumSize(QtCore.QSize(60,25))

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
        self.upperAbort.setPalette(palette)
        self.upperAbort.setObjectName("upperAbort")
        self.hboxlayout2.addWidget(self.upperAbort)

        self.upperEncLabel = QtGui.QLabel(self.upperEnc)
        self.upperEncLabel.setObjectName("upperEncLabel")
        self.hboxlayout2.addWidget(self.upperEncLabel)

        self.upperEncRead = TauValueLabel(self.upperEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperEncRead.sizePolicy().hasHeightForWidth())
        self.upperEncRead.setSizePolicy(sizePolicy)
        self.upperEncRead.setUseParentModel(True)
        self.upperEncRead.setObjectName("upperEncRead")
        self.hboxlayout2.addWidget(self.upperEncRead)

        self.upperEncUnits = TauConfigLabel(self.upperEnc)
        self.upperEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.upperEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.upperEncUnits.setUseParentModel(True)
        self.upperEncUnits.setObjectName("upperEncUnits")
        self.hboxlayout2.addWidget(self.upperEncUnits)
        self.gridlayout2.addLayout(self.hboxlayout2,0,0,1,1)
        self.gridlayout.addWidget(self.upperEnc,1,0,1,1)

        self.gapAndOffset = QtGui.QGroupBox(SCRV)
        self.gapAndOffset.setGeometry(QtCore.QRect(130,250,111,71))
        self.gapAndOffset.setFlat(True)
        self.gapAndOffset.setObjectName("gapAndOffset")

        self.vboxlayout = QtGui.QVBoxLayout(self.gapAndOffset)
        self.vboxlayout.setSpacing(8)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.gap = TauGroupBox(self.gapAndOffset)
        self.gap.setFlat(True)
        self.gap.setShowText(False)
        self.gap.setObjectName("gap")

        self.hboxlayout3 = QtGui.QHBoxLayout(self.gap)
        self.hboxlayout3.setSpacing(2)
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.gapRead = TauValueLabel(self.gap)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gapRead.sizePolicy().hasHeightForWidth())
        self.gapRead.setSizePolicy(sizePolicy)
        self.gapRead.setUseParentModel(True)
        self.gapRead.setObjectName("gapRead")
        self.hboxlayout3.addWidget(self.gapRead)

        self.gapUnits = TauConfigLabel(self.gap)
        self.gapUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapUnits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gapUnits.setUseParentModel(True)
        self.gapUnits.setObjectName("gapUnits")
        self.hboxlayout3.addWidget(self.gapUnits)
        self.vboxlayout.addWidget(self.gap)

        self.offset = TauGroupBox(self.gapAndOffset)
        self.offset.setFlat(True)
        self.offset.setShowText(False)
        self.offset.setObjectName("offset")

        self.hboxlayout4 = QtGui.QHBoxLayout(self.offset)
        self.hboxlayout4.setSpacing(2)
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.offsetRead = TauValueLabel(self.offset)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetRead.sizePolicy().hasHeightForWidth())
        self.offsetRead.setSizePolicy(sizePolicy)
        self.offsetRead.setUseParentModel(True)
        self.offsetRead.setObjectName("offsetRead")
        self.hboxlayout4.addWidget(self.offsetRead)

        self.offsetUnits = TauConfigLabel(self.offset)
        self.offsetUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetUnits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.offsetUnits.setUseParentModel(True)
        self.offsetUnits.setObjectName("offsetUnits")
        self.hboxlayout4.addWidget(self.offsetUnits)
        self.vboxlayout.addWidget(self.offset)

        self.lowerJaw = QtGui.QGroupBox(SCRV)
        self.lowerJaw.setGeometry(QtCore.QRect(10,340,231,98))
        self.lowerJaw.setObjectName("lowerJaw")

        self.gridlayout3 = QtGui.QGridLayout(self.lowerJaw)
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setVerticalSpacing(2)
        self.gridlayout3.setObjectName("gridlayout3")

        self.lowerStepper = TauGroupBox(self.lowerJaw)
        self.lowerStepper.setFlat(True)
        self.lowerStepper.setShowText(False)
        self.lowerStepper.setObjectName("lowerStepper")

        self.gridlayout4 = QtGui.QGridLayout(self.lowerStepper)
        self.gridlayout4.setMargin(0)
        self.gridlayout4.setSpacing(6)
        self.gridlayout4.setObjectName("gridlayout4")

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
        self.gridlayout4.addLayout(self.hboxlayout5,0,0,1,1)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.lowerStepperLabel = QtGui.QLabel(self.lowerStepper)
        self.lowerStepperLabel.setObjectName("lowerStepperLabel")
        self.hboxlayout6.addWidget(self.lowerStepperLabel)

        self.lowerStepperWrite = TauValueLineEdit(self.lowerStepper)
        self.lowerStepperWrite.setUseParentModel(True)
        self.lowerStepperWrite.setObjectName("lowerStepperWrite")
        self.hboxlayout6.addWidget(self.lowerStepperWrite)

        self.lowerStepperRead = TauValueLabel(self.lowerStepper)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerStepperRead.sizePolicy().hasHeightForWidth())
        self.lowerStepperRead.setSizePolicy(sizePolicy)
        self.lowerStepperRead.setUseParentModel(True)
        self.lowerStepperRead.setObjectName("lowerStepperRead")
        self.hboxlayout6.addWidget(self.lowerStepperRead)

        self.lowerStepperUnits = TauConfigLabel(self.lowerStepper)
        self.lowerStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerStepperUnits.setUseParentModel(True)
        self.lowerStepperUnits.setObjectName("lowerStepperUnits")
        self.hboxlayout6.addWidget(self.lowerStepperUnits)
        self.gridlayout4.addLayout(self.hboxlayout6,1,0,1,1)
        self.gridlayout3.addWidget(self.lowerStepper,0,0,1,1)

        self.lowerEnc = TauGroupBox(self.lowerJaw)
        self.lowerEnc.setFlat(True)
        self.lowerEnc.setShowText(False)
        self.lowerEnc.setObjectName("lowerEnc")

        self.gridlayout5 = QtGui.QGridLayout(self.lowerEnc)
        self.gridlayout5.setMargin(0)
        self.gridlayout5.setSpacing(6)
        self.gridlayout5.setObjectName("gridlayout5")

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.lowerAbort = QtGui.QPushButton(self.lowerEnc)
        self.lowerAbort.setMaximumSize(QtCore.QSize(60,25))

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
        self.lowerAbort.setPalette(palette)
        self.lowerAbort.setObjectName("lowerAbort")
        self.hboxlayout7.addWidget(self.lowerAbort)

        self.lowerEncLabel = QtGui.QLabel(self.lowerEnc)
        self.lowerEncLabel.setObjectName("lowerEncLabel")
        self.hboxlayout7.addWidget(self.lowerEncLabel)

        self.lowerEncRead = TauValueLabel(self.lowerEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowerEncRead.sizePolicy().hasHeightForWidth())
        self.lowerEncRead.setSizePolicy(sizePolicy)
        self.lowerEncRead.setUseParentModel(True)
        self.lowerEncRead.setObjectName("lowerEncRead")
        self.hboxlayout7.addWidget(self.lowerEncRead)

        self.lowerEncUnits = TauConfigLabel(self.lowerEnc)
        self.lowerEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.lowerEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.lowerEncUnits.setUseParentModel(True)
        self.lowerEncUnits.setObjectName("lowerEncUnits")
        self.hboxlayout7.addWidget(self.lowerEncUnits)
        self.gridlayout5.addLayout(self.hboxlayout7,0,0,1,1)
        self.gridlayout3.addWidget(self.lowerEnc,1,0,1,1)

        self.gapLabel = QtGui.QLabel(SCRV)
        self.gapLabel.setGeometry(QtCore.QRect(30,240,71,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.gapLabel.setFont(font)
        self.gapLabel.setObjectName("gapLabel")

        self.offsetLabel = QtGui.QLabel(SCRV)
        self.offsetLabel.setGeometry(QtCore.QRect(30,280,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.offsetLabel.setFont(font)
        self.offsetLabel.setObjectName("offsetLabel")

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

        self.retranslateUi(SCRV)
        QtCore.QMetaObject.connectSlotsByName(SCRV)

    def retranslateUi(self, SCRV):
        SCRV.setWindowTitle(QtGui.QApplication.translate("SCRV", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SCRVName.setText(QtGui.QApplication.translate("SCRV", "SCRVName", None, QtGui.QApplication.UnicodeUTF8))
        self.upperJawLabel.setText(QtGui.QApplication.translate("SCRV", "Upper Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.rightJawLabel.setText(QtGui.QApplication.translate("SCRV", "Lower Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLabelState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLedState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitN.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitLabel.setText(QtGui.QApplication.translate("SCRV", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.upperLimitP.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.upperStepperLabel.setText(QtGui.QApplication.translate("SCRV", "Stepper", None, QtGui.QApplication.UnicodeUTF8))
        self.upperStepperWrite.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.upperStepperRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.upperStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.upperAbort.setText(QtGui.QApplication.translate("SCRV", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncLabel.setText(QtGui.QApplication.translate("SCRV", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.upperEncUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLabelState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLedState.setModel(QtGui.QApplication.translate("SCRV", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitN.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitLabel.setText(QtGui.QApplication.translate("SCRV", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerLimitP.setModel(QtGui.QApplication.translate("SCRV", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerStepperLabel.setText(QtGui.QApplication.translate("SCRV", "Stepper", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerStepperWrite.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerStepperRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerStepperUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerAbort.setText(QtGui.QApplication.translate("SCRV", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncLabel.setText(QtGui.QApplication.translate("SCRV", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncRead.setModel(QtGui.QApplication.translate("SCRV", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.lowerEncUnits.setModel(QtGui.QApplication.translate("SCRV", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapLabel.setText(QtGui.QApplication.translate("SCRV", "Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("SCRV", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("SCRV", "Abort", None, QtGui.QApplication.UnicodeUTF8))

from tau.widget import TauConfigLabel, TauGroupBox, TauValueLineEdit, TauLimitSwitch, TauValueLabel, TauStateLed
import scrapers_rc
import scrapers_rc

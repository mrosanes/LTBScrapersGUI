# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCRH.ui'
#
# Created: Tue May 27 17:30:43 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SCRH(object):
    def setupUi(self, SCRH):
        SCRH.setObjectName("SCRH")
        SCRH.resize(QtCore.QSize(QtCore.QRect(0,0,708,235).size()).expandedTo(SCRH.minimumSizeHint()))

        self.SCRHName = QtGui.QLabel(SCRH)
        self.SCRHName.setGeometry(QtCore.QRect(260,30,288,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        font.setWeight(75)
        font.setItalic(True)
        font.setUnderline(True)
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
        self.rightJawLabel.setGeometry(QtCore.QRect(560,80,142,41))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.rightJawLabel.setFont(font)
        self.rightJawLabel.setObjectName("rightJawLabel")

        self.rightJaw = QtGui.QGroupBox(SCRH)
        self.rightJaw.setGeometry(QtCore.QRect(470,120,231,101))
        self.rightJaw.setObjectName("rightJaw")

        self.gridlayout = QtGui.QGridLayout(self.rightJaw)
        self.gridlayout.setMargin(0)
        self.gridlayout.setVerticalSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        self.rightStepper = TauGroupBox(self.rightJaw)
        self.rightStepper.setFlat(True)
        self.rightStepper.setShowText(False)
        self.rightStepper.setObjectName("rightStepper")

        self.gridlayout1 = QtGui.QGridLayout(self.rightStepper)
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.rightLabelState = TauValueLabel(self.rightStepper)
        self.rightLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.rightLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.rightLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.rightLabelState.setShowQuality(False)
        self.rightLabelState.setUseParentModel(True)
        self.rightLabelState.setObjectName("rightLabelState")
        self.hboxlayout.addWidget(self.rightLabelState)

        self.rightLedState = TauStateLed(self.rightStepper)
        self.rightLedState.setUseParentModel(True)
        self.rightLedState.setObjectName("rightLedState")
        self.hboxlayout.addWidget(self.rightLedState)

        spacerItem = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.rightLimitN = TauLimitSwitch(self.rightStepper)
        self.rightLimitN.setUseParentModel(True)
        self.rightLimitN.setBoolIndex(2)
        self.rightLimitN.setObjectName("rightLimitN")
        self.hboxlayout.addWidget(self.rightLimitN)

        self.rightLimitLabel = QtGui.QLabel(self.rightStepper)
        self.rightLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rightLimitLabel.setObjectName("rightLimitLabel")
        self.hboxlayout.addWidget(self.rightLimitLabel)

        self.rightLimitP = TauLimitSwitch(self.rightStepper)
        self.rightLimitP.setUseParentModel(True)
        self.rightLimitP.setBoolIndex(1)
        self.rightLimitP.setObjectName("rightLimitP")
        self.hboxlayout.addWidget(self.rightLimitP)
        self.gridlayout1.addLayout(self.hboxlayout,0,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.rightStepperLabel = QtGui.QLabel(self.rightStepper)
        self.rightStepperLabel.setObjectName("rightStepperLabel")
        self.hboxlayout1.addWidget(self.rightStepperLabel)

        self.rightStepperWrite = TauValueLineEdit(self.rightStepper)
        self.rightStepperWrite.setUseParentModel(True)
        self.rightStepperWrite.setObjectName("rightStepperWrite")
        self.hboxlayout1.addWidget(self.rightStepperWrite)

        self.rightStepperRead = TauValueLabel(self.rightStepper)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightStepperRead.sizePolicy().hasHeightForWidth())
        self.rightStepperRead.setSizePolicy(sizePolicy)
        self.rightStepperRead.setUseParentModel(True)
        self.rightStepperRead.setObjectName("rightStepperRead")
        self.hboxlayout1.addWidget(self.rightStepperRead)

        self.rightStepperUnits = TauConfigLabel(self.rightStepper)
        self.rightStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightStepperUnits.setUseParentModel(True)
        self.rightStepperUnits.setObjectName("rightStepperUnits")
        self.hboxlayout1.addWidget(self.rightStepperUnits)
        self.gridlayout1.addLayout(self.hboxlayout1,1,0,1,1)
        self.gridlayout.addWidget(self.rightStepper,0,0,1,1)

        self.rightEnc = TauGroupBox(self.rightJaw)
        self.rightEnc.setFlat(True)
        self.rightEnc.setShowText(False)
        self.rightEnc.setObjectName("rightEnc")

        self.gridlayout2 = QtGui.QGridLayout(self.rightEnc)
        self.gridlayout2.setMargin(0)
        self.gridlayout2.setSpacing(6)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.rightEncLabel = QtGui.QLabel(self.rightEnc)
        self.rightEncLabel.setObjectName("rightEncLabel")
        self.hboxlayout2.addWidget(self.rightEncLabel)

        self.rightEncRead = TauValueLabel(self.rightEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightEncRead.sizePolicy().hasHeightForWidth())
        self.rightEncRead.setSizePolicy(sizePolicy)
        self.rightEncRead.setUseParentModel(True)
        self.rightEncRead.setObjectName("rightEncRead")
        self.hboxlayout2.addWidget(self.rightEncRead)

        self.rightEncUnits = TauConfigLabel(self.rightEnc)
        self.rightEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.rightEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.rightEncUnits.setUseParentModel(True)
        self.rightEncUnits.setObjectName("rightEncUnits")
        self.hboxlayout2.addWidget(self.rightEncUnits)
        self.gridlayout2.addLayout(self.hboxlayout2,0,0,1,1)
        self.gridlayout.addWidget(self.rightEnc,1,0,1,1)

        self.leftJaw = QtGui.QGroupBox(SCRH)
        self.leftJaw.setGeometry(QtCore.QRect(10,120,231,101))
        self.leftJaw.setObjectName("leftJaw")

        self.gridlayout3 = QtGui.QGridLayout(self.leftJaw)
        self.gridlayout3.setMargin(0)
        self.gridlayout3.setVerticalSpacing(2)
        self.gridlayout3.setObjectName("gridlayout3")

        self.leftStepper = TauGroupBox(self.leftJaw)
        self.leftStepper.setFlat(True)
        self.leftStepper.setShowText(False)
        self.leftStepper.setObjectName("leftStepper")

        self.gridlayout4 = QtGui.QGridLayout(self.leftStepper)
        self.gridlayout4.setMargin(0)
        self.gridlayout4.setSpacing(6)
        self.gridlayout4.setObjectName("gridlayout4")

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.leftLabelState = TauValueLabel(self.leftStepper)
        self.leftLabelState.setMinimumSize(QtCore.QSize(50,22))
        self.leftLabelState.setFrameShape(QtGui.QFrame.NoFrame)
        self.leftLabelState.setFrameShadow(QtGui.QFrame.Plain)
        self.leftLabelState.setShowQuality(False)
        self.leftLabelState.setUseParentModel(True)
        self.leftLabelState.setObjectName("leftLabelState")
        self.hboxlayout3.addWidget(self.leftLabelState)

        self.leftLedState = TauStateLed(self.leftStepper)
        self.leftLedState.setUseParentModel(True)
        self.leftLedState.setObjectName("leftLedState")
        self.hboxlayout3.addWidget(self.leftLedState)

        spacerItem2 = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.leftLimitN = TauLimitSwitch(self.leftStepper)
        self.leftLimitN.setUseParentModel(True)
        self.leftLimitN.setBoolIndex(2)
        self.leftLimitN.setObjectName("leftLimitN")
        self.hboxlayout3.addWidget(self.leftLimitN)

        self.leftLimitLabel = QtGui.QLabel(self.leftStepper)
        self.leftLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.leftLimitLabel.setObjectName("leftLimitLabel")
        self.hboxlayout3.addWidget(self.leftLimitLabel)

        self.leftLimitP = TauLimitSwitch(self.leftStepper)
        self.leftLimitP.setUseParentModel(True)
        self.leftLimitP.setBoolIndex(1)
        self.leftLimitP.setObjectName("leftLimitP")
        self.hboxlayout3.addWidget(self.leftLimitP)
        self.gridlayout4.addLayout(self.hboxlayout3,0,0,1,1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.leftStepperLabel = QtGui.QLabel(self.leftStepper)
        self.leftStepperLabel.setObjectName("leftStepperLabel")
        self.hboxlayout4.addWidget(self.leftStepperLabel)

        self.leftStepperWrite = TauValueLineEdit(self.leftStepper)
        self.leftStepperWrite.setUseParentModel(True)
        self.leftStepperWrite.setObjectName("leftStepperWrite")
        self.hboxlayout4.addWidget(self.leftStepperWrite)

        self.leftStepperRead = TauValueLabel(self.leftStepper)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftStepperRead.sizePolicy().hasHeightForWidth())
        self.leftStepperRead.setSizePolicy(sizePolicy)
        self.leftStepperRead.setUseParentModel(True)
        self.leftStepperRead.setObjectName("leftStepperRead")
        self.hboxlayout4.addWidget(self.leftStepperRead)

        self.leftStepperUnits = TauConfigLabel(self.leftStepper)
        self.leftStepperUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftStepperUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftStepperUnits.setUseParentModel(True)
        self.leftStepperUnits.setObjectName("leftStepperUnits")
        self.hboxlayout4.addWidget(self.leftStepperUnits)
        self.gridlayout4.addLayout(self.hboxlayout4,1,0,1,1)
        self.gridlayout3.addWidget(self.leftStepper,0,0,1,1)

        self.leftEnc = TauGroupBox(self.leftJaw)
        self.leftEnc.setFlat(True)
        self.leftEnc.setShowText(False)
        self.leftEnc.setObjectName("leftEnc")

        self.gridlayout5 = QtGui.QGridLayout(self.leftEnc)
        self.gridlayout5.setMargin(0)
        self.gridlayout5.setSpacing(6)
        self.gridlayout5.setObjectName("gridlayout5")

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem3)

        self.leftEncLabel = QtGui.QLabel(self.leftEnc)
        self.leftEncLabel.setObjectName("leftEncLabel")
        self.hboxlayout5.addWidget(self.leftEncLabel)

        self.leftEncRead = TauValueLabel(self.leftEnc)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftEncRead.sizePolicy().hasHeightForWidth())
        self.leftEncRead.setSizePolicy(sizePolicy)
        self.leftEncRead.setUseParentModel(True)
        self.leftEncRead.setObjectName("leftEncRead")
        self.hboxlayout5.addWidget(self.leftEncRead)

        self.leftEncUnits = TauConfigLabel(self.leftEnc)
        self.leftEncUnits.setMinimumSize(QtCore.QSize(35,24))
        self.leftEncUnits.setMaximumSize(QtCore.QSize(35,24))
        self.leftEncUnits.setUseParentModel(True)
        self.leftEncUnits.setObjectName("leftEncUnits")
        self.hboxlayout5.addWidget(self.leftEncUnits)
        self.gridlayout5.addLayout(self.hboxlayout5,0,0,1,1)
        self.gridlayout3.addWidget(self.leftEnc,1,0,1,1)

        self.gapAndOffset = QtGui.QGroupBox(SCRH)
        self.gapAndOffset.setGeometry(QtCore.QRect(250,180,211,41))
        self.gapAndOffset.setFlat(True)
        self.gapAndOffset.setObjectName("gapAndOffset")

        self.hboxlayout6 = QtGui.QHBoxLayout(self.gapAndOffset)
        self.hboxlayout6.setSpacing(0)
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.gap = TauGroupBox(self.gapAndOffset)
        self.gap.setFlat(True)
        self.gap.setShowText(False)
        self.gap.setObjectName("gap")

        self.gridlayout6 = QtGui.QGridLayout(self.gap)
        self.gridlayout6.setMargin(0)
        self.gridlayout6.setObjectName("gridlayout6")

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.gapRead = TauValueLabel(self.gap)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gapRead.sizePolicy().hasHeightForWidth())
        self.gapRead.setSizePolicy(sizePolicy)
        self.gapRead.setUseParentModel(True)
        self.gapRead.setObjectName("gapRead")
        self.hboxlayout7.addWidget(self.gapRead)

        self.gapUnits = TauConfigLabel(self.gap)
        self.gapUnits.setMinimumSize(QtCore.QSize(35,24))
        self.gapUnits.setMaximumSize(QtCore.QSize(35,24))
        self.gapUnits.setUseParentModel(True)
        self.gapUnits.setObjectName("gapUnits")
        self.hboxlayout7.addWidget(self.gapUnits)
        self.gridlayout6.addLayout(self.hboxlayout7,0,0,1,1)
        self.hboxlayout6.addWidget(self.gap)

        self.offset = TauGroupBox(self.gapAndOffset)
        self.offset.setFlat(True)
        self.offset.setShowText(False)
        self.offset.setObjectName("offset")

        self.gridlayout7 = QtGui.QGridLayout(self.offset)
        self.gridlayout7.setMargin(0)
        self.gridlayout7.setObjectName("gridlayout7")

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.offsetRead = TauValueLabel(self.offset)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetRead.sizePolicy().hasHeightForWidth())
        self.offsetRead.setSizePolicy(sizePolicy)
        self.offsetRead.setUseParentModel(True)
        self.offsetRead.setObjectName("offsetRead")
        self.hboxlayout8.addWidget(self.offsetRead)

        self.offsetUnits = TauConfigLabel(self.offset)
        self.offsetUnits.setMinimumSize(QtCore.QSize(35,24))
        self.offsetUnits.setMaximumSize(QtCore.QSize(35,24))
        self.offsetUnits.setUseParentModel(True)
        self.offsetUnits.setObjectName("offsetUnits")
        self.hboxlayout8.addWidget(self.offsetUnits)
        self.gridlayout7.addLayout(self.hboxlayout8,0,0,1,1)
        self.hboxlayout6.addWidget(self.offset)

        self.gapLabel = QtGui.QLabel(SCRH)
        self.gapLabel.setGeometry(QtCore.QRect(250,140,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.gapLabel.setFont(font)
        self.gapLabel.setObjectName("gapLabel")

        self.offsetLabel = QtGui.QLabel(SCRH)
        self.offsetLabel.setGeometry(QtCore.QRect(350,140,88,40))

        font = QtGui.QFont()
        font.setPointSize(25)
        self.offsetLabel.setFont(font)
        self.offsetLabel.setObjectName("offsetLabel")

        self.retranslateUi(SCRH)
        QtCore.QMetaObject.connectSlotsByName(SCRH)

    def retranslateUi(self, SCRH):
        SCRH.setWindowTitle(QtGui.QApplication.translate("SCRH", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SCRHName.setText(QtGui.QApplication.translate("SCRH", "SCRHName", None, QtGui.QApplication.UnicodeUTF8))
        self.leftJawLabel.setText(QtGui.QApplication.translate("SCRH", "Left Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.rightJawLabel.setText(QtGui.QApplication.translate("SCRH", "Right Jaw", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLabelState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLedState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitN.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitLabel.setText(QtGui.QApplication.translate("SCRH", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.rightLimitP.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.rightStepperLabel.setText(QtGui.QApplication.translate("SCRH", "Stepper", None, QtGui.QApplication.UnicodeUTF8))
        self.rightStepperWrite.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.rightStepperRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.rightStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncLabel.setText(QtGui.QApplication.translate("SCRH", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.rightEncUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLabelState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLedState.setModel(QtGui.QApplication.translate("SCRH", "/State", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitN.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitLabel.setText(QtGui.QApplication.translate("SCRH", "- lim +", None, QtGui.QApplication.UnicodeUTF8))
        self.leftLimitP.setModel(QtGui.QApplication.translate("SCRH", "/Limit_switches", None, QtGui.QApplication.UnicodeUTF8))
        self.leftStepperLabel.setText(QtGui.QApplication.translate("SCRH", "Stepper", None, QtGui.QApplication.UnicodeUTF8))
        self.leftStepperWrite.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.leftStepperRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.leftStepperUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncLabel.setText(QtGui.QApplication.translate("SCRH", "Encoder", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.leftEncUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.gapUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetRead.setModel(QtGui.QApplication.translate("SCRH", "/Position", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetUnits.setModel(QtGui.QApplication.translate("SCRH", "/Position?configuration=unit", None, QtGui.QApplication.UnicodeUTF8))
        self.gapLabel.setText(QtGui.QApplication.translate("SCRH", "Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("SCRH", "Offset", None, QtGui.QApplication.UnicodeUTF8))

from tau.widget import TauConfigLabel, TauGroupBox, TauValueLineEdit, TauLimitSwitch, TauValueLabel, TauStateLed
import scrapers_rc

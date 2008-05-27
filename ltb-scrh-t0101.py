#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from ui_scrh import Ui_SCRH

SCRAPPER_NAME = 'LT-DI-SCRH-T0101'

# SCRH01-MOTL
LEFT_STEPPER = 'motor/ipapctrl/5'
# SCRH01-MOTR
RIGHT_STEPPER = 'motor/ipapctrl/6'

LEFT_ENC = 'pm/pmenc5ctrl/1'
RIGHT_ENC = 'pm/pmenc6ctrl/1'
GAP = 'pm/slitH01ctrl/1'
OFFSET = 'pm/slitH01ctrl/2'

class SCRH_T0101(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRH()
        self.ui.setupUi(self)

        # Connect Motors
        self.ConnectMotors()
        
    def ConnectMotors(self):

        # Scrapper name
        self.ui.SCRHName.setText(SCRAPPER_NAME)
        
        # Real Motors
        self.ui.leftStepper.setModel(LEFT_STEPPER)
        self.ui.rightStepper.setModel(RIGHT_STEPPER)
        
        # Pseudo Motors:
        self.ui.leftEnc.setModel(LEFT_ENC)
        self.ui.rightEnc.setModel(RIGHT_ENC)
        self.ui.gap.setModel(GAP)
        self.ui.offset.setModel(OFFSET)

       
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    scrh = SCRH_T0101()
    scrh.show()

    sys.exit(app.exec_())

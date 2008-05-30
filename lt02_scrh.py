#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from ui_scrh import Ui_SCRH

SCRAPPER_NAME = 'LT-DI-SCRH-T0201'

# SCRHT02_MOTL
LEFT_STEPPER = 'motor/ltb_ipapctrl/1'
# SCRHT02_MOTR
RIGHT_STEPPER = 'motor/ltb_ipapctrl/2'

# LT01/DI/ADC-SCR-01 Channel 0
LEFT_ENC = 'pm/lt02_pmenchlctrl/1'
# LT01/DI/ADC-SCR-01 Channel 1
RIGHT_ENC = 'pm/lt02_pmenchrctrl/'

GAP = 'pm/lt02_hslitctrl/1'
OFFSET = 'pm/lt02_hslitctrl/2'

class SCRH_T0201(QtGui.QMainWindow):
    
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
    scrh = SCRH_T0201()
    scrh.show()

    sys.exit(app.exec_())

#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from ui_scrh import Ui_SCRH

SCRAPPER_NAME = 'LT-DI-SCRH-T0101'

# SCRHT01-MOTL
LEFT_STEPPER = 'motor/ltb_ipapctrl/5'
# SCRHT01-MOTR
RIGHT_STEPPER = 'motor/ltb_ipapctrl/6'

# LT01/DI/ADC-SCR-01 Channel 4
LEFT_ENC = 'pm/lt01_pmenchlctrl/1'
# LT01/DI/ADC-SCR-01 Channel 5
RIGHT_ENC = 'pm/lt01_pmenchrctrl/1'

GAP = 'pm/lt01_hslitctrl/1'
OFFSET = 'pm/lt01_hslitctrl/2'

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

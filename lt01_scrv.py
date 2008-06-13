#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from ui_scrv import Ui_SCRV

#SCRAPER_NAME = 'LT-DI-SCRV-T0101'
SCRAPER_NAME = 'Vertical Scraper\nLinac To Booster Line'

# SCRVT01-MOTU
UPPER_STEPPER = 'motor/ltb_ipapctrl/3'
# SCRVT01-MOTD
LOWER_STEPPER = 'motor/ltb_ipapctrl/4'

# LT01/DI/ADC-SCR-01 Channel 2
UPPER_ENC = 'pm/lt01_pmencvuctrl/1'
# LT01/DI/ADC-SCR-01 Channel 3
LOWER_ENC = 'pm/lt01_pmencvdctrl/1'

GAP = 'pm/lt01_vslitctrl/1'
OFFSET = 'pm/lt01_vslitctrl/2'

class SCRV_T0101(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRV()
        self.ui.setupUi(self)

        # Connect Motors
        self.ConnectMotors()
        
    def ConnectMotors(self):

        # Scraper name
        self.ui.SCRVName.setText(SCRAPER_NAME)
        
        # Real Motors
        self.ui.upperStepper.setModel(UPPER_STEPPER)
        self.ui.lowerStepper.setModel(LOWER_STEPPER)
        
        # Pseudo Motors:
        self.ui.upperEnc.setModel(UPPER_ENC)
        self.ui.lowerEnc.setModel(LOWER_ENC)
        self.ui.gap.setModel(GAP)
        self.ui.offset.setModel(OFFSET)

       
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    scrh = SCRV_T0101()
    scrh.show()

    sys.exit(app.exec_())

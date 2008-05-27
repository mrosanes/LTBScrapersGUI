#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from ui_scrv import Ui_SCRV

SCRAPER_NAME = 'LT-DI-SCRV-T0101'

# SCRV-MOTU
UPPER_STEPPER = 'motor/ipapctrl/3'
# SCRV-MOTD
LOWER_STEPPER = 'motor/ipapctrl/4'

UPPER_ENC = 'pm/pmenc3ctrl/1'
LOWER_ENC = 'pm/pmenc4ctrl/1'

GAP = 'pm/slitV01ctrl/1'
OFFSET = 'pm/slitV01ctrl/2'

class SCRV_T0101(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRV()
        self.ui.setupUi(self)

        # Connect Motors
        self.ConnectMotors()
        
    def ConnectMotors(self):

        # Scrapper name
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

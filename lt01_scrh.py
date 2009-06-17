#!/usr/bin/env python

import sys
import tau.core
from PyQt4 import QtGui,QtCore
from ui_scrh import Ui_SCRH
from scrapercontroller import ScraperController

SCRAPER_NAME = 'Horizontal Scraper\nLinac To Booster Line'
SCRAPER_NAME_TOOLTIP = 'LT-DI-SCRH-T0101'

# SCRHT01-MOTL
LEFT_STEPPER = 'motor/ltb_ipapctrl/5'
# SCRHT01-MOTR
RIGHT_STEPPER = 'motor/ltb_ipapctrl/6'

# LT01/DI/ADC-SCR-01 Channel 4
LEFT_ENC = 'pm/lt01_pmenchl/1'
# LT01/DI/ADC-SCR-01 Channel 5
RIGHT_ENC = 'pm/lt01_pmenchr/1'

GAP = 'pm/lt01_hslit/1'
OFFSET = 'pm/lt01_hslit/2'

########################################
# GCUNI FOR TESTING
GCUNI_TESTING = False
if GCUNI_TESTING:
    SCRAPER_NAME = "GCUNI - TESTING @controls01"
    LEFT_STEPPER = 'tango://controls01:10000/motor/gc_simmotctrl/1'
    RIGHT_STEPPER = 'tango://controls01:10000/motor/gc_simmotctrl/2'

    LEFT_ENC = 'tango://controls01:10000/motor/gc_simmotctrl/1'
    RIGHT_ENC = 'tango://controls01:10000/motor/gc_simmotctrl/2'
    
    GAP = 'tango://controls01:10000/pm/gc_hslit/1'
    OFFSET = 'tango://controls01:10000/pm/gc_hslit/2'
########################################

class SCRH_T0101(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRH()
        self.ui.setupUi(self)

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,LEFT_STEPPER,RIGHT_STEPPER
            ,self.ui.abort
            ,self.ui.leftInValue,self.ui.leftMoveIn
            ,self.ui.leftOutValue,self.ui.leftMoveOut
            ,self.ui.leftAbsValue,self.ui.leftMoveAbs
            ,self.ui.rightInValue,self.ui.rightMoveIn
            ,self.ui.rightOutValue,self.ui.rightMoveOut
            ,self.ui.rightAbsValue,self.ui.rightMoveAbs)

        self.setTextAndModels()
        
    def setTextAndModels(self):
        # Scraper name
        self.ui.SCRHName.setText(SCRAPER_NAME)
        self.ui.SCRHName.setToolTip(SCRAPER_NAME_TOOLTIP)
        
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
    scrh.setWindowTitle(SCRAPER_NAME.replace("\n"," "))
    scrh.show()
    sys.exit(app.exec_())

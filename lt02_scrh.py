#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
from ui_scrh import Ui_SCRH
from scrapercontroller import ScraperController

SCRAPER_NAME = 'Horizontal Scraper - Diagnostics Line'
SCRAPER_NAME_TOOLTIP = 'LT-DI-SCRH-T0201'

# SCRHT02_MOTL
#LEFT_STEPPER = 'lt02_scrhl'
LEFT_STEPPER = 'motor/lt_ipapscrapers_ctrl/1'
# SCRHT02_MOTR
#RIGHT_STEPPER = 'lt02_scrhr'
RIGHT_STEPPER = 'motor/lt_ipapscrapers_ctrl/2'

# LT/DI/ADC-SCR-01 Channel 0
#LEFT_ENC = 'lt02_scrhl_enc'
#LEFT_ENC = 'pm/lt02_pmenchl_ctrl/1'
LEFT_ENC = LEFT_STEPPER

# LT/DI/ADC-SCR-01 Channel 1
#RIGHT_ENC = 'lt02_scrhr_enc'
#RIGHT_ENC = 'pm/lt02_pmenchr_ctrl/1'
RIGHT_ENC = RIGHT_STEPPER

#GAP = 'lt02_hgap'
GAP = 'pm/lt02_hslit_ctrl/1'
#OFFSET = 'lt02_hoffset'
OFFSET = 'pm/lt02_hslit_ctrl/2'

class SCRH_T0201(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRH()
        self.ui.setupUi(self)

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,LEFT_ENC,RIGHT_ENC
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
    scrh = SCRH_T0201()
    scrh.setWindowTitle(SCRAPER_NAME.replace("\n"," "))
    scrh.show()
    sys.exit(app.exec_())

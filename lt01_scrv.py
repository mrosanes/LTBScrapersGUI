#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
from ui_scrv import Ui_SCRV
from scrapercontroller import ScraperController

SCRAPER_NAME = 'Vertical Scraper\nLinac To Booster Line'
SCRAPER_NAME_TOOLTIP = 'LT-DI-SCRV-T0101'

# SCRVT01-MOTU
#UPPER_STEPPER = 'lt01_scrvu'
UPPER_STEPPER = 'motor/lt_ipapscrapers_ctrl/3'
# SCRVT01-MOTD
#LOWER_STEPPER = 'lt01_scrvd'
LOWER_STEPPER = 'motor/lt_ipapscrapers_ctrl/4'

# LT01/DI/ADC-SCR-01 Channel 2
#UPPER_ENC = 'lt01_scrvu_enc'
#UPPER_ENC = 'pm/lt01_pmencvu_ctrl/1'
UPPER_ENC = UPPER_STEPPER

# LT01/DI/ADC-SCR-01 Channel 3
#LOWER_ENC = 'lt01_scrvd_enc'
#LOWER_ENC = 'pm/lt01_pmencvd_ctrl/1'
LOWER_ENC = LOWER_STEPPER

#GAP = 'lt01_vgap'
GAP = 'pm/lt01_vslit_ctrl/1'
#OFFSET = 'lt01_voffset'
OFFSET = 'pm/lt01_vslit_ctrl/2'

class SCRV_T0101(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRV()
        self.ui.setupUi(self)

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,UPPER_ENC,LOWER_ENC
            ,self.ui.abort
            ,self.ui.upperInValue,self.ui.upperMoveIn
            ,self.ui.upperOutValue,self.ui.upperMoveOut
            ,self.ui.upperAbsValue,self.ui.upperMoveAbs
            ,self.ui.lowerInValue,self.ui.lowerMoveIn
            ,self.ui.lowerOutValue,self.ui.lowerMoveOut
            ,self.ui.lowerAbsValue,self.ui.lowerMoveAbs)

        self.setTextAndModels()
        
    def setTextAndModels(self):
        # Scraper name
        self.ui.SCRVName.setText(SCRAPER_NAME)
        self.ui.SCRVName.setToolTip(SCRAPER_NAME_TOOLTIP)
        
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
    scrv = SCRV_T0101()
    scrv.setWindowTitle(SCRAPER_NAME.replace("\n"," "))
    scrv.show()

    sys.exit(app.exec_())

#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
from ui_scrv import Ui_SCRV
from scrapercontroller import ScraperController

SCRAPER_NAME = 'Vertical Scraper\nLinac To Booster Line'
SCRAPER_NAME_TOOLTIP = 'LT-DI-SCRV-T0101'

# SCRVT01-MOTU
UPPER_STEPPER = 'lt01_scrvu'
# SCRVT01-MOTD
LOWER_STEPPER = 'lt01_scrvd'

# LT01/DI/ADC-SCR-01 Channel 2
UPPER_ENC = 'lt01_scrvu_enc'
# LT01/DI/ADC-SCR-01 Channel 3
LOWER_ENC = 'lt01_scrvd_enc'

GAP = 'lt01_vgap'
OFFSET = 'lt01_voffset'

########################################
# GCUNI FOR TESTING
GCUNI_TESTING = False
if GCUNI_TESTING:
    SCRAPER_NAME = "GCUNI - TESTING @controls01"
    UPPER_STEPPER = 'tango://controls01:10000/motor/gc_simmotctrl/3'
    LOWER_STEPPER = 'tango://controls01:10000/motor/gc_simmotctrl/4'

    UPPER_ENC = 'tango://controls01:10000/motor/gc_simmotctrl/3'
    LOWER_ENC = 'tango://controls01:10000/motor/gc_simmotctrl/4'
    
    GAP = 'tango://controls01:10000/pm/gc_vslit/1'
    OFFSET = 'tango://controls01:10000/pm/gc_vslit/2'
########################################

class SCRV_T0101(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRV()
        self.ui.setupUi(self)

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,UPPER_STEPPER,LOWER_STEPPER
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

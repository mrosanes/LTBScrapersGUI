#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
from ui_scrh import Ui_SCRH
from ui_scrv import Ui_SCRV
from scrapercontroller import ScraperController

class SCRH(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, models, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRH()
        self.ui.setupUi(self)

        self.scraper_name = models['SCRAPER_NAME']
        self.scraper_name_tooltip = models['SCRAPER_NAME_TOOLTIP']
        self.left_stepper = models['LEFT_STEPPER']
        self.right_stepper = models['RIGHT_STEPPER']
        self.left_enc = models['LEFT_ENC']
        self.right_enc = models['RIGHT_ENC']
        self.gap = models['GAP']
        self.offset = models['OFFSET']

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,self.left_enc,self.right_enc
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
        self.ui.SCRHName.setText(self.scraper_name)
        self.ui.SCRHName.setToolTip(self.scraper_name_tooltip)
        
        # Real Motors
        self.ui.leftStepper.setModel(self.left_stepper)
        self.ui.rightStepper.setModel(self.right_stepper)
        
        # Pseudo Motors:
        self.ui.leftEnc.setModel(self.left_enc)
        self.ui.rightEnc.setModel(self.right_enc)
        self.ui.gap.setModel(self.gap)
        self.ui.offset.setModel(self.offset)

class SCRV(QtGui.QMainWindow,ScraperController):
    
    def __init__(self, models, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRV()
        self.ui.setupUi(self)

        self.scraper_name = models['SCRAPER_NAME']
        self.scraper_name_tooltip = models['SCRAPER_NAME_TOOLTIP']
        self.upper_stepper = models['UPPER_STEPPER']
        self.lower_stepper = models['LOWER_STEPPER']
        self.upper_enc = models['UPPER_ENC']
        self.lower_enc = models['LOWER_ENC']
        self.gap = models['GAP']
        self.offset = models['OFFSET']

        # The scraper controller functionality needs the UI components
        ScraperController.__init__(
            self,self.upper_enc,self.lower_enc
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
        self.ui.SCRVName.setText(self.scraper_name)
        self.ui.SCRVName.setToolTip(self.scraper_name_tooltip)
        
        # Real Motors
        self.ui.upperStepper.setModel(self.upper_stepper)
        self.ui.lowerStepper.setModel(self.lower_stepper)
        
        # Pseudo Motors:
        self.ui.upperEnc.setModel(self.upper_enc)
        self.ui.lowerEnc.setModel(self.lower_enc)
        self.ui.gap.setModel(self.gap)
        self.ui.offset.setModel(self.offset)

LT02_SCRH_MODELS = {}
LT02_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper - Diagnostics Line'
LT02_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRH-T0201'
LT02_SCRH_MODELS['LEFT_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/1'
LT02_SCRH_MODELS['RIGHT_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/2'
LT02_SCRH_MODELS['LEFT_ENC'] = LT02_SCRH_MODELS['LEFT_STEPPER']
LT02_SCRH_MODELS['RIGHT_ENC'] = LT02_SCRH_MODELS['RIGHT_STEPPER']
LT02_SCRH_MODELS['GAP'] = 'pm/lt02_hslit_ctrl/1'
LT02_SCRH_MODELS['OFFSET'] = 'pm/lt02_hslit_ctrl/2'

LT01_SCRV_MODELS = {}
LT01_SCRV_MODELS['SCRAPER_NAME'] = 'Vertical Scraper\nLinac To Booster Line'
LT01_SCRV_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRV-T0101'
LT01_SCRV_MODELS['UPPER_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/3'
LT01_SCRV_MODELS['LOWER_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/4'
LT01_SCRV_MODELS['UPPER_ENC'] = LT01_SCRV_MODELS['UPPER_STEPPER']
LT01_SCRV_MODELS['LOWER_ENC'] = LT01_SCRV_MODELS['LOWER_STEPPER']
LT01_SCRV_MODELS['GAP'] = 'pm/lt01_vslit_ctrl/1'
LT01_SCRV_MODELS['OFFSET'] = 'pm/lt01_vslit_ctrl/2'

LT01_SCRH_MODELS = {}
LT01_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper\nLinac To Booster Line'
LT01_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRH-T0101'
LT01_SCRH_MODELS['LEFT_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/5'
LT01_SCRH_MODELS['RIGHT_STEPPER'] = 'motor/lt_ipapscrapers_ctrl/6'
LT01_SCRH_MODELS['LEFT_ENC'] = LT01_SCRH_MODELS['LEFT_STEPPER']
LT01_SCRH_MODELS['RIGHT_ENC'] = LT01_SCRH_MODELS['RIGHT_STEPPER']
LT01_SCRH_MODELS['GAP'] = 'pm/lt01_hslit_ctrl/1'
LT01_SCRH_MODELS['OFFSET'] = 'pm/lt01_hslit_ctrl/2'

SR_SCRV_MODELS = {}
SR_SCRV_MODELS['SCRAPER_NAME'] = 'Vertical Scraper\nInjection Straight'
SR_SCRV_MODELS['SCRAPER_NAME_TOOLTIP'] = ''
SR_SCRV_MODELS['UPPER_STEPPER'] = 'motor/sr_ipapfshscrapers_ctrl/3'
SR_SCRV_MODELS['LOWER_STEPPER'] = 'motor/sr_ipapfshscrapers_ctrl/4'
SR_SCRV_MODELS['UPPER_ENC'] = SR_SCRV_MODELS['UPPER_STEPPER']
SR_SCRV_MODELS['LOWER_ENC'] = SR_SCRV_MODELS['LOWER_STEPPER']
SR_SCRV_MODELS['GAP'] = 'pm/sr_vslit_ctrl/1'
SR_SCRV_MODELS['OFFSET'] = 'pm/sr_vslit_ctrl/2'

SR_SCRH_MODELS = {}
SR_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper\nInjection Straight'
SR_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = ''
SR_SCRH_MODELS['LEFT_STEPPER'] = 'motor/sr_ipapfshscrapers_ctrl/5'
SR_SCRH_MODELS['RIGHT_STEPPER'] = 'motor/sr_ipapfshscrapers_ctrl/6'
SR_SCRH_MODELS['LEFT_ENC'] = SR_SCRH_MODELS['LEFT_STEPPER']
SR_SCRH_MODELS['RIGHT_ENC'] = SR_SCRH_MODELS['RIGHT_STEPPER']
SR_SCRH_MODELS['GAP'] = 'pm/sr_hslit_ctrl/1'
SR_SCRH_MODELS['OFFSET'] = 'pm/sr_hslit_ctrl/2'

if __name__ == "__main__":
    usage = '\n\nUse as argument one of the following scrapers:\n\t\tlt02scrh lt01scrv lt01scrh srscrv or srscrh\n'
    if len(sys.argv) != 2:
        print usage
        sys.exit(-1)

    app = QtGui.QApplication(sys.argv)

    scraper = sys.argv[1]
    if scraper.upper() == 'LT02SCRH':
        window = SCRH(LT02_SCRH_MODELS)
    elif scraper.upper() == 'LT01SCRH':
        window = SCRH(LT01_SCRH_MODELS)
    elif scraper.upper() == 'LT01SCRV':
        window = SCRV(LT01_SCRV_MODELS)
    elif scraper.upper() == 'SRSCRH':
        window = SCRH(SR_SCRH_MODELS)
    elif scraper.upper() == 'SRSCRV':
        window = SCRV(SR_SCRV_MODELS)
    else:
        print usage
        sys.exit(-1)

    window.setWindowTitle(window.scraper_name.replace("\n"," "))
    window.show()
    sys.exit(app.exec_())

#!/usr/bin/env python

import sys
import PyTango

from PyQt4 import QtGui,QtCore
from ui_scrh import Ui_SCRH

SCRAPER_NAME = 'Horizontal Scraper - Diagnostics Line'
SCRAPER_NAME_TOOLTIP = 'LT-DI-SCRH-T0201'

# SCRHT02_MOTL
LEFT_STEPPER = 'motor/ltb_ipapctrl/1'

# SCRHT02_MOTR
RIGHT_STEPPER = 'motor/ltb_ipapctrl/2'

########################################
# GCUNI FOR TESTING
#LEFT_STEPPER = 'tango://controls01:10000/motor/gc_simumotctrl/1'
#RIGHT_STEPPER = 'tango://controls01:10000/motor/gc_simumotctrl/2'
########################################

# LT01/DI/ADC-SCR-01 Channel 0
LEFT_ENC = 'pm/lt02_pmenchlctrl/1'
# LT01/DI/ADC-SCR-01 Channel 1
RIGHT_ENC = 'pm/lt02_pmenchrctrl/1'

GAP = 'pm/lt02_hslitctrl/1'
OFFSET = 'pm/lt02_hslitctrl/2'

class SCRH_T0201(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Get graphical information
        self.ui = Ui_SCRH()
        self.ui.setupUi(self)

        # Connect ui signals
        QtCore.QObject.connect(self.ui.abort,QtCore.SIGNAL("clicked()"),self.abort)
        QtCore.QObject.connect(self.ui.leftAbort,QtCore.SIGNAL("clicked()"),self.leftAbort)
        QtCore.QObject.connect(self.ui.rightAbort,QtCore.SIGNAL("clicked()"),self.rightAbort)
        self.leftMotor = PyTango.DeviceProxy(LEFT_STEPPER)
        self.rightMotor = PyTango.DeviceProxy(RIGHT_STEPPER)
        
        # Connect Motors
        self.ConnectMotors()
        
    def ConnectMotors(self):

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

    def abort(self):
        self.leftAbort()
        self.rightAbort()
        
    def leftAbort(self):
        self.leftMotor.abort()
        
    def rightAbort(self):
        self.rightMotor.abort()
        

       
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    scrh = SCRH_T0201()
    scrh.show()

    sys.exit(app.exec_())

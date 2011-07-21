#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore

from ui_scrapersform import Ui_ScraperForm
import taurus

class ScraperWindow(QtGui.QMainWindow):
    def __init__(self, models, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.w = QtGui.QWidget()
        self.ui = Ui_ScraperForm()
        self.ui.setupUi(self.w)

        self.setCentralWidget(self.w)    

        self.scraper_name = models['SCRAPER_NAME']
        self.scraper_name_tooltip = models['SCRAPER_NAME_TOOLTIP']

        self.first_motor_name = models['FIRST_MOTOR']
        self.second_motor_name = models['SECOND_MOTOR']
        self.gap_motor_name = models['GAP']
        self.offset_motor_name = models['OFFSET']

        self.label_names = models['MOTOR_LABEL_NAMES']

        self.first_motor = taurus.Device(self.first_motor_name)
        self.second_motor = taurus.Device(self.second_motor_name)
        self.gap_motor = taurus.Device(self.gap_motor_name)
        self.offset_motor = taurus.Device(self.offset_motor_name)

        self.connect(self.ui.abort, QtCore.SIGNAL("clicked()"), self.abort)

        self.form_models = [self.first_motor_name, self.second_motor_name, self.gap_motor_name, self.offset_motor_name]
        if models.has_key('FORM_EXTRA_MODELS'):
            self.form_models += models['FORM_EXTRA_MODELS']

        self.setTextAndModels()

        ### Set some PoolMotorSlim controls visible
        ### Ubaldo also requests to change labels to something more intuitive: Upper/Lower Jaw, and Left/Right Jaw
        for motor_name in [self.first_motor_name, self.second_motor_name, self.gap_motor_name, self.offset_motor_name]:
            motor_tv_widget = self.ui.form.getItemByModel(motor_name)
            motor_pms = motor_tv_widget.customWidget()
            motor_pms.toggleHideAll()
            motor_pms.toggleMoveAbsolute(True)
            motor_pms.toggleMoveRelative(True)

            pms_label = motor_pms.taurus_value.labelWidget()
            pms_label.setFgRole('none')
            pms_label.setPrefixText(self.label_names[motor_name])

    def sizeHint(self):
        return QtCore.QSize(650,500)
        
    def setTextAndModels(self):
        # Scraper name
        self.ui.scraperName.setText(self.scraper_name)
        self.ui.scraperName.setToolTip(self.scraper_name_tooltip)
        
        # For Pool motors, use the PoolMotorSlim widget
        from taurus.qt.qtgui.extra_pool import PoolMotorSlim
        self.ui.form.setCustomWidgetMap({'SimuMotor':PoolMotorSlim,
                                         'Motor':PoolMotorSlim,
                                         'PseudoMotor':PoolMotorSlim})
        self.ui.form.setModel(self.form_models)

    def abort(self):
        exception_infos = []
        for motor in [self.first_motor, self.second_motor, self.gap_motor, self.offset_motor]:
            try:
                motor.abort()
            except:
                exception_infos.append(sys.exc_info())

        if len(exception_infos) > 0:
            print 'oups, some exceptions aborting motions'
            print exception_infos

LT02_SCRH_MODELS = {}
LT02_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper - Diagnostics Line'
LT02_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRH-T0201'
LT02_SCRH_MODELS['FIRST_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/1'
LT02_SCRH_MODELS['SECOND_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/2'
LT02_SCRH_MODELS['GAP'] = 'pm/lt02_hslit_ctrl/1'
LT02_SCRH_MODELS['OFFSET'] = 'pm/lt02_hslit_ctrl/2'
LT02_SCRH_MODELS['MOTOR_LABEL_NAMES'] = {'motor/lt_ipapscrapers_ctrl/1':'Left Jaw',
                                         'motor/lt_ipapscrapers_ctrl/2':'Right Jaw',
                                         'pm/lt02_hslit_ctrl/1':'Gap',
                                         'pm/lt02_hslit_ctrl/2':'Offset'}

LT01_SCRV_MODELS = {}
LT01_SCRV_MODELS['SCRAPER_NAME'] = 'Vertical Scraper\nLinac To Booster Line'
LT01_SCRV_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRV-T0101'
LT01_SCRV_MODELS['FIRST_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/3'
LT01_SCRV_MODELS['SECOND_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/4'
LT01_SCRV_MODELS['GAP'] = 'pm/lt01_vslit_ctrl/1'
LT01_SCRV_MODELS['OFFSET'] = 'pm/lt01_vslit_ctrl/2'
LT01_SCRV_MODELS['MOTOR_LABEL_NAMES'] = {'motor/lt_ipapscrapers_ctrl/3':'Upper Jaw',
                                         'motor/lt_ipapscrapers_ctrl/4':'Lower Jaw',
                                         'pm/lt01_vslit_ctrl/1':'Gap',
                                         'pm/lt01_vslit_ctrl/2':'Offset'}

LT01_SCRH_MODELS = {}
LT01_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper\nLinac To Booster Line'
LT01_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = 'LT-DI-SCRH-T0101'
LT01_SCRH_MODELS['FIRST_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/5'
LT01_SCRH_MODELS['SECOND_MOTOR'] = 'motor/lt_ipapscrapers_ctrl/6'
LT01_SCRH_MODELS['GAP'] = 'pm/lt01_hslit_ctrl/1'
LT01_SCRH_MODELS['OFFSET'] = 'pm/lt01_hslit_ctrl/2'
LT01_SCRH_MODELS['MOTOR_LABEL_NAMES'] = {'motor/lt_ipapscrapers_ctrl/5':'Left Jaw',
                                         'motor/lt_ipapscrapers_ctrl/6':'Right Jaw',
                                         'pm/lt01_hslit_ctrl/1':'Gap',
                                         'pm/lt01_hslit_ctrl/2':'Offset'}

SR_SCRV_MODELS = {}
SR_SCRV_MODELS['SCRAPER_NAME'] = 'Vertical Scraper\nInjection Straight'
SR_SCRV_MODELS['SCRAPER_NAME_TOOLTIP'] = 'SR-DI-SCRV-S16-01'
SR_SCRV_MODELS['FIRST_MOTOR'] = 'motor/sr_ipapfshscrapers_ctrl/3'
SR_SCRV_MODELS['SECOND_MOTOR'] = 'motor/sr_ipapfshscrapers_ctrl/4'
SR_SCRV_MODELS['GAP'] = 'pm/sr_vslit_ctrl/1'
SR_SCRV_MODELS['OFFSET'] = 'pm/sr_vslit_ctrl/2'
SR_SCRV_MODELS['MOTOR_LABEL_NAMES'] = {'motor/sr_ipapfshscrapers_ctrl/3':'Upper Jaw',
                                       'motor/sr_ipapfshscrapers_ctrl/4':'Lower Jaw',
                                       'pm/sr_vslit_ctrl/1':'Gap',
                                       'pm/sr_vslit_ctrl/2':'Offset'}
SR_SCRV_MODELS['FORM_EXTRA_MODELS'] = ['sr16/ct/scrv-plc-01/Tin','sr16/ct/scrv-plc-01/Tup','sr16/ct/scrv-plc-01/Tdown','sr16/ct/scrv-plc-01/FM_VECA']

SR_SCRH_MODELS = {}
SR_SCRH_MODELS['SCRAPER_NAME'] = 'Horizontal Scraper\nInjection Straight'
SR_SCRH_MODELS['SCRAPER_NAME_TOOLTIP'] = 'SR-DI-SCRH-S16-01'
SR_SCRH_MODELS['FIRST_MOTOR'] = 'motor/sr_ipapfshscrapers_ctrl/5'
SR_SCRH_MODELS['SECOND_MOTOR'] = 'motor/sr_ipapfshscrapers_ctrl/6'
SR_SCRH_MODELS['GAP'] = 'pm/sr_hslit_ctrl/1'
SR_SCRH_MODELS['OFFSET'] = 'pm/sr_hslit_ctrl/2'
SR_SCRH_MODELS['MOTOR_LABEL_NAMES'] = {'motor/sr_ipapfshscrapers_ctrl/5':'Left Jaw',
                                       'motor/sr_ipapfshscrapers_ctrl/6':'Right Jaw',
                                       'pm/sr_hslit_ctrl/1':'Gap',
                                       'pm/sr_hslit_ctrl/2':'Offset'}
SR_SCRH_MODELS['FORM_EXTRA_MODELS'] = ['sr16/ct/scrv-plc-01/Tin','sr16/ct/scrv-plc-01/Tleft','sr16/ct/scrv-plc-01/Tright','sr16/ct/scrv-plc-01/FM_HOCA']

TEST_MODELS = {}
TEST_MODELS['SCRAPER_NAME'] = 'Test scraper name\nTest description'
TEST_MODELS['SCRAPER_NAME_TOOLTIP'] = 'Just a description of the device'
TEST_MODELS['FIRST_MOTOR'] = 'gc_ipap1'
TEST_MODELS['SECOND_MOTOR'] = 'gc_ipap2'
TEST_MODELS['GAP'] = 'gc_hgap'
TEST_MODELS['OFFSET'] = 'gc_hoffset'
TEST_MODELS['MOTOR_LABEL_NAMES'] = {'gc_ipap1':'Upper Jaw', 'gc_ipap2':'Lower Jaw', 'gc_hgap':'Gap', 'gc_hoffset':'Offset'}
TEST_MODELS['FORM_EXTRA_MODELS'] = ['gc_ipap1/dialposition','gc_ipap2/dialposition','gc_hgap/position','gc_hoffset/position']

if __name__ == "__main__":
    usage = '\n\nUse as argument one of the following scrapers:\n\t\tlt02scrh lt01scrv lt01scrh srscrv or srscrh\n'
    if len(sys.argv) != 2:
        print usage
        sys.exit(-1)

    app = QtGui.QApplication(sys.argv)

    scraper = sys.argv[1]
    if scraper.upper() == 'LT02SCRH':
        window = ScraperWindow(LT02_SCRH_MODELS)
    elif scraper.upper() == 'LT01SCRH':
        window = ScraperWindow(LT01_SCRH_MODELS)
    elif scraper.upper() == 'LT01SCRV':
        window = ScraperWindow(LT01_SCRV_MODELS)
    elif scraper.upper() == 'SRSCRH':
        window = ScraperWindow(SR_SCRH_MODELS)
    elif scraper.upper() == 'SRSCRV':
        window = ScraperWindow(SR_SCRV_MODELS)
    elif scraper.upper() == 'TEST':
        window = ScraperWindow(TEST_MODELS)
    else:
        print usage
        sys.exit(-1)

    window.setWindowTitle(window.scraper_name.replace("\n"," "))
    window.show()
    sys.exit(app.exec_())

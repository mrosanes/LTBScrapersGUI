from tau.core import TangoFactory

from PyQt4 import QtCore

class ScraperController():
    
    def __init__(self,dev_mot1,dev_mot2
                 ,abort,mot1_rel,mot1_dec,mot1_inc,mot2_rel,mot2_dec,mot2_inc):
        
        self.mot1 = TangoFactory().getDevice(dev_mot1)
        self.mot2 = TangoFactory().getDevice(dev_mot2)

        self.ui_abort = abort
        
        self.ui_mot1_rel = mot1_rel
        self.ui_mot1_dec = mot1_dec
        self.ui_mot1_inc = mot1_inc
        
        self.ui_mot2_rel = mot2_rel
        self.ui_mot2_dec = mot2_dec
        self.ui_mot2_inc = mot2_inc

        # Connect ui signals
        QtCore.QObject.connect(self.ui_abort,QtCore.SIGNAL("clicked()"),self.abort)
        QtCore.QObject.connect(self.ui_mot1_dec,QtCore.SIGNAL("clicked()"),self.mot1RelativeDec)
        QtCore.QObject.connect(self.ui_mot1_inc,QtCore.SIGNAL("clicked()"),self.mot1RelativeInc)
        QtCore.QObject.connect(self.ui_mot2_dec,QtCore.SIGNAL("clicked()"),self.mot2RelativeDec)
        QtCore.QObject.connect(self.ui_mot2_inc,QtCore.SIGNAL("clicked()"),self.mot2RelativeInc)

        
    def abort(self):
        self.mot1.abort()
        self.mot2.abort()

        
    def mot1RelativeDec(self):
        inc = -1 * self.ui_mot1_rel.value()
        self.moveRelative(self.mot1,inc)


    def mot1RelativeInc(self):
        inc = self.ui_mot1_rel.value()
        self.moveRelative(self.mot1,inc)


    def mot2RelativeDec(self):
        inc = -1 * self.ui_mot2_rel.value()
        self.moveRelative(self.mot2,inc)


    def mot2RelativeInc(self):
        inc = self.ui_mot2_rel.value()
        self.moveRelative(self.mot2,inc)


    def moveRelative(self,motor,inc):
        pos = motor.read_attribute("Position").value
        pos = pos + float(inc)
        motor.write_attribute("Position",pos)
        


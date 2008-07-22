from tau.core import TangoFactory

from PyQt4 import QtCore

class ScraperController():
    
    def __init__(self,dev_mot1,dev_mot2
                 ,abort
                 ,mot1_in,mot1_in_b,mot1_out,mot1_out_b,mot1_abs,mot1_abs_b
                 ,mot2_in,mot2_in_b,mot2_out,mot2_out_b,mot2_abs,mot2_abs_b):
        
        self.mot1 = TangoFactory().getDevice(dev_mot1)
        self.mot2 = TangoFactory().getDevice(dev_mot2)

        self.ui_abort = abort
        
        self.ui_mot1_in = mot1_in
        self.ui_mot1_in_b = mot1_in_b
        self.ui_mot1_out = mot1_out
        self.ui_mot1_out_b = mot1_out_b
        self.ui_mot1_abs = mot1_abs
        self.ui_mot1_abs_b = mot1_abs_b
        
        self.ui_mot2_in = mot2_in
        self.ui_mot2_in_b = mot2_in_b
        self.ui_mot2_out = mot2_out
        self.ui_mot2_out_b = mot2_out_b
        self.ui_mot2_abs = mot2_abs
        self.ui_mot2_abs_b = mot2_abs_b
        
        # Connect ui signals
        QtCore.QObject.connect(self.ui_abort,QtCore.SIGNAL("clicked()"),self.abort)
        
        QtCore.QObject.connect(self.ui_mot1_in_b,QtCore.SIGNAL("clicked()"),self.mot1In)
        QtCore.QObject.connect(self.ui_mot1_out_b,QtCore.SIGNAL("clicked()"),self.mot1Out)
        QtCore.QObject.connect(self.ui_mot1_abs_b,QtCore.SIGNAL("clicked()"),self.mot1Abs)
        
        QtCore.QObject.connect(self.ui_mot2_in_b,QtCore.SIGNAL("clicked()"),self.mot2In)
        QtCore.QObject.connect(self.ui_mot2_out_b,QtCore.SIGNAL("clicked()"),self.mot2Out)
        QtCore.QObject.connect(self.ui_mot2_abs_b,QtCore.SIGNAL("clicked()"),self.mot2Abs)
        

        
    def abort(self):
        self.mot1.abort()
        self.mot2.abort()

        
    def mot1In(self):
        inc = -1 * self.ui_mot1_in.value()
        self.moveRelative(self.mot1,inc)

    def mot1Out(self):
        inc = self.ui_mot1_out.value()
        self.moveRelative(self.mot1,inc)

    def mot1Abs(self):
        pos = self.ui_mot1_abs.value()
        self.mot1.write_attribute("Position",pos)

    def mot2In(self):
        inc = -1 * self.ui_mot2_in.value()
        self.moveRelative(self.mot2,inc)


    def mot2Out(self):
        inc = self.ui_mot2_out.value()
        self.moveRelative(self.mot2,inc)

    def mot2Abs(self):
        pos = self.ui_mot2_abs.value()
        self.mot2.write_attribute("Position",pos)

    def moveRelative(self,motor,inc):
        try:
            pos = motor.read_attribute("Position").value
            pos = pos + float(inc)
            motor.write_attribute("Position",pos)
        except Exception,e:
            print "ScraperController: Some error trying to move relative",e
        

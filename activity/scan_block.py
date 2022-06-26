#!/usr/bin/env pybricks-micropython
from utilities.motors import Motors, follow_for_color
from utilities.sensor import Sensor

class ScanBlock():
    def __init__(self):
        self.sensor=Sensor()
        self.motors = Motors()
        
    def main(self):
        #self.motors.line_folower(follow_for=follow_for_color, cs=self.sensor.ColorLeft())
        self.motors.curve(-90)
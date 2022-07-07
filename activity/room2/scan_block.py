#!/usr/bin/env pybricks-micropython
from utilities.motors import Motors, follow_for_color
from utilities.sensor import Sensor
from utilities.claw import Claw

class ScanBlock():
    def __init__(self):
        self.sensor=Sensor()
        self.motors = Motors()
        self.claw = Sensor()
        
    def main(self):
        
        self.motors.line_folower(follow_for=follow_for_color, cs=self.sensor.ColorLeft())
        self.motors.move(105)
        self.motors.tank_turn(-90, cs=self.sensor.ColorLeft())
        self.claw.moveTo(50)
        self.claw.motor.hold()
        self.motors.move(20)
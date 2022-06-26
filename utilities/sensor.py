#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

class Sensor():
    def __init__(
                self, 
                speed=50,
        ):
        
        self.cs_base = ColorSensor(Port.S1)
        self.cs_left = ColorSensor(Port.S2)
        
        self.speed = speed
        self.motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        
    def ColorBase(self):
        return self.cs_base
    
    def ColorLeft(self):
        return self.cs_left
    
    def move(self, rotation):
        self.motor.run_angle(self.speed, rotation)
        
    def moveTo(self, rotation):
        self.motor.run_target(self.speed, rotation)
    
    def start(self):
        self.motor.reset_angle(0)
        self.moveTo(80)
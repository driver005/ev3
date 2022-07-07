#!/usr/bin/env pybricks-micropython
from time import sleep, time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from utilities.sensor import Sensor

class Claw():
    def __init__(
                self, 
                speed=300,
        ):
        
        self.speed = speed
        self.sensors = Sensor()
        
        self.motor = Motor(Port.A)
        
    def move(self, rotation):
        self.motor.run_angle(self.speed, rotation)
        
    def moveTo(self, rotation):
        self.motor.run_target(self.speed, rotation)
        
    def start(self):
        self.sensors.start()
        self.move(475)
        self.motor.reset_angle(0)
        self.moveTo(-40)
        self.sensors.moveTo(0)
        self.moveTo(0)
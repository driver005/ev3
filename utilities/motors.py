#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from utilities.sensor import Sensor


# line follower functions
def follow_for_forever(robot):
    return True 

def follow_for_color(robot, cs):
    if(cs.color() == Color.BLACK):
        return False
    else:
        return True

class Motors():
    def __init__(
                self, 
                speed=50, 
                sleep_time=1,
                black=9,
                white=85,
                proportional_gain=0.8, 
                wheel_diameter=17.5,
                axle_track=140
        ):
        
        self.speed = speed
        self.sleep_time = sleep_time
        self.proportional_gain = proportional_gain
        
        # Initialize the motors.
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.left_motor = Motor(Port.C)
        self.right_motor = Motor(Port.D)

        # Initialize the color sensor.
        self.threshold = (black + white) / 2
        self.line_sensor = Sensor().ColorBase()

        # Initialize the drive base.
        self.robot = DriveBase(
            self.left_motor, 
            self.right_motor, 
            wheel_diameter=self.wheel_diameter, 
            axle_track=self.axle_track
        )
        
        self.robot.settings(
            straight_speed=self.speed,
            turn_rate=self.speed,
        )
        
    def line_folower(self, follow_for=follow_for_forever, **kwargs):
        while follow_for(self, **kwargs):
            # Calculate the deviation from the threshold.
            deviation = self.line_sensor.reflection() - self.threshold

            # Calculate the turn rate.
            turn_rate = self.proportional_gain * deviation

            # Set the drive base speed and turn rate.
            self.robot.drive(self.speed, turn_rate)

            # You can wait for a short time or do other things in this loop.
            wait(self.sleep_time)
            # if(self.line_sensor.color() == Color.BLACK):
            #     self.robot.drive(self.speed, -20)
            # else:
            #     self.robot.drive(self.speed, 20)
            
    def move(self, distance):
        self.robot.straight(distance)

    def turn(self, turn):
        self.robot.turn(turn)
    
    def curve(self, turn):
        self.turn(turn-(turn/2))
        while self.line_sensor.color() != Color.BLACK:
            if(turn < 0):
                self.robot.drive(self.speed, -360)
            else:
                self.robot.drive(self.speed, 100)
            
        self.robot.stop()
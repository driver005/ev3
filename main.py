#!/usr/bin/env pybricks-micropython
from area.room import Room
from utilities.claw import Claw

claw = Claw()
room = Room()

claw.start()
room.main()

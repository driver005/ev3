#!/usr/bin/env pybricks-micropython

from activity.room1.scan_block import ScanBlock


class Room():
    def __init__(self):
        self.scan_block=ScanBlock()
    
    def main(self):
        self.scan_block.main()
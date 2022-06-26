#!/usr/bin/env pybricks-micropython

from activity.scan_block import ScanBlock


class Room():
    def __init__(self):
        self.scan_block=ScanBlock()
    
    def main(self):
        self.scan_block.main()
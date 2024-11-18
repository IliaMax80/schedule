from datetime import time


class AffairPeriod:
    def __init__(self, start: time, end: time, affair: str, schedule: 'Schedule'):
        self.start: time = start
        self.end: time = end
        self.affair: str = affair
        self.schedule: 'Schedule' = schedule

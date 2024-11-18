import abc
from abc import ABC
from datetime import date

from models.affair_period import AffairPeriod


class Schedule(ABC):
    def __init__(self, affairs: list[AffairPeriod]):
        self._affairs: list[AffairPeriod] = affairs

    @abc.abstractmethod
    def save_affair(self) -> None:
        pass

class ScheduleDay(Schedule):
    def __init__(self, current_date: date):
        super().__init__()

    pass
import abc
import datetime
from abc import ABC
from datetime import date, time

from models.affair_period import AffairPeriod
from utils.database import DataBase, ScheduleTuple, AffairPeriodTuple


class Schedule(ABC):
    def __init__(self, id: int, ids: int | None = None):
        self.id: int = id
        if ids is None:
            self.ids: list[int] = [self.id]
        else:
            self.ids: list[int] = [self.id] + [ids]
        self._affairs: list[AffairPeriod] = []
        self.setup_affair()

    def get_affairs(self) -> list[AffairPeriod]:
        return self._affairs

    @abc.abstractmethod
    def save_affair(self) -> None:
        pass

    def add_affair_period(self, affair: AffairPeriod):
        self._affairs.append(affair)
        self.update_affairs()

    def setup_affair(self) -> None:
        affair_ids: list[int] = DataBase.affair_search_id(self.ids)
        affair_tuples: list[AffairPeriodTuple] = DataBase.get_affairs(affair_ids)
        affairs: list[AffairPeriod] = self.affair_period_tuple_to_affair_period(affair_tuples)
        self._affairs: list[AffairPeriod] = affairs
        self.update_affairs()

    def update_affairs(self) -> None:
        self.check_affairs()
        self._affairs = sorted(self._affairs, key=lambda x: x.start)
        self.save_affair()
        self._affairs = [affair_period for affair_period in self._affairs if not affair_period.is_delete]

    def affair_period_tuple_to_affair_period(self, affairs: list[AffairPeriodTuple]) -> list[AffairPeriod]:
        affair_periods: list[AffairPeriod] = []
        for affair in affairs:
            start: time = datetime.datetime.strptime(affair.start, '%H:%M').time()
            end: time = datetime.datetime.strptime(affair.end, '%H:%M').time()
            affair_periods.append(
                AffairPeriod(affair.id, start, end, affair.name, self, affair.is_delete, affair.is_error))
        return affair_periods

    def check_affairs(self) -> None:
        start_times: list[tuple[time, bool]] = [(affair.start, True) for affair in self._affairs]
        end_times: list[tuple[time, bool]] = [(affair.end, False) for affair in self._affairs]
        times: list[tuple[time, bool]] = sorted(start_times + end_times, key=lambda x: (x[0], x[1]))
        print(times)
        for i in range(len(times) - 1):
            if times[i][1] == times[i + 1][1]:
                raise ValueError


class ScheduleDay(Schedule):
    def __init__(self, current_date: date):
        self.current_data: date = current_date
        id: int = DataBase.schedule_search_day_id(date=f'{current_date:%d.%m.%Y}')
        self.is_existing: bool = not (id is None)
        if self.is_existing:
            schedule_tuple: ScheduleTuple = DataBase.get_schedule(id)
            self.root_id: int = schedule_tuple.root
        else:
            self.root_id: int = DataBase.get_default_week()[current_date.weekday()]
            schedule_tuple: ScheduleTuple = ScheduleTuple(0, 0, f'{current_date:%d.%m.%Y}', '', self.root_id, None)
            id: int = DataBase.create_schedule(schedule_tuple)

        super().__init__(id, self.root_id)

    def save_affair(self) -> None:
        if self.root_id:
            tuple_root_affairs_ids: list[int] = DataBase.affair_search_id([self.root_id])
        for affair_period in self._affairs:
            tuple_affair: AffairPeriodTuple = affair_period.get_tuple_affair()
            if tuple_affair.id in tuple_root_affairs_ids:
                tuple_affair = AffairPeriodTuple(tuple_affair.id, tuple_affair.name, tuple_affair.start,
                                                 tuple_affair.end, self.root_id, tuple_affair.is_delete,
                                                 tuple_affair.is_error)
            DataBase.record_affair_period(tuple_affair)


class SchedulePattern(Schedule):
    def __init__(self, name):
        self.name = name
        id: int = DataBase.schedule_search_pattern_id(name=name)
        schedule_tuple: ScheduleTuple = DataBase.get_schedule(id)
        self.default_week: int = schedule_tuple.default_week
        super().__init__(id)

    def save_affair(self) -> None:
        for affair_period in self._affairs:
            print(affair_period.id)
            DataBase.record_affair_period(affair_period.get_tuple_affair())

from datetime import time, datetime

from utils.database import AffairPeriodTuple, DataBase


class AffairPeriod:

    def __init__(self, id: int | None, start: time, end: time, affair: str, schedule: 'Schedule', is_delete: bool,
                 is_error: bool):
        if isinstance(id, int):
            self.id: int = id
        else:
            self.id: int = max(DataBase.get_ids_affair_period()) + 1
        self.start: time = start
        self.end: time = end
        self.affair: str = affair
        self.schedule: 'Schedule' = schedule
        self.is_delete: bool = is_delete
        self.is_error: bool = is_error

    def get_tuple_affair(self) -> AffairPeriodTuple:
        start: str = f'{self.start:%H:%M}'
        end: str = f'{self.end:%H:%M}'
        schedule_id: int = self.schedule.id
        affair: AffairPeriodTuple = AffairPeriodTuple(self.id, self.affair, start, end, schedule_id,
                                                      self.is_delete, self.is_error)
        return affair

    def set_tuple_affair(self, tuple_affair: AffairPeriodTuple) -> None:
        self.id = tuple_affair.id
        self.start = datetime.strptime(tuple_affair.start, '%H:%M').time()
        self.end = datetime.strptime(tuple_affair.end, '%H:%M').time()
        self.affair = tuple_affair.name
        self.is_delete = tuple_affair.is_delete
        self.is_error = tuple_affair.is_error

    def remove(self):
        self.is_delete = True

import pathlib
import sqlite3
from datetime import date
from sqlite3 import connect
from collections import namedtuple

ScheduleTuple = namedtuple('ScheduleTuple', ['id',
                                             'is_pattern',
                                             'date',
                                             'name',
                                             'root',
                                             'default_week'])
AffairPeriodTuple = namedtuple('AffairPeriod', ['id',
                                                'name',
                                                'start',
                                                'end',
                                                'schedule',
                                                'is_delete',
                                                'is_error'])


class DataBase:
    user: str = 'test'

    @staticmethod
    def set_user(user: str) -> None:
        DataBase.user = user

    @classmethod
    def create_schedule(cls, schedule_tuple: ScheduleTuple) -> int:
        query = f'''SELECT id
                    FROM schedule'''
        id = max([i[0] for i in DataBase.query_database(query)]) + 1

        root_id: str = 'NULL' if schedule_tuple.root is None else str(schedule_tuple.root)
        default_week: str = 'NULL' if schedule_tuple.default_week is None else str(schedule_tuple.default_week)
        query = f'''INSERT INTO schedule
                    VALUES ({id}, '{cls.user}', {schedule_tuple.is_pattern}, '{schedule_tuple.date}', 
                    '{schedule_tuple.name}', {root_id}, {default_week});
                    '''
        DataBase.query_database(query, commit=True)
        return id

    @classmethod
    def affair_search_id(cls, schedule_ids: list[int]) -> list[int]:

        query = f'''SELECT id  
                    FROM affair
                    WHERE user='{cls.user}' and schedule in ({', '.join([str(id) for id in schedule_ids])});'''
        answer = DataBase.query_database(query)
        if len(answer) == 0:
            return []

        return [i[0] for i in answer]

    @classmethod
    def record_affair_period(cls, affair_period: AffairPeriodTuple) -> None:
        if affair_period.id in cls.get_ids_affair_period():
            query = f'''UPDATE affair
                        SET name='{affair_period.name}', start='{affair_period.start}', 
                        end='{affair_period.end}', schedule={affair_period.schedule}, 
                        is_delete = {int(affair_period.is_delete)}, is_error = {int(affair_period.is_error)}
                        WHERE user='{cls.user}' and id = {affair_period.id};'''
        else:
            query = f'''INSERT INTO affair
                        VALUES ({affair_period.id}, '{cls.user}', '{affair_period.name}', 
                        '{affair_period.start}', '{affair_period.end}', '{affair_period.schedule}', 
                        {affair_period.is_delete}, {affair_period.is_error} );'''
        DataBase.query_database(query, commit=True)

    @classmethod
    def get_affairs(cls, affair_ids: list[int]) -> list[AffairPeriodTuple]:
        query = f'''SELECT id, name, start, end, schedule, is_delete, is_error
                    FROM affair
                    WHERE user='{cls.user}' and id in ({', '.join([str(i) for i in affair_ids])}) and is_delete=0;'''
        affairs: list[AffairPeriodTuple] = [AffairPeriodTuple(*affair) for affair in DataBase.query_database(query)]
        return affairs

    @staticmethod
    def schedule_search_default_pattern(day_week: int) -> id:
        query = f'''SELECT id 
                    FROM affair
                    WHERE default_week='{day_week}';'''
        return DataBase.query_database(query)[0][0]

    @staticmethod
    def schedule_search_day_id(date: str = '') -> int | None:
        query = f'''SELECT id FROM schedule
                    WHERE user='{DataBase.user}' and date='{date}';'''
        records: list[list[int]] = DataBase.query_database(query)
        if len(records) == 1 and len(records[0]) == 1:
            id = DataBase.query_database(query)[0][0]
            return id

        return None
    @staticmethod
    def schedule_search_pattern_id( name: str = '') -> int | None:
        query = f'''SELECT id FROM schedule
                    WHERE user='{DataBase.user}' and name='{name}';'''
        records: list[list[int]] = DataBase.query_database(query)
        if len(records) == 1 and len(records[0]) == 1:
            id = DataBase.query_database(query)[0][0]
            return id
        return None

    @classmethod
    def get_names_schedule_pattern(cls) -> list[int]:
        query = f'''SELECT id 
                    FROM schedule
                    WHERE user='{cls.user}' and  is_pattern=1;'''
        answer = cls.query_database(query)
        return [i[0] for i in answer]

    @classmethod
    def get_ids_affair_period(cls) -> list[int]:
        query = f'''SELECT id 
                    FROM affair
                    WHERE user='{cls.user}';'''
        answer = cls.query_database(query)
        return [i[0] for i in answer]

    @staticmethod
    def query_database(query: str, commit: bool = False) -> list[list[any]]:
        path = pathlib.PurePath(__file__)
        path = path.parent.parent.joinpath('database', 'schedule')
        con = connect(path)
        curses = con.cursor()
        print(query)
        curses.execute(query)
        if commit:
            con.commit()
        records = curses.fetchall()
        return records

    @classmethod
    def get_schedules(cls, ids: list[int]) -> list[ScheduleTuple]:
        query = f'''SELECT id, is_pattern, date, name, root, default_week  
                    FROM schedule
                    WHERE user='{cls.user}' and id in ({', '.join([str(i) for i in ids])});'''
        schedules: list[ScheduleTuple] = [ScheduleTuple(*schedule) for schedule in DataBase.query_database(query)]
        return schedules

    @classmethod
    def get_schedule(cls, id: int) -> ScheduleTuple:
        return DataBase.get_schedules([id])[0]

    @classmethod
    def set_default_week(cls, index_day: int, schedule_id: int) -> None:
        default_week: list[int] = cls.get_default_week()
        if isinstance(default_week[index_day], int):
            query = f'''UPDATE schedule
                        SET default_week=NULL
                        WHERE user='{cls.user}' and id = {default_week[index_day]};'''
            cls.query_database(query, commit=True)
        query = f'''UPDATE schedule
                    SET default_week={index_day}
                    WHERE user='{cls.user}' and id = {schedule_id};'''
        cls.query_database(query, commit=True)

    @classmethod
    def get_default_week(cls) -> list[int]:
        default_week: list[int] = list()
        for i in range(7):
            query = f'''SELECT id 
                        FROM schedule
                        WHERE user='{cls.user}' and default_week={i};'''
            records = cls.query_database(query)
            schedule_id = None
            if len(records) != 0:
                if len(records[0]) != 0:
                    schedule_id = records[0][0]
            default_week.append(schedule_id)
        return default_week

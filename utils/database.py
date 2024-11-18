import pathlib
from sqlite3 import connect


class DataBase():
    user: str = 'test'

    @staticmethod
    def set_user(user: str) -> None:
        DataBase.user = user

    @staticmethod
    def query_datebase(query: str):
        path = pathlib.PurePath(__file__)
        path = path.parent.parent.joinpath('database', 'schedule')
        con = connect(path)
        curses = con.cursor()
        curses.execute(query)
        records = curses.fetchall()
        return records
    @staticmethod
    def search_record(table, identifier) -> int | None:
        pass

    @staticmethod
    def get_names_schedule_pattern(self) -> list[str]:
        names = []
        query = f'''SELECT name FROM schedule_pattern
                   WHERE user='{DataBase.user}';'''
        return DataBase.query_datebase(query)[0]

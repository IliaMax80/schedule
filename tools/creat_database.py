import os.path
import pathlib
import sqlite3
from sqlite3 import connect, Cursor


def create_table(cursor: Cursor, name: str, identifier: str) -> None:
    try:
        delete_table = f'DROP TABLE {name};'
        cursor.execute(delete_table)
    except:
        pass
    create_table = f'''CREATE TABLE {name}
                (
                    id int,
                    user string,
                   {identifier} string'''
    for hour in range(24):
        for minute in range(60):
            create_table += f',\nhour{hour:0>2}{minute:0>2} string'
    create_table += '\n);'
    cursor.execute(create_table)


if __name__ == '__main__':
    path = pathlib.PurePath(__file__)
    path = path.parent.parent.joinpath('database', 'schedule')
    con = connect(path)
    cursor = con.cursor()
    create_table(cursor, name='schedule_day', identifier='date')
    create_table(cursor, name='schedule_pattern', identifier='name')

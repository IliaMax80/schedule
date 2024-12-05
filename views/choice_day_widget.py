from datetime import date, timedelta
from PyQt6.QtWidgets import QWidget

from models.schedule import ScheduleDay
from ui.choice_day_widget import Ui_ChoiceDayWidget
import locale

from views.schedule_widget import ScheduleWidget

locale.setlocale(locale.LC_TIME, 'ru')



class ChoiceDayWidget(QWidget, Ui_ChoiceDayWidget):
    COLOR_ACTIVE = '#C0C0C0'
    COLOR_DEFAULT = '#E1E1E1'
    def __init__(self, *args, **kwargs):
        self.active_data: date = date.today()
        self.main_window: 'MainWindow' = kwargs.pop('main_window')
        self.schedule_widget: ScheduleWidget = kwargs.pop('schedule_widget')
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.week_buttons = [
            self.monday_button,
            self.tuesday_button,
            self.wednesday_button,
            self.thursday_button,
            self.friday_button,
            self.saturday_button,
            self.sunday_button,
        ]
        self.week_name_month = [
            self.name_month_1,
            self.name_month_2,
            self.name_month_3,
            self.name_month_4,
            self.name_month_5,
            self.name_month_6,
            self.name_month_7
        ]

        self.old_week_button.clicked.connect(lambda x: self.move(-7))
        self.next_week_button.clicked.connect(lambda x: self.move(7))
        self.today_button.clicked.connect(lambda x: self.main_window.set_day(date.today()))
        for i in range(len(self.week_buttons)):
            self.week_buttons[i].clicked.connect(lambda x: None)

    def set_day(self, current_date: date) -> None:
        self.active_data: date = current_date
        start_week_day: date = self.active_data - timedelta(days=self.active_data.weekday())
        for i in range(len(self.week_buttons)):
            date_day: date = start_week_day + timedelta(days=i)
            self.week_buttons[i].setText(self.week_buttons[i].text()[:-2] + f'{date_day.day:>2}')
            self.week_buttons[i].clicked.disconnect()
            self.week_buttons[i].clicked.connect(lambda x, day=date_day: self.main_window.set_day(day))
            self.week_buttons[i].setStyleSheet('QPushButton {background-color:#E1E1E1}')
            self.week_name_month[i].setText('')

        is_two_month = False
        for i in range(len(self.week_buttons) - 1):
            date_day: date = start_week_day + timedelta(days=i)
            next_date_day: date = start_week_day + timedelta(days=i + 1)
            is_two_month = date_day.month != next_date_day.month
            if is_two_month:
                self.week_name_month[i].setText(date_day.strftime('%B'))
                self.week_name_month[i + 1].setText(next_date_day.strftime('%B'))
                break

        if not is_two_month:
            self.week_name_month[3].setText(current_date.strftime('%B'))

        self.week_buttons[current_date.weekday()].setStyleSheet('QPushButton {background-color:#C0C0C0}')
        self.schedule_widget.set_schedule(ScheduleDay(self.active_data))

    def move(self, step_day: int) -> None:
        self.main_window.set_day(self.active_data + timedelta(days=step_day))

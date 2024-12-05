from PyQt6.QtWidgets import QMainWindow, QPushButton
from ui.select_default_week_window import Ui_SelectDefaultWeek
from utils.database import DataBase


class SelectDefaultWeek(QMainWindow, Ui_SelectDefaultWeek):
    def __init__(self, *args, **kwargs):
        self.schedule_id: 'schedule' = kwargs.pop('schedule_id')

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.week_buttons: list[QPushButton] = [self.monday_button,
                                                self.tuesday_button,
                                                self.wednesday_button,
                                                self.thursday_button,
                                                self.friday_button,
                                                self.saturday_button,
                                                self.sunday_button]
        for i in range(len(self.week_buttons)):
            self.week_buttons[i].clicked.connect(lambda _, i=i: self.set_default_week(i))

        self.update_button()

    def update_button(self) -> None:
        default_week: list[int] = DataBase.get_default_week()
        for i in range(len(default_week)):
            if default_week[i] == self.schedule_id:
                self.week_buttons[i].setStyleSheet('QPushButton {background-color:#C0C0C0}')
            else:
                self.week_buttons[i].setStyleSheet('QPushButton {background-color:#E1E1E1}')

    def set_default_week(self, index_day: int) -> None:
        DataBase.set_default_week(index_day, self.schedule_id)
        self.update_button()



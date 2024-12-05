from datetime import time

from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from models.affair_period import AffairPeriod
from ui.affair_period_window import Ui_AffairPeriodWindow
from utils.database import AffairPeriodTuple


class AffairPeriodWindow(QMainWindow, Ui_AffairPeriodWindow):

    def __init__(self, *args, **kwargs):
        self.affair_period: AffairPeriod = kwargs.pop('affair_period')
        self.schedule_widget: 'ScheduleWidget' = kwargs.pop('schedule_widget')
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_affair_period(self.affair_period)
        self.delete_button.clicked.connect(self.remove_affair)
        self.save_button.clicked.connect(self.save)

    def set_affair_period(self, affair_period: AffairPeriod) -> None:
        self.affair_period = affair_period
        self.update_window()

    def update_window(self) -> None:
        self.time_start.setTime(QTime(self.affair_period.start.hour, self.affair_period.start.minute))
        self.time_end.setTime(QTime(self.affair_period.end.hour, self.affair_period.end.minute))
        self.name_affair.setText(self.affair_period.affair)

    def remove_affair(self) -> None:
        self.affair_period.remove()
        self.schedule_widget.update_affair_widget()
        self.close()

    def save(self) -> None:
        old_tuple_affair: AffairPeriodTuple = self.affair_period.get_tuple_affair()
        self.affair_period.start = time(hour=self.time_start.time().hour(), minute=self.time_start.time().minute())
        self.affair_period.end = time(hour=self.time_end.time().hour(), minute=self.time_end.time().minute())
        self.affair_period.affair = self.name_affair.text()
        try:
            self.schedule_widget.update_affair_widget()
        except ValueError:
            text = 'Извините, вы не можете устанавливать время для дел, так что они накладывается друг на друга'
            QMessageBox.about(self, 'Редактирование времени', text)
            self.affair_period.set_tuple_affair(old_tuple_affair)
            self.schedule_widget.update_affair_widget()
            self.update_window()
            print('Ошибка')
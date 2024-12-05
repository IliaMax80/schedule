from datetime import time

from PyQt6.QtWidgets import QWidget
from models.affair_period import AffairPeriod
from models.schedule import Schedule
from ui.schedule_widget import Ui_ScheduleWidget
from views.affair_period_widget import AffairPeriodWidget
from views.affair_period_window import AffairPeriodWindow


class ScheduleWidget(QWidget, Ui_ScheduleWidget):
    def __init__(self, *args, **kwargs):
        self.schedule: Schedule | None = None
        self.affair_widgets: list[AffairPeriodWidget] = []
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_affair_period)
        self.affair_period_window: AffairPeriodWindow | None = None

    def set_schedule(self, schedule: Schedule) -> None:
        self.schedule = schedule
        self.update_affair_widget()

    def update_affair_widget(self) -> None:
        self.schedule.update_affairs()

        for affair_widget in self.affair_widgets:
            self.affair_period_widget_layout.removeWidget(affair_widget)
            affair_widget.deleteLater()
        self.affair_widgets.clear()

        for affair_period in self.schedule.get_affairs():
            affair_widget_period = AffairPeriodWidget(affair_period=affair_period, schedule_widget=self)
            self.affair_period_widget_layout.addWidget(affair_widget_period)
            self.affair_widgets.append(affair_widget_period)

    def add_affair_period(self) -> None:
        start: time = time(hour=0, minute=0)
        end: time = time(hour=0, minute=1)
        affair = ''
        affair_period = AffairPeriod(None, start, end, affair, self.schedule, False, False)
        self.schedule.add_affair_period(affair_period)
        self.open_affair_window(affair_period)

    def open_affair_window(self, affair_period: AffairPeriod) -> None:
        if self.affair_period_window:
            self.affair_period_window.close()

        self.affair_period_window = AffairPeriodWindow(affair_period=affair_period, schedule_widget=self)
        self.affair_period_window.show()

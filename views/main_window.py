from views.choice_schedule_pattern_widget import ChoiceSchedulePatternWidget
from PyQt6.QtWidgets import QMainWindow, QPushButton
from ui.schedule_window import Ui_ScheduleWindow
from views.choice_day_widget import ChoiceDayWidget
from datetime import datetime, date

from views.schedule_widget import ScheduleWidget


class MainWindow(QMainWindow, Ui_ScheduleWindow):

    def __init__(self):
        super().__init__()
        self.active_date: date = datetime.today()
        self.schedule_day_widget: ScheduleWidget = ScheduleWidget()
        self.schedule_pattern_widget: ScheduleWidget = ScheduleWidget()
        self.choice_day_widget: ChoiceDayWidget = ChoiceDayWidget(main_window=self,
                                                                  schedule_widget=self.schedule_day_widget)
        self.choice_schedule_pattern_widget: ChoiceSchedulePatternWidget = (
            ChoiceSchedulePatternWidget(main_window=self,
                                        schedule_widget=self.schedule_pattern_widget))
        self.setupUi(self)
        self.set_day(self.active_date)

    def setupUi(self, main_window: QMainWindow) -> None:
        super().setupUi(self)
        self.schedule_day_layout.addWidget(self.choice_day_widget)
        self.schedule_day_layout.addWidget(self.schedule_day_widget)
        self.schedule_pattern_layout.addWidget(self.choice_schedule_pattern_widget)
        self.schedule_pattern_layout.addWidget(self.schedule_pattern_widget)

    def set_day(self, current_date: date) -> None:
        self.active_date = current_date
        self.choice_day_widget.set_day(self.active_date)

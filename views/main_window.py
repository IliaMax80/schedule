from views.choice_schedule_pattern_widget import ChoiceSchedulePatternWidget
from PyQt6.QtWidgets import QMainWindow, QPushButton
from ui.schedule_window import Ui_ScheduleWindow
from views.choice_day_widget import ChoiceDayWidget
from datetime import datetime, date


class MainWindow(QMainWindow, Ui_ScheduleWindow):

    def __init__(self):
        super().__init__()
        self.active_date: date = datetime.today()
        self.choice_day_widget: ChoiceDayWidget = ChoiceDayWidget(main_window=self)
        self.choice_schedule_pattern_widget: ChoiceSchedulePatternWidget = ChoiceSchedulePatternWidget(main_window=self)
        self.setupUi(self)
        self.set_day(self.active_date)

    def setupUi(self, main_window: QMainWindow) -> None:
        super().setupUi(self)
        self.schedule_day_layout.addWidget(self.choice_day_widget)
        self.shedule_pattern_layout.addWidget(self.choice_schedule_pattern_widget)

    def set_day(self, current_date: date) -> None:
        self.active_date = current_date
        self.choice_day_widget.set_day(self.active_date)

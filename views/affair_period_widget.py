from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QWidget

from models.affair_period import AffairPeriod
from ui.affair_period_widget import Ui_AffairPeriodWidget



class AffairPeriodWidget(QWidget, Ui_AffairPeriodWidget):

    def __init__(self, *args, **kwargs):
        self.affair_period: AffairPeriod = kwargs.pop('affair_period')
        self.schedule_widget: 'ScheduleWidget' = kwargs.pop('schedule_widget')
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_affair_period(self.affair_period)
        self.configure_button.clicked.connect(lambda _: self.schedule_widget.open_affair_window(self.affair_period))

    def set_affair_period(self, affair_period: AffairPeriod):
        self.affair_period = affair_period
        self.time_start.setTime(QTime(affair_period.start.hour, affair_period.start.minute))
        self.time_end.setTime(QTime(affair_period.end.hour, affair_period.end.minute))
        self.name_affair.setText(self.affair_period.affair)




from PyQt6.QtWidgets import QWidget

from ui.choice_schedule_pattern_widget import Ui_ChoiceSchedulePatternWidget


class ChoiceSchedulePatternWidget(QWidget, Ui_ChoiceSchedulePatternWidget):
    def __init__(self, *args, **kwargs):
        self.main_window: 'MainWindow' = kwargs.pop('main_window')
        
        super().__init__(*args, **kwargs)
        self.setupUi(self)

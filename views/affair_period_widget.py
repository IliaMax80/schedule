from PyQt6.QtWidgets import QWidget

from ui.affair_period_widget import Ui_AffairPeriodWidget


class AffairPeriodWidget(QWidget, Ui_AffairPeriodWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
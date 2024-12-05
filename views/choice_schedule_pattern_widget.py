from PyQt6.QtWidgets import QWidget

from models.schedule import SchedulePattern
from ui.choice_schedule_pattern_widget import Ui_ChoiceSchedulePatternWidget
from utils.database import DataBase, ScheduleTuple
from views.schedule_widget import ScheduleWidget
from views.select_default_week_window import SelectDefaultWeek


class ChoiceSchedulePatternWidget(QWidget, Ui_ChoiceSchedulePatternWidget):
    def __init__(self, *args, **kwargs):
        self.main_window: 'MainWindow' = kwargs.pop('main_window')
        self.schedule_widget: ScheduleWidget = kwargs.pop('schedule_widget')
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.current_index: int | None = None
        self.choice_name.activated.connect(self.select_name)
        self.update_choice_name()
        self.select_default_week_window: SelectDefaultWeek | None = None
        self.default_selection_button.clicked.connect(lambda _: self.open_default_week_window_id())
        self.create_schedule_pattern_button.clicked.connect(lambda _: self.create_schedule_pattern())

    def select_name(self, index):
        self.current_index = index
        schedule_pattern: SchedulePattern = SchedulePattern(self.choice_name.itemText(index))
        self.schedule_widget.set_schedule(schedule_pattern)

    def update_choice_name(self) -> None:
        self.choice_name.clear()
        ids: list[int] = DataBase.get_names_schedule_pattern()
        names: list[str] = [schedule.name for schedule in DataBase.get_schedules(ids)]
        self.choice_name.addItems(names)
        self.choice_name.setCurrentIndex(0)
        self.current_index = 0
        self.select_name(self.choice_name.currentIndex())

    def open_default_week_window_id(self):
        ids: list[int] = DataBase.get_names_schedule_pattern()
        schedule_name_id: list[(str, int)] = [(schedule.name, schedule.id) for schedule in DataBase.get_schedules(ids)]
        schedule_id: int | None = None
        for name, id in schedule_name_id:
            if isinstance(self.current_index, int):
                if str(self.choice_name.itemText(self.current_index)) == name:
                    schedule_id = id
                    break

        self.select_default_week_window = SelectDefaultWeek(schedule_id=schedule_id)
        self.select_default_week_window.show()

    def create_schedule_pattern(self):
        names: list[int] = []
        for i in range(self.choice_name.count()):
            _, x = self.choice_name.itemText(i).split()
            names.append(int(x))
        print(names)
        new_name = 'Шаблон ' + str(max(names) + 1)
        schedule_pattern: ScheduleTuple = ScheduleTuple(0, 1, None, new_name, None, None)
        DataBase.create_schedule(schedule_pattern)
        self.update_choice_name()

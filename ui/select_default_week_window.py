# Form implementation generated from reading ui file 'SelectDefaultWeek.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SelectDefaultWeek(object):
    def setupUi(self, SelectDefaultWeek):
        SelectDefaultWeek.setObjectName("SelectDefaultWeek")
        SelectDefaultWeek.resize(293, 267)
        self.centralwidget = QtWidgets.QWidget(parent=SelectDefaultWeek)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.monday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.monday_button.setObjectName("monday_button")
        self.verticalLayout.addWidget(self.monday_button)
        self.tuesday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tuesday_button.setObjectName("tuesday_button")
        self.verticalLayout.addWidget(self.tuesday_button)
        self.wednesday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.wednesday_button.setObjectName("wednesday_button")
        self.verticalLayout.addWidget(self.wednesday_button)
        self.thursday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.thursday_button.setObjectName("thursday_button")
        self.verticalLayout.addWidget(self.thursday_button)
        self.friday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.friday_button.setObjectName("friday_button")
        self.verticalLayout.addWidget(self.friday_button)
        self.saturday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saturday_button.setObjectName("saturday_button")
        self.verticalLayout.addWidget(self.saturday_button)
        self.sunday_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sunday_button.setObjectName("sunday_button")
        self.verticalLayout.addWidget(self.sunday_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        SelectDefaultWeek.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectDefaultWeek)
        QtCore.QMetaObject.connectSlotsByName(SelectDefaultWeek)

    def retranslateUi(self, SelectDefaultWeek):
        _translate = QtCore.QCoreApplication.translate
        SelectDefaultWeek.setWindowTitle(_translate("SelectDefaultWeek", "Выбор поумолчанию"))
        self.monday_button.setText(_translate("SelectDefaultWeek", "Понедельник"))
        self.tuesday_button.setText(_translate("SelectDefaultWeek", "Вторник"))
        self.wednesday_button.setText(_translate("SelectDefaultWeek", "Среда"))
        self.thursday_button.setText(_translate("SelectDefaultWeek", "Четверг"))
        self.friday_button.setText(_translate("SelectDefaultWeek", "Пятница"))
        self.saturday_button.setText(_translate("SelectDefaultWeek", "Суббота"))
        self.sunday_button.setText(_translate("SelectDefaultWeek", "Воскресенье"))

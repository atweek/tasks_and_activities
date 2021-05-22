# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(989, 662)
        Dialog.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 71, 661))
        self.frame.setStyleSheet("background-color: #EAEAEA;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 71, 661))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.main = QtWidgets.QPushButton(self.splitter)
        self.main.setStyleSheet("background-color: #EAEAEA;")
        self.main.setText("")
        icon = QtGui.QIcon.fromTheme("/home/ramil/Desktop/pyqt/img/free-icon-avatar-126486.png")
        self.main.setIcon(icon)
        self.main.setCheckable(False)
        self.main.setDefault(False)
        self.main.setFlat(False)
        self.main.setObjectName("main")
        self.events = QtWidgets.QPushButton(self.splitter)
        self.events.setStyleSheet("background-color: #EAEAEA;")
        self.events.setText("")
        icon = QtGui.QIcon.fromTheme("/home/ramil/Desktop/pyqt/img/free-icon-musical-note-126493.png")
        self.events.setIcon(icon)
        self.events.setCheckable(False)
        self.events.setDefault(False)
        self.events.setFlat(False)
        self.events.setObjectName("events")
        self.tasks = QtWidgets.QPushButton(self.splitter)
        self.tasks.setStyleSheet("background-color: #EAEAEA;")
        self.tasks.setText("")
        icon = QtGui.QIcon.fromTheme("/home/ramil/Desktop/pyqt/img/free-icon-pie-chart-126484.png")
        self.tasks.setIcon(icon)
        self.tasks.setCheckable(False)
        self.tasks.setDefault(False)
        self.tasks.setFlat(False)
        self.tasks.setObjectName("tasks")
        self.seting = QtWidgets.QPushButton(self.splitter)
        self.seting.setStyleSheet("background-color: #EAEAEA;")
        self.seting.setText("")
        icon = QtGui.QIcon.fromTheme("/home/ramil/Desktop/pyqt/img/free-icon-settings-126472.png")
        self.seting.setIcon(icon)
        self.seting.setCheckable(False)
        self.seting.setDefault(False)
        self.seting.setFlat(False)
        self.seting.setObjectName("seting")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(70, -10, 931, 131))
        self.frame_2.setMinimumSize(QtCore.QSize(931, 0))
        self.frame_2.setStyleSheet("background-color: #EAEAEA;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setGeometry(QtCore.QRect(30, 20, 189, 100))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.avatar = QtWidgets.QLabel(self.splitter_2)
        self.avatar.setMinimumSize(QtCore.QSize(100, 100))
        self.avatar.setStyleSheet("border-radius: 1px;")
        self.avatar.setText("")
        self.avatar.setPixmap(QtGui.QPixmap("../avatar/av1.jpeg"))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")
        self.name = QtWidgets.QLabel(self.splitter_2)
        self.name.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        font.setKerning(True)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 170, 891, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.agenda = QtWidgets.QFrame(self.layoutWidget)
        self.agenda.setStyleSheet("background-color: #808080;")
        self.agenda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.agenda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.agenda.setObjectName("agenda")
        self.label_ag = QtWidgets.QLabel(self.agenda)
        self.label_ag.setGeometry(QtCore.QRect(200, 10, 51, 17))
        self.label_ag.setObjectName("label_ag")
        self.layoutWidget1 = QtWidgets.QWidget(self.agenda)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 50, 371, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ag_1 = QtWidgets.QFrame(self.layoutWidget1)
        self.ag_1.setStyleSheet("background-color: #EAEAEA;")
        self.ag_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag_1.setObjectName("ag_1")
        self.ag_1_1 = QtWidgets.QFrame(self.ag_1)
        self.ag_1_1.setGeometry(QtCore.QRect(0, 0, 71, 121))
        self.ag_1_1.setStyleSheet("background-color: #DCDCDC;")
        self.ag_1_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag_1_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag_1_1.setObjectName("ag_1_1")
        self.gridLayout = QtWidgets.QGridLayout(self.ag_1_1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.num_1 = QtWidgets.QLabel(self.ag_1_1)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setKerning(True)
        self.num_1.setFont(font)
        self.num_1.setScaledContents(True)
        self.num_1.setAlignment(QtCore.Qt.AlignCenter)
        self.num_1.setObjectName("num_1")
        self.verticalLayout_3.addWidget(self.num_1)
        self.mon_1 = QtWidgets.QLabel(self.ag_1_1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.mon_1.setFont(font)
        self.mon_1.setScaledContents(True)
        self.mon_1.setAlignment(QtCore.Qt.AlignCenter)
        self.mon_1.setObjectName("mon_1")
        self.verticalLayout_3.addWidget(self.mon_1)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.event_name = QtWidgets.QLabel(self.ag_1)
        self.event_name.setGeometry(QtCore.QRect(80, 10, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.event_name.setFont(font)
        self.event_name.setObjectName("event_name")
        self.event_desc = QtWidgets.QLabel(self.ag_1)
        self.event_desc.setGeometry(QtCore.QRect(80, 30, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_desc.setFont(font)
        self.event_desc.setObjectName("event_desc")
        self.event_date = QtWidgets.QLabel(self.ag_1)
        self.event_date.setGeometry(QtCore.QRect(80, 50, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_date.setFont(font)
        self.event_date.setObjectName("event_date")
        self.event_time = QtWidgets.QLabel(self.ag_1)
        self.event_time.setGeometry(QtCore.QRect(130, 50, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_time.setFont(font)
        self.event_time.setObjectName("event_time")
        self.event_place = QtWidgets.QLabel(self.ag_1)
        self.event_place.setGeometry(QtCore.QRect(190, 50, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_place.setFont(font)
        self.event_place.setObjectName("event_place")
        self.verticalLayout_2.addWidget(self.ag_1)
        self.ag_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.ag_2.setStyleSheet("background-color: #EAEAEA;")
        self.ag_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag_2.setObjectName("ag_2")
        self.ag2_1 = QtWidgets.QFrame(self.ag_2)
        self.ag2_1.setGeometry(QtCore.QRect(0, 0, 71, 121))
        self.ag2_1.setStyleSheet("background-color: #DCDCDC;")
        self.ag2_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag2_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag2_1.setObjectName("ag2_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ag2_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.num_2 = QtWidgets.QLabel(self.ag2_1)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setKerning(True)
        self.num_2.setFont(font)
        self.num_2.setScaledContents(True)
        self.num_2.setAlignment(QtCore.Qt.AlignCenter)
        self.num_2.setObjectName("num_2")
        self.verticalLayout_4.addWidget(self.num_2)
        self.mon_2 = QtWidgets.QLabel(self.ag2_1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.mon_2.setFont(font)
        self.mon_2.setScaledContents(True)
        self.mon_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mon_2.setObjectName("mon_2")
        self.verticalLayout_4.addWidget(self.mon_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.event_place_2 = QtWidgets.QLabel(self.ag_2)
        self.event_place_2.setGeometry(QtCore.QRect(190, 50, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_place_2.setFont(font)
        self.event_place_2.setObjectName("event_place_2")
        self.event_name_2 = QtWidgets.QLabel(self.ag_2)
        self.event_name_2.setGeometry(QtCore.QRect(80, 10, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.event_name_2.setFont(font)
        self.event_name_2.setObjectName("event_name_2")
        self.event_desc_2 = QtWidgets.QLabel(self.ag_2)
        self.event_desc_2.setGeometry(QtCore.QRect(80, 30, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_desc_2.setFont(font)
        self.event_desc_2.setObjectName("event_desc_2")
        self.event_date_2 = QtWidgets.QLabel(self.ag_2)
        self.event_date_2.setGeometry(QtCore.QRect(80, 50, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_date_2.setFont(font)
        self.event_date_2.setObjectName("event_date_2")
        self.event_time_2 = QtWidgets.QLabel(self.ag_2)
        self.event_time_2.setGeometry(QtCore.QRect(130, 50, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_time_2.setFont(font)
        self.event_time_2.setObjectName("event_time_2")
        self.verticalLayout_2.addWidget(self.ag_2)
        self.ag_3 = QtWidgets.QFrame(self.layoutWidget1)
        self.ag_3.setStyleSheet("background-color: #EAEAEA;")
        self.ag_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag_3.setObjectName("ag_3")
        self.ag_3_1 = QtWidgets.QFrame(self.ag_3)
        self.ag_3_1.setGeometry(QtCore.QRect(0, 0, 71, 121))
        self.ag_3_1.setStyleSheet("background-color: #DCDCDC;")
        self.ag_3_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ag_3_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ag_3_1.setObjectName("ag_3_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ag_3_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.num_3 = QtWidgets.QLabel(self.ag_3_1)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setKerning(True)
        self.num_3.setFont(font)
        self.num_3.setScaledContents(True)
        self.num_3.setAlignment(QtCore.Qt.AlignCenter)
        self.num_3.setObjectName("num_3")
        self.verticalLayout_5.addWidget(self.num_3)
        self.man_3 = QtWidgets.QLabel(self.ag_3_1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.man_3.setFont(font)
        self.man_3.setScaledContents(True)
        self.man_3.setAlignment(QtCore.Qt.AlignCenter)
        self.man_3.setObjectName("man_3")
        self.verticalLayout_5.addWidget(self.man_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.event_desc_3 = QtWidgets.QLabel(self.ag_3)
        self.event_desc_3.setGeometry(QtCore.QRect(80, 30, 221, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_desc_3.setFont(font)
        self.event_desc_3.setObjectName("event_desc_3")
        self.event_place_3 = QtWidgets.QLabel(self.ag_3)
        self.event_place_3.setGeometry(QtCore.QRect(190, 50, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_place_3.setFont(font)
        self.event_place_3.setObjectName("event_place_3")
        self.event_name_3 = QtWidgets.QLabel(self.ag_3)
        self.event_name_3.setGeometry(QtCore.QRect(80, 10, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.event_name_3.setFont(font)
        self.event_name_3.setObjectName("event_name_3")
        self.event_date_3 = QtWidgets.QLabel(self.ag_3)
        self.event_date_3.setGeometry(QtCore.QRect(80, 50, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_date_3.setFont(font)
        self.event_date_3.setObjectName("event_date_3")
        self.event_long_3 = QtWidgets.QLabel(self.ag_3)
        self.event_long_3.setGeometry(QtCore.QRect(130, 50, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.event_long_3.setFont(font)
        self.event_long_3.setObjectName("event_long_3")
        self.verticalLayout_2.addWidget(self.ag_3)
        self.tool_agenda = QtWidgets.QToolButton(self.agenda)
        self.tool_agenda.setGeometry(QtCore.QRect(0, 390, 26, 24))
        self.tool_agenda.setObjectName("tool_agenda")
        self.horizontalLayout.addWidget(self.agenda)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_4.setStyleSheet("background-color: #808080;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 37, 18))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 441, 341))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 425, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.task_1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_1.setEnabled(True)
        self.task_1.setMinimumSize(QtCore.QSize(400, 50))
        self.task_1.setMaximumSize(QtCore.QSize(400, 30))
        self.task_1.setStyleSheet("background-color: #EAEAEA;")
        self.task_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_1.setObjectName("task_1")
        self.tdesc_1 = QtWidgets.QLabel(self.task_1)
        self.tdesc_1.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_1.setFont(font)
        self.tdesc_1.setObjectName("tdesc_1")
        self.checkBox = QtWidgets.QCheckBox(self.task_1)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.name_1 = QtWidgets.QLabel(self.task_1)
        self.name_1.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_1.setFont(font)
        self.name_1.setObjectName("name_1")
        self.t_date_1 = QtWidgets.QLabel(self.task_1)
        self.t_date_1.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_1.setObjectName("t_date_1")
        self.verticalLayout.addWidget(self.task_1)
        self.task_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_2.setEnabled(True)
        self.task_2.setMinimumSize(QtCore.QSize(400, 50))
        self.task_2.setMaximumSize(QtCore.QSize(400, 30))
        self.task_2.setStyleSheet("background-color: #EAEAEA;")
        self.task_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_2.setObjectName("task_2")
        self.tdesc_2 = QtWidgets.QLabel(self.task_2)
        self.tdesc_2.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_2.setFont(font)
        self.tdesc_2.setObjectName("tdesc_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.task_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.name_2 = QtWidgets.QLabel(self.task_2)
        self.name_2.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_2.setFont(font)
        self.name_2.setObjectName("name_2")
        self.t_date_2 = QtWidgets.QLabel(self.task_2)
        self.t_date_2.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_2.setObjectName("t_date_2")
        self.verticalLayout.addWidget(self.task_2)
        self.task_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_3.setEnabled(True)
        self.task_3.setMinimumSize(QtCore.QSize(400, 50))
        self.task_3.setMaximumSize(QtCore.QSize(400, 30))
        self.task_3.setStyleSheet("background-color: #EAEAEA;")
        self.task_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_3.setObjectName("task_3")
        self.tdesc_3 = QtWidgets.QLabel(self.task_3)
        self.tdesc_3.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_3.setFont(font)
        self.tdesc_3.setObjectName("tdesc_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.task_3)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.name_3 = QtWidgets.QLabel(self.task_3)
        self.name_3.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_3.setFont(font)
        self.name_3.setObjectName("name_3")
        self.t_date_3 = QtWidgets.QLabel(self.task_3)
        self.t_date_3.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_3.setObjectName("t_date_3")
        self.verticalLayout.addWidget(self.task_3)
        self.task_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_4.setEnabled(True)
        self.task_4.setMinimumSize(QtCore.QSize(400, 50))
        self.task_4.setMaximumSize(QtCore.QSize(400, 30))
        self.task_4.setStyleSheet("background-color: #EAEAEA;")
        self.task_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_4.setObjectName("task_4")
        self.tdesc_4 = QtWidgets.QLabel(self.task_4)
        self.tdesc_4.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_4.setFont(font)
        self.tdesc_4.setObjectName("tdesc_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.task_4)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.name_4 = QtWidgets.QLabel(self.task_4)
        self.name_4.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_4.setFont(font)
        self.name_4.setObjectName("name_4")
        self.t_date_4 = QtWidgets.QLabel(self.task_4)
        self.t_date_4.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_4.setObjectName("t_date_4")
        self.verticalLayout.addWidget(self.task_4)
        self.task_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_5.setEnabled(True)
        self.task_5.setMinimumSize(QtCore.QSize(400, 50))
        self.task_5.setMaximumSize(QtCore.QSize(400, 30))
        self.task_5.setStyleSheet("background-color: #EAEAEA;")
        self.task_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_5.setObjectName("task_5")
        self.tdesc_5 = QtWidgets.QLabel(self.task_5)
        self.tdesc_5.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_5.setFont(font)
        self.tdesc_5.setObjectName("tdesc_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.task_5)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.name_5 = QtWidgets.QLabel(self.task_5)
        self.name_5.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_5.setFont(font)
        self.name_5.setObjectName("name_5")
        self.t_date_5 = QtWidgets.QLabel(self.task_5)
        self.t_date_5.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_5.setObjectName("t_date_5")
        self.verticalLayout.addWidget(self.task_5)
        self.task_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_10.setEnabled(True)
        self.task_10.setMinimumSize(QtCore.QSize(400, 50))
        self.task_10.setMaximumSize(QtCore.QSize(400, 30))
        self.task_10.setStyleSheet("background-color: #EAEAEA;")
        self.task_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_10.setObjectName("task_10")
        self.tdesc_10 = QtWidgets.QLabel(self.task_10)
        self.tdesc_10.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_10.setFont(font)
        self.tdesc_10.setObjectName("tdesc_10")
        self.checkBox_10 = QtWidgets.QCheckBox(self.task_10)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.name_10 = QtWidgets.QLabel(self.task_10)
        self.name_10.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_10.setFont(font)
        self.name_10.setObjectName("name_10")
        self.t_date_10 = QtWidgets.QLabel(self.task_10)
        self.t_date_10.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_10.setObjectName("t_date_10")
        self.verticalLayout.addWidget(self.task_10)
        self.task_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_9.setEnabled(True)
        self.task_9.setMinimumSize(QtCore.QSize(400, 50))
        self.task_9.setMaximumSize(QtCore.QSize(400, 30))
        self.task_9.setStyleSheet("background-color: #EAEAEA;")
        self.task_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_9.setObjectName("task_9")
        self.tdesc_9 = QtWidgets.QLabel(self.task_9)
        self.tdesc_9.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_9.setFont(font)
        self.tdesc_9.setObjectName("tdesc_9")
        self.checkBox_9 = QtWidgets.QCheckBox(self.task_9)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.name_9 = QtWidgets.QLabel(self.task_9)
        self.name_9.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_9.setFont(font)
        self.name_9.setObjectName("name_9")
        self.t_date_9 = QtWidgets.QLabel(self.task_9)
        self.t_date_9.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_9.setObjectName("t_date_9")
        self.verticalLayout.addWidget(self.task_9)
        self.task_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_8.setEnabled(True)
        self.task_8.setMinimumSize(QtCore.QSize(400, 50))
        self.task_8.setMaximumSize(QtCore.QSize(400, 30))
        self.task_8.setStyleSheet("background-color: #EAEAEA;")
        self.task_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_8.setObjectName("task_8")
        self.tdesc_8 = QtWidgets.QLabel(self.task_8)
        self.tdesc_8.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_8.setFont(font)
        self.tdesc_8.setObjectName("tdesc_8")
        self.checkBox_8 = QtWidgets.QCheckBox(self.task_8)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.name_8 = QtWidgets.QLabel(self.task_8)
        self.name_8.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_8.setFont(font)
        self.name_8.setObjectName("name_8")
        self.t_date_8 = QtWidgets.QLabel(self.task_8)
        self.t_date_8.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_8.setObjectName("t_date_8")
        self.verticalLayout.addWidget(self.task_8)
        self.task_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_7.setEnabled(True)
        self.task_7.setMinimumSize(QtCore.QSize(400, 50))
        self.task_7.setMaximumSize(QtCore.QSize(400, 30))
        self.task_7.setStyleSheet("background-color: #EAEAEA;")
        self.task_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_7.setObjectName("task_7")
        self.tdesc_7 = QtWidgets.QLabel(self.task_7)
        self.tdesc_7.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_7.setFont(font)
        self.tdesc_7.setObjectName("tdesc_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.task_7)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.name_7 = QtWidgets.QLabel(self.task_7)
        self.name_7.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_7.setFont(font)
        self.name_7.setObjectName("name_7")
        self.t_date_7 = QtWidgets.QLabel(self.task_7)
        self.t_date_7.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_7.setObjectName("t_date_7")
        self.verticalLayout.addWidget(self.task_7)
        self.task_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.task_6.setEnabled(True)
        self.task_6.setMinimumSize(QtCore.QSize(400, 50))
        self.task_6.setMaximumSize(QtCore.QSize(400, 30))
        self.task_6.setStyleSheet("background-color: #EAEAEA;")
        self.task_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task_6.setObjectName("task_6")
        self.tdesc_6 = QtWidgets.QLabel(self.task_6)
        self.tdesc_6.setGeometry(QtCore.QRect(30, 4, 211, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tdesc_6.setFont(font)
        self.tdesc_6.setObjectName("tdesc_6")
        self.checkBox_6 = QtWidgets.QCheckBox(self.task_6)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 20, 14, 15))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.name_6 = QtWidgets.QLabel(self.task_6)
        self.name_6.setGeometry(QtCore.QRect(260, 6, 131, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_6.setFont(font)
        self.name_6.setObjectName("name_6")
        self.t_date_6 = QtWidgets.QLabel(self.task_6)
        self.t_date_6.setGeometry(QtCore.QRect(260, 29, 121, 20))
        self.t_date_6.setObjectName("t_date_6")
        self.verticalLayout.addWidget(self.task_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.toolButton = QtWidgets.QToolButton(self.frame_4)
        self.toolButton.setGeometry(QtCore.QRect(0, 390, 26, 24))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.frame_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name.setText(_translate("Dialog", "Name"))
        self.label_ag.setText(_translate("Dialog", "agenda"))
        self.num_1.setText(_translate("Dialog", "15"))
        self.mon_1.setText(_translate("Dialog", "may"))
        self.event_name.setText(_translate("Dialog", "какое-то название"))
        self.event_desc.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.event_date.setText(_translate("Dialog", "дата"))
        self.event_time.setText(_translate("Dialog", "долго"))
        self.event_place.setText(_translate("Dialog", "место..................."))
        self.num_2.setText(_translate("Dialog", "15"))
        self.mon_2.setText(_translate("Dialog", "may"))
        self.event_place_2.setText(_translate("Dialog", "место..................."))
        self.event_name_2.setText(_translate("Dialog", "какое-то название"))
        self.event_desc_2.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.event_date_2.setText(_translate("Dialog", "дата"))
        self.event_time_2.setText(_translate("Dialog", "долго"))
        self.num_3.setText(_translate("Dialog", "15"))
        self.man_3.setText(_translate("Dialog", "may"))
        self.event_desc_3.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.event_place_3.setText(_translate("Dialog", "место..................."))
        self.event_name_3.setText(_translate("Dialog", "какое-то название"))
        self.event_date_3.setText(_translate("Dialog", "дата"))
        self.event_long_3.setText(_translate("Dialog", "долго"))
        self.tool_agenda.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Task"))
        self.tdesc_1.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_1.setText(_translate("Dialog", "from: atweek"))
        self.t_date_1.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_2.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_2.setText(_translate("Dialog", "from: atweek"))
        self.t_date_2.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_3.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_3.setText(_translate("Dialog", "from: atweek"))
        self.t_date_3.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_4.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_4.setText(_translate("Dialog", "from: atweek"))
        self.t_date_4.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_5.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_5.setText(_translate("Dialog", "from: atweek"))
        self.t_date_5.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_10.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_10.setText(_translate("Dialog", "from: atweek"))
        self.t_date_10.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_9.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_9.setText(_translate("Dialog", "from: atweek"))
        self.t_date_9.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_8.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_8.setText(_translate("Dialog", "from: atweek"))
        self.t_date_8.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_7.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_7.setText(_translate("Dialog", "from: atweek"))
        self.t_date_7.setText(_translate("Dialog", "up to:1111-11-11"))
        self.tdesc_6.setText(_translate("Dialog", "Коментарий_кккккккккккк..."))
        self.name_6.setText(_translate("Dialog", "from: atweek"))
        self.t_date_6.setText(_translate("Dialog", "up to:1111-11-11"))
        self.toolButton.setText(_translate("Dialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smartDevice.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QStackedWidget, QTabWidget, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 750))
        MainWindow.setMaximumSize(QSize(900, 750))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(50, 50, 50);\n"
"	font-weight: bold;\n"
"	color: white;\n"
"	font-family: Comfortaa;\n"
"}\n"
"QPushButton{\n"
"	font-family: Comfortaa;\n"
"	font-weight: bold;\n"
"}\n"
"QScrollBar {\n"
"	border: none;\n"
"	background: rgba(0, 0, 0, 0);\n"
"    width:3px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(175, 175, 175);\n"
"	min-height: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"	background: rgba(175, 175, 175, 0);\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;	\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"	background: rgba(175, 175, 175, 0);\n"
"	height: 0 px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	background: rgba(175, 175, 175, 0);\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;	\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	background: rgba(175, 175, 175, 0);\n"
"	height:"
                        " 0 px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.screens = QStackedWidget(self.centralwidget)
        self.screens.setObjectName(u"screens")
        self.screens.setGeometry(QRect(0, 0, 900, 750))
        self.screens.setLayoutDirection(Qt.RightToLeft)
        self.screens.setStyleSheet(u"")
        self.screens.setMidLineWidth(0)
        self.start_screen = QWidget()
        self.start_screen.setObjectName(u"start_screen")
        self.start_screen.setStyleSheet(u"QLineEdit {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	font-weight: Bold;\n"
"	font-family: Comfortaa;\n"
"	color: white;	\n"
"	border-top: 0px solid rgb(90, 90, 90);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QLineEdit:hover{\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"\n"
"QPushButton  {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	color: white;	\n"
"	border-top: 1px solid rgba(90, 90, 90, 0);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-left-radius: 1%;\n"
"	border-bottom-right-radius: 1%;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 3px;\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}")
        self.addFrame = QFrame(self.start_screen)
        self.addFrame.setObjectName(u"addFrame")
        self.addFrame.setGeometry(QRect(100, 200, 700, 300))
        self.addFrame.setFrameShape(QFrame.StyledPanel)
        self.addFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.addFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.key = QLineEdit(self.addFrame)
        self.key.setObjectName(u"key")

        self.gridLayout.addWidget(self.key, 6, 1, 1, 1)

        self.ver = QLineEdit(self.addFrame)
        self.ver.setObjectName(u"ver")

        self.gridLayout.addWidget(self.ver, 6, 0, 1, 1)

        self.ip = QLineEdit(self.addFrame)
        self.ip.setObjectName(u"ip")

        self.gridLayout.addWidget(self.ip, 4, 1, 1, 1)

        self.id = QLineEdit(self.addFrame)
        self.id.setObjectName(u"id")

        self.gridLayout.addWidget(self.id, 4, 0, 1, 1)

        self.clear = QPushButton(self.addFrame)
        self.clear.setObjectName(u"clear")

        self.gridLayout.addWidget(self.clear, 7, 0, 1, 1)

        self.add = QPushButton(self.addFrame)
        self.add.setObjectName(u"add")

        self.gridLayout.addWidget(self.add, 7, 1, 1, 1)

        self.deviceName = QLineEdit(self.addFrame)
        self.deviceName.setObjectName(u"deviceName")

        self.gridLayout.addWidget(self.deviceName, 2, 0, 1, 1)

        self.deviceType = QComboBox(self.addFrame)
        self.deviceType.setObjectName(u"deviceType")
        self.deviceType.setLayoutDirection(Qt.LeftToRight)
        self.deviceType.setStyleSheet(u"QComboBox {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	font-family: Comfortaa;\n"
"	color: white;	\n"
"	padding-top: -1px;\n"
"	padding-left: 25px;\n"
"	border-top: 0px solid rgb(90, 90, 90);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"}\n"
"QComboBox:hover{\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(50, 50, 50);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background: #484848;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.deviceType, 2, 1, 1, 1)

        self.screens.addWidget(self.start_screen)
        self.main_screen = QWidget()
        self.main_screen.setObjectName(u"main_screen")
        self.main_screen.setStyleSheet(u"QLabel{\n"
"	font-family: Comfortaa;\n"
"	font-weight: Bold;\n"
"	font-size: 24px;\n"
"	color: white;\n"
"}")
        self.type_devices = QStackedWidget(self.main_screen)
        self.type_devices.setObjectName(u"type_devices")
        self.type_devices.setGeometry(QRect(0, 0, 900, 750))
        self.RGB_Light = QWidget()
        self.RGB_Light.setObjectName(u"RGB_Light")
        self.RGB_Light.setStyleSheet(u"QLabel{\n"
"	font-family: Comfortaa;\n"
"	font-weight: Bold;\n"
"	font-size: 12px;\n"
"}")
        self.mode = QTabWidget(self.RGB_Light)
        self.mode.setObjectName(u"mode")
        self.mode.setGeometry(QRect(0, 50, 900, 750))
        self.mode.setLayoutDirection(Qt.LeftToRight)
        self.mode.setStyleSheet(u"QTabWidget::pane {\n"
"\n"
"	border: none;\n"
"  	background: rgba(245, 245, 245, 0); \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"	height: 25px;\n"
"	width:150px;\n"
"	font-size: 18px;\n"
"	font-weight: Bold;\n"
"	font-family: Comfortaa;\n"
"	color: white;	\n"
" 	background: rgba(230, 230, 230, 0); \n"
"	margin-left: 15px;\n"
"	margin-right: 15px;\n"
"	padding-left: 22px;\n"
"	padding-right: 22px;\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"\n"
"\n"
"\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
" 	background: rgba(245, 245, 245, 0); \n"
"\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"QTabBar::tab:!selected:hover {\n"
"    background: rgb(60, 60, 60);\n"
"\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"}")
        self.mode.setTabShape(QTabWidget.Rounded)
        self.mode.setElideMode(Qt.ElideNone)
        self.mode.setUsesScrollButtons(False)
        self.mode.setTabBarAutoHide(False)
        self.white = QWidget()
        self.white.setObjectName(u"white")
        self.whiteRound = QLabel(self.white)
        self.whiteRound.setObjectName(u"whiteRound")
        self.whiteRound.setGeometry(QRect(225, 50, 450, 450))
        self.whiteRound.setStyleSheet(u"")
        self.whiteRound.setPixmap(QPixmap(u"design/coldWarm.png"))
        self.whiteRound.setScaledContents(True)
        self.whiteRound.setAlignment(Qt.AlignCenter)
        self.onOFF = QPushButton(self.white)
        self.onOFF.setObjectName(u"onOFF")
        self.onOFF.setGeometry(QRect(400, 225, 100, 100))
        self.onOFF.setStyleSheet(u"QPushButton { \n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 50%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(120, 120, 120, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"	 background-color: rgba(60, 60, 60, 25);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"design/modeOFF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.onOFF.setIcon(icon)
        self.onOFF.setIconSize(QSize(96, 96))
        self.brightSlider = QSlider(self.white)
        self.brightSlider.setObjectName(u"brightSlider")
        self.brightSlider.setEnabled(True)
        self.brightSlider.setGeometry(QRect(250, 566, 400, 22))
        self.brightSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"\n"
"")
        self.brightSlider.setMaximum(100)
        self.brightSlider.setValue(100)
        self.brightSlider.setOrientation(Qt.Horizontal)
        self.dial = QDial(self.white)
        self.dial.setObjectName(u"dial")
        self.dial.setEnabled(True)
        self.dial.setGeometry(QRect(195, 25, 510, 500))
        self.dial.setStyleSheet(u"QDial{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setWrapping(False)
        self.brightness = QLabel(self.white)
        self.brightness.setObjectName(u"brightness")
        self.brightness.setGeometry(QRect(140, 560, 131, 31))
        self.brightness.setStyleSheet(u"color: white;")
        self.brightBar = QProgressBar(self.white)
        self.brightBar.setObjectName(u"brightBar")
        self.brightBar.setEnabled(True)
        self.brightBar.setGeometry(QRect(250, 570, 400, 15))
        self.brightBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.brightBar.setValue(100)
        self.brightBar.setTextVisible(False)
        self.mode.addTab(self.white, "")
        self.whiteRound.raise_()
        self.dial.raise_()
        self.brightness.raise_()
        self.brightBar.raise_()
        self.brightSlider.raise_()
        self.onOFF.raise_()
        self.color = QWidget()
        self.color.setObjectName(u"color")
        self.colourSlider = QSlider(self.color)
        self.colourSlider.setObjectName(u"colourSlider")
        self.colourSlider.setEnabled(True)
        self.colourSlider.setGeometry(QRect(250, 606, 400, 22))
        self.colourSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"")
        self.colourSlider.setMaximum(100)
        self.colourSlider.setValue(100)
        self.colourSlider.setOrientation(Qt.Horizontal)
        self.colourBar = QProgressBar(self.color)
        self.colourBar.setObjectName(u"colourBar")
        self.colourBar.setGeometry(QRect(250, 610, 400, 15))
        self.colourBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.colourBar.setValue(100)
        self.colourBar.setTextVisible(False)
        self.colourTemp = QLabel(self.color)
        self.colourTemp.setObjectName(u"colourTemp")
        self.colourTemp.setGeometry(QRect(140, 600, 131, 31))
        self.colourTemp.setStyleSheet(u"color: white;")
        self.dial_color = QDial(self.color)
        self.dial_color.setObjectName(u"dial_color")
        self.dial_color.setEnabled(True)
        self.dial_color.setGeometry(QRect(195, 25, 510, 500))
        self.dial_color.setStyleSheet(u"QDial{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.dial_color.setMinimum(0)
        self.dial_color.setMaximum(100)
        self.dial_color.setWrapping(True)
        self.brightSlider_color = QSlider(self.color)
        self.brightSlider_color.setObjectName(u"brightSlider_color")
        self.brightSlider_color.setEnabled(True)
        self.brightSlider_color.setGeometry(QRect(250, 566, 400, 22))
        self.brightSlider_color.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"\n"
"")
        self.brightSlider_color.setMaximum(100)
        self.brightSlider_color.setValue(100)
        self.brightSlider_color.setOrientation(Qt.Horizontal)
        self.onOFF_color = QPushButton(self.color)
        self.onOFF_color.setObjectName(u"onOFF_color")
        self.onOFF_color.setGeometry(QRect(400, 225, 100, 100))
        self.onOFF_color.setStyleSheet(u"QPushButton { \n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 50%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(120, 120, 120, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"	 background-color: rgba(60, 60, 60, 25);\n"
"}\n"
"")
        self.onOFF_color.setIcon(icon)
        self.onOFF_color.setIconSize(QSize(96, 96))
        self.brightness_color = QLabel(self.color)
        self.brightness_color.setObjectName(u"brightness_color")
        self.brightness_color.setGeometry(QRect(140, 560, 131, 31))
        self.brightness_color.setStyleSheet(u"color: white;")
        self.brightBar_color = QProgressBar(self.color)
        self.brightBar_color.setObjectName(u"brightBar_color")
        self.brightBar_color.setEnabled(True)
        self.brightBar_color.setGeometry(QRect(250, 570, 400, 15))
        self.brightBar_color.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.brightBar_color.setValue(100)
        self.brightBar_color.setTextVisible(False)
        self.rgb = QLabel(self.color)
        self.rgb.setObjectName(u"rgb")
        self.rgb.setGeometry(QRect(225, 50, 450, 450))
        self.rgb.setStyleSheet(u"")
        self.rgb.setPixmap(QPixmap(u"design/rgb.png"))
        self.rgb.setScaledContents(True)
        self.rgb.setAlignment(Qt.AlignCenter)
        self.mode.addTab(self.color, "")
        self.rgb.raise_()
        self.colourBar.raise_()
        self.colourTemp.raise_()
        self.dial_color.raise_()
        self.brightness_color.raise_()
        self.brightBar_color.raise_()
        self.brightSlider_color.raise_()
        self.colourSlider.raise_()
        self.onOFF_color.raise_()
        self.scene = QWidget()
        self.scene.setObjectName(u"scene")
        self.editScene = QFrame(self.scene)
        self.editScene.setObjectName(u"editScene")
        self.editScene.setGeometry(QRect(470, 50, 430, 560))
        self.editScene.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-bottom: 2px solid rgb(120, 120, 120);\n"
"	border-top: 2px solid rgb(120, 120, 120);\n"
"	border-left: 2px solid rgb(120, 120, 120);\n"
"	font-size: 20px;\n"
"	border-top-left-radius: 10%;\n"
"	border-bottom-left-radius: 10%;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	border-bottom: 0px;\n"
"	border-top: 0px;\n"
"	border-left: 0px;\n"
"}\n"
"\n"
"QLineEdit {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	color: white;	\n"
"	border-top: 0px solid rgb(90, 90, 90);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QLineEdit:hover{\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"\n"
"QPushButton  {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	color: white;	\n"
"	border-top: 1px solid rgba(90, 90, 90, 0);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
""
                        "	background-color: rgb(60, 60, 60);\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-left-radius: 1%;\n"
"	border-bottom-right-radius: 1%;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 3px;\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}")
        self.editScene.setFrameShape(QFrame.StyledPanel)
        self.editScene.setFrameShadow(QFrame.Raised)
        self.nameScene = QLabel(self.editScene)
        self.nameScene.setObjectName(u"nameScene")
        self.nameScene.setGeometry(QRect(10, 60, 410, 30))
        self.nameScene.setAlignment(Qt.AlignCenter)
        self.nameSceneEdit = QLineEdit(self.editScene)
        self.nameSceneEdit.setObjectName(u"nameSceneEdit")
        self.nameSceneEdit.setGeometry(QRect(10, 100, 410, 24))
        self.nameSceneEdit.setAlignment(Qt.AlignCenter)
        self.colourScene = QLabel(self.editScene)
        self.colourScene.setObjectName(u"colourScene")
        self.colourScene.setGeometry(QRect(10, 150, 410, 30))
        self.colourScene.setAlignment(Qt.AlignCenter)
        self.modeColourFlicker = QLabel(self.editScene)
        self.modeColourFlicker.setObjectName(u"modeColourFlicker")
        self.modeColourFlicker.setGeometry(QRect(10, 250, 410, 30))
        self.modeColourFlicker.setAlignment(Qt.AlignCenter)
        self.modeColourFlickerBox = QComboBox(self.editScene)
        self.modeColourFlickerBox.addItem("")
        self.modeColourFlickerBox.addItem("")
        self.modeColourFlickerBox.addItem("")
        self.modeColourFlickerBox.setObjectName(u"modeColourFlickerBox")
        self.modeColourFlickerBox.setGeometry(QRect(10, 290, 410, 24))
        self.modeColourFlickerBox.setStyleSheet(u"QComboBox {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	font-family: Comfortaa;\n"
"	color: white;	\n"
"	padding-top: 3px;\n"
"	padding-left: 160px;\n"
"	border-top: 0px solid rgb(90, 90, 90);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"}\n"
"QComboBox:hover{\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"QComboBox::drop-down {\n"
"  	subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(50, 50, 50);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background: #484848;\n"
"}")
        self.speedFlickerBar = QProgressBar(self.editScene)
        self.speedFlickerBar.setObjectName(u"speedFlickerBar")
        self.speedFlickerBar.setGeometry(QRect(10, 380, 410, 16))
        self.speedFlickerBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.speedFlickerBar.setValue(0)
        self.speedFlickerBar.setTextVisible(False)
        self.speedFlickerSlider = QSlider(self.editScene)
        self.speedFlickerSlider.setObjectName(u"speedFlickerSlider")
        self.speedFlickerSlider.setGeometry(QRect(10, 380, 410, 16))
        self.speedFlickerSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"")
        self.speedFlickerSlider.setMaximum(100)
        self.speedFlickerSlider.setOrientation(Qt.Horizontal)
        self.speedFlicker = QLabel(self.editScene)
        self.speedFlicker.setObjectName(u"speedFlicker")
        self.speedFlicker.setGeometry(QRect(10, 340, 410, 30))
        self.speedFlicker.setAlignment(Qt.AlignCenter)
        self.addNewScene = QPushButton(self.editScene)
        self.addNewScene.setObjectName(u"addNewScene")
        self.addNewScene.setGeometry(QRect(10, 510, 410, 31))
        self.exitFromScene = QPushButton(self.editScene)
        self.exitFromScene.setObjectName(u"exitFromScene")
        self.exitFromScene.setGeometry(QRect(380, 10, 40, 24))
        self.sceneColoursList = QFrame(self.editScene)
        self.sceneColoursList.setObjectName(u"sceneColoursList")
        self.sceneColoursList.setGeometry(QRect(2, 190, 430, 50))
        self.sceneColoursList.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-bottom: 0px solid rgb(120, 120, 120);\n"
"	border-top: 0px solid rgb(120, 120, 120);\n"
"	border-left: 0px solid rgb(120, 120, 120);\n"
"}\n"
"QPushButton { \n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 20%;\n"
"	border-top: 0px;\n"
"	border-bottom: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(60, 60, 60);\n"
"}\n"
"QPushButton:pressed {\n"
"	 background-color:  rgb(60, 60, 60);\n"
"}\n"
"QPushButton:!enabled {\n"
"	 background-color:  rgb(60, 60, 60);\n"
"}")
        self.sceneColoursList.setFrameShape(QFrame.StyledPanel)
        self.sceneColoursList.setFrameShadow(QFrame.Raised)
        self.baseColour = QPushButton(self.sceneColoursList)
        self.baseColour.setObjectName(u"baseColour")
        self.baseColour.setGeometry(QRect(15, 5, 40, 40))
        self.baseColour.setStyleSheet(u"image: url(design/plus.png);")
        self.sceneImage = QLabel(self.editScene)
        self.sceneImage.setObjectName(u"sceneImage")
        self.sceneImage.setGeometry(QRect(10, 440, 410, 30))
        self.sceneImage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sceneImageButton = QPushButton(self.editScene)
        self.sceneImageButton.setObjectName(u"sceneImageButton")
        self.sceneImageButton.setGeometry(QRect(310, 420, 75, 75))
        self.sceneImageButton.setStyleSheet(u"QPushButton { \n"
"	background-color: #ecd105;\n"
"	border-radius: 37%;\n"
"	border-top: 0px;\n"
"	border-bottom: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #ddc004;\n"
"}\n"
"QPushButton:pressed {\n"
"	 background-color: #c6ac03;\n"
"}\n"
"QPushButton:!enabled {\n"
"	 background-color: #c6b43e;\n"
"}")
        self.sceneImageButton.setIconSize(QSize(75, 75))
        self.colourSceneEdit = QFrame(self.editScene)
        self.colourSceneEdit.setObjectName(u"colourSceneEdit")
        self.colourSceneEdit.setGeometry(QRect(0, 190, 430, 370))
        self.colourSceneEdit.setFrameShape(QFrame.StyledPanel)
        self.colourSceneEdit.setFrameShadow(QFrame.Raised)
        self.addNewColour = QPushButton(self.colourSceneEdit)
        self.addNewColour.setObjectName(u"addNewColour")
        self.addNewColour.setGeometry(QRect(10, 320, 410, 31))
        self.exitFromColour = QPushButton(self.colourSceneEdit)
        self.exitFromColour.setObjectName(u"exitFromColour")
        self.exitFromColour.setGeometry(QRect(380, 10, 40, 24))
        self.colourSceneSlider = QSlider(self.colourSceneEdit)
        self.colourSceneSlider.setObjectName(u"colourSceneSlider")
        self.colourSceneSlider.setGeometry(QRect(10, 130, 410, 16))
        self.colourSceneSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"")
        self.colourSceneSlider.setMaximum(100)
        self.colourSceneSlider.setOrientation(Qt.Horizontal)
        self.colourSceneBar = QProgressBar(self.colourSceneEdit)
        self.colourSceneBar.setObjectName(u"colourSceneBar")
        self.colourSceneBar.setGeometry(QRect(10, 130, 410, 16))
        self.colourSceneBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.colourSceneBar.setValue(0)
        self.colourSceneBar.setTextVisible(False)
        self.brightSceneSlider = QSlider(self.colourSceneEdit)
        self.brightSceneSlider.setObjectName(u"brightSceneSlider")
        self.brightSceneSlider.setGeometry(QRect(10, 190, 410, 16))
        self.brightSceneSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"")
        self.brightSceneSlider.setMaximum(1000)
        self.brightSceneSlider.setOrientation(Qt.Horizontal)
        self.brightSceneBar = QProgressBar(self.colourSceneEdit)
        self.brightSceneBar.setObjectName(u"brightSceneBar")
        self.brightSceneBar.setGeometry(QRect(10, 190, 410, 16))
        self.brightSceneBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.brightSceneBar.setMaximum(1000)
        self.brightSceneBar.setValue(0)
        self.brightSceneBar.setTextVisible(False)
        self.deleteSceneColour = QPushButton(self.colourSceneEdit)
        self.deleteSceneColour.setObjectName(u"deleteSceneColour")
        self.deleteSceneColour.setGeometry(QRect(330, 50, 91, 24))
        icon1 = QIcon()
        icon1.addFile(u"design/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteSceneColour.setIcon(icon1)
        self.deleteSceneColour.setIconSize(QSize(16, 16))
        self.colourMode = QRadioButton(self.colourSceneEdit)
        self.colourMode.setObjectName(u"colourMode")
        self.colourMode.setGeometry(QRect(20, 40, 50, 50))
        self.colourMode.setLayoutDirection(Qt.LeftToRight)
        self.colourMode.setStyleSheet(u"QRadioButton::indicator{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	border-radius: 20%;\n"
"	width: 40px;\n"
"	height: 40px;\n"
"	margin-left:5px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 25%\n"
"}")
        self.warmMode = QRadioButton(self.colourSceneEdit)
        self.warmMode.setObjectName(u"warmMode")
        self.warmMode.setGeometry(QRect(80, 40, 50, 50))
        self.warmMode.setStyleSheet(u"QRadioButton::indicator{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(255, 221, 161, 255), stop:1 rgba(220, 249, 255, 255));\n"
"	border-radius: 20%;\n"
"	width: 40px;	\n"
"	height: 40px;\n"
"	margin-left:5px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"	background-color:  rgb(60, 60, 60);\n"
"	border-radius: 25%\n"
"}")
        self.colourTempSceneSlider = QSlider(self.colourSceneEdit)
        self.colourTempSceneSlider.setObjectName(u"colourTempSceneSlider")
        self.colourTempSceneSlider.setGeometry(QRect(10, 250, 410, 16))
        self.colourTempSceneSlider.setStyleSheet(u"QSlider{\n"
"	background-color:rgba(120, 120, 120, 0);\n"
"	}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color:rgba(120, 120, 120, 0);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color:rgb(60, 60, 60);\n"
"    border: 2px solid white;\n"
"    width: 10px;\n"
"    margin: -5px 0;\n"
"	border-radius: 7.4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"	background-color:  rgb(102, 102, 102);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"	background-color: rgb(135, 135, 135)\n"
"}\n"
"\n"
"")
        self.colourTempSceneSlider.setMaximum(1000)
        self.colourTempSceneSlider.setOrientation(Qt.Horizontal)
        self.colourTempSceneBar = QProgressBar(self.colourSceneEdit)
        self.colourTempSceneBar.setObjectName(u"colourTempSceneBar")
        self.colourTempSceneBar.setGeometry(QRect(10, 250, 410, 16))
        self.colourTempSceneBar.setStyleSheet(u"QProgressBar {	\n"
"	background-color: rgb(120, 120, 120);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.colourTempSceneBar.setMaximum(1000)
        self.colourTempSceneBar.setValue(0)
        self.colourTempSceneBar.setTextVisible(False)
        self.colourTempSceneBar.raise_()
        self.brightSceneBar.raise_()
        self.colourSceneBar.raise_()
        self.addNewColour.raise_()
        self.exitFromColour.raise_()
        self.colourSceneSlider.raise_()
        self.brightSceneSlider.raise_()
        self.deleteSceneColour.raise_()
        self.colourMode.raise_()
        self.warmMode.raise_()
        self.colourTempSceneSlider.raise_()
        self.speedFlicker.raise_()
        self.nameScene.raise_()
        self.nameSceneEdit.raise_()
        self.colourScene.raise_()
        self.modeColourFlicker.raise_()
        self.modeColourFlickerBox.raise_()
        self.speedFlickerBar.raise_()
        self.speedFlickerSlider.raise_()
        self.addNewScene.raise_()
        self.exitFromScene.raise_()
        self.sceneColoursList.raise_()
        self.sceneImage.raise_()
        self.sceneImageButton.raise_()
        self.colourSceneEdit.raise_()
        self.editSceneButton = QPushButton(self.scene)
        self.editSceneButton.setObjectName(u"editSceneButton")
        self.editSceneButton.setGeometry(QRect(790, 10, 91, 31))
        self.editSceneButton.setStyleSheet(u"QPushButton  {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	color: white;	\n"
"	border-top: 1px solid rgba(90, 90, 90, 0);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-left-radius: 1%;\n"
"	border-bottom-right-radius: 1%;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 3px;\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"design/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editSceneButton.setIcon(icon2)
        self.editSceneButton.setIconSize(QSize(24, 24))
        self.sceneMode = QFrame(self.scene)
        self.sceneMode.setObjectName(u"sceneMode")
        self.sceneMode.setGeometry(QRect(0, 513, 900, 160))
        self.sceneMode.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-bottom: 2px solid rgb(120, 120, 120);\n"
"	border-top: 2px solid rgb(120, 120, 120);\n"
"	font-size: 20px;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	border-bottom: 0px;\n"
"	border-top: 0px;\n"
"	border-left: 0px;\n"
"}\n"
"\n"
"QPushButton { \n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 37%;\n"
"	border-top: 0px;\n"
"	border-bottom: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(120, 120, 120, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"	 padding-top: 3px;\n"
"	 background-color: rgba(60, 60, 60, 25);\n"
"}\n"
"")
        self.sceneMode.setFrameShape(QFrame.StyledPanel)
        self.sceneMode.setFrameShadow(QFrame.Raised)
        self.scene1Button = QPushButton(self.sceneMode)
        self.scene1Button.setObjectName(u"scene1Button")
        self.scene1Button.setGeometry(QRect(40, 20, 75, 75))
        self.scene1Button.setStyleSheet(u"")
        self.scene1Button.setIconSize(QSize(75, 75))
        self.scene1Label = QLabel(self.sceneMode)
        self.scene1Label.setObjectName(u"scene1Label")
        self.scene1Label.setGeometry(QRect(27, 110, 100, 21))
        self.scene1Label.setAlignment(Qt.AlignCenter)
        self.scene2Button = QPushButton(self.sceneMode)
        self.scene2Button.setObjectName(u"scene2Button")
        self.scene2Button.setGeometry(QRect(145, 20, 75, 75))
        self.scene2Button.setStyleSheet(u"")
        self.scene2Button.setIconSize(QSize(75, 75))
        self.scene3Button = QPushButton(self.sceneMode)
        self.scene3Button.setObjectName(u"scene3Button")
        self.scene3Button.setGeometry(QRect(250, 20, 75, 75))
        self.scene3Button.setStyleSheet(u"")
        self.scene3Button.setIconSize(QSize(75, 75))
        self.scene4Button = QPushButton(self.sceneMode)
        self.scene4Button.setObjectName(u"scene4Button")
        self.scene4Button.setGeometry(QRect(355, 20, 75, 75))
        self.scene4Button.setStyleSheet(u"")
        self.scene4Button.setIconSize(QSize(75, 75))
        self.scene5Button = QPushButton(self.sceneMode)
        self.scene5Button.setObjectName(u"scene5Button")
        self.scene5Button.setGeometry(QRect(460, 20, 75, 75))
        self.scene5Button.setStyleSheet(u"")
        self.scene5Button.setIconSize(QSize(75, 75))
        self.scene6Button = QPushButton(self.sceneMode)
        self.scene6Button.setObjectName(u"scene6Button")
        self.scene6Button.setGeometry(QRect(565, 20, 75, 75))
        self.scene6Button.setStyleSheet(u"")
        self.scene6Button.setIconSize(QSize(75, 75))
        self.scene7Button = QPushButton(self.sceneMode)
        self.scene7Button.setObjectName(u"scene7Button")
        self.scene7Button.setGeometry(QRect(670, 20, 75, 75))
        self.scene7Button.setStyleSheet(u"")
        self.scene7Button.setIconSize(QSize(75, 75))
        self.scene8Button = QPushButton(self.sceneMode)
        self.scene8Button.setObjectName(u"scene8Button")
        self.scene8Button.setGeometry(QRect(775, 20, 75, 75))
        self.scene8Button.setStyleSheet(u"")
        self.scene8Button.setIconSize(QSize(75, 75))
        self.scene2Label = QLabel(self.sceneMode)
        self.scene2Label.setObjectName(u"scene2Label")
        self.scene2Label.setGeometry(QRect(133, 110, 100, 21))
        self.scene2Label.setAlignment(Qt.AlignCenter)
        self.scene3Label = QLabel(self.sceneMode)
        self.scene3Label.setObjectName(u"scene3Label")
        self.scene3Label.setGeometry(QRect(237, 110, 100, 21))
        self.scene3Label.setAlignment(Qt.AlignCenter)
        self.scene4Label = QLabel(self.sceneMode)
        self.scene4Label.setObjectName(u"scene4Label")
        self.scene4Label.setGeometry(QRect(343, 110, 100, 21))
        self.scene4Label.setAlignment(Qt.AlignCenter)
        self.scene5Label = QLabel(self.sceneMode)
        self.scene5Label.setObjectName(u"scene5Label")
        self.scene5Label.setGeometry(QRect(447, 110, 100, 21))
        self.scene5Label.setAlignment(Qt.AlignCenter)
        self.scene6Label = QLabel(self.sceneMode)
        self.scene6Label.setObjectName(u"scene6Label")
        self.scene6Label.setGeometry(QRect(553, 110, 100, 21))
        self.scene6Label.setAlignment(Qt.AlignCenter)
        self.scene7Label = QLabel(self.sceneMode)
        self.scene7Label.setObjectName(u"scene7Label")
        self.scene7Label.setGeometry(QRect(657, 110, 100, 21))
        self.scene7Label.setAlignment(Qt.AlignCenter)
        self.scene8Label = QLabel(self.sceneMode)
        self.scene8Label.setObjectName(u"scene8Label")
        self.scene8Label.setGeometry(QRect(763, 110, 100, 21))
        self.scene8Label.setAlignment(Qt.AlignCenter)
        self.onOFF_scene = QPushButton(self.scene)
        self.onOFF_scene.setObjectName(u"onOFF_scene")
        self.onOFF_scene.setGeometry(QRect(400, 225, 100, 100))
        self.onOFF_scene.setStyleSheet(u"QPushButton { \n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 50%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(120, 120, 120, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"	 background-color: rgba(60, 60, 60, 25);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"design/modeOFF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.onOFF_scene.setIcon(icon3)
        self.onOFF_scene.setIconSize(QSize(96, 96))
        self.active_scene = QLabel(self.scene)
        self.active_scene.setObjectName(u"active_scene")
        self.active_scene.setGeometry(QRect(225, 50, 450, 450))
        self.active_scene.setStyleSheet(u"")
        self.active_scene.setPixmap(QPixmap(u"design/icon.png"))
        self.active_scene.setScaledContents(True)
        self.active_scene.setAlignment(Qt.AlignCenter)
        self.mode.addTab(self.scene, "")
        self.editSceneButton.raise_()
        self.active_scene.raise_()
        self.sceneMode.raise_()
        self.onOFF_scene.raise_()
        self.editScene.raise_()
        self.music = QWidget()
        self.music.setObjectName(u"music")
        self.onOFF_music = QPushButton(self.music)
        self.onOFF_music.setObjectName(u"onOFF_music")
        self.onOFF_music.setGeometry(QRect(400, 225, 100, 100))
        self.onOFF_music.setStyleSheet(u"QPushButton { \n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 50%;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(120, 120, 120, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-top: 3px;\n"
"	 background-color: rgba(60, 60, 60, 25);\n"
"}\n"
"")
        self.onOFF_music.setIcon(icon3)
        self.onOFF_music.setIconSize(QSize(96, 96))
        self.mode.addTab(self.music, "")
        self.type_devices.addWidget(self.RGB_Light)
        self.Light = QWidget()
        self.Light.setObjectName(u"Light")
        self.type_devices.addWidget(self.Light)
        self.deviceName_onScreen = QLabel(self.main_screen)
        self.deviceName_onScreen.setObjectName(u"deviceName_onScreen")
        self.deviceName_onScreen.setGeometry(QRect(350, 5, 200, 40))
        self.deviceName_onScreen.setAlignment(Qt.AlignCenter)
        self.screens.addWidget(self.main_screen)
        self.sideBarButton = QPushButton(self.centralwidget)
        self.sideBarButton.setObjectName(u"sideBarButton")
        self.sideBarButton.setGeometry(QRect(10, 10, 30, 30))
        self.sideBarButton.setStyleSheet(u"QPushButton  {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	border-radius: 5%;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 60, 60);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 3px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"design/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sideBarButton.setIcon(icon4)
        self.sideBarButton.setIconSize(QSize(24, 24))
        self.sideBar = QFrame(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setGeometry(QRect(0, 0, 230, 750))
        self.sideBar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-bottom: 2px solid rgb(120, 120, 120);\n"
"	border-right: 2px solid rgb(120, 120, 120);\n"
"	border-top: 2px solid rgb(120, 120, 120);\n"
"\n"
"}\n"
"QPushButton  {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 18px;\n"
"	color: white;	\n"
"	border-top: 1px solid rgba(90, 90, 90, 0);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"\n"
"	border-top-left-radius: 10%;\n"
"	border-top-right-radius: 10%;\n"
"	border-bottom-left-radius: 1%;\n"
"	border-bottom-right-radius: 1%;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding-top: 3px;\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"\n"
"QLabel{\n"
"	font-family: Comfortaa;\n"
"	font-weight: Bold;\n"
"	font-size: 24px;\n"
"	color: white;\n"
"	border: none;\n"
"}")
        self.sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.sideBarClose = QPushButton(self.sideBar)
        self.sideBarClose.setObjectName(u"sideBarClose")
        self.sideBarClose.setGeometry(QRect(160, 10, 60, 24))
        self.devicesList = QComboBox(self.sideBar)
        self.devicesList.setObjectName(u"devicesList")
        self.devicesList.setGeometry(QRect(10, 120, 210, 29))
        self.devicesList.setStyleSheet(u"QComboBox {	\n"
"	background-color: rgba(120, 120, 120, 0);\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"	font-family: Comfortaa;\n"
"	color: white;	\n"
"	padding-top: 6px;\n"
"	padding-left: 25px;\n"
"	border-top: 0px solid rgb(90, 90, 90);\n"
"	border-bottom: 2px solid rgb(90, 90, 90);\n"
"}\n"
"QComboBox:hover{\n"
"	border-bottom: 2px solid rgb(175, 175, 175);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid rgb(236, 236, 236);\n"
"}\n"
"QComboBox::drop-down {\n"
"  	subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(50, 50, 50);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	color: white;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background: #484848;\n"
"}\n"
"")
        self.addButton = QPushButton(self.sideBar)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(10, 200, 210, 29))
        self.removeButton = QPushButton(self.sideBar)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(10, 250, 210, 29))
        self.devicesList_label = QLabel(self.sideBar)
        self.devicesList_label.setObjectName(u"devicesList_label")
        self.devicesList_label.setGeometry(QRect(10, 75, 210, 35))
        self.devicesList_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.deviceType, self.deviceName)
        QWidget.setTabOrder(self.deviceName, self.ip)
        QWidget.setTabOrder(self.ip, self.id)
        QWidget.setTabOrder(self.id, self.key)
        QWidget.setTabOrder(self.key, self.ver)
        QWidget.setTabOrder(self.ver, self.add)
        QWidget.setTabOrder(self.add, self.clear)
        QWidget.setTabOrder(self.clear, self.sideBarButton)
        QWidget.setTabOrder(self.sideBarButton, self.mode)
        QWidget.setTabOrder(self.mode, self.onOFF)
        QWidget.setTabOrder(self.onOFF, self.brightSlider)
        QWidget.setTabOrder(self.brightSlider, self.dial)
        QWidget.setTabOrder(self.dial, self.colourSlider)
        QWidget.setTabOrder(self.colourSlider, self.dial_color)
        QWidget.setTabOrder(self.dial_color, self.brightSlider_color)
        QWidget.setTabOrder(self.brightSlider_color, self.onOFF_color)
        QWidget.setTabOrder(self.onOFF_color, self.nameSceneEdit)
        QWidget.setTabOrder(self.nameSceneEdit, self.modeColourFlickerBox)
        QWidget.setTabOrder(self.modeColourFlickerBox, self.speedFlickerSlider)
        QWidget.setTabOrder(self.speedFlickerSlider, self.addNewScene)
        QWidget.setTabOrder(self.addNewScene, self.exitFromScene)
        QWidget.setTabOrder(self.exitFromScene, self.baseColour)
        QWidget.setTabOrder(self.baseColour, self.sceneImageButton)
        QWidget.setTabOrder(self.sceneImageButton, self.addNewColour)
        QWidget.setTabOrder(self.addNewColour, self.exitFromColour)
        QWidget.setTabOrder(self.exitFromColour, self.colourSceneSlider)
        QWidget.setTabOrder(self.colourSceneSlider, self.brightSceneSlider)
        QWidget.setTabOrder(self.brightSceneSlider, self.deleteSceneColour)
        QWidget.setTabOrder(self.deleteSceneColour, self.colourMode)
        QWidget.setTabOrder(self.colourMode, self.warmMode)
        QWidget.setTabOrder(self.warmMode, self.colourTempSceneSlider)
        QWidget.setTabOrder(self.colourTempSceneSlider, self.editSceneButton)
        QWidget.setTabOrder(self.editSceneButton, self.scene1Button)
        QWidget.setTabOrder(self.scene1Button, self.scene2Button)
        QWidget.setTabOrder(self.scene2Button, self.scene3Button)
        QWidget.setTabOrder(self.scene3Button, self.scene4Button)
        QWidget.setTabOrder(self.scene4Button, self.scene5Button)
        QWidget.setTabOrder(self.scene5Button, self.scene6Button)
        QWidget.setTabOrder(self.scene6Button, self.scene7Button)
        QWidget.setTabOrder(self.scene7Button, self.scene8Button)
        QWidget.setTabOrder(self.scene8Button, self.onOFF_scene)
        QWidget.setTabOrder(self.onOFF_scene, self.onOFF_music)
        QWidget.setTabOrder(self.onOFF_music, self.sideBarClose)
        QWidget.setTabOrder(self.sideBarClose, self.devicesList)
        QWidget.setTabOrder(self.devicesList, self.addButton)
        QWidget.setTabOrder(self.addButton, self.removeButton)

        self.retranslateUi(MainWindow)
        self.sideBarClose.clicked.connect(self.sideBar.hide)
        self.sideBarButton.clicked.connect(self.sideBar.show)
        self.editSceneButton.clicked.connect(self.editScene.show)
        self.exitFromScene.clicked.connect(self.editScene.hide)
        self.exitFromColour.clicked.connect(self.colourSceneEdit.hide)
        self.baseColour.clicked.connect(self.colourSceneEdit.show)
        self.speedFlickerSlider.valueChanged.connect(self.speedFlickerBar.setValue)
        self.colourTempSceneSlider.valueChanged.connect(self.colourTempSceneBar.setValue)
        self.colourSlider.valueChanged.connect(self.colourBar.setValue)
        self.brightSlider.valueChanged.connect(self.brightBar.setValue)
        self.brightSlider_color.valueChanged.connect(self.brightBar_color.setValue)
        self.brightSceneSlider.valueChanged.connect(self.brightSceneBar.setValue)
        self.addNewColour.clicked.connect(self.colourSceneEdit.hide)
        self.addNewScene.clicked.connect(self.editScene.hide)

        self.screens.setCurrentIndex(0)
        self.mode.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Local Key", None))
        self.ver.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.ip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Device IP", None))
        self.id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Device ID", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"Add new device", None))
        self.deviceName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Device Name", None))
        self.whiteRound.setText("")
        self.onOFF.setText("")
        self.brightness.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.mode.setTabText(self.mode.indexOf(self.white), QCoreApplication.translate("MainWindow", u"White", None))
        self.colourTemp.setText(QCoreApplication.translate("MainWindow", u"Colour", None))
        self.onOFF_color.setText("")
        self.brightness_color.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.rgb.setText("")
        self.mode.setTabText(self.mode.indexOf(self.color), QCoreApplication.translate("MainWindow", u"Color", None))
        self.nameScene.setText(QCoreApplication.translate("MainWindow", u"Scene name", None))
        self.colourScene.setText(QCoreApplication.translate("MainWindow", u"Scene color", None))
        self.modeColourFlicker.setText(QCoreApplication.translate("MainWindow", u"Jumping color mode", None))
        self.modeColourFlickerBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Static", None))
        self.modeColourFlickerBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Jumping", None))
        self.modeColourFlickerBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Gradient", None))

        self.speedFlicker.setText(QCoreApplication.translate("MainWindow", u"Jumping speed", None))
        self.addNewScene.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.exitFromScene.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.baseColour.setText("")
        self.sceneImage.setText(QCoreApplication.translate("MainWindow", u"Scene image", None))
        self.sceneImageButton.setText("")
        self.addNewColour.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.exitFromColour.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.deleteSceneColour.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.colourMode.setText("")
        self.warmMode.setText("")
        self.editSceneButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.scene1Button.setText("")
        self.scene1Label.setText(QCoreApplication.translate("MainWindow", u"Scene1", None))
        self.scene2Button.setText("")
        self.scene3Button.setText("")
        self.scene4Button.setText("")
        self.scene5Button.setText("")
        self.scene6Button.setText("")
        self.scene7Button.setText("")
        self.scene8Button.setText("")
        self.scene2Label.setText(QCoreApplication.translate("MainWindow", u"Scene2", None))
        self.scene3Label.setText(QCoreApplication.translate("MainWindow", u"Scene3", None))
        self.scene4Label.setText(QCoreApplication.translate("MainWindow", u"Scene4", None))
        self.scene5Label.setText(QCoreApplication.translate("MainWindow", u"Scene5", None))
        self.scene6Label.setText(QCoreApplication.translate("MainWindow", u"Scene6", None))
        self.scene7Label.setText(QCoreApplication.translate("MainWindow", u"Scene7", None))
        self.scene8Label.setText(QCoreApplication.translate("MainWindow", u"Scene8", None))
        self.onOFF_scene.setText("")
        self.active_scene.setText("")
        self.mode.setTabText(self.mode.indexOf(self.scene), QCoreApplication.translate("MainWindow", u"Scene", None))
        self.onOFF_music.setText("")
        self.mode.setTabText(self.mode.indexOf(self.music), QCoreApplication.translate("MainWindow", u"Music", None))
        self.deviceName_onScreen.setText(QCoreApplication.translate("MainWindow", u"Device name", None))
        self.sideBarButton.setText("")
        self.sideBarClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add new device", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove device", None))
        self.devicesList_label.setText(QCoreApplication.translate("MainWindow", u"Devices list", None))
    # retranslateUi


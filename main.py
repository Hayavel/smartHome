from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QComboBox,
                               QProgressBar, QSlider, QLineEdit, QDial, QLabel,
                               QFrame, QRadioButton, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont

from ui import Ui_MainWindow
from warning import WarningDialog

import sys
import json
import time

#from smartDevice import Bulb
#from roundedImage import rounded_image
#import hexadecimal as hexDec
#import local_statistics as lStat


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.active_devices = {}

        self.setWindowTitle('SmartDevice')
        self.setWindowIcon(QIcon('design/icon.ico'))
        font = QFont('Comfortaa', 24)
        font.setBold(True)
        self.setFont(font)

        self.sideBar.setVisible(False)
        self.editScene.setVisible(False)
        self.colourSceneEdit.setVisible(False)

        self.add.clicked.connect(lambda: self.add_new_device())
        self.clear.clicked.connect(lambda: self.clear_addFrame())

    def add_new_device(self):
        '''Add new Light and save updated list'''
        deviceName = self.deviceName.text()
        deviceId = self.id.text()
        deviceIp = self.ip.text()
        deviceKey = self.key.text()
        deviceVersion = self.ver.text()
        deviceType = self.deviceType.currentText() if self.deviceType.currentIndex()!=-1 else ''

        if deviceName!='' and deviceId!='' and deviceIp!='' and\
           deviceKey!='' and deviceVersion!='' and deviceType!='':
            
            self.active_devices[self.deviceName.text()] = dict
            self.active_devices[self.deviceName.text()]['type'] = self.deviceType.currentText()
            self.active_devices[self.deviceName.text()]['id'] = self.id.text()
            self.active_devices[self.deviceName.text()]['ip'] = self.ip.text()
            self.active_devices[self.deviceName.text()]['key'] = self.key.text()
            self.active_devices[self.deviceName.text()]['ver'] = self.ver.text()

            self.devicesList.addItem(self.deviceName.text())
            self.clear_addFrame()
            self.screens.setCurrentIndex(1)

            with open('devicesList.json', 'w') as f:
                f.write(json.dumps(self.active_devices, indent=4))

        else:
            dlg = WarningDialog()
            dlg.exec()

    def clear_addFrame(self):
        '''Clear all LineEdit element in AddFrame'''
        self.deviceName.clear()
        self.id.clear()
        self.ip.clear()
        self.key.clear()
        self.ver.clear()
        
           
if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()
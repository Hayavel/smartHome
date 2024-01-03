from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QComboBox,
                               QProgressBar, QSlider, QLineEdit, QDial, QLabel,
                               QFrame, QRadioButton, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont

from ui import Ui_MainWindow
from warning import WarningDialog, RemoveDeviceDialog

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

        self._adding_devices_in_devicesList() # Data preload
        self._adding_device_types_in_deviceType() # Data preload

        self.sideBar.setVisible(False)
        self.editScene.setVisible(False)
        self.colourSceneEdit.setVisible(False)

        self.devicesList_start.currentIndexChanged.connect(self.devicesList.setCurrentIndex) # Reverse swap index
        self.devicesList.currentIndexChanged.connect(self.devicesList_start.setCurrentIndex) # Reverse swap index

        self.add.clicked.connect(lambda: self.add_new_device())
        self.clear.clicked.connect(lambda: self.clear_addFrame())
        self.addFrameClose.clicked.connect(lambda: self.close_addFrame()) # Close Add device screen

        self.addButton_start.clicked.connect(lambda: self.open_addFrame())
        self.addButton.clicked.connect(lambda: self.open_addFrame())

        self.select_start.clicked.connect(lambda: self.set_selected_device(self.devicesList_start.currentText()))
        self.select.clicked.connect(lambda: self.set_selected_device(self.devicesList.currentText()))

        self.removeButton_start.clicked.connect(lambda: self.remove_device())
        self.removeButton.clicked.connect(lambda: self.remove_device())


    def _adding_devices_in_devicesList(self):
        '''Add all local devices'''
        try:
            with open('devicesList.json', 'r') as f:
                self.active_devices = f.read()
                self.active_devices = json.loads(self.active_devices)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            self.active_devices = {}

        self.devicesList_start.addItems(self.active_devices)
        self.devicesList.addItems(self.active_devices)

    def _adding_device_types_in_deviceType(self):
        '''Add all available devices types'''
        types = ['RGB Light', 'Light']
        self.deviceType.addItems(types)
    
    def _change_active_device_name(self, text:str):
        self.deviceName_onScreen.setText(text)


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
            
            self.active_devices[deviceName] = {}
            self.active_devices[deviceName]['type'] = deviceType
            self.active_devices[deviceName]['id'] = deviceId
            self.active_devices[deviceName]['ip'] = deviceIp
            self.active_devices[deviceName]['key'] = deviceKey
            self.active_devices[deviceName]['ver'] = deviceVersion

            self.devicesList_start.addItem(deviceName)
            self.devicesList.addItem(deviceName)
            self.clear_addFrame()
            self.screens.setCurrentIndex(2)

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
        
    def open_addFrame(self):
        self.sideBar.hide()
        self.screens.setCurrentIndex(1)

    def set_selected_device(self, text:str):
        self._change_active_device_name(text)
        self.screens.setCurrentIndex(2)

    def close_addFrame(self):
        '''Сloses if there are already devices'''
        if self.devicesList.currentIndex() == -1:
            dlg = WarningDialog()
            dlg.exec()
        else:
            self.screens.setCurrentIndex(2)

    def remove_device(self):
        '''Open remove dialog and if answer is Yes delete selected device'''
        remove_dialog = RemoveDeviceDialog()
        if remove_dialog.exec():
            removed_device = self.devicesList.currentText()
            removed_device_index = self.devicesList.currentIndex()
            self.devicesList_start.removeItem(removed_device_index)
            self.devicesList.removeItem(removed_device_index)
            self.active_devices.pop(removed_device)
    
           
if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()
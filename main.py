from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QComboBox,
                               QProgressBar, QSlider, QLineEdit, QDial, QLabel,
                               QFrame, QRadioButton, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont

from ui import Ui_MainWindow
from warning import WarningDialog, RemoveDeviceDialog

import sys
import json
import time

from smartDevice import *
#from roundedImage import rounded_image
#import hexadecimal as hexDec
#import local_statistics as lStat


device_types = {'RGB Light': 0, # Device type and Page interface
                'Light': 1}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('SmartDevice')
        self.setWindowIcon(QIcon('design/icon.ico'))
        font = QFont('Comfortaa', 24)
        font.setBold(True)
        self.setFont(font)

        self._adding_devices_in_devicesList() # Data preload
        self._adding_device_types_in_deviceType() # Data preload

        # Hide element in RGB Light screen
        self.sideBar.setVisible(False)
        self.editScene.setVisible(False)
        self.colourSceneEdit.setVisible(False)

        # Hide element in Light screen
        self.editScene_Light.setVisible(False)
        self.colourSceneEdit_Light.setVisible(False)
        self.sceneMode_Light.setVisible(False)
        self.editSceneButton_Light.setVisible(False)

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

        self.screens.currentChanged.connect(self.set_device_state)
        self.type_screens.currentChanged.connect(self.set_device_state)

        # Change mode on Light screen
        self.white_Light.clicked.connect(lambda: self.switch_mode_Light(self.white_Light.text()))
        self.scene_Light.clicked.connect(lambda: self.switch_mode_Light(self.scene_Light.text()))

        self.mode.currentChanged.connect(self.switch_mode_RGB_Light)
        

        # Switch state of device on main screen
        self.onOFF_Light.clicked.connect(lambda: self.switch_state_of_device())
        self.onOFF_RGB_Light.clicked.connect(lambda: self.switch_state_of_device())

        self.dial_white.valueChanged.connect(self.change_colourTemp)
        self.dial_color.valueChanged.connect(self.change_hsv)
        self.dial_Light.valueChanged.connect(self.change_colourTemp)
        
        self.brightSlider_white.valueChanged.connect(self.change_brightness)
        self.brightSlider_color.valueChanged.connect(self.change_hsv)
        self.colourSlider.valueChanged.connect(self.change_hsv)
        self.brightSlider_Light.valueChanged.connect(self.change_brightness)


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
        self.deviceType.addItems(device_types.keys())
    
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
            self.type_screens.setCurrentIndex(device_types[deviceType])
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

    def set_selected_device(self, text:str):
        '''Switch on device type screen
            and connection to device'''
        self._change_active_device_name(text)

        selected_device = self.active_devices[text] # Selected device data

        deviceClassName = selected_device['type']
        deviceClassName = deviceClassName.replace(' ', '_')
        deviceClassName = globals()[deviceClassName] # Get variable of device type

        self.current_device = deviceClassName(selected_device['id'],
                                              selected_device['ip'],
                                              selected_device['key'],
                                              float(selected_device['ver']))

        deviceType = selected_device['type']
        self.type_screens.setCurrentIndex(device_types[deviceType]) # Switch on device type screen

        self.switch_icon_state_of_device() # Switch device state(on/off)

        self.screens.setCurrentIndex(2)

    def switch_icon_state_of_device(self):
        '''Switching the button icon to the one corresponding to the device state'''
        state = self.current_device.get_state()
        
        ui_device_type = self.type_screens.currentWidget().objectName()
        name_button = f'self.onOFF_{ui_device_type}'
        
        match state['is_on']:
            case True:
                icon = QIcon('design/modeON.png')
                exec(f'{name_button}.setIcon(icon)') # Switching the icon of the current button

            case False:
                 icon = QIcon('design/modeOFF.png')
                 exec(f'{name_button}.setIcon(icon)') # Switching the icon of the current button

    def switch_state_of_device(self):
        '''Switching the state of the device itself'''
        state = self.current_device.get_state()
        reState = not state['is_on']
        self.current_device.set_state(reState)

        self.switch_icon_state_of_device()

    def set_device_state(self):
        '''Set on screen device state by type'''
        device = self.type_screens.currentWidget().objectName()

        match device:
            case 'RGB_Light':
                self.switch_mode_RGB_Light()
            case 'Light':
                mode = self.current_device.get_state()['mode']
                self.switch_mode_Light(mode)

    def switch_mode_Light(self, mode:str):
        '''Hide or Show "scene" element on Light device screen.
        Set saved Light state(mode, brightness, colourTemp)'''
        mode = mode.lower()
        match mode:
            case 'white':
                self.editScene_Light.setVisible(False)
                self.colourSceneEdit_Light.setVisible(False)
                self.sceneMode_Light.setVisible(False)
                self.editSceneButton_Light.setVisible(False)

                self.current_device.set_mode(mode)
                
                colourTemp = self.current_device.get_colourtemp() / 10
                brightness = self.current_device.get_brightness() / 10

                self.dial_Light.setValue(colourTemp)
                self.brightSlider_Light.setValue(brightness)
            case 'scene':
                self.sceneMode_Light.setVisible(True)
                self.editSceneButton_Light.setVisible(True)

                self.current_device.set_mode(mode)
            case _: # Set white mode
                self.editScene_Light.setVisible(False)
                self.colourSceneEdit_Light.setVisible(False)
                self.sceneMode_Light.setVisible(False)
                self.editSceneButton_Light.setVisible(False)

                self.current_device.set_mode('white') 
                
                colourTemp = self.current_device.get_colourtemp() / 10
                brightness = self.current_device.get_brightness() / 10

                self.dial_Light.setValue(colourTemp)
                self.brightSlider_Light.setValue(brightness)

    def switch_mode_RGB_Light(self, index=None):
        '''Switch mode of RGB Light.
        Set saved RGB Light state(mode, hue, saturation, brightness)'''
        if index != None:
            mode = self.mode.currentWidget().objectName()
        else:
            modes = {'white': 0, 'colour': 1, 'scene': 2, 'music': 3}
            mode = self.current_device.get_state()['mode']

            self.mode.setCurrentIndex(modes[mode])

        self.current_device.set_mode(mode)

        match mode:
            case 'white':
                colourTemp = self.current_device.get_colourtemp() / 10
                brightness = self.current_device.get_brightness() / 10

                self.dial_white.setValue(colourTemp)
                self.brightSlider_white.setValue(brightness)
            case 'colour':
                hsv = self.current_device.get_hsv()
                self.dial_color.setValue(hsv[0]*100)
                self.colourSlider.setValue(hsv[1]*100)
                self.brightSlider_color.setValue(hsv[2]*100)

            case 'scene':
                pass
            case 'music':
                pass

    def change_brightness(self, value):
        '''Change brightness of Light'''
        self.current_device.set_brightness(value)
    
    def change_colourTemp(self, value):
        '''Change Light Temperature'''
        self.current_device.set_colourTemp(value)
    
    def change_hsv(self):
        '''Change colour in 'colour' mode'''
        h = self.dial_color.value() / 100
        s = self.colourSlider.value() / 100
        v = self.brightSlider_color.value() / 100

        self.current_device.set_hsv(h, s, v)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()
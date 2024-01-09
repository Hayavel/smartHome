from PySide6.QtWidgets import (QMainWindow, QApplication, QPushButton, QComboBox,
                               QProgressBar, QSlider, QLineEdit, QDial, QLabel,
                               QFrame, QRadioButton, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont

from ui import Ui_MainWindow
from warning import WarningDialog, RemoveDeviceDialog

import sys
import json
import time
from copy import deepcopy

from smartDevice import *
from roundedImage import rounded_image
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

        self.sceneLabels_RGB = [self.scene1Label, self.scene2Label, self.scene3Label, self.scene4Label,
                               self.scene5Label, self.scene6Label, self.scene7Label, self.scene8Label]
        self.sceneButtons_RGB = [self.scene1Button, self.scene2Button, self.scene3Button, self.scene4Button,
                        self.scene5Button, self.scene6Button, self.scene7Button, self.scene8Button]
        self.sceneLabels_Light = [self.scene1Label_Light, self.scene2Label_Light, self.scene3Label_Light,
                        self.scene4Label_Light, self.scene5Label_Light, self.scene6Label_Light,
                        self.scene7Label_Light, self.scene8Label_Light]
        self.sceneButtons_Light = [self.scene1Button_Light, self.scene2Button_Light, self.scene3Button_Light,
                        self.scene4Button_Light, self.scene5Button_Light, self.scene6Button_Light,
                        self.scene7Button_Light, self.scene8Button_Light]
        
        self.scene1Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','0'))
        self.scene2Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','1'))
        self.scene3Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','2'))
        self.scene4Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','3'))
        self.scene5Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','4'))
        self.scene6Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','5'))
        self.scene7Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','6'))
        self.scene8Button.clicked.connect(lambda: self.switch_current_scene('RGB Light','7'))

        self.scene1Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','0'))
        self.scene2Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','1'))
        self.scene3Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','2'))
        self.scene4Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','3'))
        self.scene5Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','4'))
        self.scene6Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','5'))
        self.scene7Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','6'))
        self.scene8Button_Light.clicked.connect(lambda: self.switch_current_scene('Light','7'))


        self.sceneImageButton.clicked.connect(self.set_new_image_to_scene)
        self.sceneImageButton_Light.clicked.connect(self.set_new_image_to_scene)

        self.exitFromScene.clicked.connect(self.close_editScene_panel)
        self.exitFromScene_Light.clicked.connect(self.close_editScene_panel)


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
                with open('lightScene.json', 'r') as f:
                    scenes_data = f.read()
                    self.scenes_data = json.loads(scenes_data)

                self.switch_mode_RGB_Light()
            case 'Light':
                with open('lightScene.json', 'r') as f:
                    scenes_data = f.read()
                    self.scenes_data = json.loads(scenes_data)

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
                self.dial_Light.setVisible(True)

                self.current_device.set_mode(mode)
                
                colourTemp = self.current_device.get_colourtemp() / 10
                brightness = self.current_device.get_brightness() / 10

                self.dial_Light.setValue(colourTemp)
                self.brightSlider_Light.setValue(brightness)

                self.whiteRound_Light.clear()
                pixmap = QPixmap('design/coldWarm.png')
                self.whiteRound_Light.setPixmap(pixmap)
            case 'scene':
                self.sceneMode_Light.setVisible(True)
                self.editSceneButton_Light.setVisible(True)
                self.dial_Light.setVisible(False)

                self.current_device.set_mode(mode)
                self.set_Light_scenes('Light')
                self.set_name_and_image_scenes('Light')

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
                self.set_Light_scenes('RGB Light')
                self.set_name_and_image_scenes('RGB Light')
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

    def set_Light_scenes(self, light_type:str):
        '''Set Scene Image and Name for Light or RGB Light'''
        data = deepcopy(self.scenes_data[light_type])

        status = self.current_device.get_status()

        for key, scene in data.items():
            if status['dps']['25'] == scene['data']:
                self.current_scene = [key, data[key]]
                break
            else:
                self.current_scene = ['0', data['0']]

        match light_type:
            case 'RGB Light':
                pixmap = QPixmap(self.current_scene[1]['image'])
                self.active_scene.clear()
                self.active_scene.setPixmap(pixmap)

            case 'Light':
                pixmap = QPixmap(self.current_scene[1]['image'])
                self.whiteRound_Light.clear()
                self.whiteRound_Light.setPixmap(pixmap)

    def set_name_and_image_scenes(self, light_type:str):
        '''Set actual scene's name and image'''

        data = deepcopy(self.scenes_data[light_type])

        match light_type:
            case 'RGB Light':
                sceneButtons = self.sceneButtons_RGB
                sceneLabels = self.sceneLabels_RGB
            case 'Light':
                sceneButtons = self.sceneButtons_Light
                sceneLabels = self.sceneLabels_Light

        for id in range(len(sceneButtons)):
            sceneLabels[id].setText(data[str(id)]['name'])
            image = QIcon(data[str(id)]['image'])
            sceneButtons[id].setIcon(image)
    
    def switch_current_scene(self, light_type:str, id:str):
        self.current_scene = [id, self.scenes_data[light_type][id]]
        self.current_device.set_scene(self.current_scene[1]['data'])
        
        pixmap = QPixmap(self.current_scene[1]['image'])
        match light_type:
            case 'RGB Light':
                self.active_scene.clear()
                self.active_scene.setPixmap(pixmap)
            case 'Light':
                self.whiteRound_Light.clear()
                self.whiteRound_Light.setPixmap(pixmap)
    
    def set_new_image_to_scene(self):
        '''Call QFileDialog to change image.
        Image save in 'design/sceneImage/' folder after accept changes'''
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Directory', '', 'Image (*.png *.jpg *jpeg)')
        if filename:
            new_path_image = rounded_image(filename, 'design/sceneImage/')

            image = QIcon(new_path_image)
            button = self.sender()
            button.setIcon(image)
            self.current_scene[1]['image'] = new_path_image
            print(self.scenes_data['RGB Light'][self.current_scene[0]])
            print(self.current_scene)

    def close_editScene_panel(self):
        '''If closed EditScene Panel, then return old Scene data'''
        light_type = self.type_screens.currentWidget().objectName()
        light_type = light_type.replace('_', ' ')
        data = deepcopy(self.scenes_data[light_type][self.current_scene[0]])
        self.current_scene[1] =  data
        print(self.scenes_data[light_type][self.current_scene[0]])
        print(self.current_scene)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog)

from PySide6.QtGui import QPixmap, QIcon, QFontDatabase, QFont
from PySide6.QtCore import QThreadPool, Slot

from ui import Ui_MainWindow
from colourButton import ColourButton
from warning import WarningDialog, RemoveDeviceDialog

import sys
import json
from copy import deepcopy
import numpy as np

from smartDevice import *
from roundedImage import rounded_image
import hexadecimal as hexDec
import audioRecorder as ar


device_types = {'RGB Light': 0, # Device type and Page interface
                'Light': 1}
modes = {'white': 0, 'colour': 1, 'scene': 2, 'music': 3}
devicesList_filename = 'devicesList.json'

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
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)

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
        self.select.clicked.connect(self.sideBar.hide)

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

        self.dial_white.valueChanged.connect(lambda: self.threadpool.start(self.change_colourTemp))
        self.dial_color.valueChanged.connect(lambda: self.threadpool.start(self.change_hsv))
        self.dial_Light.valueChanged.connect(lambda: self.threadpool.start(self.change_colourTemp))
        
        self.brightSlider_white.valueChanged.connect(lambda: self.threadpool.start(self.change_brightness))
        self.brightSlider_color.valueChanged.connect(lambda: self.threadpool.start(self.change_hsv))
        self.colourSlider.valueChanged.connect(lambda: self.threadpool.start(self.change_hsv))
        self.brightSlider_Light.valueChanged.connect(lambda: self.threadpool.start(self.change_brightness))

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

        self.exitFromScene.clicked.connect(lambda: self.close_editScene_panel('RGB Light'))
        self.exitFromScene.clicked.connect(self.colourSceneEdit.hide)
        self.exitFromScene_Light.clicked.connect(lambda: self.close_editScene_panel('Light'))
        self.exitFromScene_Light.clicked.connect(self.colourSceneEdit_Light.hide)

        self.editSceneButton.clicked.connect(self.add_scene_data_to_editScene)
        self.editSceneButton_Light.clicked.connect(self.add_scene_data_to_editScene)
        
        self.warmMode.toggled.connect(lambda: self.set_mode_to_colourSceneBar('white'))
        self.colourMode.toggled.connect(lambda: self.set_mode_to_colourSceneBar('colour'))

        self.addNewColour.clicked.connect(lambda: self.set_new_colour_to_editScene('RGB Light'))
        self.addNewColour.clicked.connect(lambda: self.add_new_colour_in_scene('RGB Light',
                                                                    self.sceneColoursList.children()[-1].objectName()))
        self.deleteSceneColour.clicked.connect(lambda: self.delete_current_colour('RGB Light'))

        self.addNewScene.clicked.connect(lambda: self.save_new_Scene_data('RGB Light'))


        self.addNewColour_Light.clicked.connect(lambda: self.set_new_colour_to_editScene('Light'))
        self.addNewColour_Light.clicked.connect(lambda: self.add_new_colour_in_scene('Light',
                                                            self.sceneColoursList_Light.children()[-1].objectName()))
        self.deleteSceneColour_Light.clicked.connect(lambda: self.delete_current_colour('Light'))

        self.addNewScene_Light.clicked.connect(lambda: self.save_new_Scene_data('Light'))

    def _adding_devices_in_devicesList(self):
        '''Add all local devices'''
        try:
            with open(devicesList_filename, 'r') as f:
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

        try:
            float(deviceVersion)
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
                self.set_selected_device(deviceName)
                self.screens.setCurrentIndex(2)

                with open(devicesList_filename, 'w') as f:
                    f.write(json.dumps(self.active_devices, indent=4))

            else:
                dlg = WarningDialog()
                dlg.exec()
        except ValueError:
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

            with open(devicesList_filename, 'w') as f:
                f.write(json.dumps(self.active_devices, indent=4))

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


        match self.current_device.get_state(): # Check correct device's local ip
            case {'Error': 'Invalid JSON Response from Device'}:
                self.current_device.get_actual_devices_ip(devicesList_filename)

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
        if self.screens.currentIndex() != 1:
            device = self.type_screens.currentWidget().objectName()
            with open('lightScene.json', 'r') as f:
                scenes_data = f.read()
                self.scenes_data = json.loads(scenes_data)

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
                self.start_record_audio()
                self.threadpool.start(self.record_audio)


    @Slot()
    def change_brightness(self):
        '''Change brightness of Light'''
        match self.type_screens.currentWidget().objectName():
            case 'RGB_Light':
                value = self.brightSlider_white.value()
                self.current_device.set_brightness(value)
            case 'Light':
                value = self.brightSlider_Light.value()
                self.current_device.set_brightness(value)
    
    @Slot()
    def change_colourTemp(self):
        '''Change Light Temperature'''
        match self.type_screens.currentWidget().objectName():
            case 'RGB_Light':
                value = self.dial_white.value()
                self.current_device.set_colourTemp(value)
            case 'Light':
                value = self.dial_Light.value()
                self.current_device.set_colourTemp(value)
    
    @Slot()
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

    def close_editScene_panel(self, light_type:str):
        '''If closed EditScene Panel, then return old Scene data'''

        data = deepcopy(self.scenes_data[light_type][self.current_scene[0]])
        self.current_scene[1] =  data
        colours_count = len(data['color_list'])
        if light_type == 'RGB Light':
            colours_list = self.sceneColoursList
        else:
            colours_list = self.sceneColoursList_Light
        for i, widget in enumerate(colours_list.children()):
            if i >= colours_count:
                widget.deleteLater()

    def add_scene_data_to_editScene(self):
        '''Get actual scene data, and add to EditScene Panel'''
        parent = self.sender().parent().objectName()
        data = self.current_scene[1]
        match parent:
            case 'scene':
                self.nameSceneEdit.setText(data['name'])
                self.speedFlickerSlider.setValue(data['transition_interval'])
                self.modeColourFlickerBox.setCurrentIndex(data['lightning_mode'])
                match data['white']:
                    case True:
                        self.warmMode.setChecked(True)
                        self.set_mode_to_colourSceneBar('white')
                    case False:
                        self.colourMode.setChecked(True)
                        self.set_mode_to_colourSceneBar('colour')

                for i, color in enumerate(data['color_list']):
                    self.add_new_colour_in_scene('RGB Light', i, color)
                self.add_new_colour_in_scene('RGB Light',i+1)

                image = QIcon(data['image'])
                self.sceneImageButton.setIcon(image)

            case 'Light':
                self.nameSceneEdit_Light.setText(data['name'])
                self.speedFlickerSlider_Light.setValue(data['transition_interval'])
                self.modeColourFlickerBox_Light.setCurrentIndex(data['lightning_mode'])

                for i, color in enumerate(data['color_list']):
                    self.add_new_colour_in_scene('Light', i, color)
                self.add_new_colour_in_scene('Light', i+1)

                image = QIcon(data['image'])
                self.sceneImageButton_Light.setIcon(image)

    def set_mode_to_colourSceneBar(self, mode:str):
        '''Set actual stylesheet to colourSceneBar(Colour or Warm)'''
        match mode:
            case 'white':
                self.colourSceneBar.setMaximum(1000)
                self.colourSceneSlider.setMaximum(1000)
                self.colourTempSceneBar.setVisible(False)
                self.colourTempSceneSlider.setVisible(False)
                self.colourTempSceneLabel.setVisible(False)
            case 'colour':
                self.colourSceneBar.setMaximum(360)
                self.colourSceneSlider.setMaximum(360)
                self.colourTempSceneBar.setVisible(True)
                self.colourTempSceneSlider.setVisible(True)
                self.colourTempSceneLabel.setVisible(True)

        with open(f'design/sceneColourBarEdit_{mode}.css', 'r') as f:
            self.colourSceneBar.setStyleSheet(f.read())
    
    def add_new_colour_in_scene(self, light_type:str, i, color=None):
        '''Add colour button in sceneColorList with colour from scene data or
          without(with Plus icon)'''
        if type(i) == str:
            if self.current_baseColour.objectName() != i:
                return
            i = int(i[-1]) + 1

        if light_type == 'RGB Light':
            colours_list = self.sceneColoursList
            scene_edit = self.colourSceneEdit
        elif light_type == 'Light':
            colours_list = self.sceneColoursList_Light
            scene_edit = self.colourSceneEdit_Light

        for c in colours_list.children():
            if c.objectName() == f'baseColour{i}':
                button = c
                break
        else:
            button = ColourButton()
            button.setParent(colours_list)
            button.setObjectName(f'baseColour{i}')

        x = 5 + (50*i)
        button.setGeometry(x, 5, 40, 40)
        if color:
            stylesheet = self.set_colour(light_type, color)
            button.setStyleSheet(stylesheet)
            button.setIcon(QIcon())
        else:
            button.setStyleSheet('')
            button.setIcon(QIcon('design/plus.png'))
        button.setVisible(True)
        button.clicked.connect(scene_edit.show)
        button.clicked.connect(self.get_current_baseColour)

    def set_colour(self, light_type:str, color:dict):
        '''Read and convert HSV data to baseColour button stylesheet'''
        if light_type == 'RGB Light':
            if self.colourMode.isChecked() == True:
                hue = color['hue']
                if hue == 360:
                    hue -= 1

                saturation = 0 + (((color['saturation'] - 0)*(255-0)) / 1000)

                value = 0 + (((color['value'] - 0)*(255-0)) / 1000)
                
                data = f'hsv({hue}, {saturation}, {value});'
            
            elif self.warmMode.isChecked() == True:
                start = [255, 221, 161] # const
                end = [220, 249, 255] # const

                color_temp = color['color_temp']

                k_R = start[0] + (color_temp/1000) * (end[0] - start[0])
                k_G = start[1] + (color_temp/1000) * (end[1] - start[1])
                k_B = start[2] + (color_temp/1000) * (end[2] - start[2])
                
                data = f'rgb({k_R}, {k_G}, {k_B});'
        elif light_type == 'Light':
            start = [255, 221, 161] # const
            end = [220, 249, 255] # const

            color_temp = color['color_temp']

            k_R = start[0] + (color_temp/1000) * (end[0] - start[0])
            k_G = start[1] + (color_temp/1000) * (end[1] - start[1])
            k_B = start[2] + (color_temp/1000) * (end[2] - start[2])
            
            data = f'rgb({k_R}, {k_G}, {k_B});'

        stylesheet = f'background-color: {data}'
        return stylesheet     

    def get_current_baseColour(self):
        '''Saved clicked baseColour button for further editing'''
        self.current_baseColour = self.sender()
        id = int(self.current_baseColour.objectName()[-1])
        try: # If add new colour
            color = self.current_scene[1]['color_list'][id]
            light_type = self.type_screens.currentWidget().objectName()
            if light_type == 'RGB_Light':
                if self.current_scene[1]['white']:
                    self.colourSceneSlider.setValue(color['color_temp'])
                    self.brightSceneSlider.setValue(color['brightness'])
                else:
                    self.colourSceneSlider.setValue(color['hue'])
                    self.colourTempSceneSlider.setValue(color['saturation'])
                    self.brightSceneSlider.setValue(color['value'])
            elif light_type == 'Light':
                self.colourSceneSlider_Light.setValue(color['color_temp'])
                self.brightSceneSlider_Light.setValue(color['brightness'])
        except IndexError:
            pass

    def set_new_colour_to_editScene(self, light_type:str):
        '''Set current colour to last clicked baseColour button'''
        if light_type == 'RGB Light':
            if self.colourMode.isChecked():
                hue = self.colourSceneSlider.value()
                saturation = self.colourTempSceneBar.value()
                value = self.brightSceneBar.value()
                brightness = 0
                color_temp = 0
            else:
                hue = 0
                saturation = 0
                value = 0
                brightness = self.brightSceneBar.value()
                color_temp = self.colourSceneSlider.value()
        elif light_type == 'Light':
            hue = 0
            saturation = 0
            value = 0
            brightness = self.brightSceneBar_Light.value()
            color_temp = self.colourSceneSlider_Light.value()

        color = {'hue': hue, 'saturation': saturation, 'value': value,
                 'brightness': brightness, 'color_temp': color_temp}

        color_id = int(self.current_baseColour.objectName()[-1])

        if color_id < len(self.current_scene[1]['color_list']):
            self.current_scene[1]['color_list'][color_id] = color
        else:
            self.current_scene[1]['color_list'].append(color)


        stylesheet = self.set_colour(light_type, color)
        self.current_baseColour.setStyleSheet(stylesheet)
        self.current_baseColour.setIcon(QIcon())

    def save_new_Scene_data(self, light_type:str):
        '''Save new Scene data and send to Light'''
        scene_id = self.current_scene[1]['scene_id']

        if light_type == 'RGB Light':
            name = self.nameSceneEdit.text()
            transition_interval = self.speedFlickerSlider.value()
            lightning_duration = self.speedFlickerSlider.value()
            lightning_mode = self.modeColourFlickerBox.currentIndex()
        elif light_type == 'Light':
            name = self.nameSceneEdit_Light.text()
            transition_interval = self.speedFlickerSlider_Light.value()
            lightning_duration = self.speedFlickerSlider_Light.value()
            lightning_mode = self.modeColourFlickerBox_Light.currentIndex()

        color_list = self.current_scene[1]['color_list']

        new_data = hexDec.scene_data(scene_id=scene_id,
                                     transition_interval=transition_interval,
                                     lightning_duration=lightning_duration,
                                     lightning_mode=lightning_mode,
                                     color_list=color_list)
        
        self.current_scene[1]['name'] = name
        self.current_scene[1]['transition_interval'] = transition_interval
        self.current_scene[1]['lightning_duration'] = lightning_duration
        self.current_scene[1]['lightning_mode'] = lightning_mode
        self.current_scene[1]['color_list'] = color_list
        self.current_scene[1]['data'] = new_data

        self.scenes_data[light_type][str(scene_id)] = self.current_scene[1]
        with open('lightScene.json', 'w') as f:
            f.write(json.dumps(self.scenes_data, indent=4))
        self.set_name_and_image_scenes(light_type)
        self.switch_current_scene(light_type, str(scene_id))

    def delete_current_colour(self, light_type:str):
        '''Delete color and shifts the list of color button by one'''
        color_id = int(self.current_baseColour.objectName()[-1])
        self.current_scene[1]['color_list'].pop(color_id)

        if light_type == 'RGB Light':
            colours_list = self.sceneColoursList
            scene_edit = self.colourSceneEdit
        elif light_type == 'Light':
            colours_list = self.sceneColoursList_Light
            scene_edit = self.colourSceneEdit_Light

        color_button_list = colours_list.children()

        for id, color in enumerate(color_button_list[:-2]):
            stylesheet = self.set_colour(light_type, self.current_scene[1]['color_list'][id])
            color.setStyleSheet(stylesheet)

        color_button_list[-2].setStyleSheet('')
        color_button_list[-2].setIcon(QIcon('design/plus.png'))
        
        color_button_list[-1].deleteLater()

        scene_edit.hide()

    @Slot()
    def convert_audio_to_color(self, data):
        '''
        Convert median audio data to color of bulb.
        And send it to device
        '''
        median = int(ar.convert_audio(data, min_range=240, max_range=0))
        color = hexDec.music_data(median)
        self.current_device.send_music_data(color)

    def start_record_audio(self):
        '''
        Create an AudioRecorder object and start recording
        '''
        self.recorder = ar.AudioRecorder()
        self.target_device = self.recorder.get_default_wasapi_device()
        self.sample_size = self.recorder.get_sample_size()
        self.sample_rate = self.target_device['defaultSampleRate']
        self.recorder.start_recording(self.target_device)

    @Slot()
    def record_audio(self):
        '''
        Real-time recording function
        '''
        while True:
            data = self.recorder.stream.read(10240)
            try:
                buffer = np.frombuffer(data, dtype=np.float32)
            except ValueError: # If audio data is none
                buffer = [0.0]
            
            self.threadpool.start(self.convert_audio_to_color(buffer))

            if self.mode.currentIndex() != modes["music"]:
                self.recorder.stop_stream()
                self.recorder.close_stream()
                break


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('design/Comfortaa.ttf')
    window = MainWindow()
    window.show()
    app.exec()
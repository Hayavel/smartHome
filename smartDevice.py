import tinytuya
import json

class Light:
    def __init__(self, id:str, ip:str, local_key:str, ver:float, nowait=True):
        self.id = id
        self.ip = ip
        self.local_key = local_key
        self.ver = ver
        self.nowait = nowait

        self.device = tinytuya.BulbDevice(
            dev_id=self.id,
            address=self.ip,      # Or set to 'Auto' to auto-discover IP address
            local_key=self.local_key, 
            version=self.ver,
            connection_timeout=2,
            connection_retry_limit=1,
            connection_retry_delay=1)

    def get_actual_devices_ip(self):
        devices = tinytuya.deviceScan(maxretry=4)
        if self.ip not in devices:
            for device in devices.values():
                if device['gwId'] == self.id:
                    self.ip = device['ip']
                    with open('devicesList.json', 'r') as f:
                        new = f.read()
                        new = json.loads(new)
                    for n in new.values():
                        if n['id'] == self.id:
                            n['ip'] = self.ip
                            break
                    with open('devicesList.json', 'w') as f:
                        f.write(json.dumps(new, indent=4))
                    break
        self.__init__(self.id, self.ip, self.local_key, self.ver)

    def get_state(self):
        '''Return state of Light'''
        return self.device.state()
    
    def get_status(self):
        '''Return full status of Light'''
        return self.device.status()
    
    def get_brightness(self):
        '''Return brightness value'''
        return self.device.brightness()
    
    def get_colourtemp(self):
        '''Return colourtemp value'''
        return self.device.colourtemp()

    def set_state(self, value:bool):
        '''On or Off Bulb'''
        self.device.set_value(20, value, nowait=self.nowait)

    def set_mode(self, mode:str):
        '''Set white, colour, scene and music mode'''
        self.device.set_mode(mode,nowait=self.nowait)

    def set_brightness(self, value:int):
        self.device.set_brightness_percentage(value, nowait=self.nowait)

    def set_colourTemp(self, value:int):
        self.device.set_colourtemp_percentage(value, nowait=self.nowait)

    def set_scene(self, value:str):
        '''
            Get hexadecimal data:

        Example: 01255002016803E803E800000000

        01: scene_id: 00 to 99
        25: transition_interval: interval between lightning modes(0 to 100)
        50: lightning_duration: 0 to 100
        02: lightning_mode: 0.Static, 1.Jumping, 2.Gradient
        0168: hue: 0 to 360, in hexadecimal 0X0000 to 0X0168
        03E8: saturation: 0 to 1000, in hexadecimal 0X0000 to 0X03E8
        03E8: value: 0 to 1000, in hexadecimal 0X0000 to 0X03E8
        0000: brightness: 0 to 1000, in hexadecimal...
        0000: color_temp: 0 to 1000, in hexadecimal...
        '''
        self.device.set_value(25, value, nowait=self.nowait)

class RGB_Light(Light):

    def get_hsv(self):
        '''Return hsv value'''
        return self.device.colour_hsv()

    def set_hsv(self, h:float, s:float, v:float):
        self.device.set_hsv(h, s, v, nowait=self.nowait)

    def send_music_data(self, value:str):
        '''
            Get hexadecimal data and send without response

        Example: 1007603e803e800120025

        1: indicates modes(0.jumping, 1.gradient)
        0076: indicates hue is 0x0076
        03E8: indicates saturation is 0x03E8
        0012: indicates brightness is 18%
        0025: indicates color temperature is 37%
        '''
        #self.device.set_socketPersistent(True)
        payload = self.device.generate_payload(tinytuya.CONTROL, {'27': value})
        self.device.send(payload)
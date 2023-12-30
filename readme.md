# SmartHome
<img src='https://i.ibb.co/30dppbL/Smart-Device.png'>

## About
Это приложение использует [tinytuya](https://github.com/jasonacox/tinytuya) для управления устройствами умного дома.


Controlling and monitoring Tuya devices on your network requires the following:
* *Address* - Network address (IPv4) of the device e.g. 10.0.1.100
* *Device ID* - Unique identifier for the Tuya device
* *Version* - Tuya protocol version used (3.1, 3.2, 3.3, 3.4 or 3.5)
* *Local_Key* - Security key needed to access the Tuya device.


Для получения данных для подключения устройства используйте [инструкцию](https://github.com/jasonacox/tinytuya#tuya-device-preparation).

## Features
- [ ] RGB Light
    - [X] White mode
    - [X] Color mode
    - [X] Scene mode
    - [ ] Music mode


## Installation
- Download and extract the repository.
- Run the following commands from the extracted repo directory:
```
python.exe -m pip install -r requirements.txt
```
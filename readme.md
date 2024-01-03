# SmartHome
<img src='https://i.ibb.co/MpQfCvZ/image.png'>

## About
This app uses [tinytuya](https://github.com/jasonacox/tinytuya) to control smart home devices.

Controlling and monitoring Tuya devices on your network requires the following:
* *Address* - Network address (IPv4) of the device e.g. 10.0.1.100
* *Device ID* - Unique identifier for the Tuya device
* *Version* - Tuya protocol version used (3.1, 3.2, 3.3, 3.4 or 3.5)
* *Local_Key* - Security key needed to access the Tuya device.


To obtain data to connect the device, use [instructions](https://github.com/jasonacox/tinytuya#tuya-device-preparation).

## Features
- [ ] RGB Light
    - [ ] White mode
    - [ ] Color mode
    - [ ] Scene mode
    - [ ] Music mode
- [ ] Light
    - [ ] White mode
    - [ ] Scene mode

## Installation
- Download and extract the repository.
- Run the following commands from the extracted repo directory:
```
python.exe -m pip install -r requirements.txt
```

P.S Qt designer is used for UI.
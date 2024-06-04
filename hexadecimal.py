
def digit_to_2hex(value):
    result = hex(value)[2:]
    result = '0'*(2-len(result)) + result
    return result

def digit_to_4hex(value):
    result = hex(value)[2:]
    result = '0'*(4-len(result)) + result 
    return result

def hex_to_digit(value:str):
    return int(value, 16)

def scene_data(scene_id:int, transition_interval:int, lightning_duration:int, lightning_mode:int,
               color_list:list=[{'hue':int, 'saturation':int, 'value':int, 'brightness':int, 'color_temp':int}]):
    '''
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

    result_data = digit_to_2hex(scene_id)
    interval_duration_mode = digit_to_2hex(transition_interval) + digit_to_2hex(lightning_duration)\
                             + digit_to_2hex(lightning_mode)

    for i in color_list:
        hue = digit_to_4hex(i['hue'])
        saturation = digit_to_4hex(i['saturation'])
        value = digit_to_4hex(i['value'])
        brightness = digit_to_4hex(i['brightness'])
        color_temp = digit_to_4hex(i['color_temp'])

        result_data += interval_duration_mode + hue + saturation + value + brightness + color_temp
    
    return result_data

def music_data(hue:int, saturation=1000, value=1000, brightness=0, color_temp=0, mode=0):

    '''
    Example: 1016803E803E800000000
    1:    mode: indicates gradient mode (0.Jumping, 1.Gradient)
    0168: hue: 0 to 360, in hexadecimal 0X0000 to 0X0168
    03E8: saturation: 0 to 1000, in hexadecimal 0X0000 to 0X03E8
    03E8: value: 0 to 1000, in hexadecimal 0X0000 to 0X03E8
    0000: brightness: 0 to 1000, in hexadecimal...
    0000: color_temp: 0 to 1000, in hexadecimal...
    '''

    hex_hue = digit_to_4hex(hue)
    hex_saturation = digit_to_4hex(saturation)
    hex_value = digit_to_4hex(value)
    hex_brightness = digit_to_4hex(brightness)
    hex_color_temp = digit_to_4hex(color_temp)

    result_data = str(mode) + hex_hue + hex_saturation + hex_value + hex_brightness + hex_color_temp

    return result_data
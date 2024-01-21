from Smart_Home import Lamp
from Smart_Home import MotionSensor
from Smart_Home import Thermostat
"""Импортирование всех классов и функций для запуска работы программы"""

correct_action = ['lamp', 'temp', 'safe']
request = input('Select your action from the list\n'
                '(lamp, temp, safe): ').lower()
print(f'You have selected a section: {request.upper()}')

if request == 'lamp':
    try:
        lamp = Lamp.LampInTheHome(input('Input shining or darkly: ').lower())
        Lamp.LampInTheHome.lamp_sensor(lamp)
    except ValueError:
        print('Input error! Input shining or darkly:', input())

elif request == 'temp':
    try:
        therm = Thermostat.ThermostatInTheHome(float(input('Enter the room temperature: ')))
    except ValueError:
        print('Input error. The temperature can only be a number!')
        therm = float(input('Enter the format temperature 0.00. '))
        print(f'The temperature of the air conditioner is set {therm}')

elif request == 'safe':
    try:
        motion = MotionSensor.MotionSensorInTheHome(float(input('Input speed: ')),
                                                    input('Are you in the house?\n'
                                                          'Specify:\n'
                                                          '"Yes" - if you are!\n'
                                                          '"No" - if someone else is: ').lower())
        MotionSensor.MotionSensorInTheHome.motion_sensor(motion)
    except ValueError:
        print('Input error! Enter the format speed 0.00', float(input('Input speed: ')))

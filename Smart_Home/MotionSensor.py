class MotionSensorInTheHome:
    """Класс работы датчика движения"""
    not_move = 0

    def __init__(self, move, people):
        """Функция инициализации запуска класса"""
        self.people = people
        self.move = move

    def motion_sensor(self):
        """Функция проверки корректности ввода и вывод результата работы"""
        if self.move > self.not_move:
            if self.people != 'yes':
                print('Send a notification to your phone with a text:\n'
                      ' Strangers have entered your home\n'
                      'Turn on the "Alarm"! and call the police!')

            else:
                print('Turn off the alarm!')

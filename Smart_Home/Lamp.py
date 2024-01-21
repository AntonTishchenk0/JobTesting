class LampInTheHome:
    """Класс работы датчика света"""
    correct_input = ['shining', 'darkly']

    def __init__(self, lighting):
        """Функция инициализации запуска класса"""
        self.lighting = lighting

    def lamp_sensor(self):
        """Функция проверки корректности данных и вывод результата работы"""
        while self.lighting not in self.correct_input:
            print('Incorrect input!')
            self.lighting = input('Input shining or darkly:')

        if self.lighting == 'shining':
            print('Turn off light! The room is bright')

        elif self.lighting == 'darkly':
            print("Turn on light! It's already dark in the room.")

        return self.lighting

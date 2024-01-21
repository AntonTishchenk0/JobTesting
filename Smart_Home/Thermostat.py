class ThermostatInTheHome:
    """Класс работы Термостата"""
    temp_min = 20
    temp_max = 30

    def __init__(self, temp_actual, temp_use=None):
        """Функция инициализации запуска класса"""
        self.set_conditioner(temp_actual, temp_use)
        self.set_radiator(temp_actual, temp_use)
        self.get_cond_rad()
        self.temp_actual = temp_actual
        self.temp_use = temp_use

    def set_conditioner(self, temp_actual, temp_use):
        """Функция проверки корректности ввода данных для кондиционера"""
        self.temp_actual = temp_actual
        self.temp_use = temp_use
        try:
            if self.temp_actual > self.temp_max:
                print('Turn on the air conditioner!')
                self.temp_use = float(input('Enter the temperature of the air conditioner that you want to set. '))
                if self.temp_use < self.temp_min:
                    print(f'You have set the temperature below {self.temp_min}\n'
                          "Are you sure that's what you want?")
                    self.temp_use = input('Click:\n'
                                          '"Yes" - if you want!\n'
                                          '"No" - if you want to change the temperature!\n'
                                          'Input: ').lower()
                    if self.temp_use == 'no':
                        self.temp_use = float(input('Enter the temperature you want to set. '))

        except ValueError:
            print('Input error. The temperature can only be a number!')
            self.temp_use = float(input('Enter the format temperature 0.00. '))

    def set_radiator(self, temp_actual, temp_use):
        """Функция проверки корректности ввода данных для обогревателя"""
        self.temp_actual = temp_actual
        self.temp_use = temp_use
        try:
            if self.temp_actual < self.temp_min:
                print('Turn on the radiator!')
                self.temp_use = float(input('Enter the radiator temperature you want to set. '))
                if self.temp_use > self.temp_max:
                    print(f'You have set the temperature higher {self.temp_max}\n'
                          'Is that exactly what you want?')
                    self.temp_use = input('Click:\n'
                                          '"Yes" - if you want!\n'
                                          '"No" - if you want to change the temperature!\n'
                                          'Input: ').lower()
                    if self.temp_use == 'no':
                        self.temp_use = float(input('Enter the temperature you want to set. '))
        except ValueError:
            print('Input error. The temperature can only be a number!')
            self.temp_use = float(input('Enter the format temperature 0.00. '))

    def get_cond_rad(self):
        """Функция вывода данных"""
        if self.temp_min <= self.temp_actual <= self.temp_max:
            print('The temperature is comfortable!')
        elif self.temp_use != type(str):
            print('The temperature of the air conditioner is set!')

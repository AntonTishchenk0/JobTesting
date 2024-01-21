def get_save(*args):
    """Функция для хранения всех данных"""
    lst = []
    lst.append(args)
    return lst


def summa(first_numb, second_numb):
    """Функция суммы двух чисел"""
    return first_numb + second_numb


def sub(first_numb, second_numb):
    """Функция вычитания двух чисел"""
    return first_numb - second_numb


def multi(first_numb, second_numb):
    """Функция умножения двух чисел"""
    return first_numb * second_numb


def div(first_numb, second_numb):
    """Функция деления двух чисел"""
    return first_numb / second_numb


def calc(first_numb, second_numb, operations):
    """Функция выбора операции между двумя числами"""
    result = None

    if operations == '+':
        result = summa(first_numb, second_numb)

    elif operations == '-':
        result = sub(first_numb, second_numb)

    elif operations == '*':
        result = multi(first_numb, second_numb)

    elif operations == '/':
        if (second_numb == 0):
            print('Division by zero is prohibited!')
            return
        result = div(first_numb, second_numb)
    else:
        print('Incorrect operation!')
    return result


def action_operation():
    """Функция проверки корректности выбора операции"""
    messenge = input('Select an operation: (Input +, -, *, /):\n'
                     '"+" - adding two numbers\n'
                     '"-" - subtracting two numbers\n'
                     '"*" - multiplication of two numbers\n'
                     '"/" - dividing two numbers\n'
                     'Input operation: ')
    if messenge == '+':
        print('You have chosen the amount!')

    elif messenge == '-':
        print('You have chosen subtraction!')

    elif messenge == '*':
        print('You have chosen multiplication!')

    elif messenge == '/':
        print('You have chosen the division!')

    correct_operations = ['+', '-', '*', '/']
    while messenge not in correct_operations:
        print('There is no such operation in the list. Enter the correct sign!')
        messenge = input('Input +, -, * or /')
    return messenge


def run():
    """Функция запуска калькулятора и вывода результата"""
    try:
        first_numb = float(input('Input a first number: '))
    except ValueError:
        first_numb = float(input('You entered incorrect data. Please enter an integer: '))

    try:
        second_numb = float(input('Input a second number: '))
    except ValueError:
        second_numb = float(input('You entered incorrect data. Please enter an integer: '))

    op = action_operation()
    result = calc(first_numb, second_numb, op)
    x = get_save(first_numb, op, second_numb, '=', result)
    print(f'Recent actions: {x}')
    print(f'Your result: {result}')


program_is_running = True
while (program_is_running):
    run()
    answer = input('Would you like to continue?\n'
                   'Input + if "Yes" or other symbol, if "No": ')
    if answer != '+':
        program_is_running = False

from math import sqrt

print('Добро пожаловать в самую лучшую программу для вычисления '
      'квадратного корня из заданного числа.')


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Проверяет положительное ли число."""
    if your_number > 0:
        result = calculate_square_root(your_number)
        print('Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {result}')
    return 'Невозможно извлечь корень '


calc(25.5)

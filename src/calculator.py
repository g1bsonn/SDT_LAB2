"""
Калькулятор
"""
def add(x: float, y: float) -> float:
    """Возвращает сумму двух чисел."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Возвращает разность двух чисел."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Возвращает произведение двух чисел."""
    return x * y

def divide(x: float, y: float) -> float:
    """Возвращает частное двух чисел."""
    if y == 0:
        raise ValueError("Деление на ноль недопустимо!")
    return x / y

def power(n: float, m: float) -> float:
    """Возвращает n в степени m."""
    return n ** m

def factorial(n: int) -> int:
    """Возвращает факториал числа n."""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
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

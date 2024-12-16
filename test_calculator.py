"""
Модуль для тестирования калькулятора.
"""
import pytest
from calculator import add, subtract, multiply, divide, power, factorial

def test_add():
    """Получение суммы"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4  # Тест с плавающей запятой
    assert add(-1.5, -2.5) == -4  # Тест с отрицательными числами с плавающей запятой

def test_subtract():
    """Получение суммы"""
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1
    assert subtract(1, 1) == 0
    assert subtract(1.5, 0.5) == 1  # Тест с плавающей запятой
    assert subtract(-1.5, -0.5) == -1  # Тест с отрицательными числами с плавающей запятой

def test_multiply():
    """Получение суммы"""
    assert multiply(3, 2) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
    assert multiply(1.5, 2) == 3  # Тест с плавающей запятой
    assert multiply(-1.5, -2) == 3  # Тест с отрицательными числами с плавающей запятой

def test_divide():
    """Получение суммы"""
    assert divide(6, 2) == 3
    assert divide(-1, 1) == -1
    assert divide(1.5, 0.5) == 3  # Тест с плавающей запятой
    assert divide(-1.5, -0.5) == 3  # Тест с отрицательными числами с плавающей запятой

def test_divide_by_zero():
    """Получение суммы"""
    with pytest.raises(ValueError):
        divide(10, 0)
    with pytest.raises(ValueError):
        divide(-10, 0)  # Тест с отрицательным числом

def test_power():
    """Получение суммы"""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-3, 3) == -27
    assert power(2, -2) == 0.25  # Тест с отрицательной степенью
    assert power(2, 0.5) == 1.4142135623730951  # Тест с дробной степенью

def test_factorial():
    """Получение суммы"""
    assert factorial(5) == 120  # тест для значения 5
    assert factorial(0) == 1  # тест для значения 0
    assert factorial(1) == 1  # тест для значения 1
    assert factorial(3) == 6  # Дополнительный тест для значения 3

    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-5)  # Тест с другим отрицательным числом


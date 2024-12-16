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


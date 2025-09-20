# exemplo.py

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números. Retorna None se b for zero."""
    if b == 0:
        return None
    return a / b

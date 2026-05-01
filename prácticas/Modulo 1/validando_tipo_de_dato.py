""" 

Escribe una función llamada describir_variable que reciba un valor e imprima lo siguiente:

Valor: 42
Tipo: <class 'int'>
¿Es numérico?: Sí

Requisitos:

Requisitos — solo con lo que ya sabemos:

Usa type() para mostrar el tipo
Detecta si es int o float con type() ==  y operadores lógicos
Pruébala con 4 valores: un int, un float, un str y un bool

"""

def describir_variable(valor):
    if type(valor) == int or type(valor) == float:    
        print(f"{valor}\nSí, es un valor númerico tipo:")
        print(type(valor))
    else:
        print(f"{valor}\nNo es un valor númerico es un tipo:")
        print(type(valor))

valor: int = 42
describir_variable(valor)

valor: float = 3.14
describir_variable(valor)

valor: str = "miondator"
describir_variable(valor)

valor: bool = False
describir_variable(valor)
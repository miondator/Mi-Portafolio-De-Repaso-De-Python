"""

Completa la función. Pruébala con una lista con valores y con una lista vacía. Imprime el resultado y su tipo en ambos casos.

def buscar_mayor(lista):
    # Si la lista está vacía, retorna None
    # Si no, retorna el mayor elemento
    pass

"""

# lista = []
# lista = ["dos", 5, True, 3.14, None, -10, 'doce']  No es posible buscar números de forma directa entre diferentes tipos de datos, así que esta lista retornaría un error
lista = [2, -7, 10, .101, -1000, 6, 10.1]

def buscar_mayor(lista):

    if len(lista) > 0: # Si al comparar tiene más de 0 retorna el mayor elemento
        return f'El mayor elemento dentro de la lista es: {max(lista)}'

    else: # Si la lista está vacía, retorna None
        return None

print(buscar_mayor(lista))
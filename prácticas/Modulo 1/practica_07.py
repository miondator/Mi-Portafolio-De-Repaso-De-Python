"""

Usando solo funciones built-in, imprime:

Cuántos elementos tiene la lista
El mayor y el menor
La suma total
El valor absoluto del menor
La lista ordenada de menor a mayor

"""

numeros = [4, -7, 2, -1, 9, 3, -5]

print(f'Cantidad de números en lista: {len(numeros)}')
print(f'Número mayor: {max(numeros)}\nNúmero menor: {min(numeros)}')
print(f'La suma de todos los números es igual a: {sum(numeros)}')
print(f'El absoluto del número menor ({min(numeros)}) es: {abs(min(numeros))}')
print(f'Estos son los números almacenados en la lista (sin ordenar): {numeros}\nY esta es la lista de números ya ordenada: {sorted(numeros)}')
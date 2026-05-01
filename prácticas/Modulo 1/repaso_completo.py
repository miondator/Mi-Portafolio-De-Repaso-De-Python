"""

Crea un programa que:

Declare 5 variables de tipos distintos (incluyendo None)
Las guarde en una sola línea de asignación múltiple
Use round, abs, len, max, min al menos una vez cada una
Imprima todo con f-strings bien formateados

"""

texto, numero, buleano, vacio, flotante = "Palabra", -23, True, None, 3.14

print(f'Estoy imprimiendo la variable texto que contiene lo siguiente: {texto}\nY la variable texto se le está aplicando el built-in len por lo tanto la longitud de lo que contiene la variable texto es: {len(texto)}\n')

print(f'Estoy imprimiendo la variable buleano que contiene lo siguiente: {buleano}\nY la variable buleano se le está aplicando el built-in abs por lo tanto el absoluto de esta variable al ser un buleano puede ser considerado como 0 y 1 siendo False y True respectivamente por lo tanto al aplicar abs obtenemos: {abs(buleano)}\n')

print(f'En este caso estoy imprimiendo un flotante ({flotante}) y le estoy aplicando un built-in de round por lo que al redondear ese valor el resultado es: {round(flotante)}\n')

print(f'En este caso estoy aplicando el built-in max a varias variables, siendo la variable texto ({texto}, a la cual para poder comparar estoy usando el built-in len para que pase como un número que sería {len(texto)}), numero ({numero}) y flotante ({flotante}), siendo entonces que el valor máximo entre los 3 es: {max(len(texto), numero, flotante)}\n')

print(f'Aquí al igual que lo anterior estoy usando las mismas variables y el built-in len para la variable texto pero ahora mostraré el de valor menor de todos el cual es: {min(len(texto), numero, flotante)}\n')

print(f'A la variable vacio que contene "{vacio}" no es posible aplicarle algún built-in')
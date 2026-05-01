# Desempaqueta esa tupla en 4 variables en una sola línea, y luego imprime cada valor junto a su tipo con este formato:
#     nombre  → Rafa   | tipo: <class 'str'>
#     edad    → 22     | tipo: <class 'int'>
#     ...

# Asignación múltiple y type(). Dado esto:
datos = ("Rafa", 22, 1.87, True)

nombre, edad, estatura, estudiante = datos # Datos asignado a cada variable

# Impresión de datos
print(f'Nombre -> {nombre} | Tipo {type(nombre)}')
print(f'Edad -> {edad} | Tipo {type(edad)}')
print(f'Estatura -> {estatura} | Tipo {type(estatura)}')
print(f'Estudiante activo -> {estudiante} | Tipo {type(estudiante)}')

# Declara las siguientes variables con los valores y tipos correctos:

# Tu nombre
# Tu edad
# Tu altura en metros
# Si estás estudiando actualmente (True o False)
# Tu lenguaje favorito

# Luego imprime una sola línea con toda esa info usando un f-string, con este formato exacto:

#   Hola, soy [nombre], tengo [edad] años, mido [altura]m, estudio: [True/False]. Mi lenguaje favorito es [lenguaje].

# Y por último, imprime el tipo de dato de cada variable usando type().

# Declaración de variables
nombre = "Rafa Gonzalez"
edad = 22
altura = 1.87
estudiante = True
lenguaje_favorito = "Python"

print(f'Hola soy {nombre}, tengo {edad} años, mido {altura}m, estudio: {estudiante}. Mi lenguaje favorito es {lenguaje_favorito}.')

# Imprimir el tipo de dato de cada variable
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(estudiante))
print(type(lenguaje_favorito))
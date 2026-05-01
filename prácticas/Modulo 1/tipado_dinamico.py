""" 

Después de cada reasignación imprime el valor y su tipo. Luego responde en un comentario: ¿qué ventaja y qué riesgo tiene el tipado dinámico?

x = 10
x = "ahora soy texto"
x = 3.14
x = True
x = None

"""

x = 10
print(f'El valor de x es: "{x}" y es de tipo: {type(x)}')

x = "ahora soy texto"
print(f'El nuevo valor de x es: "{x}" y es de tipo:{type(x)}')

x = 3.14
print(f'El nuevo valor de x es: "{x}" y es de tipo:{type(x)}')

x = True
print(f'El nuevo valor de x es: "{x}" y es de tipo:{type(x)}')

x = None
print(f'El nuevo valor de x es: "{x}" y es de tipo:{type(x)}')

# La ventaja que yo le veo es que puedes mutar el valor de una variable según tu convenencia pero tambien ahí está el gran problema que pueda que al estar intercambiando el tipo de dato pierdas la noción de que dato estás manipulando después de varios cambios y esto es un problema por ejemplo cuando por ejemplo en una condicional o en una función esperas  recibir un tipo de dato especifico pero recibes algo completamente distito, por ejemplo si en una comparación deseas comparar números pero de un lado tienes el número que quieres comparar pero en tu variable tienes un string habrá un error porque son tipo de datos completamente distintos
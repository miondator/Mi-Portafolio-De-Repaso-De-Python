""" 
Encuentra y corrige todos los errores de este código. Hay varios. No los ejecutes todavía — primero identifícalos leyendo:

1variable = "Python"
Lenguaje = "javascript"
for = 5
mensaje = 'Hola" + lenguaje
print(Mensaje)

"""

# 1variable = "Python" El error está en que se está declarando una variable con un número de manera inicial y esto en Python es completamente incorrecto
variable = "Python"

# Lenguaje = "javascript" Aquí realmente no hay ningún error, solo como buena práctica es recomendable comenzar con una minúscula e ir separando por mayúsculas las palabras si son varias o por guíones bajos

lenguaje = "javascript"

# for = 5 El error se encuentra en la declaracion, como en todos los lenguajes existen palabras reservadas, palabras que ejecutan ciertas acciones o cumplen con una función dentro del lenguaje, pues bien, en el caso de Python la palabra "for" es una palabra reservada para ejecutar bucles, por lo tanto es una palabra que imposible utilizar para declarar

numero = 5 # Cambio la variable for por otra palabra que haga sentido a lo que quiero almacenar en este caso un número y la palabra número al no ser una palabra reservada es posible utilizarla

# mensaje = 'Hola" + lenguaje Aquí el error está en las comillas, cuando quieres almacenar un dato tipo string debes escribir tu texto entre comillas pero ojo, pueden ser comillas simples o comillas dobles pero nunca una y una como es este caso, lo correcto sería lo siguiente

mensaje = "Hola" + lenguaje # Solo como dato extra anteriormente como cambié la variable Lenguaje a lenguaje (la pasé a minúsculas) la mandé a llamar de la nueva manera en que la declaré

# print(Mensaje) Aquí en teoría no habría error pero como esta función está tratando de imprimir una variable que definimos anteriormente el error está en que se está mandando a llamar con una mayúscula al inicio comvirtiendola en una variable completamente diferente a la que nosotros declaramos anteriormente por lo tanto el resultado correcto sería el siguiente

print(mensaje)

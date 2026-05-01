# Ahora trabajamos el scope. Predice qué imprimirá este código antes de ejecutarlo, y luego explica por qué:
x = "global"

def funcion():
    x = "local"
    print(x)

funcion()
print(x)

#Respuesta al acertijo
"""
Este fragmento de código imprimirá dos resultados, "local" y "global", exactamente en ese orden pero, porque?

Pues bien esto sucede por una razón y es que si bien se declara primero x = "global" la realidad es que quien se manda a llamar primero es a la función llamada "funcion" por lo tanto primero se ejecutará lo que se hay dentro de esa función y algo a resaltar de porque se imprimen dos valores es lo siguiente, aquí se declara x en dos ocaciones, pero veamos más de cerca y podremos notar que x = "global" se declara en un entorno global, es decir, está fuera de cualquier función, clase u algoritmo pero la segunda vez que se declara x = "local" lo hace dentro de "funcion" es decir, está en el scope de esa función declarada, así que cuando se ejecuta funcion() y print(x) primero ejecuta lo que hay dentro de funcion y que hay dentro? Pues hay una variable que contiene un dato tipo string, la palabra local, y una orden de imprimir esa variable, después de esto está la orden de imprimir x pero esto ya fuera de la función y x fuera de la función tiene el valor de "global" por lo tanto imprimirá "global" en lugar de "local". 
Por lo tanto lo que se imprimirá al ejecutar ese pequeño fragmento de código será 
# local
# global  
"""

# Y ahora esta variante:

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()
print(contador)

"""
El resultado impreso será 3, porque el código declara que contador empieza con un valor de 0 pero al ejecutar 3 veces la función incrementar pasa lo siguiente, al iniciarla una vez la función incrementar primeramente declara como una variable global a la variable contador así que lo que pase dentro de la función incrementar afectará a la variable contador sin importar en que parte del código se encuentre, ahora, después de haber declarado a la variable contador como global pasa a la siguiente linea de código y de dice, que a contrador se le sumará el valor 1, es decir, ahora la variable contador es igual a 1 (contador = 1), termina de ejecutarse la función incrementar al ya no haber más lineas dentro de la función y regresa a la linea de código donde se manda a llamar a la función incrementar (en mi caso es la linea 29) y aquí está lo importarte y es algo que olvidé mencionar en el ejercicio anterior, el interprete de python recorre tu código de forma descendente, es decir, lee tu código de arriba hacía abajo, o sea que en este caso el interpretede python al haber leido ya la linea 29 que en mi caso manda a llamar a la función incrementar y al haber concluido con lo que había dentro de esa función regresa a la linea de código en donde había quedado previamente que sería la 29 y pasa a la siguiente que es la 30 y oh sorpresa nuevamente se está mandando a llamar a la función incrementar, es decir, volverá a ejecutarse lo que hay dentro de esa función por lo tanto a la variable contador se le volverá a sumar +1 así que ahora la variable contador pasará a almacenar el valor 2 (contador = 2), vuelve a terminar de ejecutar la función y regresa a la linea de código 30 y pasa a la 31 que sucede lo mismo llama a incrementar así que contador es igual a 3 y finalmente está la orden print(contador) y que pasa aquí? esto es diferente al ejemplo anterior, si bien aquí contador se declara en dos ocaciones igual que en el ejemplo anterior se declaraba x en dos ocaciones ahora la cosa es diferente porque lo primero que pensarías es que print(contador) mostrará como resultado 0 porque eso se declara en un inicio pero aquí está el truco, antes del print se ejecuta como ya lo dije 3 veces la función incrementar y que sucede dentro de esta función? Exacto, declara a la variable contador que está dentro de incrementar y lo que pase dentro de incrementar afectará a la variable contador en cualquier parte del código y como se estuvo ejecutando 3 veces que a contador se le sume +1 entonces 3 veces +1 es igual a 3 por lo tanto contador sería igual a 3 y al ejecutar la orden print(contador) el valor es 3 
"""
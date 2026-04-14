# 🐍 Módulo 02 — Sintaxis Básica y Variables

> 📖 Referencia: [ellibrodepython.com/sintaxis-python](https://ellibrodepython.com/sintaxis-python) | [ellibrodepython.com/variables-python](https://ellibrodepython.com/variables-python)

---

## 1. Sintaxis Básica

Python se diferencia de la mayoría de lenguajes por usar **indentación** (espacios) en lugar
de llaves `{}` para definir bloques de código. Esto obliga a que el código sea visualmente limpio.

```python
# ✅ Correcto — 4 espacios de indentación
if True:
    print("Este bloque está bien indentado")
    print("Esta línea también pertenece al if")

print("Esta línea ya está fuera del if")
```

```python
# ❌ Error — mezclar tabs y espacios causa IndentationError
if True:
    print("ok")
  print("esto rompe Python")  # IndentationError!
```

### Comentarios

```python
# Esto es un comentario de una línea

"""
Esto es un comentario
de múltiples líneas
(técnicamente es un string sin asignar)
"""

x = 5  # Comentario al final de una línea
```

### El punto y coma `;` es opcional (y no Pythónico)

```python
# ❌ Funciona pero no es Pythónico
x = 5; y = 10; print(x + y)

# ✅ Pythónico
x = 5
y = 10
print(x + y)
```

---

## 2. Variables

En Python **no declaras el tipo** de una variable. Python lo infiere automáticamente.

```python
nombre = "Ana"        # str
edad = 25             # int
altura = 1.68         # float
es_estudiante = True  # bool
```

### Reglas para nombrar variables

| Regla | Ejemplo válido | Ejemplo inválido |
|-------|---------------|-----------------|
| Solo letras, números y `_` | `mi_variable` | `mi-variable` ❌ |
| No puede empezar con número | `variable1` | `1variable` ❌ |
| Sensible a mayúsculas | `edad` ≠ `Edad` ≠ `EDAD` | — |
| No puede ser palabra reservada | — | `for = 5` ❌ |

### Convenciones de nombres (PEP8)

```python
# Variables y funciones → snake_case
nombre_completo = "Ana García"
precio_con_iva = 121.0

# Constantes → MAYÚSCULAS
PI = 3.14159
MAX_INTENTOS = 3

# Clases → PascalCase
class MiClase:
    pass

# "Privado" (convención) → guión bajo al inicio
_variable_interna = 42

# "Muy privado" → doble guión bajo
__variable_muy_interna = 99
```

---

## 3. Tipos de datos básicos

```python
# int — números enteros
x = 10
y = -5
z = 1_000_000  # Los guiones bajos ayudan a leer números grandes

# float — números decimales
pi = 3.14159
temperatura = -2.5
notacion_cientifica = 1.5e10  # 15000000000.0

# str — cadenas de texto
nombre = "Python"
frase = 'También puedes usar comillas simples'
multilinea = """
Esto es un texto
de múltiples líneas
"""

# bool — booleano
activo = True
eliminado = False

# NoneType — ausencia de valor
resultado = None
```

### Saber el tipo de una variable

```python
x = 42
print(type(x))        # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hola"))   # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
```

---

## 4. Asignación múltiple

```python
# Varias variables en una línea
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Mismo valor a múltiples variables
a = b = c = 0
print(a, b, c)  # 0 0 0

# Intercambiar valores (¡sin variable temporal!)
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10  ← pythónico y elegante
```

---

## 5. Alcance de variables (Scope)

El **scope** define dónde una variable es accesible.

```python
# Variable GLOBAL — accesible en todo el módulo
mensaje = "Hola desde el global"

def mi_funcion():
    # Variable LOCAL — solo existe dentro de la función
    mensaje_local = "Hola desde la función"
    print(mensaje)        # ✅ Puede acceder al global
    print(mensaje_local)  # ✅ Puede acceder al local

mi_funcion()
print(mensaje)        # ✅ Funciona
print(mensaje_local)  # ❌ NameError — no existe aquí
```

### La palabra clave `global`

```python
contador = 0

def incrementar():
    global contador  # Avisa que vamos a modificar la variable global
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

> ⚠️ **Evita usar `global` cuando sea posible.** Hace el código difícil de mantener.
> Mejor pasa valores como parámetros y retorna resultados.

---

## 6. Tipado dinámico

Python es **dinámicamente tipado**: una variable puede cambiar de tipo.

```python
x = 10
print(type(x))  # <class 'int'>

x = "ahora soy un string"
print(type(x))  # <class 'str'>

x = [1, 2, 3]
print(type(x))  # <class 'list'>
```

### Type Hints (anotaciones de tipo)

Desde Python 3.5 puedes **anotar tipos** para mayor claridad (no son obligatorias):

```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"

edad: int = 25
precios: list[float] = [9.99, 14.99, 4.99]
```

---

## 7. Funciones built-in esenciales

Python incluye funciones disponibles sin importar nada:

```python
print("Hola")              # Imprimir en pantalla
len("Python")              # 6 — longitud
type(42)                   # <class 'int'>
int("10")                  # 10 — convertir a entero
float("3.14")              # 3.14 — convertir a float
str(100)                   # "100" — convertir a string
bool(0)                    # False
input("¿Tu nombre? ")      # Leer del teclado
range(5)                   # 0, 1, 2, 3, 4
abs(-7)                    # 7 — valor absoluto
round(3.14159, 2)          # 3.14
max(1, 5, 3)               # 5
min(1, 5, 3)               # 1
sum([1, 2, 3, 4])          # 10
sorted([3, 1, 2])          # [1, 2, 3]
```

---

## ⚠️ Errores comunes

```python
# Error 1: Usar variable antes de definirla
print(nombre)  # NameError: name 'nombre' is not defined
nombre = "Ana"

# Error 2: Case sensitivity
Nombre = "Ana"
print(nombre)  # NameError — 'nombre' != 'Nombre'

# Error 3: Palabras reservadas como nombres
for = 5    # SyntaxError
class = 1  # SyntaxError
```

---

## 📋 Resumen

| Concepto | Clave |
|----------|-------|
| Indentación | 4 espacios, no tabs |
| Variables | Sin declaración de tipo |
| Nombrado | snake_case para variables/funciones |
| Tipado | Dinámico (puede cambiar) |
| Scope | Local dentro de funciones, global fuera |
| Type hints | Opcionales pero recomendados |

---

*Módulo 02 — Sintaxis y Variables | Curso Intensivo de Repaso Python*

# ============================================================
# PYTHON - VARIABLES, TIPOS Y OPERACIONES BÁSICAS
# 5TO AÑO - PROGRAMACIÓN
# Duración estimada: 80 minutos
# ============================================================
#
# En esta clase vamos a aprender:
#
# 1. Variables
# 2. Tipos de datos
# 3. Función type()
# 4. Modificación de variables
# 5. Operaciones matemáticas
# 6. División entera y resto
# 7. Potencias
# 8. Operaciones combinadas
# 9. Función input()
# 10. Conversión de tipos
# 11. Ejemplo práctico
# 12. Calculadora básica
# 13. Actividad integradora
#
# IMPORTANTE:
# Ejecutar cada sección por separado para poder observar
# qué hace cada parte del código.
# ============================================================


# ============================================================
# SECCIÓN 1 - VARIABLES
# ============================================================

# Una variable es un espacio donde podemos guardar información.
#
# Para crear una variable utilizamos:
#
# nombre_variable = valor
#
# En este ejemplo guardamos un nombre.

nombre = "Lautaro"

# Guardamos un número entero en una variable.

edad = 17

# Guardamos un número decimal.

altura = 1.75

# Mostramos el contenido de las variables.

print(nombre)
print(edad)
print(altura)


# ============================================================
# SECCIÓN 2 - TIPOS DE DATOS
# ============================================================

# Python permite trabajar con diferentes tipos de datos.
#
# Los principales tipos que vamos a utilizar son:
#
# str   -> texto
# int   -> número entero
# float -> número decimal
# bool  -> verdadero o falso


# STR
# Un string representa un texto.
# Los textos se escriben entre comillas.

nombre = "Lautaro"

# INT
# Un integer representa un número entero.

edad = 17

# FLOAT
# Un float representa un número decimal.

altura = 1.75

# BOOL
# Un boolean solamente puede tener dos valores:
#
# True  -> verdadero
# False -> falso

es_estudiante = True


# Mostramos todos los valores.

print(nombre)
print(edad)
print(altura)
print(es_estudiante)


# ============================================================
# SECCIÓN 3 - CONOCER EL TIPO DE UNA VARIABLE
# ============================================================

# La función type() nos permite conocer
# qué tipo de dato contiene una variable.

nombre = "Lautaro"
edad = 17
altura = 1.75
es_estudiante = True


# Mostramos el tipo de cada variable.

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))


# El resultado será parecido a:
#
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>


# ============================================================
# SECCIÓN 4 - LAS VARIABLES PUEDEN CAMBIAR
# ============================================================

# Una característica importante de las variables
# es que podemos cambiar su contenido.

puntos = 10

# Mostramos el valor inicial.

print("Puntos iniciales:", puntos)


# Modificamos el valor de la variable.

puntos = 20

print("Después de modificar:", puntos)


# Volvemos a modificarla.

puntos = 50

print("Valor final:", puntos)


# La variable "puntos" fue cambiando:
#
# 10
# 20
# 50
#
# El último valor asignado es el que queda guardado.


# ============================================================
# SECCIÓN 5 - OPERACIONES MATEMÁTICAS BÁSICAS
# ============================================================

# Python permite realizar operaciones matemáticas
# utilizando diferentes operadores.


numero1 = 10
numero2 = 5


# SUMA
# Utilizamos el operador +

suma = numero1 + numero2


# RESTA
# Utilizamos el operador -

resta = numero1 - numero2


# MULTIPLICACIÓN
# Utilizamos el operador *

multiplicacion = numero1 * numero2


# DIVISIÓN
# Utilizamos el operador /

division = numero1 / numero2


# Mostramos los resultados.

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


# Los operadores básicos son:
#
# +  -> suma
# -  -> resta
# *  -> multiplicación
# /  -> división


# ============================================================
# SECCIÓN 6 - DIVISIÓN ENTERA
# ============================================================

# El operador // realiza una división entera.
#
# Es decir, elimina la parte decimal del resultado.

numero1 = 17
numero2 = 5

division_normal = numero1 / numero2

division_entera = numero1 // numero2


print("División normal:", division_normal)
print("División entera:", division_entera)


# 17 / 5 = 3.4
#
# 17 // 5 = 3


# ============================================================
# SECCIÓN 7 - RESTO DE UNA DIVISIÓN
# ============================================================

# El operador % permite obtener el resto
# de una división.

numero1 = 17
numero2 = 5

resto = numero1 % numero2

print("Resto:", resto)


# 17 dividido 5 da como resultado 3
# y sobra 2.
#
# Por eso:
#
# 17 % 5 = 2


# Un ejemplo de la vida cotidiana:
#
# Tenemos 17 caramelos y queremos repartirlos
# entre 5 personas.
#
# Cada persona recibe 3 caramelos.
# Sobran 2 caramelos.

caramelos = 17
personas = 5

caramelos_por_persona = caramelos // personas
caramelos_sobrantes = caramelos % personas

print("Caramelos por persona:", caramelos_por_persona)
print("Caramelos sobrantes:", caramelos_sobrantes)


# ============================================================
# SECCIÓN 8 - POTENCIAS
# ============================================================

# Para realizar una potencia utilizamos **
#
# número ** exponente

numero = 5

resultado = numero ** 2

print("5 elevado al cuadrado:", resultado)


# Otro ejemplo:

base = 2
exponente = 3

resultado = base ** exponente

print("Resultado:", resultado)


# 2 ** 3 significa:
#
# 2 x 2 x 2 = 8


# ============================================================
# SECCIÓN 9 - TODAS LAS OPERACIONES
# ============================================================

# Vamos a utilizar dos números
# y realizar diferentes operaciones.

numero1 = 20
numero2 = 6

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** numero2


print("Número 1:", numero1)
print("Número 2:", numero2)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Resto:", resto)
print("Potencia:", potencia)


# ============================================================
# SECCIÓN 10 - OPERACIONES COMBINADAS
# ============================================================

# Python respeta el orden de las operaciones matemáticas.

resultado = 10 + 5 * 2

print("Resultado:", resultado)


# Primero se realiza la multiplicación:
#
# 5 * 2 = 10
#
# Después:
#
# 10 + 10 = 20


# Podemos utilizar paréntesis para cambiar el orden.

resultado = (10 + 5) * 2

print("Resultado con paréntesis:", resultado)


# En este caso:
#
# Primero:
# 10 + 5 = 15
#
# Después:
# 15 * 2 = 30


# ============================================================
# SECCIÓN 11 - VARIABLES Y OPERACIONES
# ============================================================

# Podemos utilizar variables para resolver
# problemas de la vida cotidiana.


# Precio de un producto.

precio = 1000

# Cantidad de productos.

cantidad = 3

# Calculamos el precio total.

total = precio * cantidad

print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", total)


# ============================================================
# SECCIÓN 12 - CALCULAR UN DESCUENTO
# ============================================================

# Ahora vamos a utilizar variables
# y operaciones para calcular un descuento.


precio = 1000
cantidad = 3

# Primero calculamos el precio total.

total = precio * cantidad


# Calculamos el 10% de descuento.

descuento = total * 0.10


# Restamos el descuento al precio total.

precio_final = total - descuento


print("Total:", total)
print("Descuento:", descuento)
print("Precio final:", precio_final)


# ============================================================
# SECCIÓN 13 - INPUT()
# ============================================================

# Hasta ahora nosotros escribimos los datos
# directamente dentro del programa.
#
# Con input() podemos pedirle información
# al usuario mientras el programa está funcionando.


nombre = input("Ingresá tu nombre: ")

print("Hola", nombre)


# Cuando ejecutamos el programa,
# aparecerá algo parecido a:
#
# Ingresá tu nombre:
#
# El usuario puede escribir:
#
# Lautaro
#
# Y el programa mostrará:
#
# Hola Lautaro


# ============================================================
# SECCIÓN 14 - INPUT() Y TIPOS DE DATOS
# ============================================================

# Es importante saber que input()
# siempre devuelve un texto (str).
#
# Aunque el usuario escriba un número,
# Python lo recibe inicialmente como texto.


edad = input("Ingresá tu edad: ")

print("Tu edad es:", edad)

print("Tipo de dato:", type(edad))


# Si ingresamos:
#
# 17
#
# Python lo considera:
#
# <class 'str'>


# ============================================================
# SECCIÓN 15 - CONVERTIR TEXTO A ENTERO
# ============================================================

# Para transformar un texto en un número entero
# utilizamos int().


edad = input("Ingresá tu edad: ")

# Convertimos el texto en número entero.

edad = int(edad)


# Ahora podemos realizar operaciones matemáticas.

edad_futura = edad + 5

print("Dentro de 5 años tendrás:", edad_futura)


# ============================================================
# SECCIÓN 16 - CONVERSIÓN DIRECTA CON INT()
# ============================================================

# Podemos simplificar el código
# haciendo la conversión directamente.


edad = int(input("Ingresá tu edad: "))

edad_futura = edad + 5

print("Dentro de 5 años tendrás:", edad_futura)


# ============================================================
# SECCIÓN 17 - CONVERTIR A FLOAT
# ============================================================

# Si necesitamos ingresar un número decimal,
# podemos utilizar float().


altura = float(input("Ingresá tu altura en metros: "))

print("Tu altura es:", altura)

print("Tipo de dato:", type(altura))


# Por ejemplo:
#
# 1.75
#
# será almacenado como:
#
# float


# ============================================================
# SECCIÓN 18 - CONVERSIÓN ENTRE TIPOS
# ============================================================

# También podemos convertir datos
# de un tipo a otro.


numero = 10

# Convertimos int a float.

numero_decimal = float(numero)

print(numero_decimal)
print(type(numero_decimal))


# También podemos convertir un número
# en un texto utilizando str().

edad = 17

edad_texto = str(edad)

print(edad_texto)
print(type(edad_texto))


# ============================================================
# SECCIÓN 19 - CALCULADORA BÁSICA
# ============================================================

# Ahora vamos a utilizar todo lo aprendido
# para crear una calculadora sencilla.


# Pedimos el primer número.

numero1 = float(input("Ingresá el primer número: "))


# Pedimos el segundo número.

numero2 = float(input("Ingresá el segundo número: "))


# Realizamos la suma.

suma = numero1 + numero2


# Realizamos la resta.

resta = numero1 - numero2


# Realizamos la multiplicación.

multiplicacion = numero1 * numero2


# Realizamos la división.

division = numero1 / numero2


# Mostramos los resultados.

print()
print("========== RESULTADOS ==========")

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("================================")


# ============================================================
# SECCIÓN 20 - CALCULADORA AVANZADA
# ============================================================

# Vamos a agregar dos operaciones más:
#
# Potencia
# Resto


numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 ** numero2
resto = numero1 % numero2


print()
print("========== CALCULADORA ==========")

print("Número 1:", numero1)
print("Número 2:", numero2)

print("-------------------------------")

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)
print("Resto:", resto)

print("================================")


# ============================================================
# SECCIÓN 21 - EJEMPLO INTEGRADOR
# DATOS PERSONALES
# ============================================================

# Vamos a crear un programa que solicite
# diferentes datos al usuario.


# Pedimos el nombre.

nombre = input("Ingresá tu nombre: ")


# Pedimos la edad.

edad = int(input("Ingresá tu edad: "))


# Pedimos la altura.

altura = float(input("Ingresá tu altura en metros: "))


# Pedimos el año de nacimiento.

anio_nacimiento = int(input("Ingresá tu año de nacimiento: "))


# Calculamos el año en el que cumplirá 30 años.

anio_30 = anio_nacimiento + 30


# Mostramos todos los datos.

print()
print("========== DATOS PERSONALES ==========")

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Año de nacimiento:", anio_nacimiento)

print("======================================")


# Mostramos el resultado del cálculo.

print()
print("Cumplirás 30 años aproximadamente en:", anio_30)


# También podemos consultar
# qué tipo de dato tiene cada variable.

print()
print("========== TIPOS DE DATOS ==========")

print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de altura:", type(altura))
print("Tipo de año de nacimiento:", type(anio_nacimiento))

print("====================================")


# ============================================================
# SECCIÓN 22 - ACTIVIDAD PARA LOS ALUMNOS
# ============================================================

# Crear un programa llamado:
#
# actividad_variables.py
#
# El programa debe:
#
# 1. Pedir el nombre del alumno.
# 2. Pedir su edad.
# 3. Pedir su altura.
# 4. Pedir dos números.
# 5. Calcular:
#       - suma
#       - resta
#       - multiplicación
#       - división
#       - potencia
#       - resto
# 6. Mostrar todos los resultados.
# 7. Mostrar el tipo de dato de cada variable.
#
# IMPORTANTE:
#
# Intentá resolverlo sin copiar las soluciones
# de las secciones anteriores.


# ============================================================
# SECCIÓN 23 - DESAFÍO
# ============================================================

# Crear un programa que simule una compra.
#
# El programa debe pedir:
#
# - Nombre del producto
# - Precio del producto
# - Cantidad
# - Porcentaje de descuento
#
# Luego debe calcular:
#
# 1. Precio total sin descuento.
# 2. Valor del descuento.
# 3. Precio final.
#
# Ejemplo:
#
# Producto: Remera
# Precio: 15000
# Cantidad: 2
# Descuento: 10
#
# Resultado esperado:
#
# Total: 30000
# Descuento: 3000
# Precio final: 27000


# ============================================================
# SECCIÓN 24 - DESAFÍO EXTRA
# ============================================================

# Crear un programa que calcule
# el promedio de tres notas.
#
# El programa debe pedir:
#
# - Nota 1
# - Nota 2
# - Nota 3
#
# Luego debe calcular el promedio.
#
# Fórmula:
#
# promedio = (nota1 + nota2 + nota3) / 3
#
# Finalmente debe mostrar:
#
# Nota 1:
# Nota 2:
# Nota 3:
# Promedio:


# ============================================================
# RESUMEN DE LA CLASE
# ============================================================

# VARIABLES
#
# nombre = "Lautaro"
# edad = 17


# TIPOS DE DATOS
#
# str   -> texto
# int   -> entero
# float -> decimal
# bool  -> verdadero/falso


# CONOCER EL TIPO
#
# type(variable)


# OPERACIONES
#
# +  -> suma
# -  -> resta
# *  -> multiplicación
# /  -> división
# // -> división entera
# %  -> resto
# ** -> potencia


# ENTRADA DE DATOS
#
# input()


# CONVERSIÓN DE DATOS
#
# int()
# float()
# str()
# bool()


# ============================================================
# FIN DE LA CLASE
# ============================================================
#
# Conceptos trabajados:
#
# ✓ Variables
# ✓ Tipos de datos
# ✓ str
# ✓ int
# ✓ float
# ✓ bool
# ✓ type()
# ✓ print()
# ✓ input()
# ✓ Conversión de tipos
# ✓ Suma
# ✓ Resta
# ✓ Multiplicación
# ✓ División
# ✓ División entera
# ✓ Resto
# ✓ Potencia
# ✓ Operaciones combinadas
#
# Próximo tema sugerido:
#
# ESTRUCTURAS CONDICIONALES
# if / elif / else
#
# ============================================================
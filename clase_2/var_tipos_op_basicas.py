# ============================================================
# 1. VARIABLES Y TIPOS
# ============================================================

# Guardamos un texto dentro de una variable
nombre = "Lautaro"

# Guardamos un número entero
edad = 17

# Guardamos un número decimal
altura = 1.75

# Guardamos un valor verdadero o falso
es_estudiante = True

# Mostramos el contenido de cada variable
print(nombre)
print(edad)
print(altura)
print(es_estudiante)


# ============================================================
# 2. TYPE()
# ============================================================

nombre = "Lautaro"
edad = 17
altura = 1.75
es_estudiante = True

# type() permite conocer el tipo de dato de una variable
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))


# ============================================================
# 3. MODIFICAR VARIABLES
# ============================================================

# Creamos una variable con un valor inicial
puntos = 10

print(puntos)

# Podemos cambiar el valor de una variable
puntos = 20
print(puntos)

# Volvemos a modificar el valor
puntos = 50
print(puntos)


# ============================================================
# 4. OPERACIONES BÁSICAS
# ============================================================

numero1 = 10
numero2 = 5

# Realizamos las operaciones y guardamos cada resultado
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostramos los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


# ============================================================
# 5. DIVISIÓN ENTERA Y RESTO
# ============================================================

numero1 = 17
numero2 = 5

# // devuelve solamente la parte entera de una división
division_entera = numero1 // numero2

# % devuelve el resto de una división
resto = numero1 % numero2

print("División entera:", division_entera)
print("Resto:", resto)


# ============================================================
# 6. POTENCIAS
# ============================================================

base = 2
exponente = 3

# ** permite elevar un número a una potencia
resultado = base ** exponente

print("Resultado:", resultado)


# ============================================================
# 7. OPERACIONES COMBINADAS
# ============================================================

# Primero se realiza la multiplicación
resultado = 10 + 5 * 2

print(resultado)

# Los paréntesis permiten modificar el orden de las operaciones
resultado = (10 + 5) * 2

print(resultado)


# ============================================================
# 8. VARIABLES APLICADAS A UN PROBLEMA
# ============================================================

precio = 1000
cantidad = 3

# Calculamos el precio total
total = precio * cantidad

print("Precio:", precio)
print("Cantidad:", cantidad)
print("Total:", total)


# ============================================================
# 9. DESCUENTO
# ============================================================

precio = 1000
cantidad = 3

# Calculamos el precio total sin descuento
total = precio * cantidad

# Calculamos el 10% del total
descuento = total * 0.10

# Restamos el descuento al precio total
precio_final = total - descuento

print("Total:", total)
print("Descuento:", descuento)
print("Precio final:", precio_final)


# ============================================================
# 10. INPUT()
# ============================================================

# input() permite ingresar información desde el teclado
nombre = input("Ingresá tu nombre: ")

# Mostramos el dato ingresado
print("Hola", nombre)


# ============================================================
# 11. INPUT() + INT()
# ============================================================

# input() devuelve texto, por eso usamos int()
# para convertir el dato ingresado en un número entero
edad = int(input("Ingresá tu edad: "))

# Realizamos una operación con la edad
edad_futura = edad + 5

print("Dentro de 5 años tendrás:", edad_futura)


# ============================================================
# 12. INPUT() + FLOAT()
# ============================================================

# float() convierte el dato ingresado en un número decimal
altura = float(input("Ingresá tu altura: "))

print("Tu altura es:", altura)

# Comprobamos el tipo de dato
print(type(altura))


# ============================================================
# 13. CONVERSIÓN DE TIPOS
# ============================================================

numero = 10

# Convertimos un entero a decimal
numero_decimal = float(numero)

print(numero_decimal)
print(type(numero_decimal))

edad = 17

# Convertimos un número entero en texto
edad_texto = str(edad)

print(edad_texto)
print(type(edad_texto))


# ============================================================
# 14. CALCULADORA BÁSICA
# ============================================================

# Pedimos dos números y los convertimos a decimal
numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print()
print("========== RESULTADOS ==========")

# Mostramos cada resultado
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("================================")


# ============================================================
# 15. CALCULADORA COMPLETA
# ============================================================

numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))

# Calculamos las diferentes operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 ** numero2
resto = numero1 % numero2

print()
print("========== CALCULADORA ==========")

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)
print("Resto:", resto)

print("================================")


# ============================================================
# 16. ACTIVIDAD PRINCIPAL
# ============================================================

# Pedimos información personal
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
altura = float(input("Ingresá tu altura: "))

# Pedimos dos números para realizar operaciones
numero1 = float(input("Ingresá un número: "))
numero2 = float(input("Ingresá otro número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 ** numero2
resto = numero1 % numero2

print()
print("========== RESULTADOS ==========")

# Mostramos los datos personales
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)

# Mostramos los resultados matemáticos
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)
print("Resto:", resto)

print("================================")


# ============================================================
# 17. DESAFÍO: COMPRA
# ============================================================

producto = input("Ingresá el producto: ")
precio = float(input("Ingresá el precio: "))
cantidad = int(input("Ingresá la cantidad: "))
descuento = float(input("Ingresá el descuento (%): "))

# Calculamos el precio total
total = precio * cantidad

# Calculamos cuánto dinero representa el descuento
valor_descuento = total * descuento / 100

# Restamos el descuento al total
precio_final = total - valor_descuento

print()
print("Producto:", producto)
print("Total:", total)
print("Descuento:", valor_descuento)
print("Precio final:", precio_final)


# ============================================================
# 18. DESAFÍO EXTRA: PROMEDIO
# ============================================================

# Pedimos tres notas y las convertimos a números decimales
nota1 = float(input("Ingresá la nota 1: "))
nota2 = float(input("Ingresá la nota 2: "))
nota3 = float(input("Ingresá la nota 3: "))

# Sumamos las tres notas y dividimos por la cantidad de notas
promedio = (nota1 + nota2 + nota3) / 3

print("Promedio:", promedio)
# ===========================================
# EJEMPLO INTEGRADOR
# ===========================================

# Creamos una lista vacía
notas = []

# Pedimos cinco notas
for i in range(5):

    # Solicitamos una nota
    nota = int(input(f"Ingrese la nota {i+1}: "))

    # La agregamos a la lista
    notas.append(nota)

# Variable acumuladora
suma = 0

# Recorremos todas las notas
for nota in notas:

    # Sumamos cada nota
    suma += nota

# Calculamos el promedio
promedio = suma / len(notas)

# Mostramos el promedio
print("El promedio es:", promedio)

# Evaluamos el resultado
if promedio >= 7:
    print("Aprobado")
elif promedio >= 4:
    print("Recuperatorio")
else:
    print("Desaprobado")
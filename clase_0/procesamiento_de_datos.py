# ===========================================
# PROCESAMIENTO DE DATOS
# ===========================================

# Creamos una lista de notas
notas = [8, 6, 10, 9, 7]

# Variable donde iremos acumulando la suma
suma = 0

# Recorremos cada nota
for nota in notas:

    # Vamos sumando cada nota
    suma += nota

# Calculamos el promedio
promedio = suma / len(notas)

# Mostramos el promedio
print("Promedio:", promedio)

# Verificamos si el promedio es aprobatorio
if promedio >= 7:
    print("Curso aprobado")
else:
    print("Curso desaprobado")
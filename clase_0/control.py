# ===========================================
# CONDICIONALES
# ===========================================

# Pedimos al usuario que ingrese una nota
nota = int(input("Ingrese la nota del alumno: "))

# Si la nota es mayor o igual a 7
if nota >= 7:
    print("Alumno aprobado")

# Si la nota está entre 4 y 6
elif nota >= 4:
    print("Alumno debe rendir recuperatorio")

# Si no se cumple ninguna condición
else:
    print("Alumno desaprobado")
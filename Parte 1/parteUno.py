# Parte 1

# Resolver el siguiente ejercicio de programación

# El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a 
# octubre, y 700 dólares por mes en noviembre y en diciembre. 
# En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa 
# que calcule el sueldo promedio del empleado Juan. Además, se debe indicar sí Juan se encuentra 
# cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:

# a. Sueldo bajo: por debajo de 300 dólares.
# b. Sueldo normal:  entre 300 a 900.
# c. Sueldo mejor de lo normal: más de 900 dólares.

# Tip: se debe utilizar estructuras condicionales.

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre",
        "Noviembre","Diciembre"]
losMeses = len(meses)
sumar_sueldo = 0
for mes in meses: #este for recorre la lista de meses y va sumando los sueldo ingresados por el usuario
    sueldo = float(input(f"ingresar sueldo del mes de {mes}: "))
    sumar_sueldo = sumar_sueldo + sueldo
promedio_sueldo = sumar_sueldo / losMeses 
promedio_sueldo = round(promedio_sueldo,2)

if promedio_sueldo != 0: # if para verificar que el promedio no es Cero y poder verificar el tipo de sueldo que es.
        print(f"El sueldo promedio es de {promedio_sueldo} dólares")
        if promedio_sueldo< 300:
            print("El sueldo esta por debajo de los 300 dólares es un sueldo bajo")
        elif  300 < promedio_sueldo < 900:
            print("El sueldo esta entre 300 y 900 dolares es un sueldo normal")
        else: print("El sueldo es mayor a 900 dolares es un sueldo mejor de lo normal")    
else: print("ERROR!: El sueldo es 0(cero)")
    

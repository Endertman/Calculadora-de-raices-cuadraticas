import math
import numpy as np

print("Calculadora de ecuaciones cuadráticas de segundo grado")

valores = np.array(input("Ingrese al menos 5 valores enteros (excepto 0) separados por espacios: ").split(), dtype=int)
valores.sort()
a = valores[0]
b = valores[4]
c = valores[1]

if a == 0:
    print("El numero de menor valor no puede ser 0, por favor inicie de nuevo el programa y no ingrese el valor 0 entre los valores")
    exit()
else:
    dato_a = (a)
    dato_b = (b)
    dato_c = (c)

    datos = np.array(["El valor de A es", dato_a, "El valor de B es", dato_b, "El valor de C es", dato_c])
    print(datos)

    aux = ((dato_b**2) - (4*dato_a*dato_c))
    print("el valor de aux es: " + str(aux))

    if aux < 0: 
        print("La ecuación no tiene raíces reales.")
        exit()
    else:
        aux_2 = (math.sqrt(aux))
        print("el valor de aux_2 es: " + str(aux_2))

        temp_1 = (-(dato_b)) + (aux_2)
        print("el valor de temp_1 es: " + str(temp_1))

        temp_2 = (-(dato_b)) - (aux_2)
        print("el valor de temp_2 es: " + str(temp_2))

        x1 = temp_1 / (2* (dato_a))
        x2 = temp_2 / (2* (dato_a))

        if aux == 0:
         print("La ecuación tiene una raíz real, x1=", x1)
        else:
         print("Las raíces de la ecuación son x1=", x1, "y x2=", x2)

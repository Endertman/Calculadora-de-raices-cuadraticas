#Creación de programa capaz de resolver ecuaciones cuadráticas de segundo grado para hallar X1 y X2. 

X1 = ( -b + √b² - 4ac ) / 2a. 

#Descripción de las variables/datos (Ítem 1) 

- a: coeficiente cuadrático de la ecuación 

- b: coeficiente lineal de la ecuación 

- c: término independiente de la ecuación 

- dato_a: Valor de a alojado en un array para su mejor visualización. 

- dato_b: Valor de b alojado en un array para su mejor visualización. 

- dato_c: Valor de c alojado en un array para su mejor visualización. 

- aux(Discriminante): valor de b² - 4ac utilizado para determinar la existencia de raíces reales 

- aux_2: valor conseguido después de calcular el valor de la raíz de aux 

- temp_1: variable resultado de calcular el valor de ( -dato_b + aux2 ) para hallar X1 

- temp_2: variable resultado de calcular el valor de ( -dato_b - aux2 ) para hallar X2 

- X1: Valor de X1, resultado de calcular (-b) + (√b**2 - 4 * a * c) o lo que es lo mismo (temp_1 / (2 * dato_a)) 

- X2: Valor de X1, resultado de calcular (-b) - (√b**2 - 4 * a * c) o lo que es lo mismo (temp_2 / (2 * dato_a)) 

 
#Tipos de datos. 

- Tipo de datos: float (para los coeficientes y raíces), int (para el discriminante y valores ingresados por el usuario). 

 
#Inicio del Programa. 

Como primer paso importamos las librerías que usaremos en este caso math y también podemos hacer uso de numpy, por lo que también la importaremos, en este ejemplo observamos que siempre al empezar un proyecto es recomendable como primer paso importar todas librerías a usar. 

import math 

import numpy as np 

 

#Bienvenida al usuario. 

En este caso daremos una bienvenida al usuario y le indicaremos para que funcione el programa, haciendo uso del siguiente print. 

print("Calculadora de ecuaciones cuadráticas de segundo grado") 

 

#Datos. 

Crearemos un array donde le pediremos al usuario que "Ingrese al menos 5 valores enteros (excepto 0) separados por espacios: ", estos 5 valores serán alojados en un array con la función "split", esta función separa los valores con espacios en blanco (Puede ser separado con cualquier otro string si se lo especificamos) y luego con la función ".sort" se ordenara de menor a mayor valor. 

valores = np.array(input("Ingrese al menos 5 valores enteros (excepto 0) separados por espacios: ").split(), dtype=int) 

valores.sort() 

a = valores[0] 

b = valores[4] 

c = valores[1] 

Si el coeficiente A de la ecuación cuadrática es igual a 0, la ecuación deja de ser una ecuación cuadrática porque el término cuadrático desaparece. En ese caso, la ecuación se convierte en una ecuación lineal por lo que no podemos permitir que esto sea así. 

En caso de que el usuario ingrese 0 como parte de los valores, le pediremos al usuario que reinicie el programa e ingrese los valores sin colocar 0 entre estos, de no ser así se mostrara en pantalla "El número de menor valor no puede ser 0, por favor inicie de nuevo el programa y no ingrese el valor 0 entre los valores" y por consecuencia el programa se cancelara y no avanzara. 

if a == 0: 

    print("El numero de menor valor no puede ser 0, por favor inicie de nuevo el programa y no ingrese el valor 0 entre los valores") 

    exit() 

else: 

    dato_a = (a) 

    dato_b = (b) 

    dato_c = (c) 

 

Por ultimo y como paso extra mostraremos en pantalla los valores elegidos por el usuario luego de ser ordenados por la función sort. 

datos = np.array(["El valor de A es", dato_a, "El valor de B es", dato_b, "El valor de C es", dato_c]) 

print(datos) 


#Variable AUX. 

A partir de los datos seleccionados realizaremos la operación pertinente, en este caso calcularemos el componente b**2 - 4ac, este lo alojaremos en la variable "aux", por ahora no será necesario mostrar este resultado en pantalla, pero si así lo que quisiéramos no tendríamos problemas. 

aux = ((dato_b**2) - (4*dato_a*dato_c)) 

print("el valor de aux es: " + str(aux)) 

 

AUX menor que 0 

Deberemos verificar que "aux" no sea menor que 0 porque si el discriminante (aux) es menor que 0 indicara que no hay raíces reales para la ecuación. En lugar de ser una ecuación cuadrática, se convierte en una ecuación lineal. En este caso se imprime un mensaje indicando que la ecuación no tiene raíces reales y se cerrara el programa. 

if aux < 0:  

    print("La ecuación no tiene raíces reales.") 

    exit() 

 

#Verificadores de aux 

En caso de que el discriminante sea igual a 0 solo se calculara el valor de X1 a partir de la siguiente formula (-(dato_b) / (2* (dato_a))) usando la función de if, donde si aux es igual a 0 se aplicara esto. 

De lo contrario, se procede a calcular las raíces de la ecuación utilizando la fórmula adecuada para "x1" y "x2" haciendo uso de "else". 

En ambos casos mostraremos el resultado en pantalla según corresponda. 

if aux == 0: 

 print("La ecuación tiene una raíz real, x1=", x1) 

else: 

 print("Las raíces de la ecuación son x1=", x1, "y x2=", x2) 

 

#Raíz de AUX 

Este valor lo alojaremos en la variable aux_2 y lo usaremos al momento de realizar el cálculo final. 

Para realizar este cálculo tenemos varias opciones, pero las más recomendada será la siguiente, igualmente adjuntaremos las otras opciones en caso de querer visualizar otras formas de resolver el problema. 

Calcularemos la raíz cuadrada del valor de "aux" luego de haberlo calculado para esto tenemos varias alternativas, pero ya que hemos importado las librerías haremos uso de estas, en el primer caso usaremos la librería Math y el comando "sqrt". 

aux_2 = (float(math.sqrt(aux))) 

print("el valor de aux_2 es: " + str(aux_2)) 


Para la opción 2 usaremos NumPy haciendo uso del mismo comando de la librería Math (sqrt). 

opcion_2 = np.sqrt(aux) 

print(aux_2) 


Y como opción extra tenemos las funciones predeterminadas de Python, estas pueden ser elevando "aux" a la potencia 0.5, o también podemos usar el comando "pow" haciendo algo similar al código anterior, elevaríamos "aux" a la potencia de 1/2. 

opcion_3 = (aux ** 0.5) 

print(opcion_3) 

opcion_4 = pow(aux,1/2) 

print(opcion_4) 

 

#Valor de temp_1 

Ahora calcularemos el valor de una nueva variable, está la llamaremos "temp_1", en ella almacenaremos el resultado de la siguiente operación ( - (dato_b) + (aux_2)). 

Esta variable también la usaremos más adelante al momento de hacer el cálculo completo. 

temp_1 = (-(dato_b)) + (aux_2) 

print("el valor de temp_1 es: " + str(temp_1)) 

 

#Valor de temp_2 

Ahora calcularemos el valor de "temp_2" que usaremos para encontrar x2 usando la siguiente operación ( - (dato_b) - (aux_2)). 

Esta variable también la usaremos más adelante al agrupar el código para hacer el cálculo completo. 

temp_2 = (-(dato_b)) - (aux_2) 

print("el valor de temp_2 es: " + str(temp_2)) 


#Valor de X1 y X2   

En el siguiente paso calcularemos el valor final de las variables "x1" y "x2", las calculamos a partir de (x1 = temp_1 / (2*a)) y (x2 = temp_2 / (2*a)) respectivamente, estas las usaremos en el cierre del programa.  

x1 = temp_1 / (2* (dato_a)) 

x2 = temp_2 / (2* (dato_a)) 

print(x1) 

print(x2) 

#Programa completo 

Ya habiendo realizado todos los pasos anteriores podremos realizar nuestro código completo. pero antes debemos diagramarlo de la siguiente manera para que funcione correctamente. 

Para probar todos los escenarios que hemos programado podemos usar los siguientes valores: 

- Para que la ecuación no tenga raíces reales: 1 1 1 1 1 

    - a = 1 

    - b = 1 

    - c = 1 

- Para que la ecuación tenga una raíz real(x1): 4 8 5 6 4 

    - a = 4 

    - b = 8 

    - c = 4 

- Para encontrar los valores de x1 y x2: 2 4 5 5 6  

    - a = 2 

    - b = 6 

    - c = 4 

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

 
Si el auxiliar es menor que 0 el programa se cerrara como ya lo habíamos explicado anteriormente, pero en caso de que no el resto del programa debe alojarse dentro de la función "else” para que siga funcionando. 

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

 
Por último, si “aux” es igual a 0 nos mostrara el resultado de X1, de lo contrario nos mostrara el resultado de X1 y X2 

        if aux == 0: 

         print("La ecuación tiene una raíz real, x1=", x1) 

        else: 

         print("Las raíces de la ecuación son x1=", x1, "y x2=", x2)

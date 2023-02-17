"""
1. Qué operadores utiliza Python en los siguientes casos:

A. División Modular
B. Exponenciación
C. División que retorne entero.

"""

modular = 5%3
exponenciacion = 2**3
entera = 15//2

print(f"División modular: 5%3 = {modular} \n Exponenciacion: 2**3 = {exponenciacion} \n División que retorna entero: {entera} \n")


"""
2. En la jerarquía de operadores, cuáles son los que más
prioridad tienen cuando el intérprete de Python los evalúa?

"""

print("Jerarquía de operadores de mayor a menor:\n Paréntesis ()\n Potencia **\n Multiplicación, división, módulo o residuo, división entera *,/, %, //")
print("Suma y resta +,- \nOperadores relacionales <, <=, >, >=, !=, ==, \nOperador lógico AND And \nOperador lógico OR or\n")


"""
3. Si hay operadores de igual precedencia, en qué orden se
ejecutan?

A. De izquierda a derecha
B. De derecha a izquierda

"""
A = 4 + 6 - 2
print(f"Suma y resta tienen misma prioridad, por tanto se evalúan de izquierda a derecha R = 4 + 6 - 2 = {A}")
B=4 + 6 * 2
print(f"Multiplicación mayor prioridad que la suma R = 4 + 6 * 2 = {B}")
C=10 * 5 + 4 ** 3 
print(f"Potenciación mayor prioridad a Multiplicación = {C}")
D=(10 * (5 + 4)) ** 3 
print(f"Se puede hacer una sobre escritura de las prioridades con el uso de paréntesis D = (10 * (5 + 4)) ** 3 = {D}\n")



"""
4. Que son las expresiones regulares en Python?
"""

print("Expresiones comodín que definen patrones de caracteres a emparejar y extraer de una cadena de texto [], ., ^, $, | \n")

"""
5. Enumere 5 tipos de datos en Python y suministre un valor de
ejemplo de cada uno.

"""
nombre = 'andres'
edad = 20
femenino = False
familia = ["papá, mamá, hermana"]
estatura = 1.63
print(f"String: {nombre}\nInt: {edad}\nSexo femenino: {femenino}\nfamilia: {familia}\nestatura: {estatura}\n")


"""
6. En sus propias palabras, qué son las funciones
preconstruidas y proporcione 2 ejemplos.

"""
hola = 'hola'
print("Bloque de código, que recibe cero o más argumentos y que una operación para devolvernos un valor y/o realiza una tarea específica. Ya están definidos en el lenguaje")
print(f"print('hola') Imprime en pantalla el argumento.")
print(hola)
print(f"len('hola') Determina la longitud en caracteres de una cadena.\n{len('hola')}\n")

"""
7. Cuál es la diferencia entre un condicional simple y un
condicional compuesto?
"""

print("condicional simple: Se hace, o no, una acción\ncondicional compuesta: Se tiene más de una acción posible para realizar además de no realizarla, nunca se hacen ambas\n")


"""
8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados.

"""

nombre = input('Ingrese su nombre ')
nombre = nombre.lower()
if nombre .__contains__('a'):
    apellido = input('Ingrese su apellido ')
    if not apellido:
        str
        print('Nombre incompleto')
    else:
        print(f"Buenos días {nombre.upper()} {apellido.upper()}\n")
else:
    print(f"Adiós {nombre.upper()}\n")            

"""
9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad.
"""

from datetime import date
from datetime import datetime
now = datetime.now()

nombre = input("Ingrese su nombre: ")
telefono = int(input("Ingrese su telefono: "))
ingreso = int(input("Digite su año de ingreso: "))
apellidos = input("Ingrese su(s) apellido(s): ")
edad = int(input('Ingrese su edad: '))
añoActual= int(now.year)
print(f"{nombre.upper()} {apellidos.upper()}, antiguedad en la empresa: {añoActual - ingreso} años\n")

"""
10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato

"""
mes = input('Introduzca el mes ')
valorKw = int(input("Ingrese valor del kilovatio "))
totalKw = int(input("Total de kilovatios consumidos "))
#estrato = input("Introduzca su estrato")

valorAPagar = valorKw*totalKw
print(f"El mes de {mes} se consumieron {totalKw} vatios, el total a pagar es de {valorAPagar}")



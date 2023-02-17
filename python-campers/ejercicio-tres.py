"""
3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos.
"""

sBasicokm = float
kmPorVuelta = float
kmCLider = float
totalAPagar = float
kmTotalCarrera = 3227
kmCLiderRecargo = 1800
ganador = int

kmPorVuelta = float(input("Ingrese los KM recorridos (Sin liderar): "))
while kmPorVuelta > kmTotalCarrera:
    kmPorVuelta = float(input("Valor incorrecto, ingrese la cantidad de Km recorridos de nuevo: "))

kmCLider = float(input("Ingrese los Km recorridos como lider: "))  
while kmCLider> kmTotalCarrera:
    kmPorVuelta = float(input("Valor incorrecto, ingrese la cantidad de Km recorridos de nuevo: "))      
if kmPorVuelta + kmCLider > kmTotalCarrera:
    print('Su total de Km es mayor al de la carrera, valor erroneo')
else:
    sBasicokm = float(input("Ingrese el valor de cada Km según su salario: "))
    if kmCLider > kmCLiderRecargo:
        totalAPagar = (kmCLider * sBasicokm) +  (kmCLider*sBasicokm*0.25) + (kmPorVuelta * sBasicokm)
    else:
        totalAPagar = (kmPorVuelta+kmCLider) * (sBasicokm)  
    print(f"Su total a cobrar es de: {totalAPagar}")
ganador = int(input("Ingrese su posición en la carrera: "))
if ganador == 1:
    print("además, por ganar la carrera también ganó 700M de premio")   
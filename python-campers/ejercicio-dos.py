"""
2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.
Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.
Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros.
"""

nombreAtleta = []
metrosAtleta = []

"""
SALVAME DIOS"""

def ganador_y_premio():
    ganador = max(metrosAtleta)
    for i in metrosAtleta:
        if i >= 15.50:
            records = metrosAtleta.index(i)
            print(f"{nombreAtleta[records]} rompió record: {i}")
        indiceGanador = metrosAtleta.index(ganador)
        print(f"Ganador: {nombreAtleta[indiceGanador]}, distancia: {ganador}")  
        for imetros in metrosAtleta:
            if imetros > 15.50 and imetros == ganador:
                premiado = metrosAtleta.index(imetros)  
                print(f"{nombreAtleta[premiado]} ganó y superó el record, ¡pago de 500 millones!")                             


def pedirDatos(confirmacion):
    if not confirmacion or confirmacion != 's':
        return
    else:
        while confirmacion != None and confirmacion != 'n':
            nombre = input('Nombre del atleta: ')
            nombreAtleta.append(nombre)
            salto = float(input("Marca de salto en metros. Ej: '9.5' "))
            metrosAtleta.append(salto)
            confirmacion = input("¿Desea ingresar otro dato? s/n")
            if confirmacion == '' or confirmacion != 's':
                confirmacion = None
                ganador_y_premio()




print('Ingrese: ')
nombre = input('Nombre del atleta: ')
nombreAtleta.append(nombre)
salto = float(input("Marca de salto en metros. Ej: '9,5' "))
float(salto)
metrosAtleta.append(salto)
confirmacion = input("¿Desea ingresar otro dato? s/n")
if confirmacion != 's':
    ganador_y_premio()
else:
    pedirDatos(confirmacion)

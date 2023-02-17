"""
1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control:
"""
import os

const = artemis = []
const = sputnik = []


class Camper:

    def __init__(self, cedula, nombre, edad):
        self._cedula = cedula
        self._nombre = nombre
        self._edad = edad

    @property
    def getCedula(self):
        return self._cedula

    @property
    def getNombre(self):
        return self._nombre

    @property
    def getEdad(self):
        return self._edad

    def __str__(self) -> str:
        return 'cedula: {}\nnombre: {}\nedad: {}'.format(self._cedula, self._nombre, self._edad)


def listCallData(list, group):
    for i in list:
        print(f"REGISTROS DE {group}\n{i}\n")
    selectGroup()


def addCampers(list, group):
    print(F"AGREGAR CAMPER A {group}")
    id = str(input('Ingrese la cedula: '))
    nombre = str(input('Ingrese el nombre: '))
    edad = str(input('Ingrese la edad: '))
    camper = Camper(id, nombre, edad)
    list.append(camper)
    selectGroup()


def deleteCampers(list, group):
    print(f"BORRAR CAMPER DE {group}")
    print('Ingrese la cedula del camper a eliminar')
    id = str(input(' '))
    for i in list:
        if id == i.getCedula:
            list.remove(i)
    selectGroup()


def orderList(list, group):
    print(f"ORDENAR CAMPERS DE {group}")
    count = 0
    orderList = sorted(list, key=lambda x: x._nombre)
    for i in orderList:
        print(f'          Registro #{count+1}')
        print(i)
        count += 1
    selectGroup()


def searchCamper(list, group):
    print(f"BUSCAR CAMPERS EN {group}")
    id = str(input('Ingrese la cedula a buscar: '))
    for i in list:
        if i.getCedula == id:
            print(i)
    selectGroup()


def selectedOptionMGroup(group, list, option_menu):
    if option_menu == 1.1:
        os.system('cls')
        listCallData(list, group)
    elif option_menu == 1.2:
        os.system('cls')
        addCampers(list, group)
    elif option_menu == 1.3:
        os.system('cls')
        deleteCampers(list, group)
    elif option_menu == 1.4:
        os.system('cls')
        orderList(list, group)
    elif option_menu == 1.5:
        os.system('cls')
        searchCamper(list, group)
    elif option_menu == 1.6:
        print('ADIÓS!')
    else:
        print("ERROR DE SELECCIÓN")


def menuGroup(group, option):
    keep = True
    while keep:
        print(
            f"1.1 LISTAR CAMPERS {group}\n1.2 AGREGAR CAMPERS A {group}\n1.3 ELIMINAR CAMPERS DE {group} ")
        print(
            f"1.4 ORDENAR ALFABETICAMENTE CAMPERS DE {group}\n1.5 BUSCAR CAMPERS EN {group}\n1.6 SALIR")
        option_menu = float(input("Opción: "))
        os.system('cls')
        if option == 1:
            selectedOptionMGroup(group, artemis, option_menu)
        if option == 2:
            selectedOptionMGroup(group, sputnik, option_menu)
        return option_menu


def selectGroup():
    option_group = int(
        input("1- Ir a grupo Artemis:\n2- Ir a grupo Sputnik:\n"))
    os.system('cls')
    if option_group == 1:
        menuGroup('ARTEMIS', option_group)
    elif option_group == 2:
        menuGroup('SPUTNIK', option_group)
    else:
        print("Selección no válida")
    return option_group


selectGroup()

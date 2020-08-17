"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""




import config as cf
import sys
import csv
from time import process_time
def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")

    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop-t1_start, " segundos")


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar buenas peliculas")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """

    if len(lst) == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0  # Cantidad de repeticiones
        for element in lst:
            # filtrar por palabra clave
            if criteria.lower() in element[column].lower():
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop-t1_start, " segundos")
    return counter


def filtro_por_criterio_columna(col_extraer, col_criterio, operacion, criterio, Base) -> list:
    """
    Retorna la columna indicada por col_
    """
    filtrada = []
    if len(Base) == 0:
        print("La lista esta vacía")

    else:

        t1_start = process_time()  # tiempo inicial
        filtrada = [el[col_extraer]
                    for el in Base if operacion(el[col_criterio], criterio)]

        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")

    return filtrada


def encontrar_elemento_list_dic_ordenado(buscado, llave, Datos):
    buscado = int(buscado)
    n_top = len(Datos) - 1
    n_low = 0
    ubicacion = None
    if Datos[n_top][llave] == buscado:
        return n_top
    if Datos[n_low][llave] == buscado:
        return n_low
    encontre = False
    posible = True
    while not encontre and posible:
        n_nuevo = round((n_top + n_low) / 2)
        a_mirar = int(Datos[n_nuevo][llave])
        if a_mirar == buscado:
            encontre = True
            ubicacion = n_nuevo
        elif a_mirar < buscado:
            n_low = n_nuevo + 1
        elif a_mirar > buscado:
            n_top = n_nuevo - 1

        if n_top - n_low < 0:
            posible = False

    return ubicacion


def count_por_criterio_columna(col_criterio, operacion, criterio, filas, col_filas, Base) -> int:
    counter = 0  # Cantidad de repeticiones

    if len(Base) == 0:
        print("La lista esta vacía")

    else:
        t1_start = process_time()  # tiempo inicial
        for fila in filas:
            indice = encontrar_elemento_list_dic_ordenado(
                fila, col_filas, Base)
            # filtrar por palabra clave
            if operacion(Base[indice][col_criterio], criterio):
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")

    return counter


def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    listaPrueba = []  # instanciar una lista vacia
    listaCastingS = []
    listaDetailS = []
    listaCastingL = []
    listaDetailL = []

    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                C1 = input(
                    "Desea Cargar los archivos de prueba? ingrese 0 si no y 1 si:")
                if int(C1):
                    # llamar funcion cargar datos
                    loadCSVFile(
                        "Data/SmallMoviesDetailsCleaned.csv", listaDetailS)
                    print("Datos cargados, "+str(len(listaDetailS)) +
                          " elementos cargados")

                    # llamar funcion cargar datos
                    loadCSVFile("Data/MoviesCastingRaw-small.csv",
                                listaCastingS)
                    print("Datos cargados, " +
                          str(len(listaCastingS)) + " elementos cargados")

                C2 = input(
                    "Desea Cargar los archivos de completos? ingrese 0 si no y 1 si:")
                if int(C2):
                    # llamar funcion cargar datos
                    loadCSVFile(
                        "Data/AllMoviesDetailsCleaned.csv", listaDetailL)
                    print("Datos cargados, "+str(len(listaDetailL)) +
                          " elementos cargados")

                    # llamar funcion cargar datos
                    loadCSVFile("Data/AllMoviesCastingRaw.csv", listaCastingL)
                    print("Datos cargados, "+str(len(listaCastingL)) +
                          " elementos cargados")

            elif int(inputs[0]) == 2:  # opcion 2
                if len(lista) == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0]) == 3:  # opcion 3
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsFilteredByColumn(
                    criteria, "nombre", lista)  # filtrar una columna por criterio
                print("Coinciden ", counter,
                      " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                criteria = input('Ingrese el criterio de búsqueda\n')
                counter = countElementsByCriteria(criteria, 0, lista)
                print("Coinciden ", counter, " elementos con el crtierio: '",
                      criteria, "' (en construcción ...)")
            elif int(inputs[0]) == 5:  # opcion 5
                director = input(
                    "Ingrese el nombre del director de quien quiere consultar la pelicula")
                bases_es = input(
                    "Ingrese 1 para utilizar los datos de prueba y 2 para utilizar los datos completos")

                Base1 = []
                Base2 = []

                if int(bases_es) == 1:
                    Base1 = listaCastingS
                    Base2 = listaDetailS
                elif int(bases_es) == 2:
                    Base1 = listaCastingL
                    Base2 = listaDetailL
                else:
                    print("no seleccion ninguna opcion")

                if Base1 == [] or Base2 == []:
                    print("alguna de las listas estan vacias")
                else:
                    t1_start = process_time()
                    idf = filtro_por_criterio_columna(
                        "id", "director_name", lambda x, y: x == y, director, Base1)
                    n_peliculas_buenas = count_por_criterio_columna(
                        "vote_average", lambda x, y: float(x) > y, 6, idf, "id", Base2)
                    t1_stop = process_time()  # tiempo final
                    print("Tiempo total de ejecución 1",
                          t1_stop - t1_start, " segundos")

                    print(
                        "La cantidad de peliculas buenas del director {} son {}".format(director,n_peliculas_buenas))

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()

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
from Sorting import mergesort as mg
from DataStructures import liststructure as lt

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
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Encontrar buenas películas")
    print("6- Ranking de películas")
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
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def promedio_votos_peli(lista_ids,lst):
    
    suma_votos = 0
    for id in lista_ids:
        i = 0
        while i < len(lst):
            posible_id = lst[i]["id"]
            if posible_id == id:
                vote = float(lst[i]["vote_average"])
                suma_votos = suma_votos + vote
            i +=1
    promedio = suma_votos / len(lista_ids)
    return promedio

def countElementsByCriteria(criteria, column, lst1, lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    counter = 0
    if len(lst1) == 0 or len(lst2) == 0:
        print("Alguna de las listas está vacía.")
    else:

        t1_start = process_time() #tiempo inicial
        id_peliculas_director = []
        j = 1
        filas = len(lst2)
        while j < filas:
            director_name = lst2[j][column]
            if director_name == criteria:
                id = lst2[j][0]
                id_peliculas_director.append(id)
            j +=1

        for id in id_peliculas_director:
            i = 0
            while i < filas:
                posible_id = lst1[i][0]
                if posible_id == id:
                    vote_average = lst1[i][17]

                    if vote_average >= 6:
                        counter +=1
                i +=1

        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        promedio = promedio_votos_peli(id_peliculas_director,lst1)
    return counter , promedio

def greater_rating(elem1,elem2):
    return float(elem1["vote_average"]) > float(elem2["vote_average"])

def greater_num(elem1,elem2):
    return float(elem1["vote_count"]) > float(elem2["vote_count"])

def ranking_genero(genero:str, num_peliculas:int, lst1:list, lst2:list,criterio:int):

    t1_start = process_time() #tiempo inicial
    movies_lt = lt.newList(datastructure='ARRAY_LIST', cmpfunction = None) 
    j = 1
    filas = len(lst1)
    while j < filas:
        elemento = lst1[j]["genres"]
        if genero in elemento:
            movie_name = lst1[j]["original_title"]
            movie_vote_average = float(lst1[j]["vote_average"])
            movie_vote_count = float(lst1[j]["vote_count"])
            
            movie = {'movie_name': movie_name, 'vote_average': movie_vote_average, 'vote_count': movie_vote_count}
            lt.addLast(movies_lt,movie)             
        j = j + 1

    if criterio == 1:
         mg.mergesort(movies_lt,greater_num)   
    if criterio == 2:
         mg.mergesort(movies_lt,greater_rating) 

    pedazo_mejores = lt.subList(movies_lt,1,num_peliculas)
    pos_inicial_peores = lt.size(movies_lt)-num_peliculas
    pedazo_peores = lt.subList(movies_lt,pos_inicial_peores,num_peliculas)

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return pedazo_mejores["elements"] , pedazo_peores["elements"]
 
            
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_1 = [] #instanciar una lista vacia
    lista_2 = [] #instanciar una segunda lista vacia para el segundo archivo CSV
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", lista_1) #llamar funcion cargar datos del primer archivo
                loadCSVFile("Data/MoviesCastingRaw-small.csv", lista_2) #llamar funcion cargar datos del segundo archivo
                print("Archivo: SmallMoviesDetailsCleaned.csv"+"\nDatos cargados, "+str(len(lista_1))+" elementos cargados")
                print("\nArchivo: MoviesCastingRaw.csv"+"\nDatos cargados, "+str(len(lista_2))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                i = True
                lista = input("\n1.SmallMoviesDetailsCleaned"+"\n2.MoviesCastingRaw-small"+"\nIngrese la lista que quiere consultar:")
                if lista == "1":
                    lista = lista_1
                elif lista == "2":
                    lista = lista_2
                else:
                    print("El número ingresado no es válido")
                    i = False
                if i:
                    if len(lista)==0: #obtener la longitud de la lista
                        print("La lista esta vacía")    
                    else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                i = True
                lista = input("1.SmallMoviesDetailsCleaned"+"\n2.MoviesCastingRaw-small"+"\nIngrese la lista que quiere consultar:")
                if lista == "1":
                    lista = lista_1
                elif lista == "2":
                    lista = lista_2
                else:
                    print("El número ingresado no es válido")
                    i = False
                if i:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    columna = input("Ingrese la columna en la quiere hacer la búsqueda\n")
                    counter=countElementsFilteredByColumn(criteria,columna, lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )

            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsByCriteria(criteria,12,lista_1,lista_2)
                print("Coinciden ",counter[0]," elementos con el crtierio: '", criteria, "\nCon un promedio de votos de: ", counter[1])
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

            elif int(inputs[0])==6: #opcion 6
                genero = input("Ingrese el género de búsqueda:\n")
                numero = int(input("Ingrese el número de películas que quiere ver en el ranking:\n"))
                criterio= int(input("Ingrese:\n1. Si quiere ordenar por Número de votos.\n2. Si quiere ordenar por Calificación.\n"))
                ranking=ranking_genero(genero,numero,lista_1,lista_2,criterio)
                print("El TOP ",numero," de mejores peículas es: (Nombre, Calificación, Número de votos)\n",ranking[0],"\n\nEl TOP ",numero,"de peores películas es:(Nombre, Calificación, Número de votos)\n",ranking[1])

if __name__ == "__main__":
    main()

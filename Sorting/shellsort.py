"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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

import config as cf
from ADT import list as lt

"""
Implementación del algoritmo shellsort, basado en la propuesta de Robert Sedgewick

Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne

Se utiliza la secuencia de incrementos 3x+1: 1, 4, 13, 40, 121, 364, 1093, ..... (D. Knuth)
Sedgewick: 1,5,19,41,109,209,929,2161,...
"""


def shellSort(lst, lessfunction):
    n = lt.size(lst)
    h = 1
    while h < n / 3:  # Se calcula el tamaño del primer gap. La lista se h-ordena con este tamaño
        h = 3 * h + 1  # por ejemplo para n = 100, h toma un valor inical de 13 , 4, 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and lessfunction(lt.getElement(lst, j + 1), lt.getElement(lst, j - h + 1)):
                lt.exchange(lst, j + 1, j - h + 1)
                j -= h
        h //= 3  # h se decrementa en un tercio. cuando h es igual a 1, se comporta como insertionsort

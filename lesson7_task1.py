import random
from time import time


def bubble(array):
    tic = time()
    for i in range(len(array)-1):
        for j in range(len(array)-1, i, -1):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    toc = time()
    print('Время выполнения', toc - tic)
    return array


def bubble_ext(array):
    tic = time()
    count_cycle = 0
    count_subcycle = 0
    last_in_unsorted = len(array) - 1
    i = 0
    while i < last_in_unsorted:
        count_cycle += 1
        min = array[last_in_unsorted] + 1
        un_swap = True
        for j in range(last_in_unsorted, i, -1):
            count_subcycle += 1
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                un_swap = False
            if array[j] < min:
                min = array[j]
                point_min = j
        array[point_min] = array[last_in_unsorted]
        array[last_in_unsorted] = min
        last_in_unsorted -= 1
        i += 1
        if un_swap:
            print('Число циклов', count_cycle, 'Число подциклов', count_subcycle)
            toc = time()
            print('Время выполнения', toc - tic)
            return array
    print('Число циклов', count_cycle, 'Число подциклов', count_subcycle)
    toc = time()
    print('Время выполнения', toc - tic)
    return array


size = 100
array = [i for i in range(-size, size)]
random.shuffle(array)
print(array)
bubble(array)
random.shuffle(array)
bubble_ext(array)
print(array)


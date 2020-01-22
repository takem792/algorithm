import random


def mediana(list):
    left = 0
    right = len(list) - 1

    while left <= right:
        for i in range(left, right, +1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        right -= 1

        for i in range(right, left, -1):
            if list[i - 1] > list[i]:
                list[i], list[i - 1] = list[i - 1], list[i]
        left += 1
    return list[int((len(list)-1)/2)]


m = 100
list = [i for i in range(2 * m + 1)]
random.shuffle(list)
print(mediana(list))
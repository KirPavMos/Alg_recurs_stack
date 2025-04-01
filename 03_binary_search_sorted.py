# Рекурсивная функция для выполнения бинарного
# поиска элемента в отсортированном списке

import random

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

random_list = [random.randint(1, 100) for _ in range(10)]
random_list.sort()

print("Отсортированный список:", random_list)

target = int(input("Введите число для поиска: "))
result = binary_search(random_list, target)

if result != -1:
    print(f"Число {target} найдено на позиции {result}.")
else:
    print(f"Число {target} отсутствует в списке.")
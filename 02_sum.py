# Функция для вычисления суммы всех элементов в списке

def recursive_sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])

numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))
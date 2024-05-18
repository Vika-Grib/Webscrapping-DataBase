"""
Frequency Sort
Given an array of n item values, sort the array in ascending order, first by the frequency of each value, then by the values themselves.

Example

makefile
Копировать код
n = 6
items = [4, 5, 6, 5, 4, 3]
There are 2 values that occur once: [3, 6].
There are 2 values that occur twice: [4, 4, 5, 5].
The array of items sorted by frequency and then by value in ascending order is: [3, 6, 4, 4, 5, 5].
"""

from collections import Counter
items = [4, 5, 6, 5, 4, 3]

def itemsSort(items):
    # Подсчитываем частоты элементов
    count = Counter(items)

    # Сортируем элементы по частоте, затем по значению
    sorted_items = sorted(items, key=lambda x: (count[x], x))

    return sorted_items

print(itemsSort(items))


# Чтение входных данных и вывод результата
if __name__ == '__main__':
    import sys  # Импортируем модуль sys для работы с входными данными.

    input = sys.stdin.read  # Читаем все входные данные.
    data = input().split()  # Разделяем входные данные на отдельные элементы.

    n = int(data[0])  # Первый элемент входных данных - это размер массива.
    items = list(map(int, data[1:]))   # Остальные элементы - это сам массив.

    result = itemsSort(items)   #  Сортируем массив с помощью функции itemsSort.
    print(' '.join(map(str, result)))


"""
Этот код реализует функцию itemsSort, которая сортирует массив сначала по частоте значений, 
затем по самим значениям в порядке возрастания.


Чтение данных: Вместо использования int(input().strip()), мы читаем все входные данные сразу и разделяем их пробелами.
 Это удобно для обработки входных данных в тестовой среде.
Вывод данных: Используем print('\n'.join(map(str, result))) для вывода результатов. Этот метод позволяет вывести 
каждый элемент результирующего списка на новой строке.
Попробуй запустить этот код, он должен работать корректно. Если возникнут дополнительные ошибки или вопросы,
 дай знать!"""
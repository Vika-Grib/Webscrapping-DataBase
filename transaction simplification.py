"""
Задание 2: Упрощение транзакций
Условие:
Реализуйте прототип сервиса для упрощения группы долговых транзакций.

Есть n человек и список из m долгов между ними, где debts[i] = [from[i], to[i],
amount[i]] означает, что человек from[i] должен человеку to[i] сумму amount[i].

Дан массив долгов debts, найдите минимальное количество транзакций, необходимых
для погашения всех долгов.

Пример:
Предположим, n = 3, m = 4, debts = [[0, 1, 20], [1, 0, 5], [1, 2, 10], [2, 0, 10]].
то есть 4 долговых обязательства между 3 людьми.

markdown
Копировать код
suppose 0 gives 1 a total amount of 5 units
from | to | amount
--------------------
0    | 1  | 20
1    | 0  | 5
1    | 2  | 10
2    | 0  | 10

Now 0 and 1's debts are simplified.
from | to | amount
--------------------
0    | 1  | 15
1    | 2  | 10
2    | 0  | 10

Как это используется в задаче
Мы используем эту информацию, чтобы рассчитать балансы каждого человека. Затем мы пытаемся минимизировать количество транзакций, необходимых для того, чтобы все долги были погашены.

Шаги выполнения задачи:
Рассчитываем баланс для каждого человека.
Оставляем только ненулевые балансы.
Рекурсивно находим минимальное количество транзакций, необходимых для погашения долгов.
"""





#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinTransactions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY debt
#

n = 3
debt = [
    [0, 1, 20],
    [1, 0, 5],
    [1, 2, 10],
    [2, 0, 10]
]
from collections import defaultdict

def getMinTransactions(n, debt):
    balance = defaultdict(int)

    # Рассчитываем баланс для каждого человека / balance for every person
    for u, v, w in debt:
        balance[u] -= w
        balance[v] += w
    print(dict(balance), 'balance')

    # Оставляем только ненулевые балансы / leave only non-zero balance
    debts = list(balance.values())
    debts = [x for x in debts if x != 0]

    def dfs(debts, start):
        # Пропускаем нулевые балансы / skip zero balances
        while start < len(debts) and debts[start] == 0:
            start += 1
        # Если все балансы обнулены / if all balances are reset to zero
        if start == len(debts):
            return 0
        min_trans = float('inf')
        for i in range(start + 1, len(debts)):
            # Проверяем, имеют ли значения противоположные знаки
            if debts[i] * debts[start] < 0:
                # Пытаемся погасить долг start с i / trying to pay off the debt
                debts[i] += debts[start]  # это эквивалентно debts[i] = debts[i] - debts[start]
                # Рекурсивно вызываем функцию dfs для обновленного списка debts
                min_trans = min(min_trans, 1 + dfs(debts, start + 1))
                # Откатываем изменения
                debts[i] -= debts[start]
        return min_trans

    return dfs(debts, 0)

print(getMinTransactions(n, debt))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     debt_rows = int(input().strip())
#     debt_columns = int(input().strip())
#
#     debt = []
#
#     for _ in range(debt_rows):
#         debt.append(list(map(int, input().rstrip().split())))
#
#     result = getMinTransactions(n, debt)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


"""Объяснение:

Вместо удаления элементов из списка debts, мы просто пропускаем нулевые балансы с помощью указателя start.
Функция dfs теперь принимает дополнительный аргумент start, который указывает на текущий индекс в списке debts.
В цикле мы пытаемся минимизировать количество транзакций, рекурсивно вызывая dfs и обновляя баланс.!"""


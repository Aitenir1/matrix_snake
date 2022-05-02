import random
import copy

n = int(input())
m = int(input())

twos = []

for i in range(m + 2):
    twos.append(2)

a = [
    twos.copy(),
]

for i in range(n):
    row = [2]

    row1 = list(map(int, input().split()))

    row += row1

    row.append(2)
    a.append(row)
a.append(twos.copy())
cl = copy.deepcopy(a)
while True:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            nn = 0
            if cl[i + 1][j] == 1:
                nn += 1
            if cl[i + 1][j + 1] == 1:
                nn += 1
            if cl[i][j + 1] == 1:
                nn += 1
            if cl[i - 1][j + 1] == 1:
                nn += 1
            if cl[i - 1][j] == 1:
                nn += 1
            if cl[i - 1][j - 1] == 1:
                nn += 1
            if cl[i][j - 1] == 1:
                nn += 1
            if cl[i + 1][j - 1] == 1:
                nn += 1

            if a[i][j] == 0 and nn == 3:
                a[i][j] = 1
            elif cl[i][j] == 1:
                if nn not in (2, 3):
                    a[i][j] = 0
    z = input()
    for i in range(1, n + 1):
        print(' '.join(map(str, a[i][1:-1])))


#floyd Warshall
from unicodedata import numeric

edges=[
    (0, 3, 288), (0, 16, 390), (0, 21, 346), (1, 4, 449), (1, 7, 346),
    (1, 13, 325), (2, 21, 335), (3, 6, 231), (3, 11, 437), (3, 17, 140),
    (3, 18, 325), (3, 19, 362), (3, 20, 323), (4, 7, 457), (4, 10, 234),
    (4, 15, 399), (5, 7, 101), (5, 10, 445), (5, 12, 261), (5, 13, 234),
    (5, 21, 364), (6, 19, 304), (6, 20, 461), (7, 12, 362), (7, 13, 288),
    (7, 21, 445), (8, 9, 230), (8, 22, 365), (9, 18, 154), (9, 22, 191),
    (10, 21, 433), (11, 15, 381), (11, 17, 400), (11, 20, 113), (12, 15, 402),
    (12, 21, 260), (14, 15, 320), (14, 19, 454), (14, 20, 326), (15, 17, 453),
    (15, 19, 243), (15, 20, 394), (16, 17, 308), (16, 18, 214), (17, 21, 430),
    (18, 22, 262), (19, 20, 318), (19, 21, 391)
]
num_vertex = 23

INF = float('inf')

D= [[(INF, -1) for _ in range(num_vertex) ]for _ in range(num_vertex)]
for i in range(num_vertex):
    D[i][i] = (0, -1)  # 자기 자신으로 가는 경로의 비용은 0


for i, j, w in edges:# 가중치와 바로 이동가능한 곳임을 넣어준다.
    D[i][j] = w, -1
    D[j][i] = w, -1
    #양쪽에 다 저장을 해야한다.

#k를 들렀다 가는게 더 이롭냐
for k in range(num_vertex):
    for i in range(num_vertex):
        for j in range(num_vertex):
            v=D[i][k][0]+D[k][j][0]
            # cost
            if D[i][j][0] > v:
                D[i][j] = (v,k)


def path(i,j):# i부터 j까지 경로를 나타내주는 재귀함수
    c, k =D[i][j]
    if k<0:
        return f'->{j}'
    return path(i,k)+path(k,j)

for i in range(num_vertex):
    for j in range(num_vertex):
        cost, _ = D[i][j]
        p = path(i,j)
        print(f'{i}{p} ({cost})')





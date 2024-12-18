edges = [

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
n_edges = len(edges)
print('Using Maximul Matching')

# build adj set from edges

from collections import defaultdict

g = defaultdict(set)

for u,v,w in edges:
    g[u].add(v)
    g[v].add(u)

    # 구하려는 Set Cover 해 정점들
vc = set()
import random
random.seed('kkk')
vertices = list(range(num_vertex))
covered_edge = 0

while covered_edge < n_edges:
    u = random.choice(vertices)
    vertices.remove(u)

    v = random.choice(list(g[u]))
    vertices.remove(v)

    vc.add(u)
    vc.add(v)

    for w in list(g[u]):
        g[w].remove(u)
        covered_edge += 1

    for w in list(g[v]):
        g[w].remove(v)
        covered_edge+=1

    print(len(vc), vc)
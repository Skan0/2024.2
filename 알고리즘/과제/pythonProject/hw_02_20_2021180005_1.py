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

start = 8
## Prim

# Build Graph from Input Edge List
g = { s: dict() for s in range(num_vertex) }
for s,e,w in edges:
    g[s][e] = w
    g[e][s] = w

# Prepare Data Structures
from heapdict import heapdict
mst = []
D = heapdict()
D[start] = 0
origins = dict()
origins[start] = start
completed = set()
sum = 0
# Prim Main Loop
while D:
    to_vertex, weight = D.popitem()
    fr_vertex = origins[to_vertex]
    completed.add(to_vertex)
    if fr_vertex != to_vertex:
        mst.append((fr_vertex, to_vertex, weight))
        sum += weight
    for adj, adj_w in g[to_vertex].items():
        if adj in completed: continue       # 내륙이면 무시
        if adj in D and D[adj] <= adj_w: continue # 존재하고 기존게 싸면 무시
        D[adj] = adj_w
        origins[adj] = to_vertex

print(sum, mst)

## TSP
# Build Graph from MST
mg = { s: set() for s in range(num_vertex) }
for s,e,w in mst:
    mg[s].add(e)
    mg[e].add(s)

# Make Sequence
seq = [ start ]
current = start
while True:
    if current == start and not mg[start]: break
    for k in mg[current]:
        if k not in seq:
            visit = k
            break
    else:
        visit = list(mg[current])[0]
    mg[current].remove(visit)
    seq.append(visit)
    current = visit
print(seq)
# Find Shortcut
visited = set()
index = 0
while index < len(seq):
    current = seq[index]
    if current in visited:
        seq.pop(index)
    else:
        visited.add(current)
        index += 1
seq.append(start)
print(seq)

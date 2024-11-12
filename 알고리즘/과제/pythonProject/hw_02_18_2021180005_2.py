# Prim

import heapq
from heapdict import heapdict
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
# 시작점에서 주변점까지 길이 만들어질 수 있는곳을 탐색하고 가장 작은 가중치를 가진 곳부터 연결하고 연결된 부분에서 또 새로운 점들과 만들어질 수 있는 길 추가

class MST:
    def __init__(self, nv):
        self.edges = []
        self.nv = nv
        self.graph = {u: dict() for u in range(nv)}
    def append(self, s, e, w):
        if s <= e:
            self.edges.append((s,e,w))
        else:
            self.edges.append((e,s,w))
        self.edges.sort(key=lambda e:e[0]*1000+e[1]) # s를 기준으로 먼저 정렬하고 s값이 같다면 e값으로 정렬될 수 있게 해주는 코드
    def build_graph(self, e):
        for u, v, w, in e:
            self.graph[u][v] = w
            self.graph[v][u] = w

    def prim(self):
        visited = [False]*self.nv
        heap = [(0, 8, 8)]
        while heap:
            w, s, e = heapq.heappop(heap)

            if visited[e]:
                continue
            visited[e] = True
            if s != e:
                self.append(s, e, w)

            for neighbor, next in self.graph[e].items():
                if not visited[neighbor]:
                    heapq.heappush(heap, (next, e, neighbor))

            if len(self.edges) == self.nv:
                break

    def __repr__(self):
        # result = {}
        # for s, e, w in self.edges:
        #     if s not in result:
        #         result[s] = []
        #     result[s].append((e, w))
        #
        # output = []
        # for start, connections in result.items():
        #     conn_str = ', '.join(f'{end}' for end, weight in connections)
        #     output.append(f'{start} -> {conn_str}')
        #
        # return '\n'.join(output)
        return str(self.edges)

mst = MST(num_vertex)
mst.build_graph(edges)
mst.prim()

# 점을 선택하고 점과 연결될 수 있는 간선을 모두 heap에 넣고

print(mst)
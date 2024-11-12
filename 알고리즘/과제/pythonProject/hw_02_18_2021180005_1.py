# Kruskal

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
num_vertex = 23 # 정점의 개수
# 가중치 순으로 간선을 추가 하는데 같은 노드 안에 있다면 사이클이 생성되므로 추가하지 않는다.

class MST:
    def __init__(self, nv):
        self.roots = [i for i in range(nv)]
        self.edges = []
        self.nv = nv
    def append(self, s, e, w):
        if s <= e:
            self.edges.append((s,e,w))
        else:
            self.edges.append((e,s,w))
        self.edges.sort(key=lambda e:e[0]*1000+e[1]) # s를 기준으로 먼저 정렬하고 s값이 같다면 e값으로 정렬될 수 있게 해주는 코드
    def full(self):
        return True
    def onSameTree(self, u, v):
        return self.getRoot(u) ==self.getRoot(v)
    def getRoot(self, v):
        if v != self.roots[v]:
            self.roots[v] = self.getRoot(self.roots[v])
        return self.roots[v]

    def connect(self, u, v):
        uroot = self.getRoot(u)
        vroot = self.getRoot(v)
        if uroot != vroot:
            if uroot > vroot:
                self.roots[uroot] = vroot
            else:
                self.roots[vroot] = uroot

    def __repr__(self):
        # result ={}
        # for s,e,w in self.edges:
        #     if s not in result:
        #         result[s] = []
        #     result[s].append((e,w))
        #
        # output = []
        # for start, connection in result.items():
        #     conn_str = ', '.join(f'{end}' for end, weight in connection)
        #     output.append(f'{start} -> {conn_str}')
        #
        # return '\n'.join(output)
        return str(self.edges)

    def done(self):
        return len(self.edges)>=self.nv

mst = MST(num_vertex)

edges.sort(key = lambda e: e[2])

for s,e,w in edges:
    if mst.done():
        break
    if mst.onSameTree(s,e):
        continue
    else:
        mst.connect(s,e)
        mst.append(s,e,w)

print(mst)




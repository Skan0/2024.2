# Dijkstra
import heapq

from scipy.cluster.hierarchy import weighted

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

class MST:
  def __init__(self, nv):
    self.graph = {u: dict()for u in range(nv)}
    self.edges = []
    self.nv = nv

  def build_graph(self, e):
      for u, v, w, in e:
          self.graph[u][v] = w
          self.graph[v][u] = w
  def shortest_path(self,start):
      dis = {i:float('inf')for i in range(self.nv)}
      dis[start] = 0
      heap = [(0,start)]
      visited = set()
      previous_nodes = {i:None for i in range(self.nv)}

      while heap:
          cur_dis, u = heapq.heappop(heap)
          if u in visited:
              continue
          visited.add(u)

          for neighbor, w in self.graph[u].items():
              if neighbor in visited:
                  continue
              new_dis = cur_dis+w
              if new_dis<dis[neighbor]:
                  dis[neighbor] = new_dis
                  previous_nodes[neighbor] = u
                  heapq.heappush(heap, (new_dis, neighbor))

      return dis, previous_nodes
  def get_path(self,previous_nodes, target):
      path = []
      while target is not None:
          path.append(target)
          target = previous_nodes[target]
      return path[::-1]

mst = MST(num_vertex)
mst.build_graph(edges)
distances, previous_nodes = mst.shortest_path(12)
all_paths = {}
for city in range(num_vertex):
    path = mst.get_path(previous_nodes, city)
    all_paths[city] = {
        'distance': distances[city],
        'path' : path,
    }
for i in all_paths:
    print(f"{i} {all_paths[i]}")





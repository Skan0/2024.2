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

print('Using Set Cover')

# Make U, F from Data

U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}  # 엣지 총집합

F = [set() for _ in range(num_vertex)]

for i, (v1,v2,_) in enumerate(edges):
    F[v1].add(i)
    F[v2].add(i)
    # 구하려는 Set Cover 해 정점들

vc = set()

    # Main Loop: Select C

while U:  # While there are edges left to cover
        # Select the vertex that covers the most uncovered edges
        max_i = max(range(num_vertex), key=lambda v: len(F[v] & U))  # Vertex with the max intersection with U
        vc.add(max_i)  # Add this vertex to the cover

        # Remove the covered edges from U
        U -= F[max_i]

print(len(vc), vc)

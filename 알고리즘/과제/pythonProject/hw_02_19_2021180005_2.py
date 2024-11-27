d = [2,5,9,3,3,8,4,7,2,6]
# 2,5|5,9|9,3|3,3|3,8|8,4|4,7|7,2|2,6

#A1xA2
# d[0] * d[1] * d[2]

#A(n) * A(n+1)
# d[n-1] * d[n] * d[n+1]

#A(i~j) * A(j+1~k)
# d[] * d[] * d[]

mc = len(d)-1 #matrix count
C = [[(0,0) for _ in range(mc+1)] for _ in range(mc+1)]

INF = float('inf')

for sub_problem_size in range(2, mc+1):# sub_problem_size 2 ~ mc포함까지
    sub_problem_count = mc - sub_problem_size + 1
    for beg in range(1, sub_problem_count + 1):
        end = beg + sub_problem_size - 1
        smallest = INF,0
        for k in range(beg,end):
            t = C[beg][k][0] + C[k + 1][end][0] + d[beg - 1] * d[k] * d[end]
            #1 = C[beg][k]
            #2 = C[k+1][end]
            #3 = d[?] * d[?] * d[?]
            if smallest[0]>t:
                smallest = t, k
        C[beg][end] = smallest

def path(i,j):
    if i== j:return f'A{i}'
    cost, k = C[i][j]
    return f'({path(i,k)}x{path(k+1,j)})'

a,b = C[1][mc]
print(path(1,mc), a)
coords = [
    (296, 659), (787, 278), (1123, 699), (1113, 156), (1002, 231),
    (431, 53), (126, 609), (936, 432), (1336, 404), (1487, 104),
    (130, 498), (425, 506), (1511, 604), (659, 683), (529, 850),
    (1345, 271), (434, 772), (920, 848), (868, 577), (869, 678),
    (1209, 877), (1544, 390), (796, 235), (1281, 379), (1220, 488),
    (1192, 401), (1131, 611), (1044, 133), (1240, 519), (1415, 72),
    (190, 385), (528, 455), (800, 365), (1315, 172), (133, 245),
    (442, 866), (218, 174), (206, 61), (928, 242), (527, 416),
    (471, 625), (880, 13), (1163, 145), (1426, 806), (14, 429),
    (742, 531), (1037, 630),
]
def dist_sq(a, b):
    d = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    return d

def brute_force(arr, i1, i2):
    min_dist = float('inf')
    start, end = 0, 0
    for i in range(i1, i2):
        c1 = arr[i]
        for j in range(i + 1, i2 + 1):
            c2 = arr[j]
            dist = dist_sq(c1, c2)
            if dist < min_dist:
                start, end = i, j
                min_dist = dist
    return start, end, min_dist

def dnc(arr, i1, i2):
    size = i2 - i1 + 1
    if size <= 1:  # 도시가 1개라면
        return -1, -1, 0  # "거리" 자체가 성립하지 않는다.
    if size == 2:  # 도시가 2개라면
        s, e, d = i1, i2, dist_sq(arr[i1], arr[i2])  # 그 두 도시가 가장 가깝다
        return s, e, d
    if size == 3:  # 도시가 3개라면
        s, e, d = brute_force(arr, i1, i2)
        return s, e, d

    mid = size // 2 + i1 - 1  # 왼쪽 그룹의 맨 오른쪽 점이므로 1을 뺀다
    # 왼쪽과 오른쪽으로 나눈다
    ls, le, ld = dnc(arr, i1, mid)
    rs, re, rd = dnc(arr, mid + 1, i2)

    # 두 그룹에서 가장 가까운 두 점 중 더 작은 것을 선택
    s, e, d = (ls, le, ld) if ld <= rd else (rs, re, rd)

    # 중간에서 좌우로 떨어진 점들을 찾아서 거리 갱신
    cx1 = arr[mid][0] - d  # 가운데 점에서 d 만큼 왼쪽에 있는 좌표
    cx2 = arr[mid][0] + d  # 가운데 점에서 d 만큼 오른쪽에 있는 좌표

    index1 = min(c[2] for c in arr if c[0] >= cx1 and c[2] >= i1)
    index2 = max(c[2] for c in arr if c[0] <= cx2 and c[2] <= i2)

    # index1 ~ index2 사이의 점들만 처리
    strip = [c for c in y_sorted if c[2] >= index1 and c[2] <= index2]
    n_strip = len(strip)

    for s1 in range(n_strip):
        c1 = strip[s1]
        for s2 in range(s1 + 1, n_strip):
            c2 = strip[s2]
            dy = abs(c1[1] - c2[1])
            if dy > d:
                break
            dx = abs(c1[0] - c2[0])
            if dx > d:
                continue
            dist = dist_sq(c1, c2)
            if d > dist:
                d = dist
                s, e = c1[2], c2[2]
    return s, e, d

# 좌표에 인덱스 추가

s = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]
x_sorted = sorted(s, key=lambda t: t[0])
y_sorted = sorted(s, key=lambda t: t[1])

# 분할 정복 실행
s, e, d = dnc(x_sorted, 0, len(x_sorted) - 1)
print(f'[{s=}]{coords[s]} - [{e=}]{coords[e]} = {d=}')

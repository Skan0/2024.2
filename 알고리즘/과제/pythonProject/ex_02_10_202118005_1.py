words = [
  '2021180005', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',
  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
  'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell',
  'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',
  'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn',
  'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl',
  'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range',
  'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns',
  'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber',
  'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine',
  'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit',
]

def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and key.lower()<arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def mergeSort(arr, start, end): # end = inclusive / end != exclusive
    size = end - start + 1
    if size <= 1:return
    elif size<=5:
        insertion_sort(arr, start, end)
        return

    mid = start+(end-start)//2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    merge(arr, start, mid, end)


def merge(arr, s, mid, e): # end = inclusive / mid = left subarray
    # left_array = arr[s : mid + 1]
    # right_array = arr[mid + 1 : e + 1]

    merged =[] # 임시 저장할 정렬 결과 목록
    l, r = s, mid+1

    while l <= mid and r <= e:
        if arr[l].lower() <= arr[r].lower():
            merged.append(arr[l])
            l = l + 1
        else:
            merged.append(arr[r])
            r = r + 1
    while l <= mid:
        merged.append(arr[l])
        l = l + 1
    while r <= e:
        merged.append(arr[r])
        r = r + 1

    for i in range(s, e + 1):
        arr[i] = merged[i - s]


mergeSort(words, 0, len(words)-1)
print(words)
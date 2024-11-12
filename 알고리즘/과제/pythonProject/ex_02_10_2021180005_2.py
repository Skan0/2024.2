import random
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
        while j >= start and key.lower()>arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort(arr, start, end): # end = inclusive
    size = end - start + 1
    if size<=5:
        # insertion_sort(arr, start, end)
        # 밑에서 한번만 진행한다.
        return
    pi = partition(arr, start, end)
    quick_sort(arr,start, pi - 1)
    quick_sort(arr,pi + 1, end)

def partition(arr, start, end):
    pivot = random.randint(start, end) # randint는 끝을 포함한다. end = inclusive
    # 피봇을 정하고 작은건 왼쪽 큰건 오른쪽
    arr[start], arr[pivot] = arr[pivot], arr[start]
    pivot =arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[low].lower() > pivot.lower():
            low += 1
        while low <= high and pivot.lower() > arr[high].lower():
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    return high


quick_sort(words, 0, len(words)-1)
insertion_sort(words, 0, len(words)-1)
print(words)

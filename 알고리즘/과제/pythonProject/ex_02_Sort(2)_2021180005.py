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

BASE = (ord('a') - 1)
char_count = ord('z') - ord('a') + 1

def get_slot(char):
    if char.isdigit():
        return int(char) + 26
    return ord(char.lower()) - BASE

def radix(array, left, right, depth=0):
    counts = [0 for _ in range(char_count + 11)]
    for i in range(left, right + 1):
        string = array[i]
        str_len = len(string)
        slot = get_slot(string[depth]) if str_len > depth else 0
        counts[slot] += 1

    for i in range(len(counts) - 1): # 구한 데이터 인덱싱
        counts[i + 1] += counts[i]

    for i in range(right, left - 1, -1):
        string = array[i]
        str_len = len(string)
        slot = get_slot(string[depth]) if str_len > depth else 0
        counts[slot] -= 1
        temp[left + counts[slot]] = array[i]

    array[left:right + 1] = temp[left:right + 1]

    for i in range(len(counts) - 1):
        sub_l = left + counts[i]
        sub_r = left + counts[i + 1] - 1 if i < len(counts) - 1 else right
        if sub_l < sub_r:
            radix(array, sub_l, sub_r, depth + 1)

word_count = len(words)
temp = [0 for _ in range(word_count)]
radix(words, 0, word_count - 1)

print(words)

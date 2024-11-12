import ex_02_10_2021180005_2 as qs

def selection(arr, start, end, nth): # end = inclusive
    pi = qs.partition(arr, start, end)
    #pi보다 nth가 작은가
    if nth - 1 == pi:
        return arr[pi]
    elif nth - 1 < pi:
        return selection(arr, start, pi - 1, nth)
    else:
        return selection(arr, pi + 1, end, nth)

ranks = [ 4, 10, 13, 27,]

last_word_index = len(qs.words) -1
if __name__ == '__main__':
    for rank in ranks:
        words = qs.words[:]
        word = selection(words,0, last_word_index, rank)
        print(f'{rank=} {word=}')
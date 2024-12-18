import random

random.seed('class_02')

BIN_SIZE = 40

nums = [random.randint(2, 9) for _ in range(20)]

print(nums)


# bin = [ 1, 2, 3 ]

# bins = [ bin ]


def bin_free(bin):
    return BIN_SIZE - sum(bin)


def bin_can_hold(bin, size):
    return bin_free(bin) >= size


def new_bin():
    nb = []

    bins.append(nb)

    return nb


def first_fit(size):
    for b in bins:
        if bin_can_hold(b, size):
            return b
    return new_bin()

def next_fit(size):
    global last_bin
    if last_bin is not None and bin_can_hold(last_bin, size):
        return last_bin
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE
    for b in bins:
        if bin_can_hold(b, size):
            remaining_space = bin_free(b) - size
            if remaining_space < smallest_size:
                smallest_bin = b
                smallest_size = remaining_space
    if smallest_bin is None:
        return new_bin()
    return smallest_bin

def worst_fit(size):
    largest_bin = None
    largest_size = -1
    for b in bins:
        if bin_can_hold(b, size):
            remaining_space = bin_free(b) - size
            if remaining_space > largest_size:
                largest_bin = b
                largest_size = remaining_space
    if largest_bin is None:
        return new_bin()
    return largest_bin

bins = []

last_bin = None

for num in nums:
    bin = first_fit(num)

    bin.append(num)

    last_bin = bin

print(f'Function: <<first_fit>>')

print(bins)
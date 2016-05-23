n = map(int, raw_input().split())
boxes = list(map(int, raw_input().split()))


def nim_sum(boxes):
    s = 0
    for c in boxes:
        s = c ^ s
    return s


def num_ways(boxes):
    ways = 0
    for c in boxes:
        if nim_sum(boxes) ^ c < c:
            ways += 1
    return ways

print num_ways(boxes)

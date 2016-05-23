#!/usr/bin/python


def manhattan(posr, posc, d):
    return abs(posr - d[0]) + abs(posc - d[1])


def move_to_pos(posr, posc, d):
    if posr == d[0] and posc == d[1]:
        return "CLEAN"
    if posr > d[0]:
        return "UP"
    if posr < d[0]:
        return "DOWN"
    if posc > d[1]:
        return "LEFT"
    if posc < d[1]:
        return "RIGHT"


def next_move(posr, posc, board):
    d_list = []
    for i, row in enumerate(board):
        for j, sq in enumerate(row):
            if sq == 'd':
                d_list.append((i, j))
    d = min(d_list, key=lambda x: manhattan(posr, posc, x))
    print move_to_pos(posr, posc, d)


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

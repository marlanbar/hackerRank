#!/bin/python
def displayPathtoPrincess(n, grid):
    #print all the moves here
    for i in range(n):
        if 'm' in grid[i]:
            r_y = i
            r_x = grid[i].index('m')
        if 'p' in grid[i]:
            p_y = i
            p_x = grid[i].index('p')
    while r_x != p_x and r_y != p_y:
        if r_x > p_x:
            print 'LEFT'
            r_x -= 1
        else:
            print 'RIGHT'
            r_x += 1
        if r_y > p_y:
            print 'UP'
            r_y -= 1
        else:
            print 'DOWN'
            r_y += 1

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())
displayPathtoPrincess(m, grid)

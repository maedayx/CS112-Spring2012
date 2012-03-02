#! /usr/bin/env python

grid = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    grid.append(row)

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        print val,
    print ""
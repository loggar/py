#!/usr/bin/python3

matrix = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print('matrix[{}][{}] = {}'.format(i, j, matrix[i][j]))

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        print('matrix[{}][{}] = {}'.format(i, j, col))

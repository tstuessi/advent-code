# objective is to find out how many lights are on
import sys

def turn_on(pt1, pt2):
    for i in range(pt1[0], pt2[0]+1):
        for j in range(pt1[1], pt2[1]+1):
            matrix[i][j] += 1

def turn_off(pt1, pt2):
    for i in range(pt1[0], pt2[0]+1):
        for j in range(pt1[1], pt2[1]+1):
            if matrix[i][j] > 0:
                matrix[i][j] -= 1

def toggle(pt1, pt2):
    for i in range(pt1[0], pt2[0]+1):
        for j in range(pt1[1], pt2[1]+1):
            matrix[i][j] += 2

matrix = list()
for i in range(0, 1000):
    matrix.append(1000 * [0])

data = sys.stdin.read()
for line in data.split('\n'):
    words = line.split(' ')
    if ' '.join(words[0:2]) == 'turn on':
        turn_on([int(i) for i in words[2].split(',')], [int(i) for i in words[-1].split(',')])
    elif ' '.join(words[0:2]) == 'turn off':
        turn_off([int(i) for i in words[2].split(',')], [int(i) for i in words[-1].split(',')])
    elif words[0] == 'toggle':
        toggle([int(i) for i in words[1].split(',')], [int(i) for i in words[-1].split(',')])

on = 0
for i in range(0, 1000):
    for j in matrix[i]:
        on += j

print on

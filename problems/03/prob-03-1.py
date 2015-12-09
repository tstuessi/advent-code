import sys

# get the path
path = sys.stdin.read()

x = 0
y = 0
count = 0

visited = set([(x, y)])
for c in path:
    if c is '^':
        x -= 1
    elif c is 'v':
        x += 1
    elif c is '>':
        y += 1
    elif c is '<':
        y -= 1
        visited = visited | set([(x, y)])

print len(visited)
        

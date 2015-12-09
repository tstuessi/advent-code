import sys

# get the path
path = sys.stdin.read()

a = 0
b = 0
x = 0
y = 0
count = 0

visited = set([(a, b), (x, y)])
for c in path:
    if count % 2:
        if c is '^':
            x -= 1
        elif c is 'v':
            x += 1
        elif c is '>':
            y += 1
        elif c is '<':
            y -= 1
        visited = visited | set([(x, y)])
    else:
        if c is '^':
            a -= 1
        elif c is 'v':
            a += 1
        elif c is '>':
            b += 1
        elif c is '<':
            b -= 1
        visited = visited | set([(a, b)])
    count += 1
        

print len(visited)
        

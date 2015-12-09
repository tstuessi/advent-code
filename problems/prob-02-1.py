total = 0
try:
    line = raw_input()
    while line:
        l, w, h = [int(i) for i in line.split('x')]
        total += 2*l*w + 2*w*h + 2*l*h
        total += min(l*w, w*h, l*h)
        line = raw_input()
except EOFError:
    pass
print total

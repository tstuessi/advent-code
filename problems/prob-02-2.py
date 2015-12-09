total = 0
try:
    line = raw_input()
    while line:
        dim = [int(i) for i in line.split('x')]
        total += dim[0] * dim[1] * dim[2]
        # get the max element and delete it
        dim.remove(max(dim))
        total += 2 * dim[0] + 2 * dim[1]
        line = raw_input()
except EOFError:
    pass

print total
    

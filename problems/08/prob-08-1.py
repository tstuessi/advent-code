import sys

data = sys.stdin.read()
data = data.split('\n')

code_chars = 0
out_chars = 0

for line in data:
    if line.isspace():
        break
    elif line == "":
        break
    code_chars += len(line)
    out_chars += len(line) - 2
    i = 1
    while i < len(line)-1: 
        if line[i] == '\\':
            if line[i+1] == '\\':
                out_chars -= 1
                i += 1
            elif line[i+1] == '\"':
                out_chars -= 1
                i += 1
            elif line[i+1] == 'x':
                out_chars -= 3
                i += 3
        i += 1

print code_chars - out_chars

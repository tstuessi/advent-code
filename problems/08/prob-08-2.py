import sys

data = sys.stdin.read()
data = data.split('\n')

code_chars = 0
new_chars = 0
for line in data:
    if line.isspace() or line == "":
        break
    code_chars += len(line)
    # add quotes
    new_chars += len(line) + 2
    for i in range(0, len(line)):
        if line[i] == '\\':
            new_chars += 1
        elif line[i] == '\"':
            new_chars += 1

print new_chars - code_chars

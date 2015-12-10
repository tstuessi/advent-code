import sys

def two_pair(string):
    for i in range(1, len(string)):
        for j in range(i+2, len(string)):
            if string[i-1:i+1] == string[j-1:j+1]:
                return True

    return False

def repeated_lets(string):
    for i in range(2, len(string)):
        if string[i] == string[i-2]:
            return True
    return False

data = sys.stdin.read()
data = data.split('\n')
nice = 0

for string in data:
    if repeated_lets(string) and two_pair(string):
        nice += 1
print nice

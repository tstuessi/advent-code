import sys

def contains_subs(string):
    return ('ab' in string) or ('cd' in string) or ('pq' in string) or ('xy' in string)

def two_in_row(string):
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return True
    return False

def three_vowels(string):
    count = 0
    for i in string:
        if i in 'aeiou':
            count += 1
        if count == 3:
            return True
    return False
    
data = sys.stdin.read()
data = data.split('\n')
nice = 0

for string in data:
    if not contains_subs(string) and two_in_row(string) and three_vowels(string):
        nice += 1
print nice

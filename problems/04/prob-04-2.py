# I don't actually know anything about 
# md5 hashing, so this solution came from 
# the help of cinnamennen

import hashlib

key = raw_input("key: ")
i = 1

while hashlib.md5(key+str(i)).hexdigest().startswith('000000') is False:
    i += 1

print i

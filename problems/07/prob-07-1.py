# this one is a more complex problem than the last few.
# My basic approach was to build a graph of the circuit
# then topologically sort it where processing the node
# was executing the command
import sys
from numpy import uint16

class queue:
    def __init__(self):
        self.l = list()
    def pop(self):
        return self.l.pop(0)
    def push(self, element):
        self.l.append(element)
    def empty(self):
        return len(self.l) == 0


def process(connect_dict, value_dict, tmp, key):
    command = connect_dict[tmp][key].split(' ')
    # six commands to handle
    if command[0] == "DIR":
        value_dict[key] = value_dict[tmp]
    elif command[0] == "NOT":
        value_dict[key] = ~value_dict[tmp]
    elif command[0] == "AND":
        value_dict[key] = value_dict[tmp] & value_dict[command[1]]
    elif command[0] == "OR":
        value_dict[key] = value_dict[tmp] | value_dict[command[1]]
    elif command[0] == "LSHIFT":
        value_dict[key] = value_dict[tmp] << value_dict[command[1]]
    elif command[0] == "RSHIFT":
        value_dict[key] = value_dict[tmp] >> value_dict[command[1]]

# topological sort to get all the values
def top_sort(connect_dict, value_dict, num_edges_dict):
    q = queue()
    for key in num_edges_dict:
        if num_edges_dict[key] == 0:
            q.push(key)
    while not q.empty():
        tmp = q.pop()
        for key in connect_dict[tmp]:
            process(connect_dict, value_dict, tmp, key)
            num_edges_dict[key] -= 1
            if num_edges_dict[key] == 0:
                q.push(key)

def check_exists(word, connect_dict, values_dict, num_edges_dict):
    if word not in connect_dict:
        connect_dict[word] = dict()
    if word not in values_dict:
        if word.isdigit():
            values_dict[word] = uint16(int(word))
        else:
            values_dict[word] = uint16(0)
    if word not in num_edges_dict:
        num_edges_dict[word] = 0

# dictionary of values (to be used in the topological sort)
values_dict = dict()

# connection dictionary
connect_dict = dict()

# keep track of how many edges a node has
num_edges_dict = dict()

# process the input and build the graph
data = sys.stdin.read()
for line in data.split('\n'):
    # 6 commands: AND, OR, LSHIFT, RSHIFT, NOT, and direct connection.
    words = line.split(' ')

    # check NOT
    if 'NOT' in words:
        check_exists(words[1], connect_dict, values_dict, num_edges_dict)
        check_exists(words[-1], connect_dict, values_dict, num_edges_dict)

        connect_dict[words[1]][words[-1]] = 'NOT'
        num_edges_dict[words[-1]] += 1
        continue

    for command in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
        if command in words:
            check_exists(words[0], connect_dict, values_dict, num_edges_dict)
            check_exists(words[2], connect_dict, values_dict, num_edges_dict)
            check_exists(words[-1], connect_dict, values_dict, num_edges_dict)

            connect_dict[words[0]][words[-1]] = '{} {}'.format(command, words[2])
            connect_dict[words[2]][words[-1]] = '{} {}'.format(command, words[0])
            num_edges_dict[words[-1]] += 2
            break
    else:
        if not line:
            break
        elif line.isspace():
            break
        check_exists(words[0], connect_dict, values_dict, num_edges_dict)
        check_exists(words[-1], connect_dict, values_dict, num_edges_dict)
        connect_dict[words[0]][words[-1]] = 'DIR'
        num_edges_dict[words[-1]] += 1

top_sort(connect_dict, values_dict, num_edges_dict)

print "Value Dict"
for key in values_dict:
    print "{}: {}".format(key, values_dict[key])

